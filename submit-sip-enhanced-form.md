### Submit SIP — Enhanced Harmonized Form

This is a standardized submission form that harmonizes required fields and conventions from `sip-000` (SIP Process) and an accepted technical SIP (`sip-021`). Copy this template when proposing a new SIP. Keep content concise and adhere to allowed values where specified.

---

### Preamble

- **SIP Number**: (Assigned by SIP Editors)
- **Title**: <Concise title, ≤ 20 words>
- **Authors**: <Name <email>>, <Name <email>>
- **Consideration**: <Governance | Technical | Economics | Ethics | Diversity>
- **Type**: <Consensus (soft fork) | Consensus (hard fork) | Standard | Operation | Meta | Informational>
- **Layer (if Type=Standard or Consensus)**: <Consensus (soft fork) | Consensus (hard fork) | Peer Services | API/RPC | Traits | Applications>
- **Status**: <Draft | Accepted | Recommended | Activation-In-Progress | Ratified | Rejected | Obsolete | Replaced | Withdrawn>
- **Created**: <YYYY-MM-DD>
- **License**: <BSD-2-Clause | BSD-3-Clause | CC0-1.0 | GNU-All-Permissive | GPL-2.0+ | LGPL-2.1+>
- **Discussions-To**: <link or mailing list>
- **Comments-URI (optional)**: <link>
- **Requires (optional)**: <SIP-###, SIP-###>
- **Replaces (optional)**: <SIP-###>
- **Superseded-By (optional)**: <SIP-###>
- **Sign-off (filled during process)**:
  - <Name <email>> (Role)

---

### Abstract

<High-level summary of the proposal and its goals. Aim for ≤ 300 words.>

---

### Copyright

This SIP is made available under the terms of the <License>.

---

### Introduction

<Problem statement, motivation, and overview of the proposed approach. Highlight novelty and why the change is needed.>

---

### Specification

<Detailed technical specification. Include data structures, algorithms, protocol/state-machine changes, interfaces, and validation rules. Provide diagrams or references as necessary. Ensure another implementation can be written from this section alone.>

---

### Backwards Compatibility

<Describe any breaking changes and mitigations. If non-technical, explain compatibility with existing processes.>

---

### Activation

<Explicit, falsifiable criteria and timeline for activation (who does what, how success/failure is measured, timeouts). If voting is required, describe voting mechanics and thresholds.>

---

### Related Work

<Summarize alternatives and why they were not chosen. Include a brief bibliography with enough detail to locate sources.>

---

### Reference Implementations (if any)

- <Repo/branch/tag or artifact links>

---

### Supplemental Materials (optional)

- <Diagrams, datasets, measurements, research PDFs, etc. Open formats only>

---

## Allowed Values and Guidance

- **Type**:
  - Consensus (soft fork), Consensus (hard fork), Standard, Operation, Meta, Informational
- **Consideration**:
  - Governance, Technical, Economics, Ethics, Diversity
- **Layer** (when applicable):
  - Consensus (soft fork), Consensus (hard fork), Peer Services, API/RPC, Traits, Applications
- **Status**:
  - Draft, Accepted, Recommended, Activation-In-Progress, Ratified, Rejected, Obsolete, Replaced, Withdrawn
- **License**:
  - BSD-2-Clause, BSD-3-Clause, CC0-1.0, GNU-All-Permissive, GPL-2.0+, LGPL-2.1+

Author formatting: list as `Full Name <email@example.com>`; multiple entries comma-separated. Use ISO 8601 dates for `Created`.

---

## Minimal Example (sketch)

```
SIP Number: (Assigned)
Title: Fast, reliable block propagation via signer-quorum
Authors: Jane Doe <jane@example.org>, John Smith <john@domain.tld>
Consideration: Technical
Type: Consensus (hard fork)
Layer: Consensus (hard fork)
Status: Draft
Created: 2025-09-11
License: BSD-2-Clause
Discussions-To: https://github.com/stacksgov/sips/discussions/NNN
Requires: SIP-007
Sign-off:
 - (pending)

Abstract
...
```

---

## JSON Schema (for programmatic validation)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://stacksgov.org/schemas/submit-sip-enhanced-form.json",
  "type": "object",
  "required": [
    "title",
    "authors",
    "consideration",
    "type",
    "status",
    "created",
    "license"
  ],
  "properties": {
    "sipNumber": { "type": ["integer", "null"], "minimum": 0 },
    "title": { "type": "string", "minLength": 3, "maxLength": 200 },
    "authors": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["name", "email"],
        "properties": {
          "name": { "type": "string", "minLength": 3 },
          "email": { "type": "string", "format": "email" },
          "affiliation": { "type": "string" }
        }
      },
      "minItems": 1
    },
    "consideration": {
      "type": "array",
      "items": {
        "type": "string",
        "enum": ["Governance", "Technical", "Economics", "Ethics", "Diversity"]
      },
      "minItems": 1,
      "uniqueItems": true
    },
    "type": {
      "type": "string",
      "enum": [
        "Consensus (soft fork)",
        "Consensus (hard fork)",
        "Standard",
        "Operation",
        "Meta",
        "Informational"
      ]
    },
    "layer": {
      "type": ["string", "null"],
      "enum": [
        null,
        "Consensus (soft fork)",
        "Consensus (hard fork)",
        "Peer Services",
        "API/RPC",
        "Traits",
        "Applications"
      ]
    },
    "status": {
      "type": "string",
      "enum": [
        "Draft",
        "Accepted",
        "Recommended",
        "Activation-In-Progress",
        "Ratified",
        "Rejected",
        "Obsolete",
        "Replaced",
        "Withdrawn"
      ]
    },
    "created": { "type": "string", "format": "date" },
    "license": {
      "type": "string",
      "enum": [
        "BSD-2-Clause",
        "BSD-3-Clause",
        "CC0-1.0",
        "GNU-All-Permissive",
        "GPL-2.0+",
        "LGPL-2.1+"
      ]
    },
    "discussionsTo": { "type": ["string", "null"], "format": "uri" },
    "commentsUri": { "type": ["string", "null"], "format": "uri" },
    "requires": {
      "type": "array",
      "items": { "type": "string", "pattern": "^SIP-\\d{3,}$" }
    },
    "replaces": { "type": ["string", "null"], "pattern": "^SIP-\\d{3,}$" },
    "supersededBy": { "type": ["string", "null"], "pattern": "^SIP-\\d{3,}$" },
    "abstract": { "type": "string" },
    "introduction": { "type": "string" },
    "specification": { "type": "string" },
    "backwardsCompatibility": { "type": "string" },
    "activation": { "type": "string" },
    "relatedWork": { "type": "string" },
    "referenceImplementations": {
      "type": "array",
      "items": { "type": "string", "format": "uri" }
    },
    "supplementalMaterials": {
      "type": "array",
      "items": { "type": "string", "format": "uri" }
    }
  }
}
```

---

## Submission Checklist

- [ ] Title ≤ 20 words; clear and specific
- [ ] Authors listed with emails
- [ ] Consideration(s) selected appropriately
- [ ] Type and (if applicable) Layer selected from allowed values
- [ ] License chosen from allowed list
- [ ] Activation criteria are objective and testable
- [ ] Backwards compatibility addressed
- [ ] Related work and references included
- [ ] Supplemental materials included in open formats


