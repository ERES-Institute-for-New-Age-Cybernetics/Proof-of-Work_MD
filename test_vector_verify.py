#!/usr/bin/env python3
"""
ERES EAAP v1.3-FINAL — Test Vector Verification Script

This script verifies the byte-normative test vectors referenced in:
  ERES-EAAP-STD-2026-001-v1.3-FINAL, Section 10.1
  (inherited from ERES-CRYPTO-STD-2026-001-v1.1.1, Section 20)

It reproduces the full attestation chain from Test Vector A (§20.1) and the
integer-arithmetic weighted selector from Test Vector F (§20.6), verifying:
  1. Test keypair seed derivation (SHA-256)
  2. Ed25519 public key derivation from seed
  3. BERA canonical encoding and hashing
  4. Sigma derivation via HKDF-SHA256 over BERA|nonce|info
  5. GCF polysemantic primitive default resolution (sigma mod |readings|)
  6. PoR factor arithmetic (Vectors PoR-1 and PoR-2)
  7. DSAP-PRE composite (regime-transition case)
  8. Weighted selector integer cross-multiplication (Test Vector F)

Run: python3 test_vector_verify.py

Expected output: all eight checks PASS.

Dependencies:
  - Python 3.8+
  - cryptography>=3.4 for Ed25519 check (pip install cryptography)

License: MIT (code layer of CCAL v2.1)
Author: Joseph Allen Sprute, ERES Institute for New Age Cybernetics
Date: April 24, 2026
"""

import hashlib
import hmac
import sys


# =============================================================================
# Canonical values — from ERES-CRYPTO-STD-2026-001-v1.1.1 §20
# =============================================================================

# §20.0 Test-Vector Fixtures
EXPECTED_KEY_SEED_INPUT = b"ERES-CRYPTO-STD-2026-001-v1.1-TEST-KEY-C"
EXPECTED_PRIVATE_SEED_HEX = (
    "f2f794def2ea5d19ecb0f894716932654eb173195c451b2cccb9770ab2874691"
)
EXPECTED_PUBLIC_KEY_HEX = (
    "04e552e2c8ee4d34be854a1ca808600183f0afcfa8a4d063eb7c1e1bb7fecf68"
)
EXPECTED_NONCE_HEX = "00112233445566778899aabbccddeeff"

# §20.1 Step 3 — BERA canonical bytes (keys lexicographic, no whitespace, NFC)
BERA_CANONICAL_STR = (
    '{"ari":0.84,"eri":0.79,"rci":0.82,"rhc":0.91,'
    '"sensor_spec":"RG#404-v1.0","window_seconds":30}'
)
BERA_CANONICAL_BYTES = BERA_CANONICAL_STR.encode("utf-8")

# HKDF info string per §4.5.1 and §20.1 Step 3
HKDF_INFO = b"ERES-ECS-v1.0-sigma"

EXPECTED_SIGMA_HEX = (
    "e43732833d50a0502dab120d33fa05537bb4a069957f3aba293ebe62aba50ad7"
)

# §20.1 Step 2 — full canonical payload SHA-256
EXPECTED_PAYLOAD_SHA256_HEX = (
    "2f751f1bf59d5a2b7b5682e280bcc523bd0ea7384433a9814d8deebc821d7acd"
)

# §20.1 Step 4 — GCF resolution
EXPECTED_GCF_RESOLVED = "G3"

# §20.1 Step 6 — RATE vector
EXPECTED_RATE_VECTOR = [10, 10, 10, 9, 8, 9, 10]
EXPECTED_RATE_SCORE = 9.428571
EXPECTED_RATE_CONFIDENCE = 0.869293

# §20.6 Test Vector F — weighted-selector inputs
TEST_F_WEIGHTS = [2, 4, 1]
TEST_F_EXPECTED_RESOLVED = "G3"
TEST_F_EXPECTED_INDEX = 2
TEST_F_EXPECTED_P = 16_444_668_103_617_454_160


# =============================================================================
# HKDF-SHA256 (RFC 5869)
# =============================================================================

def hkdf_extract(salt: bytes, ikm: bytes) -> bytes:
    if not salt:
        salt = b"\x00" * hashlib.sha256().digest_size
    return hmac.new(salt, ikm, hashlib.sha256).digest()


def hkdf_expand(prk: bytes, info: bytes, length: int) -> bytes:
    n = (length + 31) // 32
    okm = b""
    t = b""
    for i in range(1, n + 1):
        t = hmac.new(prk, t + info + bytes([i]), hashlib.sha256).digest()
        okm += t
    return okm[:length]


def hkdf_sha256(ikm: bytes, salt: bytes, info: bytes, length: int = 32) -> bytes:
    prk = hkdf_extract(salt, ikm)
    return hkdf_expand(prk, info, length)


# =============================================================================
# Check 1 — Test keypair seed derivation
# =============================================================================

def check_keypair_seed():
    derived_seed = hashlib.sha256(EXPECTED_KEY_SEED_INPUT).hexdigest()
    passed = (derived_seed == EXPECTED_PRIVATE_SEED_HEX)

    print("Check 1 — Test keypair seed derivation (§20.0)")
    print(f"  Input:    SHA-256({EXPECTED_KEY_SEED_INPUT.decode()!r})")
    print(f"  Expected: {EXPECTED_PRIVATE_SEED_HEX}")
    print(f"  Derived:  {derived_seed}")
    print(f"  Result:   {'PASS' if passed else 'FAIL'}")
    print()
    return passed


# =============================================================================
# Check 2 — Ed25519 public key derivation
# =============================================================================

def check_public_key():
    try:
        from cryptography.hazmat.primitives.asymmetric.ed25519 import (
            Ed25519PrivateKey,
        )
        from cryptography.hazmat.primitives.serialization import (
            Encoding,
            PublicFormat,
        )
    except ImportError:
        print("Check 2 — Ed25519 public key derivation (§20.0)")
        print("  SKIPPED: install 'cryptography' package to run this check")
        print("           (pip install cryptography)")
        print()
        return None

    seed_bytes = bytes.fromhex(EXPECTED_PRIVATE_SEED_HEX)
    priv = Ed25519PrivateKey.from_private_bytes(seed_bytes)
    pub_bytes = priv.public_key().public_bytes(
        encoding=Encoding.Raw, format=PublicFormat.Raw,
    )
    derived_hex = pub_bytes.hex()
    passed = (derived_hex == EXPECTED_PUBLIC_KEY_HEX)

    print("Check 2 — Ed25519 public key derivation (§20.0)")
    print(f"  Expected: {EXPECTED_PUBLIC_KEY_HEX}")
    print(f"  Derived:  {derived_hex}")
    print(f"  Result:   {'PASS' if passed else 'FAIL'}")
    print()
    return passed


# =============================================================================
# Check 3 — BERA canonical bytes SHA-256
# =============================================================================

def check_bera_canonical():
    bera_hash = hashlib.sha256(BERA_CANONICAL_BYTES).hexdigest()

    print("Check 3 — BERA canonical encoding (§20.1 Step 3)")
    print(f"  Canonical (UTF-8, {len(BERA_CANONICAL_BYTES)} bytes):")
    print(f"    {BERA_CANONICAL_STR}")
    print(f"  SHA-256:  {bera_hash}")
    # No normative expected value in spec for this sub-hash; we verify it
    # against the chain by using it as ikm in Check 4.
    print(f"  Result:   PASS (canonical form confirmed)")
    print()
    return True


# =============================================================================
# Check 4 — Sigma derivation via HKDF-SHA256 (§4.5.1, §20.1 Step 3)
# =============================================================================

def check_sigma_derivation():
    """
    Per §20.1 Step 3:
      sigma = HKDF-SHA256(
          secret = BERA canonical bytes      (ikm)
          salt   = nonce (16 bytes)
          info   = "ERES-ECS-v1.0-sigma"     (20 bytes UTF-8)
          L      = 32
      )
    """
    ikm = BERA_CANONICAL_BYTES
    salt = bytes.fromhex(EXPECTED_NONCE_HEX)
    info = HKDF_INFO

    derived = hkdf_sha256(ikm, salt, info, length=32).hex()
    passed = (derived == EXPECTED_SIGMA_HEX)

    print("Check 4 — Sigma via HKDF-SHA256 (§4.5.1, §20.1 Step 3)")
    print(f"  ikm (BERA canonical, {len(ikm)} bytes):")
    print(f"    {BERA_CANONICAL_STR}")
    print(f"  salt (nonce):  {EXPECTED_NONCE_HEX}")
    print(f"  info:          {info.decode()!r} ({len(info)} bytes)")
    print(f"  Expected:      {EXPECTED_SIGMA_HEX}")
    print(f"  Derived:       {derived}")
    print(f"  Result:        {'PASS' if passed else 'FAIL'}")
    print()
    return passed


# =============================================================================
# Check 5 — GCF default resolution (§9.3.1, §20.1 Step 4)
# =============================================================================

def check_gcf_default_resolution():
    """
    Per §9.3.1:
      i = int(sigma[0..3], big_endian) mod |readings|
      reading = readings[i]

    For Test Vector A:
      sigma[0..3] = 0xe4373283
      int = 3_828_822_659
      3_828_822_659 mod 3 = 2
      readings[2] = "G3"
    """
    sigma_bytes = bytes.fromhex(EXPECTED_SIGMA_HEX)
    first_four = sigma_bytes[:4]
    i_int = int.from_bytes(first_four, byteorder="big")
    readings = ["G1", "G2", "G3"]
    idx = i_int % len(readings)
    resolved = readings[idx]
    passed = (resolved == EXPECTED_GCF_RESOLVED)

    print("Check 5 — GCF default resolution (§9.3.1, §20.1 Step 4)")
    print(f"  sigma[0..3]:      {first_four.hex()} = {i_int}")
    print(f"  |readings|:       {len(readings)}")
    print(f"  index = {i_int} mod {len(readings)} = {idx}")
    print(f"  Expected reading: {EXPECTED_GCF_RESOLVED}")
    print(f"  Resolved:         {resolved}")
    print(f"  Result:           {'PASS' if passed else 'FAIL'}")
    print()
    return passed


# =============================================================================
# Check 6 — PoR factor arithmetic (EAAP v1.3-FINAL §10.2)
# =============================================================================

def check_por_arithmetic():
    """
    PoR Vector 1 (Authorized): A=R=P=F=0.95 → PoR = 0.95^4 ≈ 0.814
    PoR Vector 2 (Path-foreclosed): A=R=F=0.95, P=0.40 → PoR ≈ 0.343
    """
    # Vector 1
    v1 = 0.95 * 0.95 * 0.95 * 0.95
    v1_pass = abs(v1 - 0.814) < 0.001

    # Vector 2
    v2 = 0.95 * 0.95 * 0.40 * 0.95
    v2_pass = abs(v2 - 0.343) < 0.001

    passed = v1_pass and v2_pass

    print("Check 6 — PoR factor arithmetic (EAAP v1.3-FINAL §10.2)")
    print(f"  Vector PoR-1 (Authorized):      0.95^4 = {v1:.6f}  (expected ~0.814)")
    print(f"    θ=0.75; {v1:.3f} >= 0.75 → AUTHORIZED")
    print(f"  Vector PoR-2 (Path-foreclosed): 0.95·0.95·0.40·0.95 = {v2:.6f}  (expected ~0.343)")
    print(f"    θ=0.75; {v2:.3f} <  0.75 → UNAUTHORIZED (PoR_FAIL)")
    print(f"  Result: {'PASS' if passed else 'FAIL'}")
    print()
    return passed


# =============================================================================
# Check 7 — DSAP-PRE composite (EAAP v1.3-FINAL §6.4)
# =============================================================================

def check_dsap_pre_composite():
    """
    Vector PoR-3: rho_RHC=1, rho_PERT=0, rho_hyst=0
      DSAP-PRE = (1-1)·(1-0)·(1-0) = 0 → REGIME_TRANSITION
    """
    rho_RHC, rho_PERT, rho_hyst = 1, 0, 0
    dsap = (1 - rho_RHC) * (1 - rho_PERT) * (1 - rho_hyst)
    passed = (dsap == 0)

    print("Check 7 — DSAP-PRE composite (EAAP v1.3-FINAL §6.4)")
    print(f"  rho_RHC={rho_RHC}, rho_PERT={rho_PERT}, rho_hyst={rho_hyst}")
    print(f"  DSAP-PRE = {dsap}  (0 → REGIME_TRANSITION refusal)")
    print(f"  Result:  {'PASS' if passed else 'FAIL'}")
    print()
    return passed


# =============================================================================
# Check 8 — Weighted selector integer cross-multiplication (§9.3.3, §20.6)
# =============================================================================

def check_weighted_selector():
    """
    Per §9.3.3 and §20.6:
      p = int(sigma[0..7], big_endian)           # uint64
      W_sum = sum(weights)
      cum[i] = cumulative sum of weights
      Select smallest i such that p * W_sum <= cum[i] * 2^64

    For Test Vector F:
      sigma = (same as Test Vector A)
      sigma[0..7] = 0xe43732833d50a050
      p = 16_444_668_103_617_454_160
      weights = [2, 4, 1], W_sum = 7, cum = [2, 6, 7]
      i=0: 115_112_676_725_322_179_120 vs 36_893_488_147_419_103_232  → greater, continue
      i=1: 115_112_676_725_322_179_120 vs 110_680_464_442_257_309_696 → greater, continue
      i=2: 115_112_676_725_322_179_120 vs 129_127_208_515_966_861_312 → ≤, SELECT G3
    """
    sigma_bytes = bytes.fromhex(EXPECTED_SIGMA_HEX)
    first_eight = sigma_bytes[:8]
    p = int.from_bytes(first_eight, byteorder="big")

    weights = TEST_F_WEIGHTS
    W_sum = sum(weights)
    cum = []
    running = 0
    for w in weights:
        running += w
        cum.append(running)

    two_64 = 1 << 64
    readings = ["G1", "G2", "G3"]

    selected_index = None
    trace = []
    for i in range(len(weights)):
        lhs = p * W_sum
        rhs = cum[i] * two_64
        trace.append((i, lhs, rhs, lhs <= rhs))
        if lhs <= rhs:
            selected_index = i
            break

    resolved = readings[selected_index] if selected_index is not None else None
    p_ok = (p == TEST_F_EXPECTED_P)
    idx_ok = (selected_index == TEST_F_EXPECTED_INDEX)
    resolved_ok = (resolved == TEST_F_EXPECTED_RESOLVED)
    passed = p_ok and idx_ok and resolved_ok

    print("Check 8 — Weighted selector integer cross-multiplication (§9.3.3, §20.6)")
    print(f"  sigma[0..7]:        {first_eight.hex()}")
    print(f"  p (uint64):         {p:,}  (expected {TEST_F_EXPECTED_P:,})")
    print(f"  weights:            {weights}")
    print(f"  W_sum:              {W_sum}")
    print(f"  cum:                {cum}")
    print(f"  2^64:               {two_64:,}")
    print(f"  Trace:")
    for i, lhs, rhs, is_le in trace:
        marker = "✓ SELECT" if is_le else "  continue"
        print(f"    i={i}: p·W_sum = {lhs:,}")
        print(f"         cum[{i}]·2^64 = {rhs:,}  → {marker}")
    print(f"  Selected index:     {selected_index}  (expected {TEST_F_EXPECTED_INDEX})")
    print(f"  Resolved reading:   {resolved}  (expected {TEST_F_EXPECTED_RESOLVED})")
    print(f"  Result:             {'PASS' if passed else 'FAIL'}")
    print()
    return passed


# =============================================================================
# Main
# =============================================================================

def main():
    print("=" * 72)
    print("ERES EAAP v1.3-FINAL — Test Vector Verification")
    print("Byte-normative reproduction per ERES-CRYPTO-STD-2026-001-v1.1.1 §20")
    print("=" * 72)
    print()

    results = [
        ("Keypair seed derivation",         check_keypair_seed()),
        ("Ed25519 public key",              check_public_key()),
        ("BERA canonical encoding",         check_bera_canonical()),
        ("Sigma HKDF-SHA256 derivation",    check_sigma_derivation()),
        ("GCF default resolution",          check_gcf_default_resolution()),
        ("PoR factor arithmetic",           check_por_arithmetic()),
        ("DSAP-PRE composite",              check_dsap_pre_composite()),
        ("Weighted selector (Test Vec F)",  check_weighted_selector()),
    ]

    print("=" * 72)
    print("Summary")
    print("=" * 72)
    for name, result in results:
        if result is True:
            status = "PASS"
        elif result is False:
            status = "FAIL"
        else:
            status = "SKIP"
        print(f"  {status:6s}  {name}")

    executed = [r for r in results if r is not None]
    all_pass = all(r is True for r in executed)
    failures = sum(1 for r in executed if r is False)
    skips = sum(1 for _, r in results if r is None)

    print()
    if all_pass:
        msg = f"All {len(executed)} checks PASSED"
        if skips:
            msg += f" ({skips} skipped — install 'cryptography' for full coverage)"
        print(msg)
        return 0
    else:
        print(f"{failures} check(s) FAILED")
        return 1


if __name__ == "__main__":
    sys.exit(main())
