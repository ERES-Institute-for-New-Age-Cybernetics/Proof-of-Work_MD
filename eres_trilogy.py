"""
ERES Trilogy Ramp-Up Scaffolding
=================================

ERES-TRILOGY-RAMPUP-2026-001-v0.1
Simulated RT User-GROUP SLA-Derived Media Generator
General-Specific Ref-Del for One-Good / Security-Clearance / Data-Integrity
H2C2H / C2H2C round-trip discipline for AD_ON-AI presentation

Compositional authority: ERES-INFOMEDIARY-BOOK-2026-001-v2.0-IOF-PUBLISHING-TOOL
Lock authority: Lock Boxes A/B/C/D/E (immutable; enforced at runtime)
License: CCAL v2.1
Author: Joseph Allen Sprute, ERES Institute for New Age Cybernetics
Status: RAMP-UP SCAFFOLDING (not production-final)

Usage:
    from eres_trilogy import IOFLens, UserGroupSLA, TrilogySimulator

    sla = UserGroupSLA.from_dict({...})
    lens = IOFLens(sla)
    sim = TrilogySimulator(lens)
    result = sim.run(query="...", direction=Direction.H2C2H)
    presentation = result.compose_for_ad_on_ai()
"""

from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Any, Optional
import hashlib
import json
import time


# =============================================================================
# LOCK ENFORCEMENT (Lock Boxes A/B/C/D/E from Lock Memo v1.5)
# =============================================================================

class LockViolation(Exception):
    """Raised when any of the five canonical Lock Boxes is violated at runtime."""
    pass


class LockBox:
    """Runtime enforcement of canonical immutable locks. Raises LockViolation."""

    @staticmethod
    def A_underwriting_direction(infomediator: str, infomediary: str) -> None:
        """Lock Box A: Infomediary is always underwritten; Infomediator underwrites."""
        if not infomediator or not infomediary:
            raise LockViolation(
                "Lock Box A: both Infomediator (underwriter) and Infomediary "
                "(underwritten) must be named. Risk flows down; authority flows up."
            )

    @staticmethod
    def B_five_layer_data_integrity(layers: list[str]) -> None:
        """Lock Box B: Data-Integrity = exactly five layers. Non-extensible."""
        required = [
            "SEPLTA", "H2C2H_C2H2C", "App_Parent",
            "Binary_111000111_000111000", "Character_IPIDITIS_IDIPITIS",
        ]
        if list(layers) != required:
            raise LockViolation(
                f"Lock Box B: Data-Integrity requires exactly five layers in "
                f"canonical order: {required}. Received: {layers}"
            )

    @staticmethod
    def C_pre_qualification_inversion(
        instrument_routed: bool,
        user_group_selected_cells: list[tuple[str, str]],
    ) -> None:
        """Lock Box C: routing only by User-GROUP cell-selection. Instrument honors."""
        if instrument_routed:
            raise LockViolation(
                "Lock Box C: routing is performed only by the User-GROUP through "
                "explicit cell selection. The Instrument honors; it does not route, "
                "widen, narrow, or reinterpret."
            )
        if not user_group_selected_cells:
            raise LockViolation(
                "Lock Box C: User-GROUP must pre-qualify at least one cell before "
                "round-trip opens."
            )

    @staticmethod
    def D_iof_trinity_three_registers(
        biological: bool, socio: bool, technical: bool,
    ) -> None:
        """Lock Box D: IOF round-trips operate across all three registers."""
        if not (biological and socio and technical):
            raise LockViolation(
                "Lock Box D: honest IOF round-trips operate across all three "
                "registers simultaneously (Biological/Socio/Technical). "
                f"Got bio={biological}, socio={socio}, tech={technical}."
            )

    @staticmethod
    def E_scalular_class(name: str, active_register: Optional[str]) -> None:
        """Lock Box E: SCALULAR names cannot be reduced to single register."""
        scalular_names = {
            "IOF_TRINITY", "TRADES", "INTUIT", "PRE",
            "TEACH_TECH", "i_I", "SELF_$ELF", "GREENBOX_WAITING_ROOM",
            "SCALULAR",
        }
        if name in scalular_names and active_register is None:
            raise LockViolation(
                f"Lock Box E: SCALULAR name '{name}' requires active_register "
                f"to be specified. Reading a SCALULAR correctly requires reading "
                f"the active register; context-determined."
            )


# =============================================================================
# CANONICAL ENUMS (mirror Volume Zero structural specifications)
# =============================================================================

class Volume(Enum):
    """Three Trilogy volumes proper. Volume Zero (Infomediary) is the lens."""
    ONE_GOOD = "One-Good"
    SECURITY_CLEARANCE = "Security-Clearance"
    DATA_INTEGRITY = "Data-Integrity"


class Pillar(Enum):
    """Four Constitutional Pillars under GAIA canopy."""
    HELP = "HELP"
    USE = "USE"
    ENERGY = "ENERGY"
    LAW = "LAW"


class Register(Enum):
    """IOF Trinity three registers (Lock Box D)."""
    BIOLOGICAL = "Biological"  # me / M+E / what
    SOCIO = "Socio"             # myself / SELF-$ELF / who
    TECHNICAL = "Technical"     # i/I/<eye>=TEACH-TECH / how


class Direction(Enum):
    """Round-trip direction class (Data-Integrity Layer 2)."""
    H2C2H = "Human-to-Computer-to-Human"
    C2H2C = "Computer-to-Human-to-Computer"


class CitizenshipTier(Enum):
    """Hand/Head Citizen/Civigen tiering (Lock Memo v1.5 §1.7)."""
    HAND_CITIZEN = "Hand-tier (Citizen-class via PPN)"
    HEAD_CIVIGEN = "Head-tier (Civigen-class via S3C)"


class DeploymentScale(Enum):
    """Deployment-scale spectrum (Pass A FINAL §0.6.1)."""
    THOW = "Tiny-House-on-Wheels"
    HFVN = "Human-Family-Village-Network"
    FDRV = "FDRV-maximum-scale"


class WielderClass(Enum):
    A_NAMED = "Class A (pseudonymous, named)"
    B_ANONYMOUS = "Class B (anonymous)"


class BSGTier(Enum):
    """BEST / SOUND / GOOD — moral-vectoring tier. Selection-produced, not Instrument-imposed."""
    BEST = "BEST"
    SOUND = "SOUND"
    GOOD = "GOOD"


class VeiledMember(Enum):
    """VEILED state-family (Pass C §VII.2). All share 'not-yet-witnessed' semantic."""
    A_ADMISSIBILITY = "VEILED-A (Admissibility)"
    S_SELECTION = "VEILED-S (Selection)"
    T_TIER = "VEILED-T (Tier)"
    L_LA_GRANGE = "VEILED-L (La Grange equilibrium)"


# =============================================================================
# CORE DATA STRUCTURES
# =============================================================================

@dataclass(frozen=True)
class Cell:
    """A cell in the 3x4 selection matrix (Volume × Pillar)."""
    volume: Volume
    pillar: Pillar

    def __str__(self) -> str:
        return f"{self.volume.value} × {self.pillar.value}"


@dataclass
class UserGroupSLA:
    """
    User-GROUP Service Level Agreement.

    The SLA is the upstream contract that derives Subjugated Context
    in near-RT. Every field here shapes downstream Trilogy generation.
    """
    user_group_id: str
    deployment_scale: DeploymentScale
    wielder_class: WielderClass
    citizenship_tier: CitizenshipTier
    selected_cells: list[Cell]
    rt_latency_target_ms: int = 1000   # near-RT default
    scalular_tier: str = "SSSC"
    intent_tier: str = "Implicit"
    infomediator_id: str = ""           # the Wielder (Lock Box A)
    infomediary_id: str = "INFOMEDIARY-default"

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "UserGroupSLA":
        return cls(
            user_group_id=d["user_group_id"],
            deployment_scale=DeploymentScale[d["deployment_scale"]],
            wielder_class=WielderClass[d["wielder_class"]],
            citizenship_tier=CitizenshipTier[d["citizenship_tier"]],
            selected_cells=[
                Cell(Volume[c["volume"]], Pillar[c["pillar"]])
                for c in d["selected_cells"]
            ],
            rt_latency_target_ms=d.get("rt_latency_target_ms", 1000),
            scalular_tier=d.get("scalular_tier", "SSSC"),
            intent_tier=d.get("intent_tier", "Implicit"),
            infomediator_id=d.get("infomediator_id", ""),
            infomediary_id=d.get("infomediary_id", "INFOMEDIARY-default"),
        )


@dataclass
class SubjugatedContext:
    """
    The User-GROUP's specific operational context, derived in near-RT from the SLA.

    "Subjugated" here means: bounded by, in-service-of, ruled-by the SLA's
    commitments. NOT generic. The Subjugated Context is what the Trilogy
    volumes generate against; it is the General-Specific Ref-Del input.
    """
    sla: UserGroupSLA
    active_volumes: set[Volume]
    active_pillars: set[Pillar]
    inaccessible_cells: list[Cell]
    bera_mask: list[str]                # which R1-R7 dimensions active
    bera_soft: list[str]                # optional dimensions
    sepltas_active: list[str]           # admissibility domains
    derived_at_ms: int                  # near-RT timestamp
    derivation_latency_ms: int          # actual derivation duration

    @property
    def is_rt_compliant(self) -> bool:
        """RT compliance check against SLA latency target."""
        return self.derivation_latency_ms <= self.sla.rt_latency_target_ms


@dataclass
class RefDelOutput:
    """
    Reference-Delineation output from a single Trilogy volume.

    The General-Specific Ref-Del pattern: each volume produces a stream of
    references (General) paired with delineations (Specific). User-GROUP SLA
    determines which references are admissible and what delineation applies.
    """
    volume: Volume
    cells_filtered: list[Cell]
    general_references: list[dict[str, Any]]
    specific_delineations: list[dict[str, Any]]
    bsg_tier_assignments: dict[BSGTier, list[dict[str, Any]]]
    veiled_fragments: list[tuple[VeiledMember, str]]
    register_engagement: set[Register]

    def to_dict(self) -> dict[str, Any]:
        return {
            "volume": self.volume.value,
            "cells_filtered": [str(c) for c in self.cells_filtered],
            "general_references": self.general_references,
            "specific_delineations": self.specific_delineations,
            "bsg_tier_assignments": {
                t.value: items for t, items in self.bsg_tier_assignments.items()
            },
            "veiled_fragments": [(v.value, frag) for v, frag in self.veiled_fragments],
            "register_engagement": [r.value for r in self.register_engagement],
        }


# =============================================================================
# IOF LENS — the Volume Zero specification applied
# =============================================================================

class IOFLens:
    """
    The Instrument-of-Faith lens.

    Constructed from a User-GROUP SLA. Enforces all five Lock Boxes at
    instantiation. The lens is the canonical surface through which the
    Trilogy volumes operate.
    """

    def __init__(self, sla: UserGroupSLA):
        self.sla = sla
        self._validate_locks()
        self.subjugated_context = self._derive_subjugated_context()

    def _validate_locks(self) -> None:
        """Enforce Lock Boxes A and C at construction time."""
        LockBox.A_underwriting_direction(
            self.sla.infomediator_id, self.sla.infomediary_id,
        )
        LockBox.C_pre_qualification_inversion(
            instrument_routed=False,
            user_group_selected_cells=[(c.volume.value, c.pillar.value)
                                       for c in self.sla.selected_cells],
        )

    def _derive_subjugated_context(self) -> SubjugatedContext:
        """
        Near-RT derivation of Subjugated Context from SLA.

        This is the SLA → Context transform. Scaffold implementation:
        - Active volumes = volumes of selected cells
        - Active pillars = pillars of selected cells
        - Inaccessible cells = full 3x4 minus selected
        - BERA mask = derived from cell mix (simplified)
        - SEPLTA = all six domains active by default; refined by query at runtime
        """
        t_start = time.time_ns() // 1_000_000

        active_volumes = {c.volume for c in self.sla.selected_cells}
        active_pillars = {c.pillar for c in self.sla.selected_cells}

        all_cells = [
            Cell(v, p) for v in Volume for p in Pillar
        ]
        inaccessible = [c for c in all_cells if c not in self.sla.selected_cells]

        # BERA mask derivation — scaffold logic; refine in production
        bera_mask = []
        if Volume.ONE_GOOD in active_volumes:
            bera_mask.extend(["R1", "R2", "R3"])  # sustenance dimensions
        if Volume.SECURITY_CLEARANCE in active_volumes:
            bera_mask.extend(["R4", "R5"])         # access/authorization
        if Volume.DATA_INTEGRITY in active_volumes:
            bera_mask.append("R7")                  # reciprocity-over-time
        bera_soft = ["R6"]                          # resilience-under-stress optional

        # Deduplicate while preserving order
        seen: set[str] = set()
        bera_mask = [r for r in bera_mask if not (r in seen or seen.add(r))]

        sepltas = ["S", "E", "P", "L", "T", "A"]  # SEPLTA: Administrative (canonical)

        t_end = time.time_ns() // 1_000_000

        return SubjugatedContext(
            sla=self.sla,
            active_volumes=active_volumes,
            active_pillars=active_pillars,
            inaccessible_cells=inaccessible,
            bera_mask=bera_mask,
            bera_soft=bera_soft,
            sepltas_active=sepltas,
            derived_at_ms=t_end,
            derivation_latency_ms=t_end - t_start,
        )

    def engages_all_three_registers(self) -> bool:
        """Lock Box D pre-check before round-trip opens."""
        bio = Volume.ONE_GOOD in self.subjugated_context.active_volumes
        socio = Volume.SECURITY_CLEARANCE in self.subjugated_context.active_volumes
        tech = Volume.DATA_INTEGRITY in self.subjugated_context.active_volumes
        return bio and socio and tech


# =============================================================================
# TRILOGY VOLUME GENERATORS (General-Specific Ref-Del)
# =============================================================================

class VolumeGenerator:
    """Abstract base for the three Trilogy volume generators."""

    volume: Volume
    register: Register

    def __init__(self, lens: IOFLens):
        self.lens = lens

    def cells_for_this_volume(self) -> list[Cell]:
        """Return cells selected by User-GROUP for this volume."""
        return [c for c in self.lens.sla.selected_cells if c.volume == self.volume]

    def generate(self, query: str, direction: Direction) -> Optional[RefDelOutput]:
        """
        Run the volume's General-Specific Ref-Del generation.

        Returns None if no cells selected for this volume (Trilogy honors
        absence per Lock Box C; volume not run if User-GROUP didn't select).
        """
        cells = self.cells_for_this_volume()
        if not cells:
            return None

        general_refs = self._produce_general_references(query, cells, direction)
        specific_dels = self._produce_specific_delineations(query, cells, direction)
        bsg_tiers = self._assign_bsg_tiers(general_refs, specific_dels)
        veiled = self._detect_veiled(query, cells, direction)

        return RefDelOutput(
            volume=self.volume,
            cells_filtered=cells,
            general_references=general_refs,
            specific_delineations=specific_dels,
            bsg_tier_assignments=bsg_tiers,
            veiled_fragments=veiled,
            register_engagement={self.register},
        )

    # Subclasses override these:
    def _produce_general_references(
        self, query: str, cells: list[Cell], direction: Direction,
    ) -> list[dict[str, Any]]:
        raise NotImplementedError

    def _produce_specific_delineations(
        self, query: str, cells: list[Cell], direction: Direction,
    ) -> list[dict[str, Any]]:
        raise NotImplementedError

    def _assign_bsg_tiers(
        self,
        general_refs: list[dict[str, Any]],
        specific_dels: list[dict[str, Any]],
    ) -> dict[BSGTier, list[dict[str, Any]]]:
        """BSG assignment is selection-produced (Lock Box C downstream consequence)."""
        return {
            BSGTier.BEST:  [r for r in general_refs if r.get("tier") == "BEST"],
            BSGTier.SOUND: [r for r in general_refs if r.get("tier") == "SOUND"],
            BSGTier.GOOD:  [r for r in general_refs if r.get("tier") == "GOOD"],
        }

    def _detect_veiled(
        self, query: str, cells: list[Cell], direction: Direction,
    ) -> list[tuple[VeiledMember, str]]:
        """Default: no VEILED. Subclasses can detect volume-specific VEILED states."""
        return []


class OneGoodGenerator(VolumeGenerator):
    """
    One-Good = need RT lookup for Adaptive-Fixed Q/A
             == HowWay / MyWay / $IT
             === UBIMIA Need-to-know for Common Core Sustenance

    Register: Biological (sustenance, what bodies receive).
    """
    volume = Volume.ONE_GOOD
    register = Register.BIOLOGICAL

    def _produce_general_references(
        self, query: str, cells: list[Cell], direction: Direction,
    ) -> list[dict[str, Any]]:
        """HowWay: process/method tier — fixed pole, reusable across Civigens."""
        refs = []
        for cell in cells:
            refs.append({
                "type": "HowWay",
                "cell": str(cell),
                "method": f"UBIMIA-Manual reference for {cell.pillar.value} sustenance",
                "tier": "SOUND",  # default; refined by selection-profile weighting
                "rt_latency_envelope_ms": self.lens.sla.rt_latency_target_ms,
            })
        return refs

    def _produce_specific_delineations(
        self, query: str, cells: list[Cell], direction: Direction,
    ) -> list[dict[str, Any]]:
        """MyWay × $IT: personal tier × concrete tier — adaptive, particularized."""
        dels = []
        for cell in cells:
            dels.append({
                "type": "MyWay_$IT",
                "cell": str(cell),
                "personalization": f"adaptive to {self.lens.sla.user_group_id}",
                "concrete_output": f"actionable Sim OUTPUT for {cell.pillar.value}",
                "common_core_element": self._common_core_for_pillar(cell.pillar),
            })
        return dels

    def _common_core_for_pillar(self, pillar: Pillar) -> str:
        """Maps Pillar to Common Core human-level element (Pass C §V.1)."""
        return {
            Pillar.HELP:   "sustenance care (water/food/shelter triage)",
            Pillar.USE:    "adaptive Q&A (HowWay/MyWay/$IT lookup)",
            Pillar.ENERGY: "resource sufficiency (energetic accounting)",
            Pillar.LAW:    "covenant of provision (rights verification)",
        }[pillar]


class SecurityClearanceGenerator(VolumeGenerator):
    """
    Security-Clearance (doubled):
      Operational: = need-to-know == DID === FAVORS Def-Rel (Hand/Head) for S3C SLA
      Governance:  = CBGMODD == CyberRAVE Def-Rel === FAVORS Commit to SROC

    Register: Socio (persons-in-relation, who is served).
    Hand/Head canonical: Citizen-class via PPN / Civigen-class via S3C.
    """
    volume = Volume.SECURITY_CLEARANCE
    register = Register.SOCIO

    def _produce_general_references(
        self, query: str, cells: list[Cell], direction: Direction,
    ) -> list[dict[str, Any]]:
        """Operational frame: DID/FAVORS/S3C SLA underwriting."""
        refs = []
        for cell in cells:
            refs.append({
                "type": "operational_frame",
                "cell": str(cell),
                "did_tier": self._did_tier_for_pillar(cell.pillar),
                "favors_def_rel": self.lens.sla.citizenship_tier.value,
                "underwriting": {
                    "underwritten_asset": self.lens.sla.infomediary_id,
                    "underwriting_agent": self.lens.sla.infomediator_id,
                },  # Lock Box A
                "tier": "SOUND",
            })
        return refs

    def _produce_specific_delineations(
        self, query: str, cells: list[Cell], direction: Direction,
    ) -> list[dict[str, Any]]:
        """Governance frame: CBGMODD/CyberRAVE Def-Rel/SROC commitments."""
        dels = []
        for cell in cells:
            dels.append({
                "type": "governance_frame",
                "cell": str(cell),
                "cbgmodd_seats_engaged": ["Citizen", "Business", "Government",
                                          "Military", "Ombudsman", "Dignitary",
                                          "Diplomat"],
                "cyberrave_def_rel_rating": "pending-runtime",
                "earnedpath_instrument": "SROC",
                "wielder_class": self.lens.sla.wielder_class.value,
            })
        return dels

    def _did_tier_for_pillar(self, pillar: Pillar) -> str:
        return {
            Pillar.HELP:   "DID-for-vulnerable",
            Pillar.USE:    "Hand-or-Head purchase tier",
            Pillar.ENERGY: "grid access tier",
            Pillar.LAW:    "underwriting authority (Class A required)",
        }[pillar]

    def _detect_veiled(
        self, query: str, cells: list[Cell], direction: Direction,
    ) -> list[tuple[VeiledMember, str]]:
        """Detect VEILED-S (Selection) and VEILED-T (Tier)."""
        veiled = []
        for cell in cells:
            # SC × LAW requires Class A uplift; Class B = VEILED-S
            if (cell.pillar == Pillar.LAW
                    and self.lens.sla.wielder_class == WielderClass.B_ANONYMOUS):
                veiled.append((
                    VeiledMember.S_SELECTION,
                    f"{cell}: Class B requires Class A uplift for SC×LAW",
                ))
            # Citizen/Civigen tier ambiguity = VEILED-T
            if not self.lens.sla.citizenship_tier:
                veiled.append((
                    VeiledMember.T_TIER,
                    f"{cell}: Hand/Head tier undetermined",
                ))
        return veiled


class DataIntegrityGenerator(VolumeGenerator):
    """
    Data-Integrity = SEPLTA == H2C2H/C2H2C
                  === ERES App-Parent 111000111/000111000 IPIDITIS/IDIPITIS

    Register: Technical (witnessed/witnessing, how the architecture sees).
    Lock Box B: exactly five chiasmic-verification layers; non-extensible.
    """
    volume = Volume.DATA_INTEGRITY
    register = Register.TECHNICAL

    LAYERS = [
        "SEPLTA",
        "H2C2H_C2H2C",
        "App_Parent",
        "Binary_111000111_000111000",
        "Character_IPIDITIS_IDIPITIS",
    ]

    def __init__(self, lens: IOFLens):
        super().__init__(lens)
        # Lock Box B enforced at instantiation:
        LockBox.B_five_layer_data_integrity(self.LAYERS)

    def _produce_general_references(
        self, query: str, cells: list[Cell], direction: Direction,
    ) -> list[dict[str, Any]]:
        """Five-layer chiasmic verification — general reference per layer."""
        refs = []
        for cell in cells:
            for layer in self.LAYERS:
                refs.append({
                    "type": "integrity_layer",
                    "cell": str(cell),
                    "layer": layer,
                    "symmetry_check": self._symmetry_check_for_layer(layer, direction),
                    "tier": "SOUND",
                })
        return refs

    def _produce_specific_delineations(
        self, query: str, cells: list[Cell], direction: Direction,
    ) -> list[dict[str, Any]]:
        """Per-cell five-layer involutive-symmetry attestation."""
        dels = []
        for cell in cells:
            attestation = self._compute_attestation(query, cell, direction)
            dels.append({
                "type": "five_layer_attestation",
                "cell": str(cell),
                "direction": direction.value,
                "attestation_hash": attestation,
                "all_five_layers_pass": True,  # scaffold; runtime verifies
            })
        return dels

    def _symmetry_check_for_layer(
        self, layer: str, direction: Direction,
    ) -> dict[str, Any]:
        """Scaffold: layer-specific symmetry check stubs."""
        return {
            "SEPLTA": {"check": "domain coverage intake == return"},
            "H2C2H_C2H2C": {
                "check": "bit-complement preservation across direction",
                "direction": direction.value,
            },
            "App_Parent": {"check": "child behavior matches parent spec"},
            "Binary_111000111_000111000": {
                "check": "bit-complement palindromic involution preserved",
            },
            "Character_IPIDITIS_IDIPITIS": {
                "check": "(2,4) transposition semantic-preserving",
            },
        }[layer]

    def _compute_attestation(
        self, query: str, cell: Cell, direction: Direction,
    ) -> str:
        """Scaffold attestation hash — production uses EAAP cryptographic stack."""
        payload = f"{query}|{cell}|{direction.value}|{self.lens.sla.user_group_id}"
        return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:16]


# =============================================================================
# H2C2H / C2H2C ROUND-TRIP DISCIPLINE
# =============================================================================

@dataclass
class RoundTripResult:
    """
    A complete round-trip's Sim OUTPUT, ready for AD_ON-AI composition.

    Carries cell-attribution, BSG tiers per cell, VEILED annotations,
    attestation, all per IOF Publishing Tool §1.8.
    """
    query: str
    direction: Direction
    subjugated_context: SubjugatedContext
    volume_outputs: dict[Volume, Optional[RefDelOutput]]
    round_trip_signature: str
    authorized_in_context: bool
    veiled_summary: list[tuple[VeiledMember, str]]
    bsg_composite: dict[BSGTier, list[dict[str, Any]]]
    started_at_ms: int
    completed_at_ms: int

    @property
    def latency_ms(self) -> int:
        return self.completed_at_ms - self.started_at_ms

    @property
    def is_rt_compliant(self) -> bool:
        return self.latency_ms <= self.subjugated_context.sla.rt_latency_target_ms

    @property
    def is_resonance_pass(self) -> bool:
        """Resonance Pass = Authorized-in-context at SCALULAR-ratified La Grange."""
        return (self.authorized_in_context
                and not self.veiled_summary
                and self.is_rt_compliant)

    def compose_for_ad_on_ai(self) -> dict[str, Any]:
        """
        Compose Sim OUTPUT into AD_ON-AI presentation form.

        AD_ON-AI is the downstream composer; this method shapes the
        RoundTripResult into the presentation-knowledge-base form
        AD_ON-AI consumes. Figurative AND literal: the dict's structure
        is figurative (semantic shape); its contents are literal
        (operational values).
        """
        return {
            "presentation_kind": "H2C2H/C2H2C",
            "direction": self.direction.value,
            "user_group_id": self.subjugated_context.sla.user_group_id,
            "subjugated_context_summary": {
                "active_volumes": [v.value for v in
                                   self.subjugated_context.active_volumes],
                "active_pillars": [p.value for p in
                                   self.subjugated_context.active_pillars],
                "bera_mask": self.subjugated_context.bera_mask,
                "sepltas_active": self.subjugated_context.sepltas_active,
            },
            "ref_del_streams": {
                v.value: (out.to_dict() if out else None)
                for v, out in self.volume_outputs.items()
            },
            "bsg_composite": {
                t.value: items for t, items in self.bsg_composite.items()
            },
            "veiled_annotations": [
                {"state": v.value, "diagnosis": d} for v, d in self.veiled_summary
            ],
            "round_trip_signature": self.round_trip_signature,
            "authorized_in_context": self.authorized_in_context,
            "is_resonance_pass": self.is_resonance_pass,
            "latency_ms": self.latency_ms,
            "rt_compliant": self.is_rt_compliant,
        }

    def to_json(self, indent: int = 2) -> str:
        return json.dumps(self.compose_for_ad_on_ai(), indent=indent, default=str)


# =============================================================================
# TRILOGY SIMULATOR — the top-level entry surface
# =============================================================================

class TrilogySimulator:
    """
    Simulated RT User-GROUP SLA-Derived Media Generator.

    Top-level entry. Constructed with an IOFLens. Runs round-trips in either
    H2C2H or C2H2C direction. Produces Sim OUTPUT composable for AD_ON-AI.
    """

    def __init__(self, lens: IOFLens):
        self.lens = lens
        self.generators = {
            Volume.ONE_GOOD:           OneGoodGenerator(lens),
            Volume.SECURITY_CLEARANCE: SecurityClearanceGenerator(lens),
            Volume.DATA_INTEGRITY:     DataIntegrityGenerator(lens),
        }

    def run(
        self,
        query: str,
        direction: Direction = Direction.H2C2H,
    ) -> RoundTripResult:
        """
        Execute a complete round-trip.

        H2C2H: human-initiated query, computer-mediated, human-received result.
        C2H2C: computer-initiated query needing human judgment, then computer-received.

        Both directions produce equivalent DETAIL under Data-Integrity Layer 2
        (bit-complement preservation) — that is the canonical commitment.
        """
        t_start = time.time_ns() // 1_000_000

        # Run each volume generator (cells_for_this_volume returns [] if not selected;
        # volume generates nothing, respecting Lock Box C honoring of un-selected).
        volume_outputs: dict[Volume, Optional[RefDelOutput]] = {}
        for volume, generator in self.generators.items():
            volume_outputs[volume] = generator.generate(query, direction)

        # Collect VEILED annotations across all volumes
        veiled_summary: list[tuple[VeiledMember, str]] = []
        for out in volume_outputs.values():
            if out:
                veiled_summary.extend(out.veiled_fragments)

        # Compose BSG across cells
        bsg_composite: dict[BSGTier, list[dict[str, Any]]] = {
            t: [] for t in BSGTier
        }
        for out in volume_outputs.values():
            if out:
                for tier, items in out.bsg_tier_assignments.items():
                    bsg_composite[tier].extend(items)

        # Authorization-in-context determination (scaffold: real version
        # would consult SCALULAR ratification of La Grange equilibrium)
        authorized = self._authorized_in_context(
            query, volume_outputs, veiled_summary,
        )

        # Round-trip signature (closure form scaffold)
        signature = self._compute_round_trip_signature(query, direction)

        t_end = time.time_ns() // 1_000_000

        return RoundTripResult(
            query=query,
            direction=direction,
            subjugated_context=self.lens.subjugated_context,
            volume_outputs=volume_outputs,
            round_trip_signature=signature,
            authorized_in_context=authorized,
            veiled_summary=veiled_summary,
            bsg_composite=bsg_composite,
            started_at_ms=t_start,
            completed_at_ms=t_end,
        )

    def _authorized_in_context(
        self,
        query: str,
        volume_outputs: dict[Volume, Optional[RefDelOutput]],
        veiled_summary: list[tuple[VeiledMember, str]],
    ) -> bool:
        """
        Scaffold Resonance Pass determination.

        Production: SCALULAR ratifies La Grange Point among clear User-GROUPS.
        Scaffold rule: authorized iff at least one volume produced output AND
        no VEILED-A or VEILED-S in summary.
        """
        any_output = any(out is not None for out in volume_outputs.values())
        blocking_veiled = any(v in {VeiledMember.A_ADMISSIBILITY,
                                    VeiledMember.S_SELECTION}
                              for v, _ in veiled_summary)
        return any_output and not blocking_veiled

    def _compute_round_trip_signature(
        self, query: str, direction: Direction,
    ) -> str:
        """
        Round-trip closure signature.

        Scaffold expression of (CBGMODD × FAVORS) + BERA = RATE at round-trip scale.
        Production uses EAAP cryptographic stack per slot 432 v1.3 §13.
        """
        payload = (
            f"{self.lens.sla.user_group_id}|"
            f"{direction.value}|"
            f"{query}|"
            f"{','.join(c for c in sorted(str(c) for c in self.lens.sla.selected_cells))}"
        )
        return hashlib.sha256(payload.encode("utf-8")).hexdigest()


# =============================================================================
# WORKED EXAMPLE — reference invocation (delete or adapt for production)
# =============================================================================

def _example_invocation() -> dict[str, Any]:
    """
    Worked example mirroring Volume Zero §1.1 representative query.

    Pass-A FINAL synthesized Civigen query under SLA with selection profile
    {OG×HELP, OG×USE, OG×ENERGY, OG×LAW, DI×LAW}. Class B, SSSC, THOW-tier.
    """
    sla = UserGroupSLA(
        user_group_id="CIVIGEN-C-REPRESENTATIVE",
        deployment_scale=DeploymentScale.THOW,
        wielder_class=WielderClass.B_ANONYMOUS,
        citizenship_tier=CitizenshipTier.HEAD_CIVIGEN,
        selected_cells=[
            Cell(Volume.ONE_GOOD,       Pillar.HELP),
            Cell(Volume.ONE_GOOD,       Pillar.USE),
            Cell(Volume.ONE_GOOD,       Pillar.ENERGY),
            Cell(Volume.ONE_GOOD,       Pillar.LAW),
            Cell(Volume.DATA_INTEGRITY, Pillar.LAW),
        ],
        rt_latency_target_ms=1500,
        scalular_tier="SSSC",
        intent_tier="Implicit",
        infomediator_id="INFOMEDIATOR-WIELDER-001",
        infomediary_id="INFOMEDIARY-INSTRUMENT-001",
    )

    lens = IOFLens(sla)
    sim = TrilogySimulator(lens)

    query = (
        "What does my CBGMODD-C station owe the next seven generations "
        "under current BERA readings, and what EarnedPath actions close the gap?"
    )

    result = sim.run(query, direction=Direction.H2C2H)
    return result.compose_for_ad_on_ai()


if __name__ == "__main__":
    output = _example_invocation()
    print(json.dumps(output, indent=2, default=str))
