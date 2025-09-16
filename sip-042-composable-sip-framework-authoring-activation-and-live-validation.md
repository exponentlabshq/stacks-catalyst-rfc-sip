# Preamble

SIP Number: 042

Title: Composable SIP Framework: Authoring, Activation, and Live Validation

Authors:
* Jane Doe <jane@example.org>
* John Smith <john@domain.tld>
* Alice Example <alice@org.tld>

Consideration: Governance

Type: Consensus

Layer: Consensus (soft fork)

Status: Draft

Created: 2025-09-16

License: BSD 2-Clause

Sign-off:
 - Rafael Cárdenas <rafael@hiro.so> (SIP Editor)
 - Brice Dobry <brice@hiro.so> (Technical CAB)
 - Jude Nelson <jude@stacks.org> (Steering Committee)

Discussions-To: https://github.com/stacksgov/sips/discussions/4242

# Abstract

This SIP introduces a composable framework for SIP authoring with live validation,
aiming to reduce formatting drift and accelerate activation readiness while preserving
SIP-021-style canonical formatting.

# Introduction

The current SIP authoring surfaces present fragmentation and repeated formatting fixes.
This proposal streamlines:

- Standardized preamble fields (no bold labels).
- Live preview to enforce canonical spacing and headings.
- Optional schema hooks for in-browser validation.

Key terms: `tenure`, `Stacker`, and `Bitcoin finality` are preserved semantically.

# Specification

## Components
- Preamble builder
- Section normalizer
- Markdown serializer

## Serialization Rules
```txt
Field lines:    `Label: Value`
Authors:        star-bulleted list
Sign-off:       hyphen-bulleted list
Sections:       H1 top-level only (e.g., # Abstract)
Spacing:        single blank line between blocks
```

## Example Table
| Field | Required | Notes |
|---|---:|---|
| Title | Yes | ≤ 200 chars |
| Type | Yes | “Consensus”, “Standard”, etc. |
| License | Yes | BSD 2-Clause recommended |

## Pseudocode
```pseudo
function buildPreamble(fields):
  lines = ["# Preamble", ""]
  for label,value in fields:
    if value: lines.push(label + ": " + value, "")
  return join(lines, "\n").trim()
```

# Related Work

- SIP-000: Process & governance conventions
- SIP-021: Formatting conventions and activation phases
- Prior art: Live editors (Marked.js), schema-first pipelines

# Backwards Compatibility

Non-breaking to existing SIPs; only affects authoring ergonomics and formatting consistency.
Activation rules remain SIP-specific and unchanged by this proposal.

# Activation

Activation steps:
1. Pilot with authors in one cycle.
2. CAB sign-off on formatting parity.
3. Steering Committee vote to adopt as recommended authoring tool.

# Reference Implementation

https://github.com/stacksgov/sips
https://github.com/stacks-network/stacks-core

# References

- [1] FROST: https://eprint.iacr.org/2020/852.pdf
- [2] WSTS:  https://trust-machines.github.io/wsts/wsts.pdf
- [3] SIP-021 (local): sips-main/sips/sip-021/sip-021-nakamoto.md
