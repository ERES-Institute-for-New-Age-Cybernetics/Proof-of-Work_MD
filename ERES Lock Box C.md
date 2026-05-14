## **ACTION: PUBLISH MACHINE-READABLE SCHEMAS FOR LOCK BOX C \+ VEILED STATE MACHINE**

The following are canonical, parse-time enforceable specifications.

---

### **1\. Lock Box C — Cell Selection Schema**

File: `cell_selection.schema.json`  
Enforces: User-GROUP routes; Instrument never routes; exactly 0–12 cells may light up; each cell is a boolean.

`json`

`{`  
  `"$schema": "https://json-schema.org/draft/2020-12/schema",`  
  `"$id": "https://github.com/ERES-Institute-for-New-Age-Cybernetics/schemas/cell_selection.v1.json",`  
  `"title": "Lock Box C — User-GROUP Cell Selection",`  
  `"description": "The User-GROUP selects which of the 12 (Volume × Pillar) cells light up. The Instrument validates, never routes.",`  
  `"type": "object",`  
  `"properties": {`  
    `"user_group_id": {`  
      `"type": "string",`  
      `"format": "uuid",`  
      `"description": "Globally unique identifier for the User-GROUP instance."`  
    `},`  
    `"selection_timestamp": {`  
      `"type": "string",`  
      `"format": "date-time",`  
      `"description": "Time of selection issuance (UTC)."`  
    `},`  
    `"cells": {`  
      `"type": "object",`  
      `"properties": {`  
        `"I_H": { "type": "boolean", "description": "Volume I — HELP" },`  
        `"I_U": { "type": "boolean", "description": "Volume I — USE" },`  
        `"I_E": { "type": "boolean", "description": "Volume I — ENERGY" },`  
        `"I_L": { "type": "boolean", "description": "Volume I — LAW" },`  
        `"II_H": { "type": "boolean", "description": "Volume II — HELP" },`  
        `"II_U": { "type": "boolean", "description": "Volume II — USE" },`  
        `"II_E": { "type": "boolean", "description": "Volume II — ENERGY" },`  
        `"II_L": { "type": "boolean", "description": "Volume II — LAW" },`  
        `"III_H": { "type": "boolean", "description": "Volume III — HELP" },`  
        `"III_U": { "type": "boolean", "description": "Volume III — USE" },`  
        `"III_E": { "type": "boolean", "description": "Volume III — ENERGY" },`  
        `"III_L": { "type": "boolean", "description": "Volume III — LAW" }`  
      `},`  
      `"required": ["I_H","I_U","I_E","I_L","II_H","II_U","II_E","II_L","III_H","III_U","III_E","III_L"],`  
      `"additionalProperties": false`  
    `},`  
    `"signature": {`  
      `"type": "string",`  
      `"description": "Ed25519 signature of (user_group_id + selection_timestamp + canonical cell bitmask) by User-GROUP key. Instrument verifies, does not generate."`  
    `}`  
  `},`  
  `"required": ["user_group_id", "selection_timestamp", "cells", "signature"],`  
  `"additionalProperties": false`

`}`

Canonical cell order bitmask (for signature):  
`I_H I_U I_E I_L II_H II_U II_E II_L III_H III_U III_E III_L` → 12-bit little-endian.

---

### **2\. VEILED State Machine**

File: `veiled_state_machine.dot` (Graphviz) \+ `veiled_state_machine.schema.json`  
Replaces: All `⊥` markers. Defines legal transitions.

#### 2.1 Graphviz DOT

`dot`

`digraph VEILED_STATE_MACHINE {`  
    `rankdir=LR;`  
    `node [shape=box, style="rounded"];`

    `INIT [label="INIT (unwitnessed)"];`  
    `VEILED_A [label="VEILED-A\n(Admissibility)"];`  
    `VEILED_S [label="VEILED-S\n(Selection)"];`  
    `VEILED_T [label="VEILED-T\n(Tier)"];`  
    `VEILED_L [label="VEILED-L\n(La Grange equilibrium)"];`  
    `WITNESSED [label="WITNESSED\n(terminal, logged)"];`

    `INIT -> VEILED_A [label="admissibility_check()"];`  
    `INIT -> VEILED_S [label="selection_required()"];`  
    `INIT -> VEILED_T [label="tier_required()"];`  
      
    `VEILED_A -> VEILED_S [label="selection_applied()"];`  
    `VEILED_A -> VEILED_T [label="tier_assigned()"];`  
    `VEILED_A -> VEILED_L [label="lagrange_stable()"];`  
      
    `VEILED_S -> VEILED_T [label="tier_resolved()"];`  
    `VEILED_S -> VEILED_L [label="equilibrium_reached()"];`  
      
    `VEILED_T -> VEILED_L [label="lagrange_stable()"];`  
      
    `VEILED_L -> WITNESSED [label="witness_roundtrip()"];`  
      
    `// No transitions from WITNESSED (immutable)`  
    `// No direct INIT -> WITNESSED`  
    `// No backward transitions`

`}`

#### 2.2 JSON Schema for VEILED state instance

File: `veiled_state.schema.json`

`json`

`{`  
  `"$schema": "https://json-schema.org/draft/2020-12/schema",`  
  `"$id": "https://github.com/ERES-Institute-for-New-Age-Cybernetics/schemas/veiled_state.v1.json",`  
  `"title": "VEILED State Record",`  
  `"description": "Replaces all ⊥ markers. A witnessable state machine with legal transitions.",`  
  `"type": "object",`  
  `"properties": {`  
    `"entity_id": { "type": "string" },`  
    `"current_state": {`  
      `"type": "string",`  
      `"enum": ["INIT", "VEILED_A", "VEILED_S", "VEILED_T", "VEILED_L", "WITNESSED"]`  
    `},`  
    `"history": {`  
      `"type": "array",`  
      `"items": {`  
        `"type": "object",`  
        `"properties": {`  
          `"from_state": { "type": "string" },`  
          `"to_state": { "type": "string" },`  
          `"transition": { "type": "string" },`  
          `"timestamp": { "type": "string", "format": "date-time" },`  
          `"trigger_document_hash": { "type": "string", "description": "SHA-256 of document authorizing transition" }`  
        `},`  
        `"required": ["from_state", "to_state", "transition", "timestamp"]`  
      `}`  
    `},`  
    `"lagrange_parameter": {`  
      `"type": "number",`  
      `"description": "Present only if current_state = VEILED_L. Dimensionless equilibrium value ∈ [0,1].",`  
      `"minimum": 0,`  
      `"maximum": 1`  
    `},`  
    `"witness_proof": {`  
      `"type": "string",`  
      `"description": "Present only if current_state = WITNESSED. EAAP-attested receipt hash."`  
    `}`  
  `},`  
  `"required": ["entity_id", "current_state", "history"],`  
  `"allOf": [`  
    `{`  
      `"if": {`  
        `"properties": { "current_state": { "const": "VEILED_L" } }`  
      `},`  
      `"then": { "required": ["lagrange_parameter"] }`  
    `},`  
    `{`  
      `"if": {`  
        `"properties": { "current_state": { "const": "WITNESSED" } }`  
      `},`  
      `"then": { "required": ["witness_proof"] }`  
    `}`  
  `]`

`}`

---

### **3\. SCALULAR Register Declaration (Lock Box E)**

File: `scalular_register.schema.json`

`json`

`{`  
  `"$schema": "https://json-schema.org/draft/2020-12/schema",`  
  `"$id": "https://github.com/ERES-Institute-for-New-Age-Cybernetics/schemas/scalular_register.v1.json",`  
  `"title": "Lock Box E — SCALULAR Active Register Declaration",`  
  `"description": "Before any SCALULAR name (TRADES, INTUIT, PRE, TEACH-TECH, i_I, SELF_$ELF, GREENBOX_WAITING_ROOM, SCALULAR) is evaluated, the active IOF register must be declared.",`  
  `"type": "object",`  
  `"properties": {`  
    `"scalular_name": {`  
      `"type": "string",`  
      `"enum": ["TRADES", "INTUIT", "PRE", "TEACH-TECH", "i_I", "SELF_$ELF", "GREENBOX_WAITING_ROOM", "SCALULAR"]`  
    `},`  
    `"active_register": {`  
      `"type": "string",`  
      `"enum": ["BIOLOGICAL", "SOCIO", "TECHNICAL"],`  
      `"description": "Per Lock Box D, honest round-trip requires all three. Per Lock Box E, each SCALULAR evaluation declares exactly one."`  
    `},`  
    `"evaluation_context": {`  
      `"type": "string",`  
      `"format": "uri",`  
      `"description": "REF-DEL pointer to the specific claim or operation invoking this SCALULAR name."`  
    `},`  
    `"timestamp": { "type": "string", "format": "date-time" },`  
    `"witnessed_by": {`  
      `"type": "array",`  
      `"items": { "type": "string", "enum": ["JAS", "EMA", "DAL", "MIEVM"] },`  
      `"minItems": 1`  
    `}`  
  `},`  
  `"required": ["scalular_name", "active_register", "evaluation_context", "timestamp", "witnessed_by"],`  
  `"additionalProperties": false`

`}`

---

### **4\. Volume Zero Dependency Declaration**

File: `volume_zero.deps.json`  
Required for parse-time enforcement of "Volume Zero must be read first."

`json`

`{`  
  `"dependency_graph": {`  
    `"Volume_Zero": { "depends_on": [], "read_first": true },`  
    `"Volume_I": { "depends_on": ["Volume_Zero"], "read_first": false },`  
    `"Volume_II": { "depends_on": ["Volume_Zero", "Volume_I"], "read_first": false },`  
    `"Volume_III": { "depends_on": ["Volume_Zero", "Volume_I", "Volume_II"], "read_first": false }`  
  `},`  
  `"runtime_rule": "parse(Volume_Zero) → init_IOF_Lens() → parse(Volume_I) → parse(Volume_II) → parse(Volume_III)",`  
  `"violation_response": "REJECT with code E001: Volume Zero not instantiated"`

`}`

---

## **Implementation Status**

| Artifact | Purpose | Location (canonical) |
| :---- | :---- | :---- |
| `cell_selection.schema.json` | Lock Box C | `/schemas/lockbox_c/` |
| `veiled_state_machine.dot` | VEILED state graph | `/schemas/veiled/` |
| `veiled_state.schema.json` | VEILED instance validation | `/schemas/veiled/` |
| `scalular_register.schema.json` | Lock Box E | `/schemas/lockbox_e/` |
| `volume_zero.deps.json` | Parse-order enforcement | `/schemas/deps/` |

All schemas are CARE Commons Attribution License v2.1 (CCAL v2.1).  
Enforcement in `eres_trilogy.py` § `LockBoxValidator` — runtime-reject on violation.

---

It is so.  
The computer may now parse, validate, and obey. The Instrument routes nothing.

— *JAS · ERES Maestro*  
*Lock Boxes A–E enforced. CCAL v2.1.*

