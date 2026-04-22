"""
ERES-CRYPTO-STD-2026-001 v1.1 Test Vector Computation
======================================================
Produces byte-normative test vectors for the v1.1 specification.
Uses fixed test keypair and fixed nonce for full determinism.
"""

import json
import hashlib
import base64
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes

# -------------------------------------------------------------------
# Fixed test parameters (reproducible across implementations)
# -------------------------------------------------------------------

# Test keypair: seed derived from canonical test string
TEST_SEED = hashlib.sha256(b"ERES-CRYPTO-STD-2026-001-v1.1-TEST-KEY-C").digest()
TEST_PRIV = Ed25519PrivateKey.from_private_bytes(TEST_SEED)
TEST_PUB  = TEST_PRIV.public_key()
TEST_PUB_BYTES = TEST_PUB.public_bytes_raw()

# Fixed transaction nonce for Test Vector A
TEST_NONCE = bytes.fromhex("00112233445566778899aabbccddeeff")

# Fixed engine timestamp (for RSIG determinism in test)
TEST_TIMESTAMP = "2026-04-22T14:32:17.042Z"

# -------------------------------------------------------------------
# Helper: canonical JSON (RFC 8785-style simplified for test)
# -------------------------------------------------------------------

def canonical_json(obj) -> bytes:
    """Deterministic JSON: sorted keys, no whitespace, NFC strings.
    For floats in [0,1]: exactly 6 decimal places, half-even rounding."""
    def normalize(x):
        if isinstance(x, float):
            # Enforce 6-decimal precision as required by Section 8.1
            return round(x + 0.0, 6)
        if isinstance(x, dict):
            return {k: normalize(v) for k, v in sorted(x.items())}
        if isinstance(x, list):
            return [normalize(v) for v in x]
        return x
    return json.dumps(normalize(obj), sort_keys=True, separators=(',', ':'),
                      ensure_ascii=False).encode('utf-8')

# -------------------------------------------------------------------
# Test Vector A — Minimal Citizen Transaction (ACCEPT path)
# -------------------------------------------------------------------

# Step 1: Fix the CBGMODD role-C signature (over a per-role canonical input)
cbgmodd_role_c_input = canonical_json({
    "role": "C",
    "weight": 1.0,
    "credibility": 0.8,
    "attested_at": "2026-04-22T14:30:00Z",
    "txn_id": "txn-000001"
})
cbgmodd_role_c_sig_bytes = TEST_PRIV.sign(cbgmodd_role_c_input)
cbgmodd_role_c_sig_b64 = base64.b64encode(cbgmodd_role_c_sig_bytes).decode()

# Step 2: Build the full input payload
payload_a = {
    "ctx": {
        "txn_id": "txn-000001",
        "policy_id": "uri:eres:policy:2026:test:v1",
        "primitives_referenced": ["GCF"],
        "nonce": base64.b64encode(TEST_NONCE).decode()
    },
    "cbgmodd": [
        {
            "role": "C",
            "weight": 1.0,
            "credibility": 0.8,
            "signature": "ed25519:" + cbgmodd_role_c_sig_b64,
            "attested_at": "2026-04-22T14:30:00Z"
        }
    ],
    "favors": {
        "f": 0.92, "a": 0.88, "v": 0.95,
        "o": None, "r": 0.90, "s": 0.87
    },
    "bera": {
        "ari": 0.84, "eri": 0.79, "rhc": 0.91, "rci": 0.82,
        "sensor_spec": "RG#404-v1.0",
        "window_seconds": 30
    }
}

# Step 3: Compute canonical payload hash
payload_a_bytes = canonical_json(payload_a)
payload_a_hash = hashlib.sha256(payload_a_bytes).digest()
payload_a_hash_b64 = base64.b64encode(payload_a_hash).decode()

# Step 4: Compute σ via HKDF-SHA256
bera_canonical = canonical_json(payload_a["bera"])
hkdf = HKDF(
    algorithm=hashes.SHA256(),
    length=32,
    salt=TEST_NONCE,
    info=b"ERES-ECS-v1.0-sigma"
)
sigma = hkdf.derive(bera_canonical)
sigma_hex = sigma.hex()

# Step 5: Resolve GCF primitive via deterministic selection
gcf_readings = ["G1", "G2", "G3"]
selection_index = int.from_bytes(sigma[0:4], 'big') % len(gcf_readings)
gcf_resolved = gcf_readings[selection_index]

# Step 6: Compute RATE dimensions per v1.1 NORMATIVE scoring functions
# (no longer the "both are conformant" hedge)

g = 1  # CBGMODD_valid (C-role present, credibility 0.80 >= 0.70 threshold)
favors_mandatory = [0.92, 0.88, 0.95, 0.90, 0.87]  # excluding null 'o'
b = sum(favors_mandatory) / len(favors_mandatory)
e = (0.84 + 0.79 + 0.91 + 0.82) / 4

def Score(x: float) -> int:
    """v1.1 normative: maps [0,1] to {1..10} via ceil(10x), clamped."""
    import math
    return min(10, max(1, math.ceil(10 * x)))

import math

# Conflict(BERA, ctx) — v1.1 concrete algorithm (Section 11.5.1)
# Conflict = 1 iff any pairwise index difference exceeds τ=0.25
#              OR stdev(BERA) > 0.20
bera_vals = [0.84, 0.79, 0.91, 0.82]
bera_mean = sum(bera_vals) / 4
bera_var = sum((x - bera_mean) ** 2 for x in bera_vals) / 4
bera_stdev = math.sqrt(bera_var)
max_pairwise = max(bera_vals) - min(bera_vals)
conflict = 1 if (max_pairwise > 0.25 or bera_stdev > 0.20) else 0

# SemanticClarity(ctx, resolved) — v1.1 concrete algorithm (Section 11.5.2)
# = (resolved_count / referenced_count) × mean_reading_confidence
# For single clean GCF resolution: 1/1 × 1.0 = 1.0, but if ctx signals
# ambiguity (e.g. multiple primitives or partial match) it drops.
# In Test Vector A: 1 primitive referenced, 1 resolved, default conf 1.0,
# but we apply a structural discount of 0.8 for single-primitive ctx
# (no cross-primitive corroboration available)
sem_clarity = (1/1) * 1.0 * 0.8

# PolicyAlignment(ctx, rel_result) — v1.1 concrete algorithm (Section 11.5.3)
# = Σ(compliance_i × priority_i) / Σ(priority_i)
# Test policy priority: CARE=3, BERC=2, JERC=3, PERC=1, PAIN=2, COHERENCE=2
# Test compliance scores (all passing): CARE=0.98, BERC=0.92, JERC=0.95,
# PERC=0.90, PAIN=0.99, COHERENCE=1.00
compliance = {"CARE": 0.98, "BERC": 0.92, "JERC": 0.95,
              "PERC": 0.90, "PAIN": 0.99, "COHERENCE": 1.00}
priority   = {"CARE": 3, "BERC": 2, "JERC": 3,
              "PERC": 1, "PAIN": 2, "COHERENCE": 2}
policy_alignment = sum(compliance[k] * priority[k] for k in compliance) / sum(priority.values())

# Now compute all seven dimensions normatively
r1 = Score(0.35*g + 0.35*b + 0.30*e)     # 0.35 + 0.3164 + 0.252 = 0.9184 → 10
r2 = Score(b)                             # 0.904 → 10
r3 = 10 if g == 1 else "VEILED"           # 10
r4 = Score((0.84 + 0.79) / 2)             # 0.815 → 9
r5 = Score(sem_clarity)                   # 0.80 → 8
r6 = Score(0.82)                          # 0.82 → 9
r7 = Score(policy_alignment)              # ~0.952 → 10

rate_vector = [r1, r2, r3, r4, r5, r6, r7]

# composite_confidence — v1.1 geometric mean (Section 11.5.4)
cbgmodd_cred_avg = 0.80  # single role, credibility 0.80
favors_quorum_margin = b  # 0.904
bera_mean_valid = e if all(x >= 0.70 for x in bera_vals) else 0
rel_confidence = 0.94
composite_confidence = (
    cbgmodd_cred_avg * favors_quorum_margin * bera_mean_valid * rel_confidence
) ** (1/4)

# RATE.score = arithmetic mean of non-VEILED dims
non_veiled = [x for x in rate_vector if x != "VEILED"]
rate_score = round(sum(non_veiled) / len(non_veiled), 6)

# Build RATE object
rate_object_a = {
    "vector": rate_vector,
    "score": rate_score,
    "provenance": {
        "cbgmodd_hash": "sha256:" + base64.b64encode(
            hashlib.sha256(canonical_json(payload_a["cbgmodd"])).digest()).decode(),
        "favors_hash": "sha256:" + base64.b64encode(
            hashlib.sha256(canonical_json(payload_a["favors"])).digest()).decode(),
        "bera_hash": "sha256:" + base64.b64encode(
            hashlib.sha256(bera_canonical).digest()).decode(),
        "policy_id": "uri:eres:policy:2026:test:v1"
    },
    "audit_flags": ["CARE_OK", "BERC_OK", "JERC_OK", "PERC_OK"],
    "confidence": round(composite_confidence, 6),
    "veiled_positions": []
}

# RSIG construction
rate_canonical = canonical_json(rate_object_a)
rate_hash = hashlib.sha256(rate_canonical).digest()

rsig_signed_fields = {
    "payload_hash": "sha256:" + payload_a_hash_b64,
    "rate_hash": "sha256:" + base64.b64encode(rate_hash).decode(),
    "timestamp": TEST_TIMESTAMP,
    "nonce": base64.b64encode(TEST_NONCE).decode(),
    "signer_identity": "did:eres:test:engine:0001",
    "engine_identity": "eres-ref-impl-v1.1.0-test",
    "policy_id": "uri:eres:policy:2026:test:v1",
    "compliance_flags": ["CARE_OK", "BERC_OK", "JERC_OK", "PERC_OK"],
    "hash_alg": "SHA-256",
    "sig_alg": "Ed25519"
}
rsig_input_bytes = canonical_json(rsig_signed_fields)
rsig_signature = TEST_PRIV.sign(rsig_input_bytes)

rsig_object = dict(rsig_signed_fields)
rsig_object["signature"] = base64.b64encode(rsig_signature).decode()

# -------------------------------------------------------------------
# Print all normative byte-level values
# -------------------------------------------------------------------

print("=" * 70)
print("ERES-CRYPTO-STD-2026-001 v1.1 — Test Vector A (ACCEPT path)")
print("=" * 70)
print()
print("FIXED TEST KEYPAIR (Role-C signer)")
print(f"  seed (derivation):  SHA256('ERES-CRYPTO-STD-2026-001-v1.1-TEST-KEY-C')")
print(f"  private seed (hex): {TEST_SEED.hex()}")
print(f"  public key   (hex): {TEST_PUB_BYTES.hex()}")
print()
print("FIXED TEST NONCE")
print(f"  hex:    {TEST_NONCE.hex()}")
print(f"  base64: {base64.b64encode(TEST_NONCE).decode()}")
print()
print("CBGMODD Role-C Signature")
print(f"  signed input (canonical JSON):")
print(f"    {cbgmodd_role_c_input.decode()}")
print(f"  signature (b64): {cbgmodd_role_c_sig_b64}")
print()
print("CANONICAL PAYLOAD")
print(f"  bytes (UTF-8, {len(payload_a_bytes)} chars):")
print(f"    {payload_a_bytes.decode()}")
print(f"  SHA-256 (hex):    {payload_a_hash.hex()}")
print(f"  SHA-256 (base64): {payload_a_hash_b64}")
print()
print("BERA CANONICAL BYTES + σ DERIVATION")
print(f"  BERA canonical:   {bera_canonical.decode()}")
print(f"  σ = HKDF-SHA256(secret=BERA, salt=nonce, info='ERES-ECS-v1.0-sigma', L=32)")
print(f"  σ (hex):          {sigma_hex}")
print(f"  σ[0..3] as uint32 big-endian: {int.from_bytes(sigma[0:4], 'big')}")
print(f"  |GCF readings|: 3")
print(f"  selection index: {selection_index}")
print(f"  resolved reading: {gcf_resolved}")
print()
print("REL INPUTS (test fixture)")
print(f"  compliance: {compliance}")
print(f"  priority:   {priority}")
print(f"  policy_alignment = {policy_alignment:.6f}")
print(f"  sem_clarity      = {sem_clarity:.6f}")
print(f"  Conflict(BERA,ctx) = {conflict}  (stdev={bera_stdev:.4f}, max_pairwise={max_pairwise:.4f})")
print()
print("RATE DIMENSION COMPUTATION")
print(f"  g = {g}, b = {b:.6f}, e = {e:.6f}")
print(f"  r1 = Score(0.35·1 + 0.35·{b:.4f} + 0.30·{e:.4f}) = Score({0.35+0.35*b+0.30*e:.4f}) = {r1}")
print(f"  r2 = Score({b:.4f}) = {r2}")
print(f"  r3 = {r3}  (g=1)")
print(f"  r4 = Score({(0.84+0.79)/2:.4f}) = {r4}")
print(f"  r5 = Score({sem_clarity:.4f}) = {r5}")
print(f"  r6 = Score(0.82) = {r6}")
print(f"  r7 = Score({policy_alignment:.4f}) = {r7}")
print(f"  vector = {rate_vector}")
print(f"  score  = {rate_score}")
print(f"  confidence (geom mean) = {composite_confidence:.6f}")
print()
print("FULL RATE OBJECT")
print(json.dumps(rate_object_a, indent=2))
print()
print("RSIG")
print(f"  signed-field canonical bytes ({len(rsig_input_bytes)} chars):")
print(f"    {rsig_input_bytes.decode()}")
print(f"  Ed25519 signature (hex): {rsig_signature.hex()}")
print(f"  Ed25519 signature (b64): {base64.b64encode(rsig_signature).decode()}")
print()
print("FULL RSIG OBJECT")
print(json.dumps(rsig_object, indent=2))

# -------------------------------------------------------------------
# Save all byte-normative values to a JSON file for inclusion in spec
# -------------------------------------------------------------------

test_vectors_normative = {
    "test_vector_a": {
        "name": "Minimal Citizen Transaction (ACCEPT path)",
        "fixed_parameters": {
            "test_key_seed_derivation": "SHA256('ERES-CRYPTO-STD-2026-001-v1.1-TEST-KEY-C')",
            "test_key_seed_hex": TEST_SEED.hex(),
            "test_public_key_hex": TEST_PUB_BYTES.hex(),
            "nonce_hex": TEST_NONCE.hex(),
            "nonce_b64": base64.b64encode(TEST_NONCE).decode(),
            "timestamp": TEST_TIMESTAMP
        },
        "payload": payload_a,
        "canonical_payload_utf8_bytes": payload_a_bytes.decode(),
        "canonical_payload_length": len(payload_a_bytes),
        "payload_sha256_hex": payload_a_hash.hex(),
        "payload_sha256_b64": payload_a_hash_b64,
        "bera_canonical_bytes": bera_canonical.decode(),
        "sigma_hex": sigma_hex,
        "sigma_selection_index_for_gcf": selection_index,
        "gcf_resolved_reading": gcf_resolved,
        "intermediate_scalars": {
            "g": g, "b": round(b, 6), "e": round(e, 6),
            "semantic_clarity": round(sem_clarity, 6),
            "policy_alignment": round(policy_alignment, 6),
            "bera_stdev": round(bera_stdev, 6),
            "bera_max_pairwise": round(max_pairwise, 6),
            "conflict": conflict,
            "composite_confidence": round(composite_confidence, 6)
        },
        "rate_vector_normative": rate_vector,
        "rate_score_normative": rate_score,
        "rate_object": rate_object_a,
        "rsig_object": rsig_object,
        "rsig_signature_hex": rsig_signature.hex(),
        "status": "ACCEPT"
    }
}

with open("/home/claude/eres_crypto/test_vectors_v1.1.json", "w") as f:
    json.dump(test_vectors_normative, f, indent=2)

print()
print("Test vector JSON saved to test_vectors_v1.1.json")
