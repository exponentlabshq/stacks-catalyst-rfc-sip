# Preamble

SIP Number: 021

Title: Fast and Reliable Blocks through PoX-assisted Block Propagation

Authors:
* Aaron Blankstein <aaron@hiro.so>
* Charlie Cantoni <charlie@hiro.so>
* Brice Dobry <brice@hiro.so>
* Jacinta Ferrent <jacinta@trustmachines.co>
* Diwaker Gupta <diwaker@hiro.so>
* Marvin Janssen <marvin@ryder.id>
* Jesus Najera <jnajera1917@gmail.com>
* Jude Nelson <jude@stacks.org>
* Ashton Stephens <ashton@trustmachines.co>
* Joey Yandle <joey@trustmachines.co>

Consideration: Governance, Technical, Economics

Type: Consensus

Layer: Consensus (soft fork)

Status: Accepted

Created: 2023-09-28

License: BSD 2-Clause

Sign-off:
 - Rafael Cárdenas <rafael@hiro.so> (SIP Editor)
 - Brice Dobry <brice@hiro.so> (Technical CAB)
 - Jason Schrader <jason@joinfreehold.com> (Governance CAB)
 - MattySTX <mattystx@gmail.com> (Economics CAB)
 - Jude Nelson <jude@stacks.org> (Steering Committee)

# Abstract

This document describes a consensus-breaking change to the Stacks blockchain that enables faster and more reliable Stacks blocks.

In this proposal, miners produce blocks at a fixed cadence independent of sortitions. Stackers use threshold signatures to accept or reject blocks,
preventing forks and ensuring Bitcoin finality properties for confirmed Stacks transactions.

# Introduction

This proposal, dubbed the “Nakamoto” release, separates block production from miner selection. Miners produce blocks during their tenure while Stackers
collectively sign blocks to determine inclusion. The system targets low-latency confirmations, improved reliability, and Bitcoin-level reorg resistance.

The key contribution is replacing unilateral miner confirmation with a signer quorum of Stackers, moving finality policing from miners to Stackers.

# Specification

## Overview
Stackers validate and sign each block before it is appended. Miners produce blocks; Stackers decide inclusion via weighted threshold signatures.

## Chain Structure
- Tenure-based fast blocks
- No microblocks post-Nakamoto
- Tenure start recorded via a TenureChange transaction

## Block Header (Updated)
- Version, chain length, burn spent, consensus hash, parent ID
- Tx Merkle root and state index root
- Miner ECDSA signature, Stacker Schnorr signature, signer bitvector

## Transactions
- TenureChange-BlockFound: Start of a new tenure
- TenureChange-Extend: Extend current tenure budget

## Validation Rules
- Well-formed header and roots
- Valid miner ECDSA and Stacker Schnorr signatures
- All Bitcoin tx since last sortition applied
- TenureChange first in tenure-start block

## Mining Protocol
Two phases: sortition (win tenure) and block production (propose blocks for signing).

# Related Work

This work contrasts with classical PoS systems by preserving open miner entry via BTC spend and separating miner incentives from signer responsibilities.
It builds on the prior SIPs governing PoX and consensus mechanics while replacing microblocks with signed fast blocks.

# Backwards Compatibility

This proposal is a breaking change. Existing contracts remain usable. Microblocks are removed post-activation. Activation is gated to minimize disruption.

# Activation

Two-epoch rollout:
- Epoch 2.5: PoX-4 boot, no Nakamoto rules
- Epoch 3: Nakamoto rules activate

Stackers and miners must follow voting and readiness criteria; thresholds and timing are specified to ensure safe cutover.

# Reference Implementation

https://github.com/stacks-network/stacks-core

# References

- [1] FROST: Flexible Round-Optimized Schnorr Threshold Signatures — https://eprint.iacr.org/2020/852.pdf
- [2] Weighted Schnorr Threshold Signatures (WSTS) — https://trust-machines.github.io/wsts/wsts.pdf
