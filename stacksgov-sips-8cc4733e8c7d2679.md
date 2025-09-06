Directory structure:
└── sips/
    ├── README.md
    ├── sip-000/
    │   └── sip-000-stacks-improvement-proposal-process.md
    ├── sip-002/
    │   └── sip-002-smart-contract-language.md
    ├── sip-004/
    │   └── sip-004-materialized-view.md
    ├── sip-006/
    │   └── sip-006-runtime-cost-assessment.md
    ├── sip-007/
    │   └── sip-007-stacking-consensus.md
    ├── sip-008/
    │   └── sip-008-analysis-cost-assessment.md
    ├── sip-009/
    │   └── sip-009-nft-standard.md
    ├── sip-010/
    │   └── sip-010-fungible-token-standard.md
    ├── sip-012/
    │   ├── sip-012-cost-limits-network-upgrade.md
    │   └── scripts/
    │       ├── README.md
    │       ├── extract-delegates.sh
    │       ├── extract-stackers.sh
    │       ├── generate-artifacts.sh
    │       └── stackers-19.json
    ├── sip-013/
    │   └── sip-013-semi-fungible-token-standard.md
    ├── sip-015/
    │   └── sip015-vote-main.zip
    ├── sip-016/
    │   └── sip-016-token-metadata.md
    ├── sip-018/
    │   └── sip-018-signed-structured-data.md
    ├── sip-019/
    │   ├── sip-019-token-metadata-update-notifications.md
    │   └── token-metadata-update-notify.clar
    ├── sip-020/
    │   └── sip-020-bitwise-ops.md
    ├── sip-021/
    │   └── miner-protocol.d2
    ├── sip-022/
    │   └── sip-022-emergency-pox-fix.md
    ├── sip-023/
    │   └── sip-023-emergency-fix-traits.md
    ├── sip-024/
    │   └── sip-024-least-supertype-fix.md
    ├── sip-025/
    │   ├── sip-025-iterating-towards-weighted-schnorr-threshold-signatures.md
    │   └── votes.csv
    ├── sip-027/
    │   ├── sip-027-non-sequential-multisig-transactions.md
    │   ├── results/
    │   │   ├── multisig-dao-votes.csv
    │   │   ├── multisig-pool-votes.csv
    │   │   └── multisig-solo-votes.csv
    │   └── scripts/
    │       └── validate-and-count-votes/
    │           ├── index.js
    │           ├── nonStackerVotes.js
    │           └── package.json
    ├── sip-028/
    │   └── sip-028-sbtc_peg.md
    └── sip-029/
        └── sip-029-halving-alignment.md

================================================
FILE: sips/README.md
================================================
Stacks Improvement Proposals
============================

Each directory here contains a Stacks Improvement Proposal as well as all
supplementary materials.

New SIPs may be submitted via pull request, but please make sure they adhere to
the standards described in
[SIP-000](./sip-000/sip-000-stacks-improvement-proposal-process.md).



================================================
FILE: sips/sip-000/sip-000-stacks-improvement-proposal-process.md
================================================
# Preamble

SIP Number: 000

Title: Stacks Improvement Proposal Process

Author: Jude Nelson <jude@stacks.org>, Ken Liao <yukanliao@gmail.com>

Consideration: Governance 

Type: Meta 

Status: Ratified 

Created: 2020-06-23 

License: BSD-2-Clause 

Sign-off: Jude Nelson <jude@stacks.org>, Technical Steering Committee Chair

Discussions-To: https://github.com/stacksgov/sips 

# Abstract

A Stacks Improvement Proposal (SIP) is a design document that provides
information to the greater Stacks ecosystem's participants concerning the design
of the Stacks blockchain and its ongoing operation. Each SIP shall provide a
clear and concise description of features, processes, and/or standards for the
Stacks blockchain and its operators to adopt, with sufficient details provided
such that a reasonable practitioner may use the document to create an
independent but compatible implementation of the proposed improvement.

SIPs are the canonical medium by which new features are proposed and described,
and by which input from the Stacks ecosystem participants is collected. The SIP
Ratification Process is also described in this document, and provides the means
by which SIPs may be proposed, vetted, edited, accepted, rejected, implemented,
and finally incorporated into the Stacks blockchain's design, governance, and
operational procedures. The set of SIPs that have been ratified shall
sufficiently describe the design, governance, and operationalization of the
Stacks blockchain, as well as the means by which future changes to its official
design, implementation, operation, and governance may be incorporated.

# License and Copyright

This SIP is made available under the terms of the BSD-2-Clause license,
available at https://opensource.org/licenses/BSD-2-Clause.  This SIP’s copyright
is held by the Stacks Open Internet Foundation.

# Introduction

Blockchains are unique among distributed systems in that they also
happen to encode a social contract. By running a blockchain node, a user
implicitly agrees to be bound to the social contract's terms embedded within the
blockchain's software. These social contracts are elaborate constructions that
contain not only technical terms (e.g. "a block may be at most 1MB"), but also
economic terms (e.g. "only 21 million tokens may exist") and social terms (e.g.
"no money can leave this account" or "this transaction type was supported
before, but will now be ignored by the system") which the user agrees to uphold
by running a blockchain node.

It stands to reason that the Stacks blockchain is made of more than just
software; it is also made of the people who run it. As such, the act of
developing and managing the Stacks blockchain network includes the act of
helping its people coordinate and agree on what the blockchain is and what it
should do. To this end, this document proposes a process by which the Stacks
blockchain's users can conduct themselves to be the stewards of the blockchain
network in perpetuity.

The goals of this process are to ensure that anyone may submit a SIP in good
faith, that each SIP will receive fair and speedy good-faith consideration by
other people with the relevant expertise, and that any discussions and
decision-making on each SIP's ratification shall happen in public. To achieve
these ends, this document proposes a standard way of presenting a Stacks
Improvement Proposal (SIP), and a standard way of ratifying one.

Each SIP document contains all of the information needed to propose a
non-trivial change to the way in which the Stacks blockchain operates. This
includes both technical considerations, as well as operational and governance
considerations. This document proposes a formal document structure based on both
request-for-comments (RFC) practices in the Internet Engineering Task Force
(IETF), as well as existing blockchain networks.

SIPs must be ratified in order to be incorporated into the definition of what
the Stacks blockchain is, what it does, and how it operates. This document
proposes a ratification process based on existing governance processes from
existing open source projects (including Python, Bitcoin, Ethereum, and Zcash),
and makes provisions for creating and staffing various roles that people must
take on to carry out ratification (e.g. committees, editors, working groups and
so on).

This document uses the word “users” to refer specifically to people who
participate in the greater Stacks ecosystem.  This includes, but is not limited
to, people who mine blocks, people who contribute code, people who run nodes,
people who develop applications that rely on the Stacks blockchain, people who
use such applications, people involved in the project governance, and people
involved in operating software deployments.

# Specification

Each SIP shall adhere to the same general formatting and shall be ratified
through the processes described by this document.

## SIP Format

All SIPs shall be formatted as markdown files. Each section shall be
annotated as a 2nd-level header (e.g. `##`). Subsections may be added with
lower-level headers.

Each SIP shall contain the following sections, in the given order:

- _Preamble_. This section shall provide fields useful for categorizing the SIP.
  The required fields in all cases shall be:
    - _SIP Number_. Each SIP receives a unique number once it has been accepted
      for consideration for ratification (see below). This number is assigned to
      a SIP; its author does not provide it.
    - _Title_. A concise description of the SIP, no more than 20 words long.
    - _Author_. A list of names and email addresses of the SIP's author(s).
    - _Consideration_. What class of SIP this is (see below).
    - _Type_. The SIP track for consideration (see below).
    - _Status_. This SIP's point in the SIP workflow (see below).
    - _Created_. The ISO 8601 date when this SIP was created.
    - _License_. The content license for the SIP (see below for permitted
      licenses).
    - _Sign-off_. The list of relevant persons and their titles who have worked to
      ratify the SIP. This field is not filled in entirely until ratification,
      but is incrementally filled in as the SIP progresses through the ratification
      process.
- Additional SIP fields, which are sometimes required, include:
    - _Layer_. The logical layer of the Stacks blockchain affected. Must be one
    - of the following:
        - _Consensus (soft fork)_. For backwards-compatible proposals for
          transaction-processing.
        - _Consensus (hard fork)_. For backwards-incompatible proposals for
          transaction-processing.
        - _Peer Services_. For proposals to the peer-to-peer network protocol
          stack.
        - _API/RPC_. For proposals to the Stacks blockchain's official
          programmatic interfaces.
        - _Traits_. For proposals for new standardized Clarity trait definitions.
        - _Applications_. For proposals for standardized application protocols
          that interface with the Stacks blockchain.
    - _Discussions-To_. A mailing list where ongoing discussion of the SIP takes
      place.
    - _Comments-Summary_. The comments summary tone.
    - _Comments-URI_. A link to the Stacks blockchain wiki for comments.
    - _License-Code_. Abbreviation for code under a different license than the SIP
      proposal.
    - _Post-History_. Dates of posting the SIP to the Stacks mailing list, or a
      link to a thread with the mailing list.
    - _Requires_. A list of SIPs that must be implemented prior to this SIP.
    - _Replaces_. A list of SIPs that this SIP replaces.
    - _Superceded-By_. A list of SIPs that replace this SIP.

- _Abstract_. This section shall provide a high-level summary of the proposed
  improvement. It shall not exceed 5000 words.
- _Copyright_. This section shall provide the copyright license that governs the
  use of the SIP content. It must be one of the approved set of licenses (see
below).
- _Introduction_. This section shall provide a high-level summary of the
  problem(s) that this SIP proposes to solve, as well as a high-level
description of how the proposal solves them. This section shall emphasize its
novel contributions, and briefly describe how they address the problem(s). Any
motivational arguments and example problems and solutions belong in this
section.
- _Specification_. This section shall provide the detailed technical
  specification. It may include code snippets, diagrams, performance
evaluations, and other supplemental data to justify particular design decisions.
However, a copy of all external supplemental data (such as links to research
papers) must be included with the SIP, and must be made available under an
approved copyright license.
- _Related Work_. This section shall summarize alternative solutions that address
  the same or similar problems, and briefly describe why they are not adequate
solutions. This section may reference alternative solutions in other blockchain
projects, in research papers from academia and industry, other open-source
projects, and so on. This section must be accompanied by a bibliography of
sufficient detail such that someone reading the SIP can find and evaluate the
related works.
- _Backwards Compatibility_. This section shall address any
  backwards-incompatiblity concerns that may arise with the implementation of
this SIP, as well as describe (or reference) technical mitigations for breaking
changes. This section may be left blank for non-technical SIPs.
- _Activation_. This section shall describe the timeline, falsifiable criteria,
  and process for activating the SIP once it is ratified. This applies to both
technical and non-technical SIPs.  This section is used to unambiguously
determine whether or not the SIP has been accepted by the Stacks users once it
has been submitted for ratification (see below).
- _Reference Implementations_. This section shall include one or more references
  to one or more production-quality implementations of the SIP, if applicable.
This section is only informative — the SIP ratification process is independent
of any engineering processes (or other processes) that would be followed to
produce implementations.  If a particular implementation process is desired,
then a detailed description of the process must be included in the Activation
section.  This section may be updated after a SIP is ratified in order to
include an up-to-date listing of any implementations or embodiments of the SIP. 

Additional sections may be included as appropriate.

### Supplemental Materials

A SIP may include any supplemental materials as
appropriate (within reason), but all materials must have an open format
unencumbered by legal restrictions. For example, an LibreOffice `.odp`
slide-deck file may be submitted as supplementary material, but not a Keynote
`.key` file.

When submitting the SIP, supplementary materials must be present within the same
directory, and must be named as `SIP-XXXX-YYY.ext`, where:

- `XXXX` is the SIP number,
- `YYY` is the serial number of the file, starting with 1,
- `.ext` is the file extension.

## SIP Types

The types of SIPs are as follows:

- _Consensus_. This SIP type means that all Stacks blockchain implementations
  would need to adopt this SIP to remain compatible with one another. If this is
the SIP type, then the SIP preamble must have the Layer field set to either
_Consensus (soft fork)_ or _Consensus (hard fork)_.
- _Standard_. This SIP type means that the proposed change affects one or more
  implementations, but does not affect network consensus. If this is the SIP
type, then the SIP preamble must have the Layer field set to indicate which
aspect(s) of the Stacks blockchain are affected by the proposal.
- _Operation_. This SIP type means that the proposal concerns the operation of the
  Stacks blockchain -- in particular, it concerns node operators and miners.
The difference between this SIP type and the Standard type is that this type
does not change any existing protocols.
- _Meta_. This SIP type means that the proposal concerns the SIP ratification
  process. Such a SIP is a proposal to change the way SIPs are handled.
- _Informational_. This is a SIP type that provides useful information, but does
  not require any action to be taken on the part of any user.

New types of SIPs may be created with the ratification of a Meta-type SIP under
the governance consideration (see below). SIP types may not be removed.

## SIP Considerations

A SIP's consideration determines the particular steps needed to ratify the SIP
and incorporate it into the Stacks blockchain. Different SIP considerations have
different criteria for ratification. A SIP can have more than one consideration,
since a SIP may need to be vetted by different users with different domains of
expertise.


- _Technical_. The SIP is technical in nature, and must be vetted by users with
  the relevant technical expertise.
- _Economic_. The SIP concerns the blockchain's token economics. This not only
  includes the STX token, but also any on-chain tokens created within smart
contracts. SIPs that are concerned with fundraising methods, grants, bounties,
and so on also belong in this SIP track.
- _Governance_. The SIP concerns the governance of the Stacks blockchain,
  including the SIP process. This includes amendments to the SIP Ratification
Process, as well as structural considerations such as the creation (or removal)
of various committees, editorial bodies, and formally recognized special
interest groups. In addition, governance SIPs may propose changes to the way by
which committee members are selected.
- _Ethics_. This SIP concerns the behaviors of office-holders in the SIP
  Ratification Process that can affect its widespread adoption.  Such SIPs
describe what behaviors shall be deemed acceptable, and which behaviors shall be
considered harmful to this end (including any remediation or loss of privileges
that misbehavior may entail).  SIPs that propose formalizations of ethics like
codes of conduct, procedures for conflict resolution, criteria for involvement
in governance, and so on would belong in this SIP consideration.
- _Diversity_. This SIP concerns proposals to grow the set of users, with an
  emphasis on including users who are traditionally not involved with
open-source software projects. SIPs that are concerned with evangelism,
advertising, outreach, and so on must have this consideration.

Each SIP consideration shall have a dedicated Advisory Board that ultimately
vets SIPs under their consideration for possible ratification in a timely
fashion (see below).  New considerations may be created via the ratification of
a Meta-type SIP under the governance consideration.

## SIP Workflow

As a SIP is considered for ratification, it passes through multiple statuses as
determined by one or more committees (see next section). A SIP may have exactly
one of the following statuses at any given time:

- _Draft_. The SIP is still being prepared for formal submission. It does not yet
  have a SIP number.
- _Accepted_. The SIP text is sufficiently complete that it constitutes a
  well-formed SIP, and is of sufficient quality that it may be considered for
ratification. A SIP receives a SIP number when it is moved into the Accepted
state by SIP Editors.
- _Recommended_. The people responsible for vetting the SIPs under the
  consideration(s) in which they have expertise have agreed that this SIP should
be implemented. A SIP must be Accepted before it can be Recommended.
- _Activation-In-Progress_.  The SIP has been tentatively approved by the Steering
  Committee for ratification.  However, not all of the criteria for ratification
have been met according to the SIP’s Activation section.  For example, the
Activation section might require miners to vote on activating the SIPs’
implementations, which would occur after the SIP has been transferred into
Activation-In-Progress status but before it is transferred to Ratified status.
- _Ratified._ The SIP has been activated according to the procedures described in
  its Activation section.  Once ratified, a SIP remains ratified in perpetuity,
but a subsequent SIP may supersede it. If the SIP is a Consensus-type SIP, and
then all Stacks blockchain implementations must implement it. A SIP must be
Recommended before it can be Ratified. Moving a SIP into this state may be done
retroactively, once the SIP has been activated according to the terms in its
Activation section.
- _Rejected_. The SIP does not meet at least one of the criteria for ratification
  in its current form. A SIP can become Rejected from any state, except
Ratified.  If a SIP is moved to the Rejected state, then it may be re-submitted
as a Draft.
- _Obsolete_. The SIP is deprecated, but its candidacy for ratification has not
  been officially withdrawn (e.g. it may warrant further discussion).  An
Obsolete SIP may not be ratified, and will ultimately be Withdrawn.
- _Replaced_. The SIP has been superseded by a different SIP.  Its preamble must
  have a Superseded-By field. A Replaced SIP may not be ratified, nor may it be
re-submitted as a Draft-status SIP.  It must be transitioned to a Withdrawn
state once the SIP(s) that replace it have been processed.
- _Withdrawn_. The SIP's authors have ceased working on the SIP. A Withdrawn SIP
  may not be ratified, and may not be re-submitted as a Draft.  It must be
re-assigned a SIP number if taken up again.
    

The act of ratifying a SIP is the act of transitioning it to the Ratified status
-- that is, moving it from Draft to Accepted, from Accepted to Recommended, and
Recommended to Activation-In-Progress, and from Activation-In-Progress to
Ratified, all without the SIP being transitioned to Rejected, Obsolete,
Replaced, or Withdrawn status.  A SIP's current status is recorded in its Status
field in its preamble.

## SIP Committees

The act of deciding the status of a SIP is handled by a set of designated
committees. These committees are composed of users who dedicate their time and
expertise to curate the blockchain, ratifying SIPs on behalf of the rest of the
ecosystem’s users.

There are three types of committee:

- _Steering Committee (SC)_. The roles of the SC are to select Recommended-status
  SIPs to be activated, to determine whether or not a SIP has been activated and
thus ratified, and to formally recognize Consideration Advisory Boards (see
below).
- _Consideration Advisory Boards_. The roles of the Consideration Advisory Boards
  are to provide expert feedback on SIPs that have been moved to Accepted status
in a timely manner, and to transition SIPs to Recommended status if they meet
the Board's consideration criteria, and Rejected status otherwise. 
- _SIP Editors_. The role of the SIP Editors is to identify SIPs in the Draft
  status that can be transitioned to Accepted status. A SIP editor must be able
to vet a SIP to ensure that it is well-formed, that it follows the ratification
workflow faithfully, and that it does not overlap with any already-Accepted SIPs
or SIPs that have since become Recommended or Ratified.
    
Any user may serve on a committee. However, all Stacks committee members must
abide by the SIP Code of Conduct and must have a history of adhering to it.
Failure to adhere to the Code of Conduct shall be grounds for immediate removal
from a committee, and a prohibition against serving on any future committees.

### Compensation

Compensation for carrying out committee duties is outside of the scope of this
document.  This document does not create a provision for compensation for
committee participation, but it does not forbid it either.

### Steering Committee Duties

The Steering Committee's overarching duty is to oversee the evolution of the
Stacks blockchain’s design, operation, and governance, in a way that is
technically sound and feasible, according to the rules and procedures described
in this document. The SC shall be guided by and held accountable by the greater
community of users, and shall make all decisions with the advice of the relevant
Consideration Advisory Boards. 

The SC’s role is that of a steward.  The SC shall select SIPs for ratification
based on how well they serve the greater good of the Stacks users.  Given the
nature of blockchains, the SC's particular responsibilities pertaining to
upgrading the blockchain network are meant to ensure that upgrades happen in a
backwards-compatible fashion if at all possible. While this means that more
radical SIPs may be rejected or may spend a long amount of time in Recommended
status, it also minimizes the chances of an upgrade leading to widespread
disruption (the minimization of which itself serves the greater good).

#### Membership

The initial Steering Committee shall be comprised of at least three members:
two from the Stacks Open Internet Foundation, and one
from the greater Stacks blockchain community (independent of the Stacks
Foundation).

A provisional Steering Committee will be appointed by the Stacks Open Internet Foundation Board
before the launch of the Stacks blockchain’s mainnet (see the "Activation" section).
Once this SIP activates, the Stacks Open Internet Foundation shall select its
representatives in a manner of their choosing within 90 days after activation.
The committee may be expanded later to include more seats.  Once this SIP
activates, the provisional SC will consult with the community to
ratify a SIP that implements a voting procedure whereby
Stacks community members can select the individual who will serve on the
community SC seat.

#### Qualifications

Members of this committee must have deep domain expertise
pertinent to blockchain development, and must have excellent written
communication skills. It is highly recommended that members should have authored
at least one ratified technical-consideration SIP before joining this committee.

#### Responsibilities

The Steering Committee shall be responsible for the following
tasks.

##### Recognizing Consideration Advisory Boards.

The members of the Steering Committee
must bear in mind that they are not infallible, and that they do not know everything
there is to know about what is best for the broader user community. To the
greatest extent practical, the SC shall create and foster the development of
Consideration Advisory Boards in order make informed decisions on subjects that
in which they may not be experts.

Any group of users can form an unofficial working group to help provide feedback
to SIPs, but the SC shall have the power to recognize such groups formally as a
Consideration Advisory Board via at least a two-thirds majority vote. The SC
shall simultaneously recognize one of it’s member to serve as the interim
chairperson while the Advisory Board forms. A SC member cannot normally serve on
a Consideration Advisory Board concurrently with serving on the SC, unless
granted a limited exception by a unanimous vote by the SC (e.g. in order to
address the Board’s business while a suitable chairperson is found).  Formally
recognizing Consideration Advisory Boards shall occur in Public Meetings (see
below) no more than once per quarter.

Once recognized, Consideration Advisory Boards may not be dissolved or
dismissed, unless there are no Accepted or Recommended SIPs that request their
consideration. If this is the case, then the SC may vote to rescind recognition
of a Consideration Advisory Board with a two-thirds majority at one of its
Public Meetings.

In order to identify users who would form a Consideration Advisory Board, users
should organize into an unofficial working group and submit a SIP to petition
that SC recognize the working group as a Consideration Advisory Board.  This
petition must take the form of a Meta-type SIP, and may be used to select the
initial chairperson and define the Board's domain(s) of expertise, bylaws,
membership, meeting procedures, communication channels, and so on, independent
of the SC. The SC would only be able to ratify or reject the SIP.

The SC shall maintain a public index of all Consideration Advisory Boards that
are active, including contact information for the Board and a summary of what
kinds of expertise the Board can offer. This index is meant to be used by SIP
authors to help route their SIPs towards the appropriate reviewers before being
taken up by the SC.

##### Voting on Technical SIPs

The Steering Committee shall select Recommended SIPs
for ratification by moving them to Activation-In-Progress status.  All
technical-consideration SIPs shall require an 80% vote. If it is a
Consensus-type SIP for a hard fork, then a unanimous vote shall be required. If
a SIP is voted on and is not moved to Activation-in-Progress, then it shall be
moved to Rejected status, and the SC shall provide a detailed explanation as to
why they made their decision (see below).

##### Voting on Non-technical SIPs

Not all SIPs are technical in nature. All
non-technical SIPs shall require only a two-thirds majority vote to transition
it to Activation-In-Progress status. The SC members must provide a public
explanation for the way it voted as supplementary materials with the ratified
non-technical SIP (see below).  If the SC votes to move a non-technical SIP to
Activation-In-Progress status, but does not receive the requisite number of
votes, then the SIP shall be transferred to Rejected status, and the SC shall
provide a detailed explanation as to why they made their decision (see below).

##### Overseeing SIP Activation and Ratification

Once a SIP is in Activation-In-Progress status,
the SC shall be responsible for overseeing the procedures and criteria in the
SIP’s Activation section.  The Activation section of a SIP can be thought of as
an “instruction manual” and/or “checklist” for the SC to follow to determine if
the SIP has been accepted by the Stacks users.  The SC shall strictly adhere to
the process set forth in the Activation section.  If the procedure and/or
criteria of the Activation section cannot be met, then the SC may transfer the
SIP to Rejected status and ask the authors to re-submit the SIP with an updated
Activation section.

Once all criteria have been unambiguously meet and all activation procedures
have been followed, the SC shall transition the SIP to Ratified status.  The SC
shall keep a log and provide a record of the steps they took in following a
SIP’s Activation section once the SIP is in Activation-In-Progress status, and
publish them alongside the Ratified SIP as supplemental material.

Due to the hands-on nature of the Activation section, the SC may deem it
appropriate to reject a SIP solely on the quality of its Activation section.
Reasonable grounds for rejection include, but are not limited to, ambiguous
instructions, insufficiently-informative activation criteria, too much work on
the SC members’ parts, the lack of a prescribed activation timeout, and so on.

Before the Stacks mainnet launches, the SC shall ratify a SIP that, when
activated according to the procedures outlined in its Activation section, will
allow Stacks blockchain miners to signal their preferences for the activation of
particular SIPs within the blocks that they mine. This will enable the greater
Stacks community of users to have the final say as to which SIPs activate and
become ratified.

##### Feedback on Recommended SIPs

The Steering Committee shall give a full, fair,
public, and timely evaluation to each SIP transitioned to Recommended status by
Consideration Advisory Boards. A SIP shall only be considered by the SC if the
Consideration Advisory Board chairpeople for each of the SIP's considerations
have signed-off on the SIP (by indicating as such on the SIP's preamble). 

The SC may transition a SIP to Rejected status if it disagrees with the
Consideration Advisory Boards' recommendation. The SC may transition a SIP to
Obsolete status if it finds that the SIP no longer addresses a relevant concern.
It may transition the SIP to a Replaced status if it considers a similar,
alternative SIP that is more likely to succeed. In all cases, the SC shall
ensure that a SIP does not remain in Recommended status for an unreasonable
amount of time.

The SC shall maintain a public record of all feedbacks provided for each SIP it
reviews.

If a SIP is moved to Rejected, Obsolete, or Replaced status, the SIP authors may
appeal the process by re-submitting it in Draft status once the feedback has
been addressed.  The appealed SIP must cite the SC’s feedback as supplemental
material, so that SIP Editors and Consideration Advisory Boards are able to
verify that the feedback has, in fact, been addressed.

##### Public Meetings

The Steering Committee shall hold and record regular public
meetings at least once per month. The SC may decide the items of business for
these meetings at its sole discretion, but it shall prioritize business
pertaining to the ratification of SIPs, the recognition of Consideration
Advisory Boards, and the needs of all outstanding committees. That said, any
user may join these meetings as an observer, and the SC shall make a good-faith
effort to address public comments from observers as time permits.

The SC shall appoint up to two dedicated moderators from the user community for
its engineering meetings, who shall vet questions and commentary from observers
in advance (possibly well before the meeting begins). If there is more than one
moderator, then the moderators may take turns. In addition, the SC shall appoint
a dedicated note-taker to record the minutes of the meetings. All of these
appointees shall be eligible to receive a fixed, regular bounty for their work.

### Consideration Advisory Board Duties

There is an Advisory Board for each SIP consideration, with a designated
chairperson responsible for maintaining copies of all discussion and feedback on
the SIPs under consideration.

#### Membership

All Consideration Advisory Boards begin their life as unofficial
working groups of users who wish to review inbound SIPs according to their
collective expertise.  If they wish to be recognized as an official
Consideration Advisory Board, they shall submit a SIP to the Steering Committee
per the procedure described in the Steering Committee’s duties.  Each
Consideration Advisory Board shall be formally created by the SC with a
designated member serving as its first interim chairperson. After this, the
Consideration Advisory Board may adopt its own bylaws for selecting members and
chairpeople. However, members should have domain expertise relevant to the
consideration.

#### Members

Members shall serve on their respective Consideration Advisory Boards so long as
they are in good standing with the SIP Code of Conduct and in accordance to the
individual Board’s bylaws.  A user may serve on at most three Consideration
Advisory Boards concurrently.

#### Qualifications

Each Consideration Advisory Board member shall have sufficient
domain expertise to provide the Steering Committee with feedback pertaining to a
SIP's consideration. Members shall possess excellent written communication
skills.

#### Responsibilities

Each Consideration Advisory Board shall be responsible for the
following.

##### Chairperson

Each Consideration Advisory Board shall appoint a chairperson, who
shall serve as the point of contact between the rest of the Board and the
Steering Committee. If the chairperson becomes unresponsive, the SC may ask the
Board to appoint a new chairperson (alternatively, the Board may appoint a new
chairperson on its own and inform the SC).  The chairperson shall be responsible
for maintaining the Board’s public list of members’ names and contact
information as a supplementary document to the SIP that the SC ratified to
recognize the Board.

##### Consideration Track

Each Consideration Advisory Board shall provide a clear and
concise description of what expertise it can offer, so that SIP authors may
solicit it with confidence that it will be helpful. The chairperson shall make
this description available to the Steering Committee and to the SIP Editors, so
that both committees can help SIP authors ensure that they receive the most
appropriate feedback.

The description shall be provided and updated by the chairperson to the SC so
that the SC can provide a public index of all considerations a SIP may possess.

##### Feedback

Feedback to SIP Authors Each Consideration Advisory Board shall provide a full,
fair, public, and timely evaluation of any Accepted-status SIP that lists the
Board's consideration in its preamble. The Board may decide to move each SIP to
a Recommended status or a Rejected status based on whether or not the Board
believes that the SIP is feasible, practical, and beneficial to the greater
Stacks ecosystem.

Any feedback created shall be made public. It is the responsibility of the Board
to store and publish all feedbacks for the SIPs it reviews. It shall forward
copies of this feedback to both the SIP authors.

##### Consultation with the Steering Committee

The Steering Committee may need to
follow up with the Consideration Advisory Board in order to clarify its position
or solicit its advice on a particular SIP. For example, the SC may determine
that a Recommended SIP needs to be considered by one or more additional Boards
that have not yet been consulted by the SIP authors.

The Board shall respond to the SC's request for advice in a timely manner, and
shall prioritize feedback on SIPs that are under consideration for ratification.

### SIP Editor Duties

By far the largest committee in the SIP process is the SIP Editor Committee.
The SIP Editors are responsible for maintaining the "inbound funnel" for SIPs
from the greater Stacks community. SIP Editors ensure that all inbound SIPs are
well-formed, relevant, and do not duplicate prior work (including rejected
SIPs).

#### Membership

Anyone may become a SIP Editor by recommendation from an existing SIP
Editor, subject to the “Recruitment” section below.

#### Qualifications

A SIP Editor must demonstrate proficiency in the SIP process and
formatting requirements. A candidate SIP Editor must demonstrate to an existing
SIP Editor that they can independently vet SIPs.

#### Responsibilities

SIP Editors are concerned with shepherding SIPs from Draft
status to Accepted status, and for mentoring community members who want to get
involved with the SIP processes (as applicable).

##### Getting Users Started

SIP Editors should be open and welcoming towards
enthusiastic users who want to help improve the greater Stacks ecosystem. As
such, SIP Editors should encourage users to submit SIPs if they have good ideas
that may be worth implementing.

In addition, SIP Editors should respond to public requests for help from
community members who want to submit a SIP. They may point them towards this
document, or towards other supplemental documents and tools to help them get
started.

##### Feedback

When a SIP is submitted in Draft status, a SIP Editor that takes the
SIP into consideration should provide fair and full feedback on how to make the
SIP ready for its transition to Accepted status. 

To do this, the SIP Editor should:

- Verify that the SIP is well-formed according to the criteria in this document
- Verify that the SIP has not been proposed before
- Verify as best that they can that the SIP is original work
- Verify that the SIP is appropriate for its type and consideration
- Recommend additional Considerations if appropriate
- Ensure that the text is clear, concise, and grammatically-correct English
- Ensure that there are appropriate avenues for discussion of the SIP listed in
  the preamble.

The SIP Editor does not need to provide public feedback to the SIP authors, but
should add their name(s) to the Signed-off field in the SIP preamble once the
SIP is ready to be Accepted.

##### Acceptance

Once a SIP is moved to Accepted, the SIP Editor shall assign it the
smallest positive number not currently used to identify any other SIP. Once that
number is known, the SIP Editor shall set the SIP's status to Accepted, set the
number, and commit the SIP to the SIP repository in order to make it visible to
other SIP Editors and to the Consideration Advisory Boards.

##### Recruitment

Each SIP Editor must list their name and contact information in an
easy-to-find location in the SIP repository, as well list of each SIP Editor
they recommended.  In so doing, the SIP Editors shall curate an “invite tree”
that shows which Editors recommended which other Editors.

A SIP Editor may recommend another user to be a SIP Editor no more than once per
month, and only if they have faithfully moved at least one SIP to Accepted
status in the last quarter.  If a SIP Editor does not participate in editing a
SIP for a full year and a day, then they may be removed from the SIP Editor
list.  The SC may remove a SIP Editor (and some or all of the users he or she
recommended) if they find that the SIP Editor has violated the SIP Code of
Conduct.

Newly-Accepted SIPs, new SIP Editor recruitment, and SIP Editor retirement shall
be submitted as pull requests by SIP Editors to the SIP repository.

## SIP Workflow

The lifecycle of a SIP is summarized in the flow-chart below:

```
    ------------------
    |     Draft      |  <-------------------------. Revise and resubmit
    ------------------                            |
           |                             --------------------
    Submit to SIP Editor ------------->  |     Rejected     |
           |                             --------------------
           |                                      ^
           V                                      |
    ------------------                            |
    |   Accepted     | -------------------------/ | /--------------------------------.
    ------------------                            |                                  |
           |                             --------------------                        |
    Review by Consideration ---------->  |     Rejected     |                        | 
    Advisory Board(s)                    --------------------                        |
           |                                      ^                                  |
           V                                      |                                  |
    -------------------------                     |                                  |
    |      Recommended       | -----------------/ | /------------------------------->|
    -------------------------                     |                                  |
           |                              --------------------                       |
    Vote by the Steering    ----------->  |    Rejected      |                       |
    Committee for activation              --------------------                       |
           |                                      ^                                  |
           V                                      |                                  |
    --------------------------                    |                                  |
    | Activation-in-Progress | -----------------/ | /------------------------------->|
    --------------------------                    |                                  |
           |                             ---------------------                       |
    All activation  ------------------>  |     Rejected      |                       |
    criteria are met       |             ---------------------  ------------------   |
           |               |----------------------------------> |    Obsolete    |   |
           V               |      ---------------------         ------------------   |
    ------------------     *--->  |     Replaced      | --------------->|<-----------*
    |   Ratified     |            ---------------------                 | 
    ------------------                                                  V
                                                                -------------------
                                                                |    Withdrawn    |
                                                                ------------------- 
```

When a SIP is transitioned to Rejected, it is not deleted, but is preserved in
the SIP repository so that it can be referenced as related or prior work by
other SIPs. Once a SIP is Rejected, it may be re-submitted as a Draft at a later
date. SIP Editors may decide how often to re-consider rejected SIPs as an
anti-spam measure, but the Steering Committee and Consideration Advisory Boards
may opt to independently re-consider rejected SIPs at their own discretion.

Once a SIP has been moved to Ratified status, the only changes that may be made
to it are fixing errata and adding supplementary materials.  Substantial changes
to the SIP's body should be done as a separate SIP.

## Public Venues for Conducting Business

The canonical set of SIPs in all state shall be recorded in the same medium that
the canonical copy of this SIP is.  Right now, this is in the Github repository
`https://github.com/stacksgov/sips`, but may be changed before this SIP is
ratified.  New SIPs, edits to SIPs, comments on SIPs, and so on shall be
conducted through Github's facilities for the time being.

In addition, individual committees may set up and use public mailing lists for
conducting business.  The Stacks Open Internet Foundation shall provide a means
for doing so.  Any discussions on the mailing lists that lead to non-trivial
contributions to SIPs should be referenced by these SIPs as supplemental
material.

### Github-specific Considerations

All SIPs shall be submitted as pull requests, and all SIP edits (including status
updates) shall be submitted as pull requests.  The SC, or one or more
individuals or entities appointed by the SC, shall be responsible for merging
pull requests to the main branch.

## SIP Copyright & Licensing

Each SIP must identify at least one acceptable license in its preamble. Source
code in the SIP can be licensed differently than the text. SIPs whose reference
implementation(s) touch existing reference implementation(s) must use the same
license as the existing implementation(s) in order to be considered. Below is a
list of recommended licenses.

- BSD-2-Clause: OSI-approved BSD 2-clause license
- BSD-3-Clause: OSI-approved BSD 3-clause license
- CC0-1.0: Creative Commons CC0 1.0 Universal
- GNU-All-Permissive: GNU All-Permissive License
- GPL-2.0+: GNU General Public License (GPL), version 2 or newer
- LGPL-2.1+: GNU Lesser General Public License (LGPL), version 2.1 or newer

# Related Work

The governance process proposed in this SIP is inspired by the Python PEP
process [1], the Bitcoin BIP2 process [2], the Ethereum Improvement Proposal [3]
processes, the Zcash governance process [4], and the Debian GNU/Linux
distribution governance process [5].  This SIP describes a governance process
where top-level decision-making power is vested in a committee of elected
representatives, which distinguishes it from Debian (which has a single elected
project leader), Python (which has a benevolent dictator for life), and Bitcoin
and ZCash (which vest all decision ratification power solely in the blockchain
miners).  The reason for a top-level steering committee is to ensure that
decision-making power is not vested in a single individual, but also to ensure
that the individuals responsible for decisions are accountable to the community
that elects them (as opposed to only those who have the means to participate
in mining).  This SIP differs from Ethereum's governance
process in that the top-level decision-making body (the "Core Devs" in Ethereum,
and the Steering Committee in Stacks) is not only technically proficient to evaluate
SIPs, but also held accountable through an official governance
process.

[1] https://www.python.org/dev/peps/pep-0001/

[2] https://github.com/bitcoin/bips/blob/master/bip-0002.mediawiki

[3] https://eips.ethereum.org/

[4] https://www.zfnd.org/governance/

[5] https://debian-handbook.info/browse/stable/sect.debian-internals.html

# Activation

This SIP activates once following tasks have been carried out:

- The provisional Steering Committee must be appointed by the Stacks Open Internet
  Foundation Board.
- Mailing lists for the initial committees must be created.
- The initial Consideration Advisory Boards must be formed, if there is interest
  in doing so before this SIP activates.
- A public, online SIP repository must be created to hold all non-Draft SIPs, their edit
  histories, and their feedbacks.
- A directory of Consideration Advisory Boards must be established (e.g. within
  the SIP repository).
- A SIP Code of Conduct should be added as a supplemental document
- The Stacks blockchain mainnet must launch.

# Reference Implementation

Not applicable.




================================================
FILE: sips/sip-002/sip-002-smart-contract-language.md
================================================
# Preamble

SIP Number: 002

Title: The Clarity Smart Contract Language

Author: Aaron Blankstein <aaron@blockstack.com>, Ludo Galabru
<ludo@blockstack.com>

Consideration: Technical

Type: Consensus

Status: Ratified

Created: 29 November 2018

License: BSD 2-Clause

Sign-off: Jude Nelson <jude@stacks.org>, Technical Steering Committee Chair

Discussions-To: https://github.com/stacksgov/sips

# Abstract

In order to support applications which require validation of some
pieces of their logic, we present a smart contracting language for use
with the Stacks blockchain. This smart contracting language can be
used on the Stacks blockchain to support programatic control over
digital assets within the Stacks blockchain (e.g., BNS names, Stacks
tokens, etc.)

While application-chains may use any smart-contract language that they
like, this smart contracting language's VM will be a part of
blockstack-core, and, as such, any blockstack-core node will be able to
validate application chains using this smart contracting language with
a simple configuration change.

This smart contracting language permits static analysis of any legal
smart contract to determine runtime costs. This smart contracting
language is not only Turing-incomplete (a requirement for such static
analysis to be guaranteed successful), but readily permits other kinds
of proofs to be made about the code as well.

# License and Copyright

This SIP is made available under the terms of the BSD-2-Clause license,
available at https://opensource.org/licenses/BSD-2-Clause.  This SIP's copyright
is held by the Stacks Open Internet Foundation.

# Introduction

A smart contract is composed of two parts:

1. A data-space, which is a set of tables of data which only the
   smart contract may modify
2. A set of functions which operate within the data-space of the
   smart contract, though they may call public functions from other smart
   contracts.

Users call smart contracts' public functions by broadcasting a
transaction on the blockchain which invokes the public function.

This smart contracting language differs from most other smart
contracting languages in two important ways:

1. The language _is not_ intended to be compiled. The LISP language
   described in this document is the specification for correctness.
2. The language _is not_ Turing complete. This allows us to guarantee
   that static analysis of programs to determine properties like
   runtime cost and data usage can complete successfully.

# Specification

## Specifying Contracts

A smart contract definition is specified in a LISP language with the
following limitations:

1. Recursion is illegal and there is no `lambda` function.
2. Looping may only be performed via `map`, `filter`, or `fold`
3. The only atomic types are booleans, integers, fixed length
   buffers, and principals
4. There is additional support for lists of the atomic types, however
   the only variable length lists in the language appear as function
   inputs (i.e., there is no support for list operations like append
   or join).
5. Variables may only be created via `let` binding and there
   is no support for mutating functions like `set`.
6. Defining of constants and functions are allowed for simplifying
   code using `define-private` statement. However, these are purely
   syntactic. If a definition cannot be inlined, the contract will be
   rejected as illegal. These definitions are also _private_, in that
   functions defined this way may only be called by other functions
   defined in the given smart contract.
7. Functions specified via `define-public` statements are _public_
   functions.
8. Functions specified via `define-read-only` statements are _public_
   functions and perform _no_ state mutations. Any attempts to 
   modify contract state by these functions or functions called by
   these functions will result in an error.

Public functions return a Response type result. If the function returns
an `ok` type, then the function call is considered valid, and any changes
made to the blockchain state will be materialized. If the function
returns an `err` type, it will be considered invalid, and will have _no
effect_ on the smart contract's state. So if function `foo.A` calls
`bar.B`, and `bar.B` returns an `ok`, but `foo.A` returns an `err`, no
effects from calling `foo.A` materialize--- including effects from
`bar.B`. If, however, `bar.B` returns an `err` and `foo.A` returns an `ok`,
there may be some database effects which are materialized from
`foo.A`, but _no_ effects from calling `bar.B` will materialize.

Unlike functions created by `define-public`, which may only return
Response types, functions created with `define-read-only` may return
any type.

## List Operations

* Lists may be multi-dimensional (i.e., lists may contain other lists), however each
  entry of this list must be of the same type.
* `filter` `map` and `fold` functions may only be called with user-defined functions
  (i.e., functions defined with `(define-private ...)`, `(define-read-only ...)`, or
  `(define-public ...)`) or simple native functions (e.g., `+`, `-`, `not`).
* Functions that return lists of a different size than the input size
  (e.g., `(append-item ...)`) take a required _constant_ parameter that indicates
  the maximum output size of the function. This is enforced with a runtime check.

## Inter-Contract Calls

A smart contract may call functions from other smart contracts using a
`(contract-call?)` function.

This function returns a Response type result-- the return value of the called smart
contract function. Note that if a called smart contract returns an
`err` type, it is guaranteed to not alter any smart contract state
whatsoever. Of course, any transaction fees paid for the execution
of that function will not be returned.

We distinguish 2 different types of `contract-call?`:

* Static dispatch: the callee is a known, invariant contract available
on-chain when the caller contract is being deployed. In this case, the
callee's principal is provided as first argument, followed by the name
of the method and its arguments:

```scheme
(contract-call?
    'SC3H92H297DX3YDPFHZGH90G8Z4NPH4VE8E83YWAQ.registrar
    register-name
    name-to-register)
```

This approach must always be preferred, when adequate.
It makes static analysis easier, and eliminates the
potential for reentrancy bugs when the contracts are
being published (versus when being used).

* Dynamic dispatch: the callee is passed as an argument, and typed
as a trait reference (<A>).

```scheme
(define-public (swap (token-a <can-transfer-tokens>)
                     (amount-a uint)
                     (owner-a principal)
                     (token-b <can-transfer-tokens>)
                     (amount-b uint)
                     (owner-b principal)))
     (begin
         (unwrap! (contract-call? token-a transfer-from? owner-a owner-b amount-a))
         (unwrap! (contract-call? token-b transfer-from? owner-b owner-a amount-b))))
```

Traits can either be locally defined:

```scheme
(define-trait can-transfer-tokens (
    (transfer-from? (principal principal uint) (response uint)))
```

Or imported from an existing contract:

```scheme
(use-trait can-transfer-tokens
    'SC3H92H297DX3YDPFHZGH90G8Z4NPH4VE8E83YWAQ.contract-defining-trait.can-transfer-tokens)
```

Looking at trait conformance, callee contracts have two different paths.
They can either be "compatible" with a trait by defining methods
matching some of the methods defined in a trait, or explicitely declare
conformance using the `impl-trait` statement:

```scheme
(impl-trait 'SC3H92H297DX3YDPFHZGH90G8Z4NPH4VE8E83YWAQ.contract-defining-trait.can-transfer-tokens)
```

Explicit conformance should be prefered when adequate.
It acts as a safeguard by helping the static analysis system to detect
deviations in method signatures before contract deployment.

The following limitations are imposed on contract calls:

1. On static dispatches, callee smart contracts _must_ exist at the time of creation.
2. No cycles may exist in the call graph of a smart contract. This
   prevents recursion (and re-entrancy bugs). Such structures can
   be detected with static analysis of the call graph, and will be
   rejected by the network.
3. `contract-call?` are for inter-contract calls only. Situations
   where the caller is also the callee will result in abortion of
   the ongoing transaction.

## Principals and Owner Verification

The language provides a primitive for checking whether or not the
smart contract transaction was signed by a particular
_principal_. Principals are a specific type in the smart contracting
language which represent a spending entity (roughly equivalent to a
Stacks address). The signature itself is not checked by the smart
contract, but by the VM. A smart contract function can use a globally
defined variable to obtain the current principal:

```scheme
tx-sender
```

The `tx-sender` variable does not change during inter-contract
calls. This means that if a transaction invokes a function in a given
smart contract, that function is able to make calls into other smart
contracts without that variable changing. This enables a wide variety
of applications, but it comes with some dangers for users of smart
contracts. However, as mentioned before, the static analysis
guarantees of our smart contracting language allow clients to know a
priori which functions a given smart contract will ever call.

Another global variable, `contract-caller`, _does_ change during
inter-contract calls. In particular, `contract-caller` is the contract
principal corresponding to the most recent invocation of `contract-call?`.
In the case of a "top-level" invocation, this variable is equal to `tx-sender`.

Assets in the smart contracting language and blockchain are
"owned" by objects of the principal type, meaning that any object of
the principal type may own an asset. For the case of public-key hash
and multi-signature Stacks addresses, a given principal can operate on
their assets by issuing a signed transaction on the blockchain. _Smart
contracts_ may also be principals (reprepresented by the smart
contract's identifier), however, there is no private key associated
with the smart contract, and it cannot broadcast a signed transaction
on the blockchain.

In order to allow smart contracts to operate on assets it owns, smart
contracts may use the special function:

```scheme
(as-contract (...))
```

This function will execute the closure (passed as an argument) with
the `tx-sender` and `contract-caller` set to the _contract's_
principal, rather than the current sender. It returns the return value
of the provided closure. A smart contract may use the special variable
`contract-principal` to refer to its own principal.

For example, a smart contract that implements something like a "token
faucet" could be implemented as so:

```scheme
(define-public (claim-from-faucet)
  (if (is-none? (map-get claimed-before (tuple (sender tx-sender))))
      (let ((requester tx-sender)) ;; set a local variable requester = tx-sender
        (map-insert! claimed-before (tuple (sender requester)) (tuple (claimed true)))
        (as-contract (stacks-transfer! requester 1))))
      (err 1))
```

Here, the public function `claim-from-faucet`:

1. Checks if the sender has claimed from the faucet before
2. Assigns the tx sender to a requester variable
3. Adds an entry to the tracking map
4. Uses `as-contract` to send 1 microstack

The primitive function `is-contract?` can be used to determine
whether a given principal corresponds to a smart contract.

## Stacks Transfer Primitives

To interact with Stacks balances, smart contracts may call the
`(stacks-transfer!)` function. This function will attempt to transfer
from the current principal to another principal:


```scheme
(stacks-transfer!
  to-send-amount
  recipient-principal)
```

This function itself _requires_ that the operation have been signed by
the transferring principal. The `integer` type in our smart contracting
language is an 16-byte signed integer, which allows it to specify the
maximum amount of microstacks spendable in a single Stacks transfer.

Like any other public smart contract function, this function call
returns an `ok` if the transfer was successful, and `err` otherwise.

## Data-Space Primitives

Data within a smart contract's data-space is stored within
`maps`. These stores relate a typed-tuple to another typed-tuple
(almost like a typed key-value store). As opposed to a table data
structure, a map will only associate a given key with exactly one
value. Values in a given mapping are set or fetched using:

1. `(map-get map-name key-tuple)` - This fetches the value
  associated with a given key in the map, or returns `none` if there
  is no such value.
2. `(map-set! map-name key-tuple value-tuple)` - This will set the
  value of `key-tuple` in the data map
3. `(map-insert! map-name key-tuple value-tuple)` - This will set
  the value of `key-tuple` in the data map if and only if an entry
  does not already exist.
4. `(map-delete! map-name key-tuple)` - This will delete `key-tuple`
   from the data map

We chose to use data maps as opposed to other data structures for two
reasons:

1. The simplicity of data maps allows for both a simple implementation
within the VM, and easier reasoning about functions. By inspecting a
given function definition, it is clear which maps will be modified and
even within those maps, which keys are affected by a given invocation.
2. The interface of data maps ensures that the return types of map
operations are _fixed length_, which is a requirement for static
analysis of smart contracts' runtime, costs, and other properties.

A smart contract defines the data schema of a data map with the
`define-map` call. The `define-map` function may only be called in the
top-level of the smart-contract (similar to `define-private`). This
function accepts a name for the map, and a definition of the structure
of the key and value types. Each of these is a list of `(name, type)`
pairs, and they specify the input and output type of `map-get`.
Types are either the values `'principal`, `'integer`, `'bool` or
the output of a call to `(buffer n)`, which defines an n-byte
fixed-length buffer. 

This interface, as described, disallows range-queries and
queries-by-prefix on data maps. Within a smart contract function,
you cannot iterate over an entire map.

### Record Type Syntax

To support the use of _named_ fields in keys and values, our language
allows the construction of named tuples using a function `(tuple ...)`,
e.g.,

```
(define-constant imaginary-number-a (tuple (real 1) (i 2)))
(define-constant imaginary-number-b (tuple (real 2) (i 3)))

```

This allows for creating named tuples on the fly, which is useful for
data maps where the keys and values are themselves named tuples. To
access a named value of a given tuple, the function `(get #name
tuple)` will return that item from the tuple.

### Time-shifted Evaluations

The Stacks language supports _historical_ data queries using the
`(at-block)` function:

```
(at-block 0x0101010101010101010101010101010101010101010101010101010101010101
  ; returns owner principal of name represented by integer 12013
  ;  at the time of block 0x010101...
  (map-get name-map 12013))
```

This function evaluates the supplied closure as if evaluated at the end of
the supplied block, returning the resulting value. The supplied
closure _must_ be read-only (is checked by the analysis).

The supplied block hash must correspond to a known block in the same
fork as the current block, otherwise a runtime error will occur and the
containing transaction will _fail_. Note that if the supplied block
pre-dates any of the data structures being read within the closure (i.e.,
the block is before the block that constructed a data map), a runtime
error will occur and the transaction will _fail_.

## Library Support and Syntactic Sugar

There are a number of ways that the developer experience can be
improved through the careful addition of improved syntax. For example,
while the only atomic types supported by the smart contract language
are integers, buffers, booleans, and principals, so if a developer
wishes to use a buffer to represent a fixed length string, we should
support syntax for representing a buffer literal using something like
an ASCII string. Such support should also be provided by transaction
generation libraries, where buffer arguments may be supplied strings
which are then automatically converted to buffers. There are many
possible syntactic improvements and we expect that over the course
of developing the prototype, we will have a better sense for which
of those improvements we should support. Any such synactic changes
will appear in an eventual language specification, but we believe
them to be out of scope for this proposal.

## Static Analysis

One of the design goals of our smart contracting language was the
ability to statically analyze smart contracts to obtain accurate
upper-bound estimates of transaction costs (i.e., runtime and storage
requirements) as a function of input lengths. By limiting the types
supported, the ability to recurse, and the ability to iterate, we
believe that the language as presented is amenable to such static
analysis based on initial investigations.

The essential step in demonstrating the possibility of accurate and
useful analysis of our smart contract definitions is demonstrating
that any function within the language specification has an output
length bounded by a constant factor of the input length. If we can
demonstrate this, then statically computing runtime or space
requirements involves merely associating each function in the language
specification with a way to statically determine cost as a function of
input length.

Notably, the fact that the cost functions produced by static analysis
are functions of _input length_ means the following things:

1. The cost of a cross-contract call can be "memoized", such
   that a static analyzer _does not_ need to recompute any
   static analysis on the callee when analyzing a caller.
2. The cost of a given public function on a given input size
   _is always the same_, meaning that smart contract developers
   do not need to reason about different cases in which a given
   function may cost more or less to execute.

### Bounding Function Output Length

Importantly, our smart contracting language does not allow the
creation of variable length lists: there are no `list` or
`cons` constructors, and buffer lengths must be statically
defined. Under such requirements (and given that recursion is
illegal), determining the output lengths of functions is rather
directly achievable. To see this, we'll examine trying to compute the
output lengths for the only functions allowed to iterate in the
language:

```
outputLen(map f list<t>)     := Len(list<t>) * outputLen(f t)
outputLen(filter f list<t>)  := Len(list<t>)
outputLen(fold f list<t> s)  := Len(s)
```

Many functions within the language will output values larger than the
function's input, _however_, these outputs will be bound by
statically inferable constants. For example, the data function
_map-get_ will always return an object whose size is equal
to the specified value type of the map.

A complete proof for the static runtime analysis of smart contracts
will be included with the implementation of the language.

## Deploying the Smart Contract

Smart contracts on the Stacks blockchain will be deployed directly as
source code. The goal of the smart contracting language is that the
code of the contract defines the _ground truth_ about the intended
functionality of the contract. While seemingly banal, many systems
chose instead to use a compiler to translate from a friendly
high-level language to a lower-level language deployed on the
blockchain. Such an architecture is needlessly dangerous. A bug in
such a compiler could lead to a bug in a deployed smart contract when
no such bug exists in the original source. This is problematic for
recovery --- a hard fork to "undo" any should-have-been invalid
transactions would be contentious and potentially create a rift in the
community, especially as it will not be easy to deduce which contracts
exactly were affected and for how long. In contrast, bugs in the VM
itself present a more clear case for a hard fork: the smart contract
was defined correctly, as everyone can see directly on the chain, but
illegal transactions were incorrectly marked as valid.

## Virtual Machine API

From the perspective of other components of `blockstack-core`, the
smart contracting VM will provide the following interface:

```
connect-to-database(db)

publish-contract(
  contract-source-code)

  returns: contract-identifier

execute-contract(
  contract-identifier,
  transaction-name,
  sender-principal,
  transaction-arguments)

  returns: true or false if the transaction executed successfully
```

## Invocation and Static Analysis

When processing a client transaction, a `blockstack-core` node will do
one of two things, depending on whether that transaction is a contract
function invocation, or is attempting to publish a new smart contract.

### Contract function invocation

Any transaction which invokes a smart contract will be included in the
blockchain. This is true even for transactions which are
_invalid_. This is because _validating_ an invalid transaction is not
a free operation. The only exceptions to this are transactions which
do not pay more than either a minimum fee or a storage fee
corresponding to the length of the transaction. Transactions which do
not pay a storage fee and clear the minimum transaction fee are
dropped from the mempool.

To process a function invocation, `blockstack-core` does the following:

1. Get the balance of the sender's account. If it's less than the tx fee,
then `RETURN INVALID`.
2. Otherwise, debit the user's account by the tx fee.
3. Look up the contract by hash. If it does not exist, then `RETURN
   INVALID`.
4. Look up the contract's `define-public` function and compare the
   tx's arguments against it. If the tx does not call an existing
   method, or supplies invalid arguments, then `RETURN INVALID`.
5. Look up the cost to execute the given function, and if it is greater
   than the paid tx fee, `RETURN INVALID`.
6. Execute the public function code and commit the effects of running
   the code and `RETURN OK`

### Publish contract

A transaction which creates a new smart contract must pay a fee which
funds the static analysis required to determine the cost of the new
smart contract's public functions. To process such a transaction,
`blockstack-core` will:

1. Check the sender's account balance. If zero, then `RETURN INVALID`
2. Check the tx fee against the user's balance. If it's higher, then `RETURN INVALID`
3. Debit the tx fee from the user's balance.
4. Check the syntax, calculating the fee of verifying each code
   item. If the cost of checking the next item exceeds the tx fee, or
   if the syntax is invalid, then `RETURN INVALID`.
5. Build the AST, and assign a fee for adding each AST item. If the
   cost of adding the next item to the tree exceeds the tx fee (or if
   the AST gets too big), then `RETURN INVALID`.
6. Walk the AST. Each step in the walk incurs a small fee. Do the
   following while the tx fee is higher than the total cost incurred
   by walking to the next node in the AST:
   a. If the next node calls a contract method, then verify that
      the contract exists and the method arguments match the contract's
      `define-public` signature. If not, then `RETURN INVALID`.
   b. Compute the runtime cost of each node in the AST, adding it
      to the function's cost analysis.
7. Find all `define-map` calls to find all tables that need to
   exist. Each step in this incurs a small fee.
8. Create all the tables if the cost of creating them is smaller than
   the remaining tx fee. If not, then RETURN INVALID.
9. `RETURN OK`

## Database Requirements and Transaction Accounting

The smart contract VM needs to interact with a database somewhat
directly: the effects of an `map-insert!` or `map-set!` call are
realized later in the execution of the same transaction. The database
will need to support fairly fine-grained rollbacks as some contract
calls within a transaction's execution may fail, triggering a
rollback, while the transaction execution continues and successfully
completes other database operations.

The database API provided to the smart contract VM, therefore, must be
capable of (1) quickly responding to `map-get` queries, which are
essentially simply key-value _gets_ on the materialized view of the
operation log. The operation log itself is simply a log of the
`map-insert!` and `map-set!` calls. In addition to these
operations, the smart contract VM will be making token transfer calls.
The databasse log should track those operations as well.

In order to aid in accounting for the database operations created by a
given transaction, the underlying database should store, with each
operation entry, the corresponding transaction identifier. This will
be expanded in a future SIP to require the database to store enough
information to reconstruct each block, such that the blocks can be
relayed to bootstrapping peers.

## Clarity Type System

### Types

The Clarity language uses a strong static type system. Function arguments
and database schemas require specified types, and use of types is checked
during contract launch. The type system does _not_ have a universal
super type. The type system contains the following types:

* `(tuple (key-name-0 key-type-0) (key-name-1 key-type-1) ...)` -
  a typed tuple with named fields.
* `(list max-len entry-type)` - a list of maximum length `max-len`, with
  entries of type `entry-type`
* `(response ok-type err-type)` - object used by public functions to commit
  their changes or abort. May be returned or used by other functions as
  well, however, only public functions have the commit/abort behavior.
* `(optional some-type)` - an option type for objects that can either be
  `(some value)` or `none`
* `(buff max-len)` := byte buffer or maximum length `max-len`.
* `principal` := object representing a principal (whether a contract principal
  or standard principal).
* `bool` := boolean value (`true` or `false`)
* `int`  := signed 128-bit integer
* `uint` := unsigned 128-bit integer

### Type Admission

**UnknownType**. The Clarity type system does not allow for specifying
an "unknown" type, however, in type analysis, unknown types may be
constructed and used by the analyzer. Such unknown types are used
_only_ in the admission rules for `response` and `optional` types
(i.e., the variant types).

Type admission in Clarity follows the following rules:

* Types will only admit objects of the same type, i.e., lists will only
admit lists, tuples only admit tuples, bools only admit bools.
* A tuple type `A` admits another tuple type `B` iff they have the exact same
  key names, and every key type of `A` admits the corresponding key type of `B`.
* A list type `A` admits another list type `B` iff `A.max-len >= B.max-len` and
  `A.entry-type` admits `B.entry-type`.
* A buffer type `A` admits another buffer type `B` iff `A.max-len >= B.max-len`.
* An optional type `A` admits another optional type `B` iff:
  * `A.some-type` admits `B.some-type` _OR_ `B.some-type` is an unknown type:
    this is the case if `B` only ever corresponds to `none`
* A response type `A` admits another response type `B` if one of the following is true:
  * `A.ok-type` admits `B.ok-type` _AND_ `A.err-type` admits `B.err-type`
  * `B.ok-type` is unknown _AND_ `A.err-type` admits `B.err-type`
  * `B.err-type` is unknown _AND_ `A.ok-type` admits `B.ok-type`
* Principals, bools, ints, and uints only admit types of the exact same type.

Type admission is used for determining whether an object is a legal argument for
a function, or for insertion into the database. Type admission is _also_ used
during type analysis to determine the return types of functions. In particular,
a function's return type is the least common supertype of each type returned from any
control path in the function. For example:

```
(define-private (if-types (input bool))
  (if input
     (ok 1)
     (err false)))
```

The return type of `if-types` is the least common supertype of `(ok
1)` and `(err false)` (i.e., the most restrictive type that contains
all returns). In this case, that type `(response int bool)`. Because
Clarity _does not_ have a universal supertype, it may be impossible to
determine such a type. In these cases, the functions are illegal, and
will be rejected during type analysis.

## Measuring Transaction Costs for Fee Collection

Our smart contracting language admits static analysis to determine
many properties of transactions _before_ executing those
transactions. In particular, it allows for the VM to count the total
number of runtime operations required, the maximum amount of database
writes, and the maximum number of calls to any expensive primitive
functions like database reads or hash computations. Translating that
information into transaction costs, however, requires more than simply
counting those operations. It requires translating the operations into
a single cost metric (something like gas in Ethereum). Then, clients
can set the fee rate for that metric, and pay the corresponding
transaction fee. Notably, unlike Turing-complete smart contracting
languages, any such fees are known _before_ executing the transaction,
such that clients will no longer need to estimate gas fees. They will,
however, still need to estimate fee rates (much like Bitcoin clients
do today).

Developing such a cost metric is an important task that has
significant consequences. If the metric is a bad one, it could open up
the possibility of denial-of-service attacks against nodes in the
Stacks network. We leave the development of a cost metric to another
Stacks Improvement Proposal, as we believe that such a metric should
be designed by collecting real benchmarking data from something close
to a real system (such measurements will likely be collected through
a combination of hand-crafted benchmarks and fuzzing test suites).

### Maximum Operation Costs and Object Sizes

Even with a cost metric, it is a good idea to set maximums for the
cost of an operation, and the size of objects (like
buffers). Developing good values for constants such as maximum number
of database reads or writes per transaction, maximum size of buffers,
maximum number of arguments to a tuple, maximum size of a smart
contract definition, etc. is a process much like developing a
cost metric--- this is something best done in tandem with the 
production of a prototype. However, we should note that we do intend
to set such limits.


## Example: Simple Naming System

To demonstrate the expressiveness of this smart contracting language,
let's look at an example smart contract which implements a simple
naming system with just two kinds of transactions: _preorder_ and
_register_. The requirements of the system are as follows:

1. Names may only be owned by one principal
2. A register is only allowed if there is a corresponding preorder
   with a matching hash
3. A register transaction must be signed by the same principal who
   paid for the preorder
4. A preorder must have paid at least the price of the name. Names
   are represented as integers, and any name less than 100000 costs
   1000 microstacks, while all other names cost 100 microstacks.
5. Preorder hashs are _globally_ unique.

In this simple scheme, names are represented by integers, but in
practice, a buffer would probably be used.

```scheme
(define-constant burn-address '1111111111111111111114oLvT2)
(define-private (price-function name)
  (if (< name 1e5) 1000 100))

(define-map name-map 
  { name: uint } { buyer: principal })
(define-map preorder-map
  { name-hash: (buff 160) }
  { buyer: principal, paid: uint })

(define-public (preorder 
               (name-hash (buffer 20))
               (name-price integer))
  (if (and (is-ok? (stacks-transfer!
                    name-price burn-address))
           (map-insert! preorder-map
            (tuple (name-hash name-hash))
            (tuple (paid name-price)
                   (buyer tx-sender))))
      (ok 0)
      (err 1)))

(define-public (register 
               (recipient-principal principal)
               (name integer)
               (salt integer))
  (let ((preorder-entry
          (map-get preorder-map
                         (tuple (name-hash (hash160 name salt)))))
        (name-entry 
          (map-get name-map (tuple (name name)))))
    (if (and
         ;; must be preordered
         (not (is-none? preorder-entry))
         ;; name shouldn't *already* exist
         (is-none? name-entry)
         ;; preorder must have paid enough
         (<= (price-funcion name)
             (default-to 0 (get paid preorder-entry)))
         ;; preorder must have been the current principal
         (eq? tx-sender
              (expects! (get buyer preorder-entry) (err 1)))
         (map-insert! name-table
           (tuple (name name))
           (tuple (owner recipient))))
         (ok 0)
         (err 1))))
```


Note that Blockstack PBC intends to supply a full BNS (Blockstack
Naming System) smart contract, as well as formal proofs that certain
desirable properties hold (e.g. "names are globally unique", "a
revoked name cannot be updated or transferred", "names cost stacks
based on their namespace price function", "only the principal can
reveal a name on registration", etc.).

# Related Work

Smart contract languages are not new at the time of this writing.  By far the
most well-known one at this time is Solidity [1], a Turing-complete smart
contract programming language for the Ethereum blockchain [2].  Solidity is
compiled, which makes it hard to determine whether or not any differences
between the contract's behavior and its expected behavior are due to bugs in the
source code, the compiler, or the EVM itself.  Clarity is interpreted, so any
bugs that cannot be attributed to a Clarity contract's source code must be due
to bugs in the blockchain itself.  Removing this ambiguity is important for
determining how to triage such problems.  A bug in the runtime system would
justifiably be fixed with a backwards-incompatible change, whereas a bug in the
compiler may not be.

Clarity is decidable, which removes the need for implementing an "out-of-gas"
error condition that is common in Turing-complete smart contract languages.
Clarity programs either run to completion if they do not fail static analysis
checks, or the blockchain transactions that invoke them are never mined in the
first place.

There are many other smart contract programming languages with different design
goals than Clarity.  This section deserves future expansion, and may be added to
after this SIP is ratified.  

[1] Solidity Language.  https://docs.soliditylang.org/en/v0.8.0/
[2] Ethereum blockchain.  https://ethereum.github.io/yellowpaper/paper.pdf

# Backwards Compatibility

Not applicable

# Activation

At least 20 miners must register a name in the `.miner` namespace in Stacks 1.0.
Once the 20th miner has registered, the state of Stacks 1.0 will be snapshotted.
300 Bitcoin blocks later, the Stacks 2.0 blockchain will launch.  With Stacks
2.0 will come the Clarity VM.

# Reference Implementations

The frst reference implementation can be found at
https://github.com/blockstack/stacks-blockchain.



================================================
FILE: sips/sip-004/sip-004-materialized-view.md
================================================
# Preamble

SIP Number: 004

Title: Cryptographic Commitment to Materialized Views

Author: Jude Nelson <jude@stacks.org>

Consideration: Technical

Type: Consensus

Status: Ratified

Created: 15 July 2019

License: BSD 2-Clause

Sign-off: Jude Nelson <jude@stacks.org>, Technical Steering Committee Chair

Discussions-To: https://github.com/stacksgov/sips

# Abstract

Blockchain peers are replicated state machines, and as such, must maintain a
materialized view of all of the state the transaction log represents in order to
validate a subsequent transaction.  The Stacks blockchain in particular not only
maintains a materialized view of the state of every fork, but also requires
miners to cryptographically commit to that view whenever they mine a block.
This document describes a **Merklized Adaptive Radix Forest** (MARF), an
authenticated index data structure for efficiently encoding a 
cryptographic commitment to blockchain state.

The MARF's structure is part of the consensus logic in the Stacks blockchain --
every Stacks peer must process the MARF the same way.  Stacks miners announce
a cryptographic hash of their chain tip's MARF in the blocks they produce, and in
doing so, demonstrate to each peer and each light client that they have 
applied the block's transactions to the peer's state correctly.

The MARF represents blockchain state as an authenticated directory.  State is
represented as key/value pairs.  The MARF structure gives a peer the ability to
prove to a light client that a particular key has a particular value, given the
MARF's cryptographic hash.  The proof has _O(log B)_ space for _B_ blocks, and
takes _O(log B)_ time complexity to produce and verify.  In addition, it offers
_O(1)_ expected time and space complexity for inserts and queries.
The MARF proof allows a light client to determine:

* What the value of a particular key is,
* How much cumulative energy has been spent to produce the key/value pair,
* How many confirmations the key/value pair has.

# Introduction

In order to generate a valid transaction, a blockchain client needs to be able
to query the current state of the blockchain.  For example, in Bitcoin, a client
needs to query its unspent transaction outputs (UTXOs) in order to satisfy their
spending conditions in a new transaction.  As another example, in Ethereum, a
client needs to query its accounts' current nonces in order to generate a valid
transaction to spend their tokens.

Whether or not a blockchain's peers are required to commit to the current state
in the blocks themselves (i.e. as part of the consensus logic) is a
philosophical decision.  We argue that it is a highly desirable in Blockstack's
case, since it affords light clients more security when querying the blockchain state than
not.  This is because a client often queries state that was last updated several
blocks in the past (i.e. and is "confirmed").  If a blockchain peer can prove to
a client that a particular key in the state has a particular value, and was last
updated a certain number of blocks in the past, then the client can determine
whether or not to trust the peer's proof based on factors beyond simply trusting
the remote peer to be honest.  In particular, the client can determine how
difficult it would be to generate a dishonest proof, in terms of the number of
blocks that would need to be maliciously crafted and accepted by the network.
This offers clients some protection against peers that would lie to them -- a
lying peer would need to spend a large amount of energy (and money) in order to
do so.

Specific to Blockstack, we envision that many applications will run
their own Stacks-based blockchain peer networks that operate "on top" of the
Stacks blockchain through proof-of-burn.  This means that the Blockstack
application ecosystem will have many parallel "app chains" that users may wish
to interact with.  While a cautious power user may run validator nodes for each
app chain they are interested in, we expect that most users will not do so,
especially if they are just trying out the application or are casual users.  In
order to afford these users better security than simply telling them to find a
trusted validating peer, it is essential that each Stacks peer commits to its
materialized view in each block.

On top of providing better security to light clients, committing to the materialized
state view in each block has the additional benefit of helping the peer network
detect malfunctioning miners early on.  A malfunctioning miner will calculate a
different materialized view using the same transactions, and with overwhelmingly
high probability, will also calculate a different state view hash.  This makes
it easy for a blockchain's peers to reject a block produced in this manner
outright, without having to replay its transactions.

## Design Considerations

Committing to the materialized view in each block has a non-zero cost in terms
of time and space complexity.  This cost is paid for by the transaction fee, but
it effectively sets an upper bound on how many key/value insertions can happen
per block -- in particular, generating and validating the block must be faster
than the underlying burnchain block times. This means that it
is of paramount importance to keep the materialized view digest calculation as
fast as possible.

The following considerations have a non-trivial impact on the design of the
MARF:

**A transaction can read or write any prior state in the same fork.**  This
means that the index must support fast random-access reads and fast
random writes.

**The Stacks blockchain can fork, and a miner can produce a fork at any block
height in the past.**  As argued in SIP 001, a Stacks blockchain peer must process
all forks and keep their blocks around.  This also means that a peer needs to
calculate and validate the materialized view of each fork, no matter where it
occurs.  This is also necessary because a client may request a proof for some
state in any fork -- in order to service such requests, the peer must calculate
the materialized view for all forks.

**Forks can occur in any order, and blocks can arrive in any order.**  As such,
the runtime cost of calculating the materialized view must be _independent_ of the
order in which forks are produced, as well as the order in which their blocks
arrive.  This is required in order to avoid denial-of-service vulnerabilities,
whereby a network attacker can control the schedules of both
forks and block arrivals in a bid to force each peer to expend resources
validating the fork.  It must be impossible for an attacker to
significantly slow down the peer network by maliciously varying either schedule.
This has non-trivial consequences for the design of the data structures for
encoding materialized views.

# Specification

The Stacks peer's materialized view is realized as a flat key/value store.
Transactions encode zero or more creates, inserts, updates, and deletes on this
key/value store.  As a consequence of needing to support forks from any prior block,
no data is ever removed; instead, a "delete" on a particular key is encoded 
by replacing the value with a tombstone record.  The materialized view is the
subset of key/value pairs that belong to a particular fork in the blockchain.

The Stacks blockchain separates the concern of maintaining _authenticated
index_ over data from storing a copy of the data itself.  The blockchain peers
commit to the digest of the authenticated index, but can store the data however
they want.  The authenticated index is realized as a _Merklized Adaptive Radix
Forest_ (MARF).  The MARF gives Stacks peers the ability to prove that a
particular key in the materialized view maps to a particular value in a
particular fork.

A MARF has two principal data structures:  a _merklized adaptive radix trie_
for each block and a _merklized skip-list_ that
cryptographically links merklized adaptive radix tries in prior blocks to the
current block.

## Merklized Adaptive Radix Tries (ARTs)

An _adaptive radix trie_ (ART) is a prefix tree where each node's branching
factor varies with the number of children.  In particular, a node's branching
factor increases according to a schedule (0, 4, 16, 48, 256) as more and more
children are added.  This behavior, combined with the usual sparse trie
optimizations of _lazy expansion_ and _path compression_, produce a tree-like
index over a set key/value pairs that is _shallower_ than a perfectly-balanced
binary search tree over the same values.  Details on the analysis of ARTs can
be found in [1].

To produce an _index_ over new state introduced in this block, the Stacks peer
will produce an adaptive radix trie that describes each key/value pair modified.
In particular, for each key affected by the block, the Stacks peer will:
* Calculate the hash of the key to get a fixed-length trie path,
* Store the new value and this hash into its data store,
* Insert or update the associated value hash in the block's ART at the trie path,
* Calculate the new Merkle root of the ART by hashing all modified intermediate
  nodes along the path.

In doing so, the Stacks peer produces an authenticated index for all key/value
pairs affected by a block.  The leaves of the ART are the hashes of the values,
and the hashes produced in each intermediate node and root give the peer a
way to cryptographically prove that a particular value is present in the ART
(given the root hash and the key).

The Stacks blockchain employs _path compression_ and _lazy expansion_
to efficiently represent all key/value pairs while minimizing the number of trie
nodes.  That is, if two children share a common prefix, the prefix bytes are
stored in a single intermediate node instead of being spread across multiple
intermediate nodes (path compression).  In the special case where a path suffix
uniquely identifies the leaf, the path suffix will be stored alongside the leaf
instead as a sequence of intermediate nodes (lazy expansion).  As more and more
key/value pairs are inserted, intermediate nodes and leaves with multi-byte
paths will be split into more nodes.

**Trie Structure**

A trie is made up of nodes with radix 4, 16, 48, or 256, as well as leaves.  In
the documentation below, these are called `node4`, `node16`, `node48`,
`node256`, and `leaf` nodes.  An empty trie has a single `node256` as its root.
Child pointers occupy one byte.

**Notation**

The notation `(ab)node256` means "a `node256` who descends from its parent via
byte 0xab".

The notation `node256[path=abcd]` means "a `node256` that has a shared prefix
with is children `abcd`".

**Lazy Expansion**

If a leaf has a non-zero-byte path suffix, and another leaf is inserted that
shares part of the suffix, the common bytes will be split off of the existing
leaf to form a `node4`, whose two immediate children are the two leaves.  Each
of the two leaves will store the path bytes that are unique to them.  For
example, consider this trie with a root `node256` and a single leaf, located at
path `aabbccddeeff00112233` and having value hash `123456`:

```
node256
       \
        (aa)leaf[path=bbccddeeff00112233]=123456
```

If the peer inserts the value hash `98765` at path `aabbccddeeff998877`, the
single leaf's path will be split into a shared prefix and two distinct suffixes,
as follows:

```
insert (aabbccddeeff998877, 98765)

node256                            (00)leaf[path=112233]=123456
       \                          /
        (aa)node4[path-bbccddeeff]
                                  \
                                   (99)leaf[path=887766]=98765
```

Now, the trie encodes both `aabbccddeeff00112233=123456` and
`aabbccddeeff99887766=98765`.

**Node Promotion**

As a node with a small radix gains children, it will eventually need to be
promoted to a node with a higher radix.  A `node4` will become a `node16` when
it receives its 5th child; a `node16` will become a `node48` when it receives
its 17th child, and a `node48` will become a `node256` when it receives its 49th
child.  A `node256` will never need to be promoted, because it has slots for
child pointers with all possible byte values.

For example, consider this trie with a `node4` and 4 children:

```
node256                                (00)leaf[path=112233]=123456
       \                              /
        \                            /  (01)leaf[path=445566]=67890
         \                          /  /
          (aa)node4[path=bbccddeeff]---
                                    \  \
                                     \  (02)leaf[path=778899]=abcdef
                                      \
                                       (99)leaf[path=887766]=98765
```

This trie encodes the following:
   * `aabbccddeeff00112233=123456`
   * `aabbccddeeff01445566=67890`
   * `aabbccddeeff02778899=abcdef`
   * `aabbccddeeff99887766=9876`

Inserting one more node with a prefix `aabbccddeeff` will promote the
intermediate `node4` to a `node16`:

```
insert (aabbccddeeff03aabbcc, 314159)

node256                                 (00)leaf[path=112233]=123456
       \                               /
        \                             /  (01)leaf[path=445566]=67890
         \                           /  /
          (aa)node16[path=bbccddeeff]-----(03)leaf[path=aabbcc]=314159
                                     \  \
                                      \  (02)leaf[path=778899]=abcdef
                                       \
                                        (99)leaf[path=887766]=98765
```

The trie now encodes the following:
   * `aabbccddeeff00112233=123456`
   * `aabbccddeeff01445566=67890`
   * `aabbccddeeff03aabbcc=314159`
   * `aabbccddeeff02778899=abcdef`
   * `aabbccddeeff99887766=9876`

**Path Compression**

Intermediate nodes, such as the `node16` in the previous example, store path
prefixes shared by all of their children.  If a node is inserted that shares
some of this prefix, but not all of it, the path is "decompressed" -- a new
leaf is "spliced" into the compressed path, and attached to a `node4` whose two
children are the leaf and the existing node (i.e. the `node16` in this case)
whose shared path now contains the suffix unique to its children, but distinct
from the newly-spliced leaf.

For example, consider this trie with the intermediate `node16` sharing a path
prefix `bbccddeeff` with its 5 children:

```
node256                                 (00)leaf[path=112233]=123456
       \                               /
        \                             /  (01)leaf[path=445566]=67890
         \                           /  /
          (aa)node16[path=bbccddeeff]-----(03)leaf[path=aabbcc]=314159
                                     \  \
                                      \  (02)leaf[path=778899]=abcdef
                                       \
                                        (99)leaf[path=887766]=98765
```

This trie encodes the following:
   * `aabbccddeeff00112233=123456`
   * `aabbccddeeff01445566=67890`
   * `aabbccddeeff03aabbcc=314159`
   * `aabbccddeeff02778899=abcdef`
   * `aabbccddeeff99887766=9876`

If we inserted `(aabbcc001122334455, 21878)`, the `node16`'s path would be
decompressed to `eeff`, a leaf with the distinct suffix `1122334455` would be spliced
in via a `node4`, and the `node4` would have the shared path prefix `bbcc` with
its now-child `node16` and leaf.

```
insert (aabbcc00112233445566, 21878)

                               (00)leaf[path=112233445566]=21878
                              /
node256                      /                       (00)leaf[path=112233]=123456
       \                    /                       /
        (aa)node4[path=bbcc]                       /  (01)leaf[path=445566]=67890
                            \                     /  /
                             (dd)node16[path=eeff]-----(03)leaf[path=aabbcc]=314159
                                                  \  \
                                                   \  (02)leaf[path=778899]=abcdef
                                                    \
                                                     (99)leaf[path=887766]=98765
```

The resulting trie now encodes the following:
   * `aabbcc00112233445566=21878`
   * `aabbccddeeff00112233=123456`
   * `aabbccddeeff01445566=67890`
   * `aabbccddeeff03aabbcc=314159`
   * `aabbccddeeff02778899=abcdef`
   * `aabbccddeeff99887766=9876`

## Back-pointers

The materialized view of a fork will hold key/value pairs for data produced by
applying _all transactions_ in that fork, not just the ones in the last block.  As such,
the index over all key/value pairs in a fork is encoded in the sequence of 
its block's merklized ARTs.

To ensure that random reads and writes on the a fork's materialized view remain
fast no matter which block added them, a child pointer in an ART can point to
either a node in the same ART, or a node with the same path in a prior ART.  For
example, if the ART at block _N_ has a `node16` whose path is `aabbccddeeff`, and 10
blocks ago a leaf was inserted at path `aabbccddeeff99887766`, it will
contain a child pointer to the intermediate node from 10 blocks ago whose path is
`aabbccddeeff` and who has a child node in slot `0x99`.  This information is encoded
as a _back-pointer_.  To see it visually:

```
At block N


node256                                 (00)leaf[path=112233]=123456
       \                               /
        \                             /  (01)leaf[path=445566]=67890
         \                           /  /
          (aa)node16[path=bbccddeeff]-----(03)leaf[path=aabbcc]=314159
                                     \  \
                                      \  (02)leaf[path=778899]=abcdef
                                       \
                                        |
                                        |
                                        |
At block N-10 - - - - - - - - - - - - - | - - - - - - - - - - - - - - - - - - -
                                        |
node256                                 | /* back-pointer to block N-10 */
       \                                |
        \                               |
         \                              |
          (aa)node4[path=bbccddeeff]    |
                                    \   |
                                     \  |
                                      \ |
                                       (99)leaf[path=887766]=98765
```

By maintaining trie child pointers this way, the act of looking up a path to a value in
a previous block is a matter of following back-pointers to previous tries.
This back-pointer uses the _block-hash_ of the previous block to uniquely identify
the block. In order to keep the in-memory and on-disk representations of trie nodes succint,
the MARF structure uses a locally defined unsigned 32-bit integer to identify the previous 
block, along with a local mapping of such integers to the respective block header hash.

Back-pointers are calculated in a copy-on-write fashion when calculating the ART
for the next block.  When the root node for the ART at block N+1 is created, all
of its children are set to back-pointers that point to the immediate children of
the root of block N's ART.  Then, when inserting a key/value pair, the peer
walks the current ART to the insertion point, but whenever a
back-pointer is encountered, it copies the node it points to into the current
ART, and sets all of its non-empty child pointers to back-pointers.  The peer
then continues traversing the ART until the insertion point is found (i.e. a
node has an unallocated child pointer where the leaf should go), copying
over intermediate nodes lazily.

For example, consider the act of inserting `aabbccddeeff00112233=123456` into an
ART where a previous ART contains the key/value pair
`aabbccddeeff99887766=98765`:

```
At block N


node256                                (00)leaf[path=112233]=123456
^      \                              /
|       \                            /
|        \                          /
|         (aa)node4[path=bbccddeeff]
|                 ^                 \
|                 |                  \
| /* 1. @root. */ | /* 2. @node4.  */ \  /* 3. 00 is empty, so insert */
| /* copy up, &*/ | /* copy up, &  */  |
| /* make back-*/ | /* make back-  */  |
| /* ptr to aa */ | /* ptr to 99   */  |
|                 |                    |
|- At block N-10 -|- - - - - - - - - - | - - - - - - - - - - - - - - - - - -
|                 |                    |
node256           |                    |
       \          |                    |
        \         |                    |
         \        |                    |
          (aa)node4[path=bbccddeeff]   |
                                    \  |
                                     \ |
                                      \|
                                       (99)leaf[path=887766]=98765
```

In step 1, the `node256` in block _N_ would have a back-pointer to the `node4` in
block _N - 10_ in child slot `0xaa`.  While walking path `aabbccddeeff00112233`,
the peer would follow slot `0xaa` to the `node4` in block _N - 10_ and copy it
into block _N_, and would set its child pointer at `0x99` to be a back-pointer
to the `leaf` in block _N - 10_.  It would then step to the `node4` it copied,
and walk path bytes `bbccddeeff`.  When it reaches child slot `0x00`, the peer
sees that it is unallocated, and attaches the leaf with the unexpanded path
suffix `112233`.  The back-pointer to `aabbccddeeff99887766=98765` is thus
preserved in block _N_'s ART.

**Calculating the Root Hash with Back-pointers**

For reasons that will be explained in a moment, the hash of a child node that is a
back-pointer is not calculated the usual way when calculating the root hash of
the Merklized ART.  Instead of taking the hash of the child node (as would be
done for a child in the same ART), the hash of the _block header_ is used
instead.  In the above example, the hash of the `leaf` node whose path is
`aabbccddeeff99887766` would be the hash of block _N - 10_'s header, whereas the
hash of the `leaf` node whose path is `aabbccddeeff00112233` would be the hash
of the value hash `123456`.

The main reason for doing this is to keep block validation time down by a
significant constant factor.  The block header hash is always kept in RAM,
but at least one disk seek is required to read the hash of a child in a separate
ART (and it often takes more than one seek). This does not sacrifice the security
of a Merkle proof of `aabbccddeeff99887766=98765`, but it does alter the mechanics
of calculating and verifying it.

## Merklized Skip-list

The second principal data structure in a MARF is a Merklized skip-list encoded
from the block header hashes and ART root hashes in each block.  The hash of the
root node in the ART for block _N_ is derived not only from the hash of the
root's children, but also from the hashes of the block headers from blocks
`N - 1`, `N - 2`, `N - 4`, `N - 8`, `N - 16`, and so on.  This constitutes
a _Merklized skip-list_ over the sequence of ARTs.

The reason for encoding the root node's hash this way is to make it possible for
peers to create a cryptographic proof that a particular key maps to a particular
value when the value lives in a prior block, and can only be accessed by
following one or more back-pointers.  In addition, the Merkle skip-list affords
a client _two_ ways to verify key-value pairs:  the client only needs either (1)
a known-good root hash, or (2) the sequence of block headers for the Stacks
chain and its underlying burn chain.  Having (2) allows the client to determine
(1), but calculating (2) is expensive for a client doing a small number of
queries.  For this reason, both options are supported.

### Resolving Block Height Queries

For a variety of reasons, the MARF structure must be able to resolve
queries mapping from block heights (or relative block heights) to
block header hashes and vice-versa --- for example, the Clarity VM
allows contracts to inspect this information. Most applicable to the
MARF, though, is that in order to find the ancestor hashes to include
in the Merklized Skip-list, the data structure must be able to find
the block headers which are 1, 2, 4, 8, 16, ... blocks prior in the
same fork. This could be discovered by walking backwards from the
current block, using the previous block header to step back through
the fork's history. However, such a process would require _O(N)_ steps
(where _N_ is the current block height). But, if a mapping exists for
discovering the block at a given block height, this process would instead
be _O(1)_ (because a node will have at most 32 such ancestors).

But correctly implementing such a mapping is not trivial: a given
height could resolve to different blocks in different forks. However,
the MARF itself is designed to handle exactly these kinds of
queries. As such, at the beginning of each new block, the MARF inserts
into the block's trie two entries:

1. This block's block header hash -> this block's height.
2. This block's height -> this block's block header hash.

This mapping allows the ancestor hash calculation to proceed.

## MARF Merkle Proofs

A Merkle proof for a MARF is constructed using a combination of two types of
sub-proofs:  _segment proofs_, and _shunt proofs_.  A _segment proof_ is a proof
that a node belongs to a particular Merklized ART.  It is simply a Merkle tree
proof.  A _shunt proof_ is a proof that the ART for block _N_ is exactly _K_
blocks away from the ART at block _N - K_.  It is generated as a Merkle proof
from the Merkle skip-list.

Calculating a MARF Merkle proof is done by first calculating a segment proof for a
sequence of path prefixes, such that all the nodes in a single prefix are in the
same ART.  To do so, the node walks from the current block's ART's root node
down to the leaf in question, and each time it encounters a back-pointer, it
generates a segment proof from the _currently-visited_ ART to the intermediate
node whose child is the back-pointer to follow.  If a path contains _i_
back-pointers, then there will be _i+1_ segment proofs.

Once the peer has calculated each segment proof, it calculates a shunt proof
that shows that the _i+1_th segment was reached by walking back a given number
of blocks from the _i_th segment by following the _i_th segment's back-pointer.
The final shunt proof for the ART that contains the leaf node includes all of
the prior block header hashes that went into producing its root node's hash.
Each shunt proof is a sequence of sequences of block header hashes and ART root
hashes, such that the hash of the next ART root node can be calculated from the
previous sequence.

For example, consider the following ARTs:

```
At block N


node256                                 (00)leaf[path=112233]=123456
       \                               /
        \                             /  (01)leaf[path=445566]=67890
         \                           /  /
          (aa)node16[path=bbccddeeff]-----(03)leaf[path=aabbcc]=314159
                                     \  \
                                      \  (02)leaf[path=778899]=abcdef
                                       \
                                        |
                                        |
                                        |
At block N-10 - - - - - - - - - - - - - | - - - - - - - - - - - - - - - - - - -
                                        |
node256                                 | /* back-pointer to N - 10 */
       \                                |
        \                               |
         \                              |
          (aa)node4[path=bbccddeeff]    |
                                    \   |
                                     \  |
                                      \ |
                                       (99)leaf[path=887766]=98765
```

To generate a MARF Merkle proof, the client queries a Stacks peer for a
particular value hash, and then requests the peer generate a proof that the key
and value must have been included in the calculation of the current block's ART
root hash (i.e. the digest of the materialized view of this fork). 

For example, given the key/value pair `aabbccddeeff99887766=98765` and the hash
of the ART at block _N_, the peer would generate two segment proofs for the
following paths: `aabbccddeeff` in block _N_, and `aabbccddeeff99887766` in
block `N - 10`.

```
At block N


node256
       \   /* this segment proof would contain the hashes of all other */
        \  /* children of the root, except for the one at 0xaa.        */
         \
          (aa)node16[path=bbccddeeff]

At block N-10 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

node256    /* this segment proof would contain two sequences of hashes: */
       \   /* the hashes for all children of the root besides 0xaa, and */
        \  /* the hashes of all children of the node4, except 0x99.     */
         \
          (aa)node4[path=bbccddeeff]
                                    \
                                     \
                                      \
                                       (99)leaf[path=887766]=98765
```

Then, it would calculate two shunt proofs.  The first proof, called the "head shunt proof,"
supplies the sequence of block hashes for blocks _N - 11, N - 12, N - 14, N - 18, N - 26, ..._ and the 
hash of the children of the root node of the ART for block _N - 10_.  This lets the 
client calculate the hash of the root of the ART at block _N - 10_.  The second
shunt proof (and all subsequent shunt proofs, if there are more back-pointers to
follow) is comprised of the hashes that "went into" calculating the hashes on the
skip-list from the next segment proof's root hash.

In detail, the second shunt proof would have two parts:

* the block header hashes for block _N - 9_ _N - 12_, _N - 16_, _N - 24_, ...
* the block header hashes for _N - 1_, _N - 2_, _N - 4_, _N - 16_, _N - 32_, ...

The reason there are two sequences in this shunt proof is because "walking back"
from block _N_ to block _N - 10_ requires walking first to block _N - 8_ (i.e.
following the skip-list column for 2 ** 3), and then walking to block _N - 10_
from _N - 8_ (i.e. following its skip-list column for 2 ** 1).  The first segment
proof (i.e. with the leaf) lets the client calculate the hash of the children of
the ART root node in block _N - 10_, which when combined with the first part of
this shunt proof yields the ART root hash for _N - 8_.  Then, the client
uses the hash of the children of the root node in the ART of block _N_ (calculated from the second segment
proof), combined with the root hash from node _N - 8_ and with the hashes
in the second piece of this shunt proof, to calculate the ART root hash for
block _N_.  The proof is valid if this calculated root hash matches the root
hash for which it requested the proof.

In order to fully verify the MARF Merkle proof, the client would verify that:

* The first segment proof's path's bytes are equal to the hash of the key for
  which the proof was requested.
* The first segment proof ends in a leaf node, and the leaf node contains the
  hash of the value for which the proof was requested.
* Each segment proof is valid -- the root hash could only be calculated from the
  deepest intermediate node in the segment,
* Each subsequent segment proof was generated from a prefix of the path
  represented by the current segment proof,
* Each back-pointer at the tail of each segment (except the one that terminates
  in the leaf -- i.e. the first one) was a number of blocks back that is equal
  to the number of blocks skipped over in the shunt proof linking it to the next
  segment.
* Each block header was included in the fork the client is querying,
* Each block header was generated from its associated ART root hash,
* (Optional, but encouraged): The burn chain block headers demonstrate that the
  correct difficulty rules were followed.  This step can be skipped if the
client somehow already knows that the hash of block _N_ is valid.

Note that to verify the proof, the client would need to substitute the
_block header hash_ for each intermediate node at the tail of each segment
proof.  The block header hash can either be obtained by fetching the block
headers for both the Stacks chain and burn chain _a priori_ and verifying that
they are valid, or by fetching them on-the-fly.  The second strategy should only
be used if the client's root hash it submits to the peer is known out-of-band to
be the correct hash.

The security of the proof is similar to SPV proofs in Bitcoin -- the proof is
valid assuming the client is able to either verify that the final header hash
represents the true state of the network, or the client is able to fetch the
true burn chain block header sequence.  The client has some assurance that a
_given_ header sequence is the _true_ header sequence, because the header
sequence encodes the proof-of-work that went into producing it.  A header
sequence with a large amount of proof-of-work is assumed to be infeasible for an
attacker to produce -- i.e. only the majority of the burn chain's network hash
power could have produced the header chain.  Regardless of which data the client
has, the usual security assumptions about confirmation depth apply -- a proof
that a key maps to a given value is valid only if the transaction that set
it is unlikely to be reversed by a chain reorg.

## Performance

The time and space complexity of a MARF is as follows:

* **Reads are _O(1)_** While reads may traverse multiple tries, they are always
  descending the radix trie, and resolving back pointers is constant time.
* **Inserts and updates are _O(1)._** Inserts have the same complexity
  as reads, though they require more work by constant factors (in
  particular, hash recalculations).
* **Creating a new block is _O(log B)_.** Inserting a block requires
  including the Merkle skip-list hash in the root node of the new
  ART. This is _log B_ work, where _B_ is chain length.
* **Creating a new fork is _O(log B)_.** Forks do not incur any overhead relative
  to appending a block to a prior chain-tip.
* **Generating a proof is _O(log B)_ for B blocks**.  This is the cost of
  reading a fixed number of nodes, combined with walking the Merkle skip-list.
* **Verifying a proof is _O(log B)_**.  This is the cost of verifying a fixed
  number of fixed-length segments, and verifying a fixed number of _O(log B)_
  shunt proof hashes.
* **Proof size is _O(log B)_**.  A proof has a fixed number of segment proofs,
  where each node has a constant size.  It has _O(log B)_ hashes across all of
  its shunt proofs.

## Consensus Details

The hash function used to generate a path from a key, as well as the hash
function used to generate a node hash, is SHA2-512/256.  This was chosen because
it is extremely fast on 64-bit architectures, and is immune to length extension
attacks.

The hash of an intermediate node is the hash over the following data:

* a 1-byte node ID,
* the sequence of child pointer data (dependent on the type of node),
* the 1-byte length of the path prefix this node contains,
* the 0-to-32-byte path prefix

A single child pointer contains:
* a 1-byte node ID,
* a 1-byte path character,
* the 32-byte block header hash of the pointed-to block

A `node4`, `node16`, `node48`, and `node256` each have an array of 4,
16, 48, and 256 child pointers each.

Children are listed in a `node4`, `node16`, and `node48`'s child pointer arrays in the
order in which they are inserted.  While searching for a child in a `node4` or
`node16` requires a linear scan of the child pointer array, searching a `node48` is done 
by looking up the child's index in its child pointer array using the
path character byte as an index into the `node48`'s 256-byte child pointer
index, and then using _that_ index to look up the child pointer.  Children are
inserted into the child pointer array of a `node256` by using the 1-byte
path character as the index.

The disk pointer stored in a child pointer, as well as the storage mechanism for
mapping hashes of values (leaves in the MARF) to the values themselves, are both
unspecified by the consensus rules.  Any mechanism or representation is
permitted.

# Related Work

This section will be expanded upon after this SIP is ratified.

[1] https://db.in.tum.de/~leis/papers/ART.pdf

# Backwards Compatibility

Not applicable

# Activation

At least 20 miners must register a name in the `.miner` namespace in Stacks 1.0.
Once the 20th miner has registered, the state of Stacks 1.0 will be snapshotted.
300 Bitcoin blocks later, the Stacks 2.0 blockchain will launch.  Stacks 2.0
implements the MARF internally.

# Reference Implementations

Implemented in Rust.  See https://github.com/blockstack/stacks-blockchain.




================================================
FILE: sips/sip-006/sip-006-runtime-cost-assessment.md
================================================
# Preamble

SIP Number: 006

Title: Clarity Execution Cost Assessment

Author: Aaron Blankstein <aaron@blockstack.com>, Reed Rosenbluth <reed@blockstack.com>

Consideration: Technical

Type: Consensus

Status: Ratified

Created: 19 October 2019

License: BSD 2-Clause

Sign-off: Jude Nelson <jude@stacks.org>, Technical Steering Committee Chair

Discussions-To: https://github.com/stacksgov/sips

# Abstract

This document describes the measured costs and asymptotic costs
assessed for the execution of Clarity code. This will not specify the
_constants_ associated with those asymptotic cost functions. Those
constants will necessarily be measured via benchmark harnesses and
regression analyses. Furthermore, the _analysis_ cost associated with
this code will not be covered by this proposal.

The asymptotic cost functions for Clarity functions are modifiable
via an on-chain voting mechanism. This enables new native functions to
be added to the language over time.

This document also describes the memory limit imposed during contract
execution, and the memory model for enforcing that limit.

# Introduction

Execution cost of a block of Clarity code is broken into 5 categories:

1. Runtime cost: captures the number of cycles that a single
   processor would require to process the Clarity block. This is a
   _unitless_ metric, so it will not correspond directly to cycles,
   but rather is meant to provide a basis for comparison between
   different Clarity code blocks.
2. Data write count: captures the number of independent writes
   performed on the underlying data store (see SIP-004).
3. Data read count: captures the number of independent reads
   performed on the underlying data store.
4. Data write length: the number of bytes written to the underlying
   data store.
5. Data read length: the number of bytes read from the underlying
   data store.

Importantly, these costs are used to set a _block limit_ for each
block.  When it comes to selecting transactions for inclusion in a
block, miners are free to make their own choices based on transaction
fees, however, blocks may not exceed the _block limit_. If they do so,
the block is considered invalid by the network --- none of the block's
transactions will be materialized and the leader forfeits all rewards
from the block.

## Static versus Dynamic Cost Assessment

Tracking the execution cost of a contract may be done either dynamically
or statically. Dynamic cost assessment involves tracking, at the VM level,
the various metrics as a contract is executed. Static cost assessment is
performed via analysis of the contract source code, and is inherently
a more pessimistic accounting of the execution cost: list operations
are charged according to the _maximum_ size of the list (per the type
annotations and inferences from the source code) and branching statements
are charged according to the _maximum_ branch cost (per metric tracked, i.e.,
if one branch performs 1 write and has a runtime cost of 1, and another
branch performs 0 writes and has a runtime cost of 2, the whole statement
will be assessed as having a maximum of 1 write and runtime cost of 2).

# Specification

## Costs of Common Operations

### Variable Lookup

Looking up variables in Clarity incurs a non-constant cost -- the stack
depth _and_ the length of the variable name affect this cost. However,
variable names in Clarity have bounded length -- 128 characters. Therefore,
the cost assessed for variable lookups may safely be constant with respect
to name length.

The stack depth affects the lookup cost because the variable must be
checked for in each context on the stack.

The cost model of Clarity depends on a copy-on-read semantic for
objects. This allows operations like appends, matches, wrapping/unwrapping,
to be constant cost, but it requires that variable lookups be charged for
copies.

Cost Function:

```
a*X+b*Y+c
```

a, b, and c are constants \
X := stack depth \
Y := variable size

### Function Lookup

Looking up a function in Clarity incurs a constant cost with respect
to name length (for the same reason as variable lookup). However,
because functions may only be defined in the top-level contract
context, stack depth does not affect function lookup.

Cost Function:

```
a
```

a is a constant.

### Name Binding

The cost of binding a name in Clarity -- in either a local or the contract
context is _constant_ with respect to the length of the name:

```
binding_cost = a
```

a is a constant

### Function Application

Function application in Clarity incurs a cost in addition to the
cost of executing the function's body. This cost is the cost of
binding the arguments to their passed values, and the cost of
ensuring that those arguments are of the correct type. Type checks
and argument binding are _linear_ in the size of the arguments.

The cost of applying a function is:


```
(a*X+b) + costEval(body)
```

a and b are constants \
X := the cumulative size of the argument types \
`costEval(body)` := the cost of executing the body of the function

### contract-call Transactions

User-signed transactions for contract-calls are charged for the
application of the function, as well as the loading of the contract
data. This charge is the same as a normal contract-call. _However_,
contract principals that are supplied as trait arguments must be
checked by the runtime system to ensure that they validly implement
the trait. The cost of this check is:

```
read_count = 2
read_length = trait_size + contract_size
runtime_cost = a*(contract_size) + b*(trait_size) + c
```

This check needs to read the trait, and then validate that the supplied
contract fulfills that trait by reading the contract in, and checking
the method signatures. This check must be performed for each such
trait parameter.

### Type Parsing

Parsing a type in Clarity incurs a linear cost in the size of the
AST describing the type:

```
type_parsing_cost(X) = (a*X+b)
```

a, b, are constants \
X := the number of elements in the type description AST

The type description AST is the tree of Clarity language elements used
for describing the type, e.g.:

* `(list 1 uint)` - this AST has four elements: `list`, `1`, `uint`
  and the parentheses containing them.
* `(response bool int)` - this AST has four elements: `response`, `bool`, `int`
  and the parentheses containing them.
* `int` - this AST is just one component.

### Function Definition

Defining a function in Clarity incurs an execution cost at the
time of contract publishing (unrelated to any analysis). This
is the cost of _parsing_ the function's signature, which is linear
in the length of the type signatures, and linear in the length of the
function name and argument names.

```
binding_cost + sum(a + type_parsing_cost(Y) for Y in ARG_TYPES)
```

`type_parsing_cost(Y)` := the cost of parsing argument Y \
ARG_TYPES := the function definition's argument type signatures \
a is a constant associated with the binding of argument types

### Contract Storage Cost

Storing a contract incurs both a runtime cost as well as storage costs. Both of
these are _linear_ the size of the contract AST.

```
WRITE_LENGTH = a*X+b
RUNTIME_COST = c*X+d
```

a, b, c, and d, are constants.

## Initial Native Function Costs

These are the initial set values for native function costs, however, these
can be changed as described below in the [Cost Upgrades](#cost-upgrades)
section of this document.

### Data, Token, Contract-Calls

#### Data Lookup Costs

Fetching data from the datastore requires hashing the key to be looked up.
That cost is linear in the key size:

```
data_hash_cost(X) = a*X+b
```

X := size of the key

#### Data Fetching Costs

Fetching data from the datastore incurs a runtime cost, in addition to
any costs associated with MARF accesses (which are simply counted as the
integer number of times the MARF is accessed). That runtime cost
is _linear_ in the size of the fetched value (due to parsing).

```
read_data_cost = a*X+b
```

X := size of the fetched value.

#### Data Writing Costs

Writing data to the datastore incurs a runtime cost, in addition to
any costs associated with MARF writes (which are simply counted as the
integer number of times the MARF is written). That runtime cost
is _linear_ in the size of the written value (due to data serialization).

```
write_data_cost = a*X+b
```

X := size of the stored value.

#### contract-call

Contract calls incur the cost of a normal function lookup and
application, plus the cost of loading that contract into memory from
the data store (which is linear in the size of the called contract).

```
RUNTIME_COST: (a*Y+b) + func_lookup_apply_eval(X)
READ_LENGTH: Y
```

a and b are constants \
Y := called contract size \
`func_lookup_apply_eval(X)` := the cost of looking up, applying, and
evaluating the body of the function


Note that contract-calls that use _trait_ definitions for dynamic dispatch
are _not_ charged at a different cost rate. Instead, there is a cost for
looking up the trait variable (assessed as a variable lookup), and the cost
of validating any supplied trait implementors is assessed during a transaction's
argument validation.

#### map-get

```
RUNTIME_COST: data_hash_cost(X+Y) + read_data_cost(Z)
READ_LENGTH:  Z
```

X := size of the map's _key_ tuple \
Y := the length of the map's name \
Z := the size of the map's _value_ tuple


#### contract-map-get

```
RUNTIME_COST: data_hash_cost(X) + read_data_cost(Z)
READ_LENGTH:  Z
```

X := size of the map's _key_ tuple \
Z := the size of the map's _value_ tuple

#### map-set

```
RUNTIME_COST: data_hash_cost(X+Y) + write_data_cost(Z)
WRITE_LENGTH:  Z
```

X := size of the map's _key_ tuple \
Y := the length of the map's name \
Z := the size of the map's _value_ tuple

#### map-insert

```
RUNTIME_COST: data_hash_cost(X+Y) + write_data_cost(Z)
WRITE_LENGTH:  Z
```

X := size of the map's _key_ tuple \
Y := the length of the map's name \
Z := the size of the map's _value_ tuple

#### map-delete

```
RUNTIME_COST: data_hash_cost(X+Y) + write_data_cost(1)
WRITE_LENGTH:  1
```

X := size of the map's _key_ tuple \
Y := the length of the map's name \
Y := the length of the map's name

#### var-get

```
RUNTIME_COST: data_hash_cost(1) + read_data_cost(Y)
READ_LENGTH: Y
```

Y := the size of the variable's _value_ type

#### var-set

```
RUNTIME_COST: data_hash_cost(1) + write_data_cost(Y)
WRITE_LENGTH: Y
```

Y := the size of the variable's _value_ type

#### nft-mint

```
RUNTIME_COST: data_hash_cost(Y) + write_data_cost(a) + b
WRITE_LENGTH: a
```

Y := size of the NFT type \
a is a constant: the size of a token owner \
b is a constant cost (for tracking the asset in the assetmap)

#### nft-get-owner

```
RUNTIME_COST: data_hash_cost(Y) + read_data_cost(a)
READ_LENGTH: a
```

Y := size of the NFT type \
a is a constant: the size of a token owner


#### nft-transfer

```
RUNTIME_COST: data_hash_cost(Y) + write_data_cost(a) + write_data_cost(a) + b
READ_LENGTH: a
WRITE_LENGTH: a
```

Y := size of the NFT type \
a is a constant: the size of a token owner \
b is a constant cost (for tracking the asset in the assetmap)

#### ft-mint
 
Minting a token is a constant-time operation that performs a constant
number of reads and writes (to check the total supply of tokens and
incremement).

```
RUNTIME: a
READ_LENGTH: b
WRITE_LENGTH: c
```
a, b, and c are all constants.

#### ft-transfer

Transfering a token is a constant-time operation that performs a constant
number of reads and writes (to check the token balances).

```
RUNTIME: a
READ_LENGTH: b
WRITE_LENGTH: c
```
a, b, and c are all constants.

#### ft-get-balance

Getting a token balance is a constant-time operation that performs a
constant number of reads.

```
RUNTIME: a
READ_LENGTH: b
```
a and b are constants.

#### get-block-info

```
RUNTIME: a
READ_LENGTH: b
```

a and b are constants.

## Control-Flow and Context Manipulation

### let

In addition to the cost of evaluating the body expressions of a `let`,
the cost of a `let` expression has a constant cost, plus
the cost of binding each variable in the new context (similar
to the cost of function evaluation, without the cost of type checks).


```
a + b * Y + costEval(body) + costEval(bindings)
```

a and b are constants \
Y := the number of let arguments \
`costEval(body)` := the cost of executing the body of the let \
`costEval(bindings)` := the cost of evaluating the value of each let binding

### if

```
a + costEval(condition) + costEval(chosenBranch)
```

a is a constant \
`costEval(condition)` := the cost of evaluating the if condition \
`costEval(chosenBranch)` := the cost of evaluating the chosen branch

if computed during _static analysis_, the chosen branch cost is the
`max` of the two possible branches.

### asserts!

```
a + costEval(condition) + costEval(throwBranch)
```

a is a constant \
`costEval(condition)` := the cost of evaluating the asserts condition \
`costEval(throwBranch)` := the cost of evaluating the throw branch in
the event that condition is false

if computed during _static analysis_, the thrown branch cost is always
included.

## List and Buffer iteration
### append

The cost of appending an item to a list is the cost of checking the
type of the added item, plus some fixed cost.

```
a + b * X
```

a and b is a constant \
X := the size of the list _entry_ type

### concat

The cost of concatting two lists or buffers is linear in
the size of the two sequences:

```
a + b * (X+Y)
```

a and b are constants \
X := the size of the right-hand iterable \
Y := the size of the left-hand iterable

### as-max-len?

The cost of evaluating an `as-max-len?` function is constant (the function
is performing a constant-time length check)

### map

The cost of mapping a list is the cost of the function lookup,
and the cost of each iterated function application

```
a + func_lookup_cost(F) + L * apply_eval_cost(F, i)
```

a is a constant \
`func_lookup_cost(F)` := the cost of looking up the function name F \
`apply_eval_cost(F, i)` := the cost of applying and evaluating the body of F on type i \
`i` := the list _item_ type \
`L` := the list length 

If computed during _static analysis_, L is the maximum length of the list
as specified by it's type.

### filter

The cost of filtering a list is the cost of the function lookup,
and the cost of each iterated filter application

```
a + func_lookup_cost(F) + L * apply_eval_cost(F, i)
```

a is a constant \
`func_lookup_cost(F)` := the cost of looking up the function name F \
`apply_eval_cost(F, i)` := the cost of applying and evaluating the body of F on type i \
`i` := the list _item_ type \
`L` := the list length

If computed during _static analysis_, L is the maximum length of the list
as specified by it's type.

### fold


The cost of folding a list is the cost of the function lookup,
and the cost of each iterated application

```
a + func_lookup_cost(F) + (L) * apply_eval_cost(F, i, j)
```

a is a constant \
`func_lookup_cost(F)` := the cost of looking up the function name F \
`apply_eval_cost(F, i, j)` := the cost of applying and evaluating the body of F on types i, j \
`j` := the accumulator type \
`i` := the list _item_ type \
`L` := the list length 

If computed during _static analysis_, L is the maximum length of the list
as specified by it's type.

### len

The cost of getting a list length is constant, because Clarity lists
store their lengths.

### list

The cost of constructing a new list is linear -- Clarity ensures that
each item in the list is of a matching type.

```
a*X+b
```

a and b are constants \
X := the total size of all arguments to the list constructor

### tuple

The cost of constructing a new tuple is `O(nlogn)` with respect to the number of
keys in the tuple (because tuples are represented as BTrees).

```
a*(X*log(X)) + b
```

a and b are constants \
X := the number of keys in the tuple

### get

Reading from a tuple is `O(nlogn)` with respect to the number of
keys in the tuple (because tuples are represented as BTrees).

```
a*(X*log(X)) + b
```

a and b are constants \
X := the number of keys in the tuple

## Option/Response Operations

### match

Match imposes a constant cost for evaluating the match, a cost for checking
that the match-bound name does not _shadow_ a previous variable. The
total cost of execution is:

```
a + evalCost(chosenBranch) + cost(lookupVariable)
```

where a is a constant, and `chosenBranch` is whichever branch
is chosen by the match. In static analysis, this will be:
`max(branch1, branch2)` 

### is-some, is-none, is-error, is-okay

These check functions all have constant cost.

### unwrap, unwrap-err, unwrap-panic, unwrap-err-panic, try!

These functions all have constant cost.

## Arithmetic and Logic Operations

### Variadic operators

The variadic operators (`+`,`-`,`/`,`*`, `and`, `or`) all have costs linear
in the _number_ of arguments supplied

```
(a*X+b)
```

X := the number of arguments

### Binary/Unary operators

The binary and unary operators:

```
>
>=
<
<=
mod
pow
xor
not
to-int
to-uint
```

all have constant cost, because their inputs are all of fixed sizes.

### Hashing functions

The hashing functions have linear runtime costs: the larger the value being
hashed, the longer the hashing function takes.

```
(a*X+b)
```

X := the size of the input.


## Memory Model and Limits

Clarity contract execution imposes a maximum memory usage limit for applications.
For any given Clarity value, the memory usage of that value is counted using
the _size_ of the Clarity value.

Memory is consumed by the following variable bindings:

* `let` - each value bound in the `let` consumes that amount of memory
    during the execution of the `let` block.
* `match` - the bound value in a `match` statement consumes memory during
    the execution of the `match` branch.
* function arguments - each bound value consumes memory during the execution
    of the function. this includes user-defined functions _as well as_ native
    functions.

Additionally, functions that perform _context changes_ also consume memory,
though they consume a constant amount:

* `as-contract`
* `at-block`

### Type signature size

Types in Clarity may be described using type signatures. For example,
`(tuple (a int) (b int))` describes a tuple with two keys `a` and `b`
of type `int`. These type descriptions are used by the Clarity analysis
passes to check the type correctness of Clarity code. Clarity type signatures
have varying size, e.g., the signature `int` is smaller than the signature for a
list of integers.

The size of a Clarity value is defined as follows:

```
type_size(x) :=
  if x = 
     int        => 16
    uint        => 16
    bool        => 1
    principal   => 148
    (buff y)    => 4 + y
    (some y)    => 1 + size(y)
    (ok y)      => 1 + size(y)
    (err y)     => 1 + size(y)
    (list ...)  => 4 + sum(size(z) for z in list)
    (tuple ...) => 1 + 2*(count(entries)) 
                     + sum(size(z) for each value z in tuple)
```

### Contract Memory Consumption

Contract execution requires loading the contract's program state in
memory. That program state counts towards the memory limit when
executed via a programmatic `contract-call!` or invoked by a
contract-call transaction.

The memory consumed by a contract is equal to:

```
a + b*contract_length + sum(size(x) for each constant x defined in the contract)
```

That is, a contract consumes memory which is linear in the contract's
length _plus_ the amount of memory consumed by any constants defined
using `define-constant`.

### Database Writes

While data stored in the database itself does _not_ count against the
memory limit, supporting public function abort/commit behavior requires
holding a write log in memory during the processing of a transaction.

Operations that write data to the data store therefore consume memory
_until the transaction completes_, and the write log is written to the
database. The amount of memory consumed by operations on persisted data
types is defined as:

* `data-var`: the size of the stored data var's value.
* `map`: the size of stored key + the size of the stored value.
* `nft`: the size of the NFT key
* `ft`: the size of a Clarity uint value.

## Cost Upgrades

In order to enable the addition of new native functions to the Clarity
language, there is a mechanism for voting on and changing a function's
_cost-assessment function_ (the asymptotic function that describes its
complexity and is used to calculate its cost). 

New functions can be introduced to Clarity by first being implemented
_in_ Clarity and published in a contract. This is necessary to avoid
a hard fork of the blockchain and ensure the availability of the function
across the network.

If it is decided that a published function should be a part of the Clarity
language, it can then be re-implemented as a native function in Rust and
included in a future release of Clarity. Nodes running this upgraded VM
would instead use this new native implementation of the function when they
encounter Clarity code that references it via `contract-call?`.

The new native function is likely faster and more efficient than the
prior Clarity implementation, so a new cost-assessment function may need
to be chosen for its evaluation. Until a new cost-assessment function is
agreed upon, the cost of the Clarity implementation will continue to be used.

### Voting on the Cost of Clarity Functions

New and more accurate cost-assessment functions can be agreed upon as
follows:

1. A user formulates a cost-assessment function and publishes it in a
Clarity contract as a `define-read-only` function.
2. The user proposes the cost-assessment function by calling the
`submit-proposal` function in the **Clarity Cost Voting Contract**.
3. Voting on the proposed function ensues via the voting functions in
the **Clarity Cost Voting Contract**, and the function is either
selected as a replacement for the existing cost-assessment function,
or ignored.

#### Publishing a Cost-Assessment Function

Cost-assessment functions to be included in proposals can be published
in Clarity contracts. They must be written precisely as follows:

1. The function must be `read-only`.
2. The function must return a tuple with the keys `runtime`, `write_length`,
`write_count`, `read_count`, and `read_length` (the execution cost measurement
[categories](#measurements-for-execution-cost)).
3. The values of the returned tuple must be Clarity expressions representing
the asymptotic cost functions. These expressions must be limited to **arithmetic operations**.
4. Variables used in these expressions must be listed as arguments to the Clarity
function.
5. Constant factors can be set directly in the code.

For example, suppose we have a function that implements a sorting algorithm:

```lisp
(define-public (quick-sort (input (list 1024 int))) ... )
```

The cost-assessment function should have _one_ argument, corresponding to the size
of the `input` field, e.g.

```lisp
(define-read-only (quick-sort-cost (n uint))
  {
    runtime: (* n (log n)),
    write_length: 0,
    write_count: 0,
    read_count: 0,
    read_length: 0,
  })
```

Here's another example where the cost function contains constant factors:

```lisp
(define-read-only (quick-sort-cost (n uint))
   {
     runtime: (+ 30 (* 2 n (log n))),
     write_length: 0,
     write_count: 0,
     read_count: 0,
     read_length: 0
   })
```

#### Making a Cost-Assessment Function Proposal

Stacks holders can propose cost-assessment functions by calling the
`submit-proposal` function in the **Clarity Cost Voting Contract**.

```Lisp
(define-public (submit-proposal
    (function-contract principal)
    (function-name (string-ascii 128))
    (cost-function-contract principal)
    (cost-function-name (string-ascii 128))
    ...
)
```

Description of `submit-proposal` arguments:
- `function-contract`: the principal of the contract that defines
the function for which a cost is being proposed
- `function-name`: the name of the function for which a cost is being proposed
- `cost-function-contract-principal`: the principal of the contract that defines
the cost function being proposed
- `cost-function-name`: the name of the cost-function being proposed

If submitting a proposal for a native function included in Clarity at boot,
provide the principal of the boot costs contract for the `function-contract`
argument, and the name of the corresponding cost function for the `function-name`
argument.

This function will return a response containing the proposal ID, if successful,
and an error otherwise.

Usage:
```Lisp
(contract-call?
    .cost-voting-contract
    "submit-proposal"
    .function-contract
    "function-name"
    .new-cost-function-contract
    "new-cost-function-name"
)
```

#### Viewing a Proposal

To view cost-assessment function proposals, you can use the 
`get-proposal` function in the **Clarity Cost Voting Contract**:

```Lisp
(define-read-only (get-proposal (proposal-id uint)) ... )
```

This function takes a `proposal-id` and returns a response containing the proposal
data tuple, if a proposal with the supplied ID exists, or an error code. Proposal
data tuples contain information about the state of the proposal, and take the
following form:

```Lisp
{
    cost-function-contract: principal,
    cost-function-name: (string-ascii 128),
    function-contract: principal,
    function-name: (string-ascii 128),
    expiration-block-height: uint
}
```

Usage:
```Lisp
(contract-call? .cost-voting-contract "get-proposal" 123)
```

### Voting

#### Stacks Holders

Stacks holders can vote for cost-assessment function proposals by calling the
**Clarity Cost Voting Contract's** `vote-proposal` function. The `vote-proposal`
function takes two arguments, `proposal-id` and `amount`. `proposal-id` is the ID
of the proposal being voted for. `amount` is the amount of STX the voter would like
to vote *with*. The amount of STX you include is the number of votes you are casting.

Calling the `vote` function authorizes the contract to transfer STX out
of the caller's address, and into the address of the contract. The equivalent
amount of `cost-vote-tokens` will be distributed to the voter, representing the
amount of STX they have staked in the voting contract.

STX staked for voting can be withdrawn from the voting contract by the voter with
the `withdraw-votes` function. If staked STX are withdrawn prior to confirmation,
they will not be counted as votes.

Upon withdrawal, the voter permits the contract to reclaim allocated `CFV` tokens,
and will receive the equivalent amount of their staked STX tokens.

**Voting example**
```Lisp
(contract-call? .cost-voting-contract "vote-proposal" 123 10000)
```

The `vote-proposal` function will return a successful response if the STX were staked
for voting, or an error if the staking failed.

**Withdrawal example**
```Lisp
(contract-call? .cost-voting-contract "withdraw-votes" 123 10000)
```

Like the `vote-proposal` function, the `withdraw-votes` function expects a `proposal-id` and
an `amount`, letting the voter withdraw some or all of their staked STX. This function
will return a successful response if the STX were withdrawn, and an error otherwise.

#### Miner Veto

Miners can vote *against* (veto) cost-function proposals by creating a transaction that
calls the **Clarity Cost Voting Contract's** `veto` function and mining
a block that includes this transaction. The `veto` function won't count
the veto if the block wasn't mined by the node that signed that transaction.
In other words, miners must **commit** their veto with their mining power.

Usage:
```Lisp
(contract-call? .cost-voting-contract "veto" 123)
```

This function will return a successful response if the veto was counted, or
an error if the veto failed.

### Confirming the Result of a Vote

In order for a cost-function proposal to get successfully voted in, it must be
**confirmed**. Confirmation is a two step process, involving calling the `confirm-votes`
function _before_ the proposal has expired to confirm the vote threshold was met,
and calling the `confirm-miners` function _after_ to confirm that the proposal wasn't vetoed
by miners.

#### Confirm Votes

Any stacks holder can call the `confirm-votes` function in the **Clarity
Cost Voting Contract** to attempt confirmation. `confirm-votes` will return a
success response and become **vote confirmed** if the following criteria are met.

1. The proposal must receive votes representing 20% of the liquid supply of STX.
This is calculated like such:
   
```lisp
(>= (/ (* votes u100) stx-liquid-supply) u20)
```

2. The proposal must not be expired, meaning its `expiration-height` must
not have been reached.
   
Usage:
```Lisp
(contract-call? .cost-voting-contract "confirm-votes" 123)
```

#### Confirm Miners

Like `confirm-votes`, any stacks holder can call the `confirm-miners` function.
`confirm-miners` will return a success response and the proposal will become
**miner confirmed** if the following criteria are met:

1. The number of vetos is less than 500.
2. There have been less than 10 proposals already confirmed in the current block.
3. The proposal has expired.

Usage:
```Lisp
(contract-call? .cost-voting-contract "confirm-miners" 123)
```

# Related Work

This section will be expanded upon after this SIP is ratified.

# Backwards Compatibility

All Stacks accounts from Stacks 1.0 will be imported into Stacks 2.0 when it
launches.  The state of the Stacks 1.0 chain will be snapshotted at Bitcoin
block 665750.

# Activation

At least 20 miners must register a name in the `.miner` namespace in Stacks 1.0.
Once the 20th miner has registered, the state of Stacks 1.0 will be snapshotted.
300 Bitcoin blocks later (Bitcoin block 666050), the Stacks 2.0 blockchain will launch.  Stacks 2.0
implements this SIP.

# Reference Implementations

Implemented in Rust.  See https://github.com/blockstack/stacks-blockchain.




================================================
FILE: sips/sip-007/sip-007-stacking-consensus.md
================================================
# Preamble

SIP Number: 007

Title: Stacking Consensus

Author:
    Muneeb Ali <muneeb@blockstack.com>,
    Aaron Blankstein <aaron@blockstack.com>,
    Michael J. Freedman <mfreed@cs.princeton.edu>,
    Diwaker Gupta <diwaker@blockstack.com>,
    Jude Nelson <jude@blockstack.com>, 
    Jesse Soslow <jesse@blockstack.com>, 
    Patrick Stanley <patrick@blockstack.com>

Consideration: Technical

Type: Consensus

Status: Ratified

Created: 14 January 2020

License: BSD 2-Clause

Sign-off: Jude Nelson <jude@stacks.org>, Technical Steering Committee Chair

Discussions-To: https://github.com/stacksgov/sips

# Abstract

This SIP proposes a new consensus algorithm, called Stacking, that
uses the proof-of-work cryptocurrency of an established blockchain to
secure a new blockchain. An economic benefit of the Stacking consensus
algorithm is that the holders of the new cryptocurrency can earn a
reward in a base cryptocurrency by actively participating in the
consensus algorithm.

This SIP proposes to change the mining mechanism of the Stacks
blockchain. [SIP-001](../sip-001/sip-001-burn-election.md) introduced
proof-of-burn (PoB) where a base cryptocurrency is destroyed to
participate in mining of a new cryptocurrency. This proposal argues
that a new mining mechanism called proof-of-transfer (PoX) will be an
improvement over proof-of-burn.

With proof-of-transfer, instead of destroying the base cryptocurrency,
miners are required to distribute the base cryptocurrency to existing
holders of the new cryptocurrency who participate in the consensus
algorithm. Therefore, existing holders of the new cryptocurrency have
an economic incentive to participate, do useful work for the network,
and receive rewards.

Proof-of-transfer avoids burning of the base cryptocurrency which
destroys some supply of the base cryptocurrency. Stacking in general
can be viewed as a more "efficient" algorithm where instead of
destroying a valuable resource (like electricity or base
cryptocurrency), the valuable resource is distributed to holders of
the new cryptocurrency.

The SIP describes one potential implementation of the Stacking
consensus algorithm for the Stacks blockchain using Bitcoin as the
base cryptocurrency.

# Introduction

Consensus algorithms for public blockchains require computational or
financial resources to secure the blockchain state. Mining mechanisms
used by these algorithms are broadly divided into proof-of-work (PoW),
in which nodes dedicate computational resources, and proof-of-stake
(PoS), in which nodes dedicate financial resources. The intention
behind both proof-of-work and proof-of-stake is to make it practically
infeasible for any single malicious actor to have enough computational
power or ownership stake to attack the network.

With proof-of-work, a miner does some "work" that consumes electricity
and is rewarded with digital currency. The miner is, theoretically,
converting electricity and computing power into the newly minted
digital currency. Bitcoin is an example of this and is by far the
largest and most secure PoW blockchain.

With proof-of-stake, miners stake their holdings of a new digital
currency to participate in the consensus algorithm and bad behavior
can be penalized by "slashing" the funds of the miner. PoS requires
less energy/electricity to be consumed and can give holders of the new
cryptocurrency who participate in staking a reward on their holdings
in the new cryptocurrency.

In this SIP we introduce a new consensus algorithm called
Stacking. The Stacking consensus algorithm uses a new type of mining
mechanism called *proof-of-transfer* (PoX). With PoX, miners are not
converting electricity and computing power to newly minted tokens, nor
are they staking their cryptocurrency. Rather they use an existing PoW
cryptocurrency to secure a new, separate blockchain.

This SIP proposes to change the mining
mechanism of the Stacks blockchain from proof-of-burn (SIP-001) to
proof-of-transfer.

The PoX mining mechanism is a modification of proof-of-burn (PoB)
mining (See
the [Blockstack Technical Whitepaper](https://blockstack.org/papers)
and [SIP-001](./sip-001-burn-election.md)). In
proof-of-burn mining, miners burn a base cryptocurrency to participate
in mining — effectively destroying the base cryptocurrency to mint
units of a new cryptocurrency. **In proof-of-transfer, rather than
destroying the base cryptocurrency, miners transfer the base
cryptocurrency as a reward to owners of the new cryptocurrency**. In
the case of the Stacks blockchain, miners would transfer Bitcoin to
owners of Stacks tokens in order for miners to receive newly-minted
Stacks tokens. The security properties of proof-of-transfer are
comparable to proof-of-burn.

# Specification

## Stacking with Bitcoin

In the Stacking consensus protocol, we require the base cryptocurrency
to be a proof-of-work blockchain. In this proposed implementation of
Stacking we assume that the PoW crypto-currency is Bitcoin, given it
is by far the most secure PoW blockchain. Theoretically, other PoW
blockchains can be used, but the security properties of Bitcoin are
currently superior to other PoW blockchains.

As with PoB, in PoX, the protocol selects the winning miner (*i.e.*,
the leader) of a round using a verifiable random function (VRF). The
leader writes the new block of the Stacks blockchain and mints the
rewards (newly minted Stacks). However, instead of bitcoins being sent
to burn addresses, the bitcoins are sent to a set of specific
addresses corresponding to Stacks (STX) tokens holders that are adding
value to the network. Thus, rather than being destroyed, the bitcoins
consumed in the mining process go to productive Stacks holders as a
reward based on their holdings of Stacks and participation in the
Stacking algorithm.

## Stacking Consensus Algorithm

In addition to the normal tasks of PoB mining
(see [SIP-001](./sip-001-burn-election.md)), the Stacking consensus
algorithm *must* determine the set of addresses that miners may
validly transfer funds to. PoB mining does not need to perform these
steps, because the address is always the same — the burn
address. However, with Stacking, network participants must be able to
validate the addresses that are sent to.

Progression in Stacking consensus happens over *reward cycles*. In
each reward cycle, a set of Bitcoin addresses are iterated over, such
that each Bitcoin address in the set of reward addresses has exactly
one Bitcoin block in which miners will transfer funds to the reward
address.

To qualify for a reward cycle, an STX holder must:


* Control a Stacks wallet with >= 0.02% of the total share of unlocked
  Stacks tokens (currently, there are ~470m unlocked Stacks tokens,
  meaning this would require ~94k Stacks). This threshold level
  adjusts based on the participation levels in the Stacking protocol.
* Broadcast a signed message before the reward cycle begins that:
    * Locks the associated Stacks tokens for a protocol-specified
      lockup period.
    * Specifies a Bitcoin address to receive the funds.
    * Votes on a Stacks chain tip.

Miners participating in the Stacks blockchain compete to lead blocks
by transferring Bitcoin. Leaders for particular Stacks blocks are
chosen by sortition, weighted by the amount of Bitcoin sent (see
SIP-001). Before a reward cycle begins, the Stacks network must reach
consensus on which addresses are valid recipients. Reaching consensus
on this is non-trivial: the Stacks blockchain itself has many
properties independent from the Bitcoin blockchain, and may experience
forks, missing block data, etc., all of which make reaching consensus
difficult. As an extreme example, consider a miner that forks the
Stacks chain with a block that claims to hold a large fraction (e.g.,
100%) of all Stacks holdings, and proceeds to issue block commitments
that pay all of the fees to themselves. How can other nodes on the
network detect that this miner’s commitment transfers are invalid?

The Stacking algorithm addresses this with a two-phase cycle. Before
each reward cycle, Stacks nodes engage in a *prepare* phase, in which
two items are decided:


1. An **anchor block** — the anchor block is a Stacks chain block. For
   the duration of the reward cycle, mining any descendant forks of
   the anchor block requires transferring mining funds to the
   appropriate reward addresses.
2. The **reward set** -- the reward set is the set of Bitcoin
   addresses which will receive funds in the reward cycle. This set is
   determined using Stacks chain state from the anchor block.

During the reward cycle, miners contend with one another to become the
leader of the next Stacks block by broadcasting *block commitments* on
the Bitcoin chain. These block commitments send Bitcoin funds to
either a burn address or a PoX reward address.

Address validity is determined according to two different rules:


1. If a miner is building off of any chain tip *which is not a
   descendant of the anchor block*, all of the miner's commitment
   funds must be burnt.
2. If a miner is building off a descendant of the anchor block, the
   miner must send commitment funds to 2 addresses from the reward
   set, chosen as follows:
    * Use the verifiable random function (also used by sortition) to
      choose 2 addresses from the reward set. These 2 addresses are
      the reward addresses for this block.
    * Once addresses have been chosen for a block, these addresses are
      removed from the reward set, so that future blocks in the reward
      cycle do not repeat the addresses.

Note that the verifiable random function (VRF) used for address
selection ensures that the same addresses are chosen by each miner
selecting reward addresses. If a miner submits a burn commitment which
*does not* send funds to a valid address, those commitments are
ignored by the rest of the network (because other network participants
can deduce that the transfer addresses are invalid).

To reduce the complexity of the consensus algorithm, Stacking reward
cycles are fixed length --- if fewer addresses participate in the
Stacking rewards than there are slots in the cycle, then the remaining
slots are filled with *burn* addresses. Burn addresses are included
in miner commitments at fixed intervals (e.g, if there are 1000 burn
addresses for a reward cycle, then each miner commitment would have
1 burn address as an output).

### Adjusting Reward Threshold Based on Participation

Each reward cycle may transfer miner funds to up to 4000 Bitcoin
addresses (2 addresses in a 2000 burn block cycle). To ensure that
this number of addresses is sufficient to cover the pool of
participants (given 100% participation of liquid STX), the threshold
for participation must be 0.025% (1/4000th) of the liquid supply of
STX. However, if participation is _lower_ than 100%, the reward pool
could admit lower STX holders. The Stacking protocol specifies **2
operating levels**:

* **25%** If fewer than `0.25 * STX_LIQUID_SUPPLY` STX participate in
  a reward cycle, participant wallets controlling `x` STX may include
  `floor(x / (0.0000625*STX_LIQUID_SUPPLY))` addresses in the reward set.
  That is, the minimum participation threshold is 1/16,000th of the liquid
  supply.
* **25%-100%** If between `0.25 * STX_LIQUID_SUPPLY` and `1.0 *
  STX_LIQUID_SUPPLY` STX participate in a reward cycle, the reward
  threshold is optimized in order to maximize the number of slots that
  are filled. That is, the minimum threshold `T` for participation will be
  roughly 1/4,000th of the participating STX (adjusted in increments
  of 10,000 STX). Participant wallets controlling `x` STX may
  include `floor(x / T)` addresses in the
  reward set.

In the event that a Stacker signals and locks up enough STX to submit
multiple reward addresses, but only submits one reward address, that
reward address will be included in the reward set multiple times.

### Submitting Reward Address and Chain Tip Signaling

Stacking participants must broadcast signed messages for three purposes:

1. Indicating to the network how many STX should be locked up, and for
   how many reward cycles.
2. Indicate support for a particular chain tip.
3. Specifying the Bitcoin address for receiving Stacking rewards.

These messages may be broadcast either on the Stacks chain or the
Bitcoin chain. If broadcast on the Stacks chain, these messages must
be confirmed on the Stacks chain _before_ the anchor block for the
reward period. If broadcast on the Bitcoin chain, they may be
broadcast during the prepare phase, but must be included before
the prepare phase finishes.

These signed messages are valid for at most 12 reward cycles (25200 Bitcoin
blocks or ~7 months). If the signed message specifies a lockup period `x` less
than 25200 blocks, then the signed message is only valid for Stacking
participation for `floor(x / 2100)` reward cycles (the minimum participation
length is one cycle: 2100 blocks).


## Anchor Blocks and Reward Consensus

In the **prepare** phase of the Stacking algorithm, miners and network
participants determine the anchor block and the reward set. The
prepare phase is a window `w` of Bitcoin blocks *before* the reward
cycle begins (e.g., the window may be 100 Bitcoin blocks).

At a high-level, nodes determine whether any block was confirmed by
`F*w` blocks during the phase, where `F` is a large fraction (e.g.,
`0.8`). Once the window `w` closes at time `cur`, Stacks nodes find
the potential anchor block as described in the following pseudocode:


```python
def find_anchor_block(cur):
  blocks_worked_on = get_all_stacks_blocks_between(cur - w, cur)

  # get the highest/latest ancestor before the PREPARE phase for each block worked
  # on during the PREPARE phase.

  candidate_anchors = {}
  for block in blocks_worked_on:
    pre_window_ancestor = last_ancestor_of_block_before(block, cur - w)
    if pre_window_ancestor is None:
      continue
    if pre_window_ancestor in candidate_anchors:
      candidate_anchors[pre_window_ancestor] += 1
    else:
      candidate_anchors[pre_window_ancestor] = 1

  # if any block is confirmed by at least F*w, then it is the anchor block.
  for candidate, confirmed_by_count in candidate_anchors.items():
    if confirmed_by_count >= F*w
      return candidate

  return None
```

Note that there can be at most one anchor block (so long as `F >
0.5`), because:

* Each of the `w` blocks in the prepare phase has at most one
  candidate ancestor.
* The total possible number of confirmations for anchor blocks is `w`.
* If any block is confirmed by `>= 0.5*w`, then any other block must
  have been confirmed by `< 0.5*w`.

The prepare phase, and the high threshold for `F`, are necessary to
protect the Stacking consensus protocol from damage due to natural
forks, missing block data, and potentially malicious participants. As
proposed, PoX and the Stacking protocol require that Stacks nodes are
able to use the anchor block to determine the *reward set*. If, by
accident or malice, the data associated with the anchor block is
unavailable to nodes, then the Stacking protocol cannot operate
normally — nodes cannot know whether or not a miner is submitting
valid block commitments. A high threshold for `F` ensures that a large
fraction of the Stacks mining power has confirmed the receipt of the
data associated with the anchor block.

### Recovery from Missing Data

In the extreme event that a malicious miner *is* able to get a hidden
or invalid block accepted as an anchor block, Stacks nodes must be
able to continue operation. To do so, Stacks nodes treat missing
anchor block data as if no anchor block was chosen for the reward
cycle — the only valid election commitments will therefore be *burns*
(this is essentially a fallback to PoB). If anchor block data which
was previously missing is revealed to the Stacks node, it must
reprocess all of the leader elections for that anchor block's
associated reward cycle, because there may now be many commitments
which were previously invalid that are now valid.

Reprocessing leader elections is computationally expensive, and
would likely result in a large reorganization of the Stacks
chain. However, such an election reprocessing may only occur once per
reward window (only one valid anchor block may exist for a reward
cycle, whether it was hidden or not). Crucially, intentionally
performing such an attack would require collusion amongst a large
fraction `F` of the Stacks mining power — because such a hidden block
must have been confirmed by `w*F` subsequent blocks. If collusion
amongst such a large fraction of the Stacks mining power is possible,
we contend that the security of the Stacks chain would be compromised
through other means beyond attacking anchor blocks.

### Anchoring with Stacker Support.

The security of anchor block selection is further increased through
Stacker support transactions. In this protocol, when Stacking
participants broadcast their signed participation messages, they
signal support of anchor blocks. This is specified by the chain tip's
hash, and the support signal is valid as long as the message itself is
valid.

This places an additional requirement on anchor block selection. In
addition to an anchor block needing to reach a certain number of miner
confirmations, it must also pass some threshold `t` of valid Stacker
support message signals. This places an additional burden on an anchor
block attack --- not only must the attacker collude amongst a large
fraction of mining power, but they must also collude amongst a
majority of the Stacking participants in their block.

## Stacker Delegation

The process of delegation allows a Stacks wallet address (the
represented address) to designate another address (the delegate
address) for participating in the Stacking protocol. This delegate
address, for as long as the delegation is valid, is able to sign and
broadcast Stacking messages (i.e., messages which lock up Stacks,
designate the Bitcoin reward address, and signal support for chain
tips) on behalf of the represented address. This allows the owner of
the represented address to contribute to the security of the network
by having the delegate address signal support for chain tips. This
combats potential attacks on the blockchain stability by miners that
may attempt to mine hidden forks, hide eventually invalid forks, and
other forms of miner misbehavior.

Supporting delegation adds two new transaction types to the Stacks
blockchain:

* **Delegate Funds.** This transaction initiates a
  represented-delegate relationship. It carries the following data:
    * Delegate address
    * End Block: the Bitcoin block height at which this relationship
      terminates, unless a subsequent delegate funds transaction updates
      the relationship.
    * Delegated Amount: the total amount of STX from this address
      that the delegate address will be able to issue Stacking messages
      on behalf of.
    * Reward Address (_optional_): a Bitcoin address that must be
      designated as the funds recipient in the delegate’s Stacking
      messages. If unspecified, the delegate can choose the address.
* **Terminate Delegation.** This transaction terminates a
  represented-delegate relationship. It carries the following data:
    * Delegate Address
    
_Note_: There is only ever one active represented-delegate
relationship between a given represented address and delegate address
(i.e., the pair _(represented-address, delegate-address)_ uniquely
identifies a relationship). If a represented-delegate relationship is
still active and the represented address signs and broadcasts a new
"delegate funds" transaction, the information from the new transaction
replaces the prior relationship.

Both types of delegation transactions must be signed by the
represented address. These are transactions on the Stacks blockchain,
and will be implemented via a native smart contract, loaded into the
blockchain during the Stacks 2.0 genesis block. These transactions,
therefore, are `contract-call` invocations. The invoked methods are
guarded by:

```
    (asserts! (is-eq contract-caller tx-sender) (err u0))
```

This insures that the methods can only be invoked by direct
transaction execution.

**Evaluating Stacking messages in the context of delegation.** In
order to determine which addresses’ STX should be locked by a given
Stacking message, the message must include the represented address in
the Stacking message. Therefore, if a single Stacks address is the
delegate for many represented Stacks addresses, the delegate address
must broadcast a Stacking message for each of the represented
addresses.

## Addressing Miner Consolidation in Stacking

PoX when used for Stacking rewards could lead to miner
consolidation. Because miners that _also_ participate as Stackers
could gain an advantage over miners who do not participate as
Stackers, miners would be strongly incentivized to buy Stacks and use
it to crowd out other miners. In the extreme case, this consolidation
could lead to centralization of mining, which would undermine the
decentralization goals of the Stacks blockchain. While we are actively
investigating additional mechanisms to address this potential
consolidation, we propose a time-bounded PoX mechanism and a Stacker-
driven mechanism here.

**Time-Bounded PoX.** Stacking rewards incentivize miner consolidation
if miners obtain _permanent_ advantages for obtaining the new
cryptocurrency. However, by limiting the time period of PoX, this
advantage declines over time. To do this, we define two time periods for Pox:

1. **Initial Phase.** In this phase, Stacking rewards proceed as
   described above -- commitment funds are sent to Stacking rewards
   addresses, except if a miner is not mining a descendant of the
   anchor block, or if the registered reward addresses for a given
   reward cycle have all been exhausted. This phase will last for
   approximately 2 years (100,000 Bitcoin blocks).

2. **Sunset Phase.** After the initial phase, a _sunset_ block is
   determined. This sunset block will be ~8 years (400,000 Bitcoin
   blocks) after the sunset phase begins. After the sunset block,
   _all_ miner commitments must be burned, rather than transfered to
   reward addresses. During the sunset phase, the reward / burn ratio
   linearly decreases by `0.25%` (1/400) on each reward cycle, such
   that in the 200th reward cycle, the ratio of funds that are
   transfered to reward addresses versus burnt must be equal to
   `0.5`. For example, if a miner commits 10 BTC, the miner must send
   5 BTC to reward addresses and 5 BTC to the burn address.

By time-bounding the PoX mechanism, we allow the Stacking protocol to
use PoX to help bootstrap support for the new blockchain, providing
miners and holders with incentives for participating in the network
early on. Then, as natural use cases for the blockchain develop and
gain steam, the PoX system could gradually scale down.

**Stacker-driven PoX.**  To further discourage miners from consolidating,
holders of liquid (i.e. non-Stacked) STX tokens may vote to disable PoX in the next upcoming
reward cycle.  This can be done with any amount of STX, and the act of voting
to disable PoX does not lock the tokens.

This allows a community of vigilent
users guard the chain from bad miner behavior arising from consolidation
on a case-by-case basis.  Specifically, if a fraction _R_ of liquid STX
tokens vote to disable PoX, it is disabled
only for the next reward cycle.  To continuously deactivate PoX, the STX
holders must continuously vote to disable it.

Due to the costs of remaining vigilent, this proposal recommends _R = 0.25_.
At the time of this writing, this is higher than any single STX allocation, but
not so high that large-scale cooperation is needed to stop a mining cartel.

## Bitcoin Wire Formats

Supporting PoX in the Stacks blockchain requires modifications to the
wire format for leader block commitments, and the introduction of new
wire formats for burnchain PoX participation (e.g., performing the STX
lockup on the burnchain).


### Leader Block Commits

For PoX, leader block commitments are similar to PoB block commits: the constraints on the
BTC transaction's inputs are the same, and the `OP_RETURN` output is identical. However,
the _burn output_ is no longer the same. For PoX, the following constraints are applied to
the second through nth outputs:

1. If the block commitment is in a reward cycle, with a chosen anchor block, and this block
   commitment builds off a descendant of the PoX anchor block (or the anchor block itself),
   then the commitment must use the chosen PoX recipients for the current block.
      * PoX recipients are chosen as described in "Stacking Consensus Algorithm": addresses
        are chosen without replacement, by using the previous burn block's sortition hash,
        mixed with the previous burn block's burn header hash as the seed for the ChaCha12
        pseudorandom function to select M addresses.
      * The leader block commit transaction must use the selected M addresses as outputs [1, M]
        That is, the second through (M+1)th output correspond to the select PoX addresses.
        The order of these addresses does not matter. Each of these outputs must receive the
        same amount of BTC.
      * If the number of remaining addresses in the reward set N is less than M, then the leader
        block commit transaction must burn BTC by including (M-N) burn outputs.
2. Otherwise, the second through (M+1)th output must be burn addresses, and the amount burned by
   these outputs will be counted as the amount committed to by the block commit.

In addition, during the sunset phase (i.e., between the 100,000th and 500,000th burn block in the chain),
the miner must include a _sunset burn_ output. This is an M+1 indexed output that includes the burn amount
required to fulfill the sunset burn ratio, and must be sent to the burn address:

```
sunset_burn_amount = (total_block_commit_amount) * (reward_cycle_start_height - 100,000) / (400,000)
```

Where `total_block_commit_amount` is equal to the sum of outputs [1, M+1].

After the sunset phase _ends_ (i.e., blocks >= 500,000th burn block), block commits are _only_ burns, with
a single burn output at index 1.

### STX Operations on Bitcoin

As described above, PoX allows stackers to submit `stack-stx`
operations on Bitcoin as well as on the Stacks blockchain. The Stacks
chain also allows addresses to submit STX transfers on the Bitcoin
chain. Such operations are only evaluated by the miner of an anchor block
elected in the burn block that immediately follows the burn block that included the
operations. For example, if a `TransferStxOp` occurs in burnchain block 100, then the
Stacks block elected by burnchain block 101 will process that transfer.

In order to submit on the Bitcoin chain, stackers must submit two Bitcoin transactions:

* `PreStxOp`: this operation prepares the Stacks blockchain node to validate the subsequent
  `StackStxOp` or `TransferStxOp`.
* `StackStxOp`: this operation executes the `stack-stx` operation.
* `TransferStxOp`: this operation transfers STX from a sender to a recipient

The wire formats for the above operations are as follows:

#### PreStxOp

This operation includes an `OP_RETURN` output for the first Bitcoin output that looks as follows:

```
            0      2  3
            |------|--|
             magic  op 
```

Where `op = p` (ascii encoded).

Then, the second Bitcoin output _must_ be Stacker address that will be used in a `StackStxOp`. This
address must be a standard address type parseable by the stacks-blockchain node.

#### StackStxOp

The first input to the Bitcoin operation _must_ consume a UTXO that is
the second output of a `PreStxOp`. This validates that the `StackStxOp` was signed
by the appropriate Stacker address.

This operation includes an `OP_RETURN` output for the first Bitcoin output:

```
            0      2  3                             19        20
            |------|--|-----------------------------|---------|
             magic  op         uSTX to lock (u128)     cycles (u8)
```

Where `op = x` (ascii encoded).

Where the unsigned integer is big-endian encoded.

The second Bitcoin output will be used as the reward address for any stacking rewards.

#### TransferStxOp

The first input to the Bitcoin operation _must_ consume a UTXO that is
the second output of a `PreStxOp`. This validates that the `TransferStxOp` was signed
by the appropriate STX address.

This operation includes an `OP_RETURN` output for the first Bitcoin output:

```
            0      2  3                             19        80
            |------|--|-----------------------------|---------|
             magic  op     uSTX to transfer (u128)     memo (up to 61 bytes)
```

Where `op = $` (ascii encoded).

Where the unsigned integer is big-endian encoded.

The second Bitcoin output is either a `p2pkh` or `p2sh` output such
that the recipient Stacks address can be derived from the
corresponding 20-byte hash (hash160).

# Related Work

This section will be expanded upon after this SIP is ratified.

# Backwards Compatibility

Not applicable.

# Activation

At least 20 miners must register a name in the `.miner` namespace in Stacks 1.0.
Once the 20th miner has registered, the state of Stacks 1.0 will be snapshotted.
300 Bitcoin blocks later (Bitcoin block 666050), the Stacks 2.0 blockchain will launch.  Stacks 2.0
implements this SIP.

# Reference Implementations

Implemented in Rust.  See https://github.com/blockstack/stacks-blockchain.




================================================
FILE: sips/sip-008/sip-008-analysis-cost-assessment.md
================================================
# Preamble

SIP Number: 008

Title: Clarity Parsing and Analysis Cost Assessment

Author: Aaron Blankstein <aaron@blockstack.com>

Consideration: Technical

Type: Consensus

Status: Ratified

Created: 5 March 2020

License: BSD 2-Clause

Sign-off: Jude Nelson <jude@stacks.org>, Technical Steering Committee Chair

Discussions-To: https://github.com/stacksgov/sips

# Abstract

This document describes the measured costs and asymptotic costs
assessed for parsing Clarity code into an abstract syntax tree (AST)
and the static analysis of that Clarity code (type-checking and
read-only enforcement). This will not specify the _constants_
associated with those asymptotic cost functions. Those constants will
necessarily be measured via benchmark harnesses and regression
analyses.

# Introduction

The cost of analyzing Clarity code is measured using the same 5 categories
described in SIP-006 for the measurement of execution costs:

1. Runtime cost: captures the number of cycles that a single
   processor would require to process the Clarity block. This is a
   _unitless_ metric, so it will not correspond directly to cycles,
   but rather is meant to provide a basis for comparison between
   different Clarity code blocks.
2. Data write count: captures the number of independent writes
   performed on the underlying data store (see SIP-004).
3. Data read count: captures the number of independent reads
   performed on the underlying data store.
4. Data write length: the number of bytes written to the underlying
   data store.
5. Data read length: the number of bytes read from the underlying
   data store.

Importantly, these costs are used to set a _block limit_ for each
block.  When it comes to selecting transactions for inclusion in a
block, miners are free to make their own choices based on transaction
fees, however, blocks may not exceed the _block limit_. If they do so,
the block is considered invalid by the network --- none of the block's
transactions will be materialized and the leader forfeits all rewards
from the block.

Costs for static analysis are assessed during the _type check_ pass.
The read-only and trait-checking passes perform work which is strictly
less than the work performed during type checking, and therefore, the
cost assessment can safely fold any costs that would be incurred during
those passes into the type checking pass.

# Specification

## Common Analysis Metrics and Costs

### AST Parsing

The Clarity parser has a runtime that is linear with respect to the Clarity
program length.

```
a*X+b
```

where a and b are constants, and

X := the program length in bytes

### Dependency cycle detection

Clarity performs cycle detection for intra-contract dependencies (e.g.,
functions that depend on one another). This detection is linear in the
number of dependency edges in the smart contract:

```
a*X+b
```

where a and b are constants, and
X := the total number of dependency edges in the smart contract

Dependency edges are created anytime a top-level definition refers 
to another top-level definition.

### Type signature size

Types in Clarity may be described using type signatures. For example,
`(tuple (a int) (b int))` describes a tuple with two keys `a` and `b`
of type `int`. These type descriptions are used by the Clarity analysis
passes to check the type correctness of Clarity code. Clarity type signatures
have varying size, e.g., the signature `int` is smaller than the signature for a
list of integers.

The signature size of a Clarity type is defined as follows:

```
type_signature_size(x) :=
  if x = 
     int      => 1
    uint      => 1
    bool      => 1
    principal => 1
    buffer    => 2
    optional  => 1 + type_signature_size(entry_type)
    response  => 1 + type_signature_size(ok_type) + type_signature_size(err_type)
    list      => 2 + type_signature_size(entry_type)
    tuple     => 1 + 2*(count(entries)) 
                   + sum(type_signature_size for each entry)
                   + sum(len(key_name) for each entry)
```

### Type annotation

Each node in a Clarity contract's AST is annotated with the type value
for that node during the type checking analysis pass.

The runtime cost of type annotation is:

```
a + b*X
```

where a and b are constants, and X is the type signature size of the
type being annotated.

### Variable lookup

Looking up variables during static analysis incurs a non-constant cost -- the stack
depth _and_ the length of the variable name affect this cost. However,
variable names in Clarity have bounded length -- 128 characters. Therefore,
the cost assessed for variable lookups may safely be constant with respect
to name length.

The stack depth affects the lookup cost because the variable must be
checked for in each context on the stack.

Cost Function:

```
a*X+b*Y+c
```

where a, b, and c are constants,
X := stack depth
Y := the type size of the looked up variable

### Function Lookup

Looking up a function incurs a constant cost with respect
to name length (for the same reason as variable lookup). However,
because functions may only be defined in the top-level contract
context, stack depth does not affect function lookup.

Cost Function:

```
a*X + b
```

where a and b are constants,
X := the sum of the type sizes for the function signature (each argument's type size, as well
    as the function's return type)

### Name Binding

The cost of binding a name in Clarity -- in either a local or the contract
context is _constant_ with respect to the length of the name, but linear in
the size of the type signature.

```
binding_cost = a + b*X
```

where a and b are constants, and
X := the size of the bound type signature

### Type check cost

The cost of a static type check is _linear_ in the size of the type signature:

```
type_check_cost(expected, actual) :=
  a + b*X
```

where a and b are constants, and

X := `max(type_signature_size(expected), type_signature_size(actual))`

### Function Application

Static analysis of a function application in Clarity requires
type checking the function's expected arguments against the
supplied types.

The cost of applying a function is:


```
a + sum(type_check_cost(expected, actual) for each argument)
```

where a is a constant.

This is also the _entire_ cost of type analysis for most function calls
(e.g., intra-contract function calls, most simple native functions). 

### Iterating the AST

Static analysis iterates over the entire program's AST in the type checker,
the trait checker, and in the read-only checker. This cost is assessed
as a constant cost for each node visited in the AST during the type
checking pass.

## Special Function Costs

Some functions require additional work from the static analysis system.

### Functions on sequences (e.g., map, filter, fold)

Functions on sequences need to perform an additional check that the
supplied type is a list or buffer before performing the normal
argument type checking. This cost is assessed as:

```
a
```

where a is a constant.

### Functions on options/responses

Similarly to the functions on sequences, option/response functions
must perform a simple check to see if the supplied input is an option or
response before performing additional argument type checking. This cost is
assessed as:

```
a
```

### Data functions (ft balance checks, nft lookups, map-get?, ...)

Static checks on intra-contract data functions do not require database lookups
(unlike the runtime costs of these functions). Rather, these functions
incur normal type lookup (i.e., fetching the type of an NFT, data map, or data var)
and type checking costs.

### get

Checking a tuple _get_ requires accessing the tuple's signature
for the specific field. This has runtime cost:

```
a*log(N) + b
```
where a and b are constants, and

N := the number of fields in the tuple type

### tuple

Constructing a tuple requires building the tuple's BTree for
accessing fields. This has runtime cost:


```
a*N*log(N) + b
```
where a and b are constants, and

N := the number of fields in the tuple type

### use-trait

Importing a trait imposes two kinds of costs on the analysis.
First, the import requires a database read. Second, the imported
trait is included in the static analysis output -- this increases
the total storage usage and write length of the static analysis.

The costs are defined as:

```
read_count = 1
write_count = 0
runtime = a*X+b
write_length = c*X+d
read_length = c*X+d
```

where a, b, c, and d are constants, and

X := the total type size of the trait (i.e., the sum of the
    type sizes of each function signature).

### contract-call?

Checking a contract call requires a database lookup to inspect
the function signature of a prior smart contract.

The costs are defined as:

```
read_count = 1
read_length = a*X+b
runtime = c*X+d
```

where a, b, c, and d are constants, and

X := the total type size of the function signature

### let

Let bindings require the static analysis system to iterate over
each let binding and ensure that they are syntactically correct.

This imposes a runtime cost:

```
a*X + b
```
where a and b are constants, and

X := the number of entries in the let binding.

# Related Work

This section will be expanded upon after this SIP is ratified.

# Backwards Compatibility

Not applicable.

# Activation

At least 20 miners must register a name in the `.miner` namespace in Stacks 1.0.
Once the 20th miner has registered, the state of Stacks 1.0 will be snapshotted.
300 Bitcoin blocks later (Bitcoin block 666050), the Stacks 2.0 blockchain will launch.  Stacks 2.0
implements this SIP.

# Reference Implementations

Implemented in Rust.  See https://github.com/blockstack/stacks-blockchain.




================================================
FILE: sips/sip-009/sip-009-nft-standard.md
================================================
# Preamble

SIP Number: 009

Title: Standard Trait Definition for Non-Fungible Tokens

Author: Friedger Müffke (mail@friedger.de), Muneeb Majeed

Consideration: Technical

Type: Standard

Status: Ratified

Created: 10 December 2020

License: CC0-1.0

Sign-off: Jude Nelson <jude@stacks.org>, Technical Steering Committee Chair

# Abstract

Non-fungible tokens or NFTs are digital assets registered on blockchain with unique identifiers and properties that distinguish them from each other.
It should be possible to uniquely identify, own and transfer a non-fungible token. This SIP aims to provide a flexible and easy-to-implement standard that can be used by developers on the Stacks blockchain when creating their own NFTs. This standard only specifies a basic set of requirements, non-fungible tokens can have more features than what's specified in this standard.

# License and Copyright

This SIP is made available under the terms of the Creative Commons CC0 1.0 Universal license, available at https://creativecommons.org/publicdomain/zero/1.0/
This SIP’s copyright is held by the Stacks Open Internet Foundation.

# Introduction

Tokens are digital assets registered on blockchain through a smart contract. A non-fungible token (NFT) is a token that is globally unique and can be identified through its unique identifier.

In blockchains with smart contracts, including the Stacks blockchain, developers and users can use smart contracts to register and interact with non-fungible tokens.

The Stacks blockchain's programming language for developing smart contracts, Clarity, has built-in language primitives to define and use non-fungible tokens. Although those primitives exists, there is value in defining a common interface (known in Clarity as a "trait") that allows different smart contracts to interoperate with non-fungible token contracts in a reusable way. This SIP defines that trait.

Each NFT always belong to one smart contract. NFTs of a smart contract are enumerated starting at 1. The current last ID is provided by a smart contract function. The asset ID together with the contract ID defines a globally unique NFT.

# Specification

Every SIP-009 compliant smart contract in Stacks blockchain must implement the trait, `nft-trait`, defined in the [Trait](#trait) section and must meet the requirements for the following functions:

### Last token ID

`(get-last-token-id () (response uint uint))`

Takes no arguments and returns the identifier for the last NFT registered using the contract. The returned ID can be used as the upper limit when iterating through all NFTs.

This function must never return an error response. It can be defined as read-only, i.e. `define-read-only`.

### Token URI

`(get-token-uri (uint) (response (optional (string-ascii 256)) uint))`

Takes an NFT identifier and returns a response containing a valid URI which resolves to the NFT's metadata. The URI string must be wrapped in an `optional`. If the corresponding NFT doesn't exist or the contract doesn't maintain metadata, the response must be `(ok none)`. If a valid URI exists for the NFT, the response must be `(ok (some "<URI>"))`. The length of the returned URI is limited to 256 characters. The specification of the metadata should be covered in a separate SIP.

This function must never return an error response. It can be defined as read-only, i.e. `define-read-only`.

### Owner

`(get-owner (uint) (response (optional principal) uint))`

Takes an NFT identifier and returns a response containing the principal owning the NFT with the given identifier. The principal must be wrapped in an optional. If the corresponding NFT doesn't exist, the response must be `(ok none)`. The owner can be a contract principal.

If a call to function `get-owner` returns some principal `A`, then it must return the same value until the `transfer` function is called with principal `A` as the sender.

For any call to `get-owner` with an ID greater than the last token ID returned by the `get-last-token-id` function, the call must return a response `(ok none)`.

This function must never return an error response. It can be defined as read-only, i.e. `define-read-only`.

### Transfer

`(transfer (uint principal principal) (response bool uint))`

The function changes the ownership of the NFT for the given identifier from the sender principal to the recipient principal.

This function must be defined with define-public, as it alters state, and must be externally callable.

After a successful call to `transfer`, the function `get-owner` must return the recipient of the `transfer` call as the new owner.

For any call to `transfer` with an ID greater than the last token ID returned by the `get-last-token-id` function, the call must return an error response.

It is recommended to use error codes from standardized list of codes and implement the function for converting the error codes to messages function that are defined in a separate SIP.

## Trait

```
(define-trait nft-trait
  (
    ;; Last token ID, limited to uint range
    (get-last-token-id () (response uint uint))

    ;; URI for metadata associated with the token
    (get-token-uri (uint) (response (optional (string-ascii 256)) uint))

     ;; Owner of a given token identifier
    (get-owner (uint) (response (optional principal) uint))

    ;; Transfer from the sender to a new principal
    (transfer (uint principal principal) (response bool uint))
  )
)
```

## Use of native asset functions

Although it is not possible to mandate in a Clarity trait, contract implementers must define at least one built-in native non-fungible [asset class](https://app.sigle.io/friedger.id/FDwT_3yuMrHDQm-Ai1OVS) that are provided as Clarity primitives. This allows clients to use Post Conditions (explained below), and takes advantages of other benefits, like native support for these asset balances and transfers through `stacks-blockchain-api`. The reference implementations included in this SIP use the native asset primitives, and provide a good boilerplate for their usage.

The native asset functions include:

- `define-non-fungible-token`
- `nft-burn?`
- `nft-get-owner?`
- `nft-mint?`
- `nft-transfer?`

The following requirements for using native asset functions are defined:

### Transfer

If the `transfer` function is called from a client without a [post-condition](https://docs.blockstack.org/understand-stacks/transactions#post-conditions) in deny mode or without any NFT condition about a changed owner, then the function call must fail with `abort_by_post_condition`.

# Using NFTs in applications

Developers who wish to use a non-fungible token contract in an application should first be provided, or keep track of, various different non-fungible token implementations. When validating a non-fungible token contract, they should fetch the interface and/or source code for that contract. If the contract implements the trait, then the application can use this standard's contract interface for making transfers and getting other details defined in this standard.

All of the functions in this trait return the `response` type, which is a requirement of trait definitions in Clarity. However, some of these functions should be "fail-proof", in the sense that they should never return an error. These "fail-proof" functions are those that have been recommended as read-only. If a contract that implements this trait returns an error for these functions, it may be an indication of a non-compliant contract, and consumers of those contracts should proceed with caution.

## Use of Post-Conditions

The Stacks blockchain includes a feature known as "Post-Conditions" or "Constraints". By defining post-conditions, users can create transactions that include pre-defined guarantees about what might happen in that contract.

For example, when applications call the `transfer` function, they should _always_ use post conditions to specify that the new owner of the NFT is the recipient principal in the `transfer` function call.

# Related Work

NFTs are an established asset class on blockchains. Read for example [here](https://www.ledger.com/academy/what-are-nft).

## EIP 721

Ethereum has [EIP 721](https://eips.ethereum.org/EIPS/eip-721) that defined non-fungible tokens on the Ethereum blockchain. Notable differences are that the transfer function in EIP 721 uses a different ordering of the arguments ending with the token id. The transfer function in this SIP uses the token ID as the first argument which is in line with the other native functions in Clarity. Furthermore, this SIP only defines a function for getting the URI pointing to the metadata of an NFT. The specifications for schema and other properties of the token metadata should be defined in a separate SIP.

# Backwards Compatibility

Not applicable

# Activation

This SIP is activated if 5 contracts are deployed that use the same trait that follows this specification. This must happen before Bitcoin tip #700,000.

A trait that follows this specification is available on mainnet as [`SP2PABAF9FTAJYNFZH93XENAJ8FVY99RRM50D2JG9.nft-trait.nft-trait`](https://explorer.stacks.co/txid/0x80eb693e5e2a9928094792080b7f6d69d66ea9cc881bc465e8d9c5c621bd4d07?chain=mainnet).

# Reference Implementations

## Source code

### Friedger's clarity-smart-contracts

https://github.com/friedger/clarity-smart-contracts/blob/master/contracts/sips/nft-trait.clar

## Deployed Contracts

- mainnet: [SP2PABAF9FTAJYNFZH93XENAJ8FVY99RRM50D2JG9.nft-trait.nft-trait](https://explorer.stacks.co/txid/SP2PABAF9FTAJYNFZH93XENAJ8FVY99RRM50D2JG9.nft-trait?chain=mainnet)
- testnet: [ST1NXBK3K5YYMD6FD41MVNP3JS1GABZ8TRVX023PT.nft-trait.nft-trait](https://explorer.stacks.co/txid/ST1NXBK3K5YYMD6FD41MVNP3JS1GABZ8TRVX023PT.nft-trait?chain=testnet)



================================================
FILE: sips/sip-010/sip-010-fungible-token-standard.md
================================================
# Preamble

SIP Number: 010

Title: Standard Trait Definition for Fungible Tokens

Author: Hank Stoever <hstove@gmail.com>, Pascal Belloncle <psq@nanorails.com>

Consideration: Technical

Type: Standard

Status: Ratified

Created: 25 January 2021

License: CC0-1.0

Sign-off: Jude Nelson <jude@stacks.org>, Technical Steering Committee Chair

Layer: Traits

Discussions-To: https://github.com/stacksgov/sips

# Abstract

Fungible tokens are digital assets that can be sent, received, combined, and divided. Most forms of cryptocurrencies are fungible tokens. They have become a building block of almost all blockchains. This SIP aims to provide a flexible and easy-to-implement standard that can be used by developers on the Stacks blockchain when creating their own tokens.

# License and Copyright

This SIP is made available under the terms of the Creative Commons CC0 1.0 Universal license, available at https://creativecommons.org/publicdomain/zero/1.0/
This SIP’s copyright is held by the Stacks Open Internet Foundation.

# Introduction

Digital assets can have the property to be fungible. A _fungible_ token can be broken down into small units and added together. An owner of a fungible asset only needs to care about their balance, that is, the total amount of a particular fungible asset that they own. Most well-known currencies are fungible. For fungible tokens, there is no difference between any two different amounts of the fungible token.

For example, if a user owns 10 units of a fungible asset, they may send 2 units to a different user. At this point, their balance is 8 units. If they later receive more units, their total balance will be updated.

On blockchains, fungible tokens are a core component. Blockchains with smart contracts, including the Stacks blockchain, allow developers and users to create and interact with smart contracts that use fungible tokens.

The Stacks blockchain has a native fungible token: the Stacks token (STX). In addition to the native STX token, the Stacks blockchain's programming language for developing smart contracts, Clarity, has built-in language primitives to define and use fungible tokens. Although those primitives exists, there is value in defining a common interface (known in Clarity as a "trait") that allows different smart contracts to interoperate with fungible token contracts in a reusable way. This SIP defines that trait.

# Specification

The fungible token trait, `sip-010-trait`, has 7 functions:

## Trait functions

### Transfer

`(transfer ((amount uint) (sender principal) (recipient principal) (memo (optional (buff 34)))) (response bool uint))`

Transfer the fungible token from the sender of this transaction to the recipient. The `amount` is an unsigned integer. It is recommended that implementing contracts use the built-in `ft-transfer?` Clarity method. If the sender does not have enough tokens to complete the transaction, the transaction should abort and return an `(err uint)`.

This method must be defined with `define-public`, as it alters state, and should be externally callable.

Contract implementers should take note to perform authorization of the `transfer` method. For example, a fungible token contract that wants to make sure that only the transaction's sender is able to move the requested tokens might first check that the sender argument is equal to tx-sender.

When returning an error in this function, the error codes should follow the same patterns as the built-in `ft-transfer?` and `stx-transfer?` functions.

| error code | reason                                          |
| ---------- | ----------------------------------------------- |
| u1         | `sender` does not have enough balance           |
| u2         | `sender` and `recipient` are the same principal |
| u3         | `amount` is non-positive                        |
| u4         | `sender` is not the same as `tx-sender`         |

Contract implementers should take note that in Stacks 2.0, the memo field won't be included in the event emitted by successful `ft-transfer?` operations. As a consequence, the implementer has to make sure that the memo is emitted by adding a `print` statement if the `ft-transfer?` is successful and the memo is not `none`. The memo should be upwrapped and emitted after the `ft-transfer?` operation.

Example:

```
  ...
  (try! (ft-transfer? token amount sender recipient))
  (match memo to-print (print to-print) 0x)
  ...
```

### Name

`(get-name () (response (string-ascii 32) uint))`

Return a human-readable name for the contract, such as "CoolPoints", etc.

This method should be defined as read-only, i.e. `define-read-only`.

### Symbol

`(get-symbol () (response (string-ascii 32) uint))`

Return a symbol that allows for a shorter representation of a token. This is sometimes referred to as a "ticker". Examples: "STX", "COOL", etc. Typically, a token could be referred to as $SYMBOL when referencing it in writing.

This method should be defined as read-only, i.e. `define-read-only`.

### Decimals

`(get-decimals () (response uint uint))`

The number of decimal places in a token. All fungible token balances must be represented as integers, but providing the number of decimals provides for an abstraction of a token that humans are more familiar dealing with. For example, the US Dollar has 2 decimals, if the base unit is "cents", as is typically done in accounting. Stacks has 6 decimals, Bitcoin has 8 decimals, and so on.

As another example, if a token has 4 decimals, and the `get-balance` method a particular user returns `100345000`, wallets and exchanges would likely represent that value as `10034.5`.

This method should be defined as read-only, i.e. `define-read-only`.

### Balance of

`(get-balance (principal) (response uint uint))`

Return the balance of a particular principal (also known as "address" or "account"). Implementations should typically use the built-in Clarity method `ft-get-balance`.

This method should be defined as read-only, i.e. `define-read-only`.

### Total supply

`(get-total-supply () (response uint uint))`

Return the total supply of this token. Implementations should typically use the built-in Clarity method `ft-get-supply`.

This method should be defined as read-only, i.e. `define-read-only`.

### Token URI

`(get-token-uri () (response (optional (string-utf8 256)) uint))`

Returns an optional string that is a valid URI which resolves to this token's metadata. This allows your token to provide off-chain metadata about the contract, such as a description and an image icon.

The JSON schema for this metadata is as follows:

```json
{
  "title": "Asset Metadata",
  "type": "object",
  "properties": {
    "name": {
      "type": "string",
      "description": "Identifies the asset to which this token represents"
    },
    "description": {
      "type": "string",
      "description": "Describes the asset to which this token represents"
    },
    "image": {
      "type": "string",
      "description": "A URI pointing to a resource with mime type image/* representing the asset to which this token represents. Consider making any images at a width between 320 and 1080 pixels and aspect ratio between 1.91:1 and 4:5 inclusive."
    }
  }
}
```

Clients that fetch this data should prefer any on-chain data, such as the name of the token, over metadata provided in `get-token-uri`.

## Trait implementation

An implementation of the proposed trait is provided below.

```clarity
(define-trait sip-010-trait
  (
    ;; Transfer from the caller to a new principal
    (transfer (uint principal principal (optional (buff 34))) (response bool uint))

    ;; the human readable name of the token
    (get-name () (response (string-ascii 32) uint))

    ;; the ticker symbol, or empty if none
    (get-symbol () (response (string-ascii 32) uint))

    ;; the number of decimals used, e.g. 6 would mean 1_000_000 represents 1 token
    (get-decimals () (response uint uint))

    ;; the balance of the passed principal
    (get-balance (principal) (response uint uint))

    ;; the current total supply (which does not need to be a constant)
    (get-total-supply () (response uint uint))

    ;; an optional URI that represents metadata of this token
    (get-token-uri () (response (optional (string-utf8 256)) uint))
  )
)
```

## Implementing in wallets and other applications

Developers who wish to interact with a fungible token contract should first be provided, or keep track of, various different fungible token implementations. When validating a fungible token contract, they should fetch the interface and/or source code for that contract. If the contract implements the trait, then the wallet can use this standard's contract interface for making transfers and getting balances.

Downstream consumers of contracts that implement this trait should be aware that the `get-name` and `get-symbol` function are not guaranteed to be globally unique. Because of this, consumers should be advised that `get-name` and `get-token` are only hints to provide a more human-readable experience. Care should always be taken to verify that a contract's identifier matches that of the token a client is intending to interact with.

All of the functions in this trait return the `response` type, which is a requirement of trait definitions in Clarity. However, some of these functions should be "fail-proof", in the sense that they should never return an error. These "fail-proof" functions are those that have been recommended as read-only. If a contract that implements this trait returns an error for these functions, it may be an indication of a faulty contract, and consumers of those contracts should proceed with caution.

## Use of native asset functions

Although it is not possible to mandate in a Clarity trait, contract implementers should always use the built-in native assets that are provided as Clarity primitives. This allows clients to use Post Conditions (explained below), and takes advantages of other benefits, like native support for these asset balances and transfers through `stacks-blockchain-api`. The reference implementations included in this SIP use the native asset primitives, and provide a good boilerplate for their usage.

The native asset primitives include:

- `define-fungible-token`
- `ft-burn?`
- `ft-get-balance`
- `ft-get-supply`
- `ft-mint?`
- `ft-transfer?`

## Use of post conditions

In addition to built-in methods for fungible token contracts, the Stacks blockchain includes a feature known as Post Conditions. By defining post conditions, users can create transactions that include pre-defined guarantees about what might happen in that contract.

One such post condition could be "I will transfer exactly 100 of X token", where "X token" is referenced as a specific contract's fungible token. When wallets and applications implement the `transfer` method, they should _always_ use post conditions to specify that the user will transfer exactly the amount of tokens that they specify in the `amount` argument of the `transfer` function. Only in very specific circumstances should such a post condition not be included.

# Related work

## Ethereum ERC20

[Ethereum ERC20 standard](https://ethereum.org/en/developers/docs/standards/tokens/erc-20/)

Perhaps the oldest, and most well known, standard for fungible tokens is Ethereum's [ERC20](https://ethereum.org/en/developers/docs/standards/tokens/erc-20/) standard. It has become one of the strongest building blocks for the Ethereum ecosystem. When all fungible tokens follow the same standard, any wallet or application developer can interact with it without having to create custom logic for handling each individual token.

Fungible tokens have become so popular that the Clarity smart contracting language has support for basic fungible token operations built-in. In fact, as can be seen in this proposal's reference implementation, very little code is required to implement a fungible token. The important part of this standard is defining a Clarity trait that all fungible tokens can implement. Even though Clarity has fungible token operations built-in, it is important for each contract to define the same methods so that their contracts are easy to integrate.

# Backwards Compatibility

Not applicable

# Activation

This trait has been deployed to mainnet: [SP3FBR2AGK5H9QBDH3EEN6DF8EK8JY7RX8QJ5SVTE.sip-010-trait-ft-standard](https://explorer.stacks.co/txid/0x99e01721e57adc2c24f7d371b9d302d581dba1d27250c7e25ea5f241af14c387?chain=mainnet)

This trait will be considered activated when this trait is deployed to mainnet, and 3 different implementations of the trait have been deployed to mainnet, no later than Bitcoin block 700000.

# Reference Implementations

An example implementation has been submitted with this proposal, along with a Javascript client and tests. https://github.com/hstove/stacks-fungible-token

Other examples of Clarity contracts that implement fungible tokens, although not exactly according to this specification:

- [@psq's trait and implementation](https://github.com/psq/flexr/blob/master/contracts/src20-trait.clar)
- [@friedger's fungible token implementation](https://github.com/friedger/clarity-smart-contracts/blob/master/contracts/tokens/fungible-token.clar)

## Deployed Contracts

- mainnet: [SP3FBR2AGK5H9QBDH3EEN6DF8EK8JY7RX8QJ5SVTE.sip-010-trait-ft-standard.sip-010-trait](https://explorer.stacks.co/txid/SP3FBR2AGK5H9QBDH3EEN6DF8EK8JY7RX8QJ5SVTE.sip-010-trait-ft-standard?chain=mainnet)
- testnet: [ST1NXBK3K5YYMD6FD41MVNP3JS1GABZ8TRVX023PT.sip-010-trait-ft-standard.sip-010-trait](https://explorer.stacks.co/txid/ST1NXBK3K5YYMD6FD41MVNP3JS1GABZ8TRVX023PT.sip-010-trait-ft-standard?chain=testnet)



================================================
FILE: sips/sip-012/sip-012-cost-limits-network-upgrade.md
================================================
# Preamble

SIP Number: 012

Title: Burn Height Selection for a Network Upgrade to Introduce New Cost-Limits

Authors:
* Asteria <asteria@syvita.org>
* Aaron Blankstein <aaron@hiro.so>
* Diwaker Gupta <diwaker@hiro.so>
* Hank Stoever <hank@stackerlabs.co>
* Jason Lau <jason@okcoin.com>
* Jude Nelson <jude@stacks.org>
* Ludovic Galabru <ludo@hiro.so>
* Trevor Owens <trevor@stacks.ac>
* Xan Ditkoff <xan@daemontechnologies.co>
* Pavitthra Pandurangan <pavitthra@hiro.so>
* Reed Rosenbluth <reed@hiro.so>

Consideration: Governance, Technical

Type: Consensus

Status: Ratified

Created: 2021-10-08

License: BSD 2-Clause

Sign-off: Harold Davis (governance) <recursive3@gmail.com>, Juliet Oberding
(governance) <juliet.oberding@gmail.com>, Jason Schrader (governance) <jason@joinfreehold.com>,
Jude Nelson (technical) <jude@stacks.org>

Discussions-To: https://github.com/stacksgov/sips

# Abstract

The Stacks 2.0 blockchain artificially constrains block goodput in two
consensus-critical ways: it assesses storage costs for lists based on their
maximum length instead of actual length, and it constrains the number of indexed
I/O operations well below what the reference implementation is capable of
handling.  Changing either of these is breaking change, which requires a
network-wide upgrade.

This SIP proposes executing a breaking change to not only
address these two constraints, but also to update all Clarity cost functions to
more accurately reflect their true performance.  The breaking change is carried
out via a network-wide vote by Stackers on the Bitcoin blockchain, which will
both serve to activate this SIP and to effectively bypass the cost voting procedure
in SIP-006.

The upgraded blockchain will be called Stacks 2.05.

# License and Copyright

This SIP is made available under the terms of the Creative Commons CC0 1.0
Universal license, available at
https://creativecommons.org/publicdomain/zero/1.0/ This SIP's copyright is held
by the Stacks Open Internet Foundation.

# Introduction

The current block limits were set very conservatively in Stacks 2.0, but
since the mainnet launch on 2021-01-14, traffic on the network has grown
steadily.  In recent months, we have seen network congestion adversely
impacting the user experience: valid transactions are not
getting mined in a timely manner because there is far more demand for block compute
capacity than supply.  For example, in Stacks blocks from height 27,672 through 28,573, 675
blocks' highest-filled compute dimension was their `runtime` dimension, but 319
blocks' highest-filled compute dimension was their `read_count` dimension ([full
report](./SIP-012-001.ods)).  In another study of 455 Stacks blocks between height
30,904 and 33,002, just over 14% of them exceeded the `read_count` dimension
and just over 85% exceeded the `runtime` dimension ([full report](https://github.com/blockstack/stacks-blockchain/discussions/2883)).

While there will likely always be more demand than supply for block compute
capacity, the current supply is artifically limited in three principal ways:

* At the time of the launch, the MARF index (see SIP-004) was implemented in
  such a way that a block could only execute 7,500 MARF index reads and writes
while being processed by a non-mining node on consumer hardware in a reasonable
amount of time.  This number was arrived at by measuring how many MARF reads and writes
could be completed on a consumer laptop in 10 seconds in 2019.  But because the block limit is a
consensus-critical constant that all Stacks nodes must agree on, increasing the
number of MARF reads and writes per block can only be done via a breaking
change.  This means that any improvements to the MARF's performance that could
permit significant increase in the number of operations per block can only
be capitalized upon via a breaking change.

* An emerging Clarity contract design pattern is to store data maps and data
  variables comprised of lists with a large maximum length.  The reason
for this, we suspect, is because it permits storing a lot of MARF-indexed data with
few MARF reads and writes.  However, the Clarity VM assesses list storage based
on its _maximum_ length, not the length of the data stored.  Assessing storage
based on the length of the data would allow contracts to make better use of the
`read_length` and `write_length` compute resources (which have been hit in
practice), but this would require a breaking change.

* Most of the cost functions in SIP-006 have constants that are far too
  conservative in practice.  The numbers used when mainnet launched were chosen
to minimize the risk of a network-wide denial-of-service arising from producing
blocks that would take an inordinate amount of time to validate; they were not
chosen through a rigorous benchmarking process.  In the months since then,
we have developed a more rigorous 
[benchmark suite](https://github.com/blockstack/clarity-benchmarking)
for the Clarity VM implementation, and have arrived at more accurate runtime
constants for the cost functions that permit suitable block validation times on contemporary
hardware.  The new limits, listed in [Appendix A](#appendix-a), 
would vastly increase the number of Clarity functions that can be
executed per block.  But in order to capitalize on this new data, STX token holders would
need to execute the SIP-006 cost voting protocol to activate new cost functions.

This SIP proposes a **breaking change** that would address these first two
limitations.  It would increase the block runtime `read_count` and `write_count`
limits by a factor of 2, in order to allow the network to capitalize on a [recent MARF performance
improvement](https://github.com/blockstack/stacks-blockchain/issues/2869).  It
would also change storage cost assessment for list data to consider the length
of the value being stored, instead of its maximum length.  In addition, this 
would bypass the voting protocol in SIP-006 to set 
[new proposed runtime cost functions parameters](https://forum.stacks.org/t/more-accurate-cost-functions-for-clarity-native-functions/12386)
via a voting protocol described in this SIP.

## A Note on Bypassing SIP-006

This SIP explicitly bypasses the voting procedure in SIP-006 by means of a separate
voting procedure described below.  However, this SIP does not supersede SIP-006,
nor does it set a precedent for this particular voting procedure's general
applicability to making collective decisions in the SIP process.  The voting
procedure in this SIP is specific to this SIP, and is only meant to activate the
changes described in this SIP.

The reason for this accommodation is that the SIP-006 voting procedure may be
too costly to use in practice, since STX holders must forego Stacking to use it.
A future SIP may study this problem further, and propose a new voting procedure 
for runtime costs in recognition of this.  However, that is not the subject of
this SIP.

# Specification

## Activation Protocol

In the text below, "Stacks 2.05" refers to the proposed network-upgrade for
cost-limits.

Due to the far-reaching effects a breaking change will have on the Stacks
ecosystem, this SIP can only be activated through a collective decision-making
process.  There are three major steps to this activation procedure:

   1.  The SIP authors will propose a Bitcoin block number at which the new cost-limits
   take effect. The block number should be at least two calendar weeks from when
   this SIP transitions into _Recommended_ status, so as to provide sufficient time for
   node operators to upgrade. Tentatively this block number would be chosen to fall
   on November 29th or November 30th, 2021.  In this document, this is the
**activation block**.

   On November 15, 2021, the SIP authors finalized the choice of Bitcoin block
713,000 to be the activation block.  This block is expected to be mined at or
around December 6, 2021.  The reason for this extra week delay over the
tentative block number is to ensure that the network upgrade happens in the
_middle_ of a reward cycle.  November 29th/30th is expected to be the start of
reward cycle 21. Executing a network upgrade at the start of a reward cycle is
needlessly risky, because if the upgrade fails for some reason during the
prepare phase, it could cause PoX rewards to be disabled for cycle 21.

   2.  In the two whole reward cycles prior to the activation block, users who
       have Stacked STX will have the opportunity to cast a vote to activate
this SIP.  The cut-off for voting will be a _separate_ Bitcoin block whose
expected arrival time is one calendar week prior to the activation block.  This
document refers to this block as the **vote deadline block.**

   On November 15, 2021, the SIP authors finalized the decision to select the
first Bitcoin block height mined after November 23, 2021 at 12:00 EST to be the
vote deadline block.  This was Bitcoin block 710,001.

   3.  If the activation voting threshold is met as of the vote deadline block,
then the Stacks Foundation will make a release of the Stacks blockchain
reference implementation with this
SIP's changes applied and set to take effect once the activation block passes.
If on the other hand there is insufficient support for this SIP by the vote
deadline block, then no action will be taken and this SIP will not activate.
   
   On November 23, 2021, the SIP authors inspected the Bitcoin and Stacks chainstate
using [vote-tallying scripts](./scripts) and determined that the the voting threshold has been met.
At least 129,615,879 stacked STX had voted in favor of this SIP, and 0 against.

To activate this SIP, users who have Stacked STX in either of the last two whole
reward cycles prior to the vote deadline block height will have the opportunity to
vote with their STX by sending a minimial amount of BTC to one of two addresses.
There will be two Bitcoin addresses whose UTXOs will be used to tally the
vote: a "yes" address, and a "no" address.

* The "yes" address will be a p2pkh Bitcoin address whose inner Hash160 is
  `00000000000000000000000000000000000000ee`.  On mainnet, this is address
`111111111111111111112czxoHN`.

* The "no" address will be a separate p2pkh Bitcoin address whose inner Hash160
  is `00000000000000000000000000000000000000ff`.  On mainnet, this is address
`111111111111111111112kmzDG2`.

Note that these are similar addresses to the PoX burn address, but they all
differ from one another in their checksums.

Vote tallying is performed by examining how many STX the Bitcoin transaction
sender has most-recently Stacked.  By examining the UTXOs for these two Bitcoin
addresses, anyone with a full copy of the Stacks chain state as of the voting
deadline will be able to calculate how many recently-Stacked STX have signaled
"yes" or "no" support for this SIP.

To match the Bitcoin transaction to the Stacker's state in the `.pox` contract,
the `scriptSig` of the first transaction input must be signed by either the user's PoX reward
address's public key(s), or the public key(s) of the standard principal Stacks address that Stacked
the tokens (the option is provided here because not all Stackers have access to their PoX
addresses).  In either case, the vote commits the Stacker's
most-recently-locked STX to "yes" or "no" if the Stacker had some STX locked
in the past two reward cycles as of the vote deadline block.

For Stackers that vote with their Stacks address key(s), the STX that the
associated standard principal had locked up will be committed to the vote.

For Stackers that vote with their PoX address key(s), the STX for _all_
associated Stacks principals that use this PoX address will be committed to the
vote (note that multiple Stacks principals may use the same PoX address).

For Stackers that have delegated STX to a Stacking pool, the pool operator must
perform the vote on their behalf.  As with a normal Stacker, the pool operator may 
sign the Bitcoin transaction with either the PoX reward address key(s) or the
standard Stacks principal address key(s).

For Stackers that have Stacked via a smart contract, only the PoX reward
address key(s) may be used to vote.

Stackers can send as many Bitcoin transactions as they like, but their STX will
only be counted once.  Only the *first* such voting transaction will be
considered to determine how the STX voted.

If a Stacker votes using both their STX address and PoX address, then the PoX
address will be used to count their STX.  A subsequent vote with the STX address
will be ignored as a duplicate vote.  In particular, the PoX address will
count *all* STX it represents.  For example, if Alice Stacks 100,000 STX with two STX
addresses that share the same PoX address, and she votes with her PoX address,
then the vote will count for 200,000 STX, and she will be unable to vote
separately with her STX addresses.  If instead she votes with only one
of her STX addresses, then that vote counts for 100,000 STX.

If a Stacker votes for both "yes" and "no," their vote will not be counted at
all.  This provides a way for a Stacker to cancel their vote, but they will be
unable to change it.

### Activation Criteria 

The SIP will be considered _Ratified_ if the vote to activate Stacks 2.05
passes. This requires:

* 2/3 of all votes passed are "yes", weighted by the STX they represent, at a
  Bitcoin block height at or before the vote deadline block.

* At least 60 million STX are represented by the "yes" votes. This is 2x the
  largest Stacker at the time of this writing.

### Rationale 

The rationale for this voting procedure is that it simultaneously gives the
community a way to veto the SIP while also accommodating low turnout. The
problem with blockchain-based voting systems in the past is that unless
there is a financial incentive to vote (e.g. mining, staking), turnout is low.
For example, the Ethereum carbon vote [1] to disable the DAO smart contract had only
5.5% turnout [2].  As another example, BitShares' [3] highest-voted delegate in its
delegated proof-of-stake consensus algorithm only received 18% of the vote [4].

This SIP's activation procedure takes the position that non-voters are passive
system participants and do not care about the outcome of this SIP -- they will
be happy either way.  But, this SIP also acknowledges that of the voters that
_do_ care about the vote outcome, those who vote "no" are financially
disincentivized to do so, because it would render the Stacks blockchain in a
worse-off state.  Therefore, this SIP requires a supermajority of "yes" votes to
activate, since a strong minority of "no" votes would be a strong signal that
something is seriously wrong with this SIP (despite its apparent benefits).

## Changes to Mining

Nodes that run Stacks 2.05 must put `0x05` in the memo field. Block-commit
transactions that do not have a value that is _at least_ `0x05` will be considered invalid.

The purpose of this change is to ensure that in the unlikely event some miners didn't know
about this SIP, they will quickly find out because their blocks will never be
confirmed or recognized by other users and exchanges that have upgraded.
Moreover, the "at least" condition is meant for future compatibility: if there
is ever another SIP that requires miners to signal support for the SIP's
activation via the memo field, then they can do so by putting in a _higher_
value while still remaining able to mine under the current rules.

## Changes to Runtime Costs

This SIP proposes two breaking changes to runtime costs, as well as a new set of
default cost functions (bypassing SIP-006's voting procedure).

### Block Limit

This SIP proposes increasing the block limits
for MARF reads and writes.  This is a breaking change.

Based on the expected performance improvements in the
implementation of the MARF (see [issue #2869](https://github.com/blockstack/stacks-blockchain/issues/2869)) 
this SIP proposes doubling the current limits on blocks:

```rust
pub const BLOCK_LIMIT_MAINNET: ExecutionCost = ExecutionCost {
    write_length: 15_000_000, // roughly 15 mb
    write_count: 15_000,
    read_length: 100_000_000,
    read_count: 15_000,
    runtime: 5_000_000_000,
};
```

### Changes to Static vs. Dynamic Tabulation of Costs

The cost assessment in Clarity for most data-handling functions (e.g.,
`map-get?`) use the static cost of the fetch rather than the dynamic cost. 
This is a breaking change.  For more information, see [issue #2864](https://github.com/blockstack/stacks-blockchain/issues/2864) in the
`stacks-blockchain` repository.

There are two motivating reasons for doing this:

* It makes static analysis of costs easier, because the cost assessed at runtime
  would always use the declared size of the map entry.
* It allows the cost to be assessed before running the operation.

However, these reasons have not been shown to be practical in production.
For (1), static analysis is always going to overestimate anyways, so system
throughput would improve by using the actual runtime overhead instead of the
maximum runtime overhead when assessing storage costs.  For (2),
allowing a single "speculative" evaluation before aborting a block due to cost
overflow is not particularly burdensome to the network: the maximum size of an
overread is a single Clarity value, which takes only 2MB.

The benefit of using dynamic costs, however, could be significant. Many contracts use
patterns where potentially long lists are stored in data maps, but in practice
the stored lists are relatively short.

Because of this, this SIP proposes using a dynamic cost for these assessments.
Specifically, it proposes changes to the inputs of the following
functions' cost functions:

* `var-get`
* `var-set`
* `map-get?`
* `map-set`
* `map-insert`
* `map-delete`
* `concat`
* `nft-mint?`
* `nft-burn?`
* `nft-transfer?`
* `nft-get-owner?`

#### `(var-get var-name) -> value`

The `x` input to the `var-get` cost function should be the length in
bytes of the consensus serialization (see [SIP-005](https://github.com/stacksgov/sips/blob/main/sips/sip-005/sip-005-blocks-and-transactions.md#clarity-value-representation)
for details on this format) of the returned `value`.

#### `(var-set var-name value)`

The `x` input to the `var-get` cost function should be the length in
bytes of the consensus serialization (see [SIP-005](https://github.com/stacksgov/sips/blob/main/sips/sip-005/sip-005-blocks-and-transactions.md#clarity-value-representation)
for details on this format) of the newly stored `value`.

The memory usage of this function should be this same value. The
memory usage of `var-set` remains in effect until the end of the
transaction (data operations remain in memory during the whole
transaction to enable rollbacks and post-conditions).

#### `(map-get? map-name key) -> value`

The `x` input to the `map-get` cost function should be the sum of the
length in bytes of the consensus serialization of the supplied `key`
and the returned `value`.

#### `(map-set map-name key value)`

The `x` input to the `map-set` cost function should be the sum of the
length in bytes of the consensus serialization of the supplied `key` and
`value` arguments.

The memory usage of this function should be this same value. The
memory usage of `map-set` remains in effect until the end of the
transaction (data operations remain in memory during the whole
transaction to enable rollbacks and post-conditions).

#### `(map-insert map-name key value)`

If the insert is successful, the `x` input to the `map-insert` cost
function should be the sum of the length in bytes of the consensus
serialization of the supplied `key` and `value` arguments.

If the insert is unsuccessful, the `x` input to the `map-insert` cost
function should be the length in bytes of the consensus serialization
of just the supplied `key` argument.

The memory usage of this function should be this same `x` value. The
memory usage of `map-insert` remains in effect until the end of the
transaction (data operations remain in memory during the whole
transaction to enable rollbacks and post-conditions).

#### `(map-delete map-name key)`

The `x` input to the `map-delete` cost function should be the length
in bytes of the consensus serialization of the supplied `key`
argument plus the length in bytes of the consensus serialization of
a `none` Clarity value.

The memory usage of this function should be this same `x` value. The
memory usage of `map-delete` remains in effect until the end of the
transaction (data operations remain in memory during the whole
transaction to enable rollbacks and post-conditions).

#### `(concat list-a list-b)`

The `x` input to the `concat` cost function should be the length of
`list-a` plus the length of `list-b`.

#### `(nft-mint? asset-class asset-identifier recipient)`

The `x` input to the `nft-mint?` cost function should be the length in bytes of
the consensus serialization of the supplied `asset-identifier`.

The memory usage of this function should be this new `x` value, plus the size of
a `principal` type.  The memory
usage of `nft-mint?` remains in effect until the end of the transaction (asset
operations remain in memory during the whole transaction to enable rollbacks and
post-conditions).

#### `(nft-burn? asset-class asset-identifier owner)`

The `x` input to the `nft-burn?` cost function should be the length in bytes of
the consensus serialization of the specified `asset-identifier`.

The memory usage of this function should be this new `x` value, plus the size of
a `principal` type.  The memory
usage of `nft-burn?` remains in effect until the end of the transaction (asset
operations remain in memory during the whole transaction to enable rollbacks and
post-conditions).

#### `(nft-transfer? asset-class asset-identifier sender recipient)`

The `x` input to the `nft-transfer?` cost function should be the length in bytes
of the consensus serialization of the specified `asset-identifier`.

The memory usage of this function should be this new `x` value, plus the size of
a `principal` type.  The memory
usage of `nft-transfer?` remains in effect until the end of the transaction (asset
operations remain in memory during the whole transaction to enable rollbacks and
post-conditions).

#### `(nft-get-owner? asset-class asset-identifier)`

The `x` input to the `nft-get-owner?` cost function should be the length in
bytes of the consensus serialization of the specified `asset-identifier`.

### New Default Cost Functions

Based on results from the
[clarity-benchmarking](https://github.com/blockstack/clarity-benchmarking)
project, this SIP proposes new default cost functions. The new costs are supplied in
the form of a new Clarity smart contract in [Appendix A](#appendix-a).

This could have been carried out through a SIP-006 cost voting procedure, but
due to the opportunity costs incurred by STX holders foregoing PoX rewards to
carry this vote out, this SIP instead proposes bypassing the SIP-006 voting
procedure in this one instance and instead using this SIP's activation procedure
to install these new functions.

# Related Work 

On-chain voting for upgrades is not a new concept.  Bitcoin has famously
executed many soft-forks using time-based activation [5], miner voting
thresholds [6], and a combination of both [7].  The voting approach in this SIP
uses both a timeout and a voting threshold to activate, but differs from
Bitcoin's approach in that it empowers Stackers as the instigators of the
upgrade.

We are aware of one other proposal
(distinct from the procedure described in SIP-006) suggested
using a voting contract to determine the block height at which a
network-upgrade, described in detail in [this Github
discussion](https://github.com/blockstack/stacks-blockchain/discussions/2845).
This SIP differs from this proposal in that the burnchain is used to identify
Stackers.

# Backwards Compatibility

This SIP proposes a breaking change.  If this SIP activates, then old miners'
block-commits will no longer be considered valid.  In addition, old nodes will
not accept new blocks as valid if they exceed the Stacks 2.0 block cost limits.
Therefore, all node operators are encouraged to upgrade immediately once SIP 012
transitions to _Activation-in-Progress_ status.

# Activation

The SIP will be considered _Ratified_ once all of the following are true:

* The cost functions in Appendix A are finalized.  This is a precondition for
  advancing the SIP to _Activation-in-Progress_ status.

* A vote deadline block height and activation block height are chosen and added
  to this SIP's text.  This is a pre-condition for advancing this SIP to
_Activation-in-Progress_ status.

* This SIP is advanced to _Activation-in-Progress_ by the respective consideration
  advisory boards.

* The SIP has garnered sufficient support by the vote deadline block height. Voting by
  sending Bitcoin transactions can begin once the SIP text is updated with the
  "yes" / "no" addresses. Voting concludes at least one week prior to the Stacks 2.05
  activation block.

* A new release of Stacks blockchain (available at
  https://github.com/blockstack/stacks-blockchain/releases) contains the updated
  cost-limits and a mechanism to use the new cost-limits beyond the activation
block height listed in this SIP.  This release is announced by the Stacks
Foundation.

* The activation block height passes on the Bitcoin chain.

## Activation Status

* On November 15, 2021, the authors finalized the choice of the activation
  block to be Bitcoin block 713,000.  This block is expected to be mined at or
around December 6, 2021 at 23:00 UTC.

* The vote deadline block will be backdated to the first Bitcoin block mined
  after November 23, 2021 at 12:00 EST.  The exact block number will be added to
this SIP's text once it is known.

# Reference Implementation

The reference implementation of this SIP is developed in the `next-costs` branch
of the reference implementation of the Stacks blockchain, available at
https://github.com/blockstack/stacks-blockchain.

# References

[1] http://v1.carbonvote.com/

[2] https://en.wikipedia.org/wiki/Ethereum_Classic#Carbon_vote

[3] https://en.bitcoinwiki.org/wiki/BitShares

[4] https://bitcointalk.org/index.php?topic=916696.330;imode

[5] https://github.com/bitcoin/bips/blob/master/bip-0016.mediawiki

[6] https://github.com/bitcoin/bips/blob/master/bip-0034.mediawiki

[7] https://github.com/bitcoin/bips/blob/master/bip-0009.mediawiki

# Appendices

## Appendix A

The new proposed cost functions, which will be instantiated at
`SP000000000000000000002Q6VF78.costs-2.05.clar`:

```lisp
;; the .costs-2 contract

;; Helper Functions

;; Return a Cost Specification with just a runtime cost
(define-private (runtime (r uint))
    {
        runtime: r,
        write_length: u0,
        write_count: u0,
        read_count: u0,
        read_length: u0,
    })

;; Linear cost-assessment function
(define-private (linear (n uint) (a uint) (b uint))
    (+ (* a n) b))

;; LogN cost-assessment function
(define-private (logn (n uint) (a uint) (b uint))
    (+ (* a (log2 n)) b))

;; NLogN cost-assessment function
(define-private (nlogn (n uint) (a uint) (b uint))
    (+ (* a (* n (log2 n))) b))


;; Cost Functions
(define-read-only (cost_analysis_type_annotate (n uint))
    (runtime (linear n u1 u9)))

(define-read-only (cost_analysis_type_check (n uint))
    (runtime (linear n u113 u1)))

(define-read-only (cost_analysis_type_lookup (n uint))
    (runtime (linear n u1 u6)))

(define-read-only (cost_analysis_visit (n uint))
    (runtime u1))

(define-read-only (cost_analysis_iterable_func (n uint))
    (runtime (linear n u2 u14)))

(define-read-only (cost_analysis_option_cons (n uint))
    (runtime u6))

(define-read-only (cost_analysis_option_check (n uint))
    (runtime u3))

(define-read-only (cost_analysis_bind_name (n uint))
    (runtime (linear n u2 u176)))

(define-read-only (cost_analysis_list_items_check (n uint))
    (runtime (linear n u2 u4)))

(define-read-only (cost_analysis_check_tuple_get (n uint))
    (runtime (logn n u1 u2)))

(define-read-only (cost_analysis_check_tuple_merge (n uint))
    (runtime (linear n u1000 u1000)))

(define-read-only (cost_analysis_check_tuple_cons (n uint))
    (runtime (nlogn n u3 u5)))

(define-read-only (cost_analysis_tuple_items_check (n uint))
    (runtime (linear n u1 u59)))

(define-read-only (cost_analysis_check_let (n uint))
    (runtime (linear n u1 u12)))

(define-read-only (cost_analysis_lookup_function (n uint))
    (runtime u20))

(define-read-only (cost_analysis_lookup_function_types (n uint))
    (runtime (linear n u1 u28)))

(define-read-only (cost_analysis_lookup_variable_const (n uint))
    (runtime u15))

(define-read-only (cost_analysis_lookup_variable_depth (n uint))
    (runtime (nlogn n u1 u34)))

(define-read-only (cost_ast_parse (n uint))
    (runtime (linear n u172 u287441)))

(define-read-only (cost_ast_cycle_detection (n uint))
    (runtime (linear n u141 u72)))

(define-read-only (cost_analysis_storage (n uint))
    {
        runtime: (linear n u2 u100),
        write_length: (linear n u1 u1),
        write_count: u1,
        read_count: u1,
        read_length: u1
    })

(define-read-only (cost_analysis_use_trait_entry (n uint))
    {
        runtime: (linear n u9 u723),
        write_length: (linear n u1 u1),
        write_count: u0,
        read_count: u1,
        read_length: (linear n u1 u1)
    })


(define-read-only (cost_analysis_get_function_entry (n uint))
    {
        runtime: (linear n u81 u1303),
        write_length: u0,
        write_count: u0,
        read_count: u1,
        read_length: (linear n u1 u1)
    })


(define-read-only (cost_analysis_fetch_contract_entry (n uint))
    {
        runtime: (linear n u1000 u1000),
        write_length: u0,
        write_count: u0,
        read_count: u1,
        read_length: (linear n u1 u1)
    })

(define-read-only (cost_lookup_variable_depth (n uint))
    (runtime (linear n u2 u14)))

(define-read-only (cost_lookup_variable_size (n uint))
    (runtime (linear n u2 u1)))

(define-read-only (cost_lookup_function (n uint))
    (runtime u16))

(define-read-only (cost_bind_name (n uint))
    (runtime u256))

(define-read-only (cost_inner_type_check_cost (n uint))
    (runtime (linear n u2 u9)))

(define-read-only (cost_user_function_application (n uint))
    (runtime (linear n u26 u140)))

(define-read-only (cost_let (n uint))
    (runtime (linear n u146 u862)))

(define-read-only (cost_if (n uint))
    (runtime u200))

(define-read-only (cost_asserts (n uint))
    (runtime u170))

(define-read-only (cost_map (n uint))
    (runtime (linear n u1210 u3314)))

(define-read-only (cost_filter (n uint))
    (runtime u460))

(define-read-only (cost_len (n uint))
    (runtime u486))

(define-read-only (cost_element_at (n uint))
    (runtime u619))

(define-read-only (cost_index_of (n uint))
    (runtime (linear n u1 u243)))

(define-read-only (cost_fold (n uint))
    (runtime u483))

(define-read-only (cost_list_cons (n uint))
    (runtime (linear n u14 u198)))

(define-read-only (cost_type_parse_step (n uint))
    (runtime u5))

(define-read-only (cost_tuple_get (n uint))
    (runtime (nlogn n u4 u1780)))

(define-read-only (cost_tuple_merge (n uint))
    (runtime (linear n u4 u646)))

(define-read-only (cost_tuple_cons (n uint))
    (runtime (nlogn n u11 u1101)))

(define-read-only (cost_add (n uint))
    (runtime (linear n u14 u157)))

(define-read-only (cost_sub (n uint))
    (runtime (linear n u14 u157)))

(define-read-only (cost_mul (n uint))
    (runtime (linear n u14 u157)))

(define-read-only (cost_div (n uint))
    (runtime (linear n u14 u157)))

(define-read-only (cost_geq (n uint))
    (runtime u170))

(define-read-only (cost_leq (n uint))
    (runtime u170))

(define-read-only (cost_le (n uint))
    (runtime u170))

(define-read-only (cost_ge (n uint))
    (runtime u170))

(define-read-only (cost_int_cast (n uint))
    (runtime u170))

(define-read-only (cost_mod (n uint))
    (runtime u170))

(define-read-only (cost_pow (n uint))
    (runtime u170))

(define-read-only (cost_sqrti (n uint))
    (runtime u170))

(define-read-only (cost_log2 (n uint))
    (runtime u170))

(define-read-only (cost_xor (n uint))
    (runtime u170))

(define-read-only (cost_not (n uint))
    (runtime u170))

(define-read-only (cost_eq (n uint))
    (runtime (linear n u7 u172)))

(define-read-only (cost_begin (n uint))
    (runtime u202))

(define-read-only (cost_hash160 (n uint))
    (runtime (linear n u1 u201)))

(define-read-only (cost_sha256 (n uint))
    (runtime (linear n u1 u100)))

(define-read-only (cost_sha512 (n uint))
    (runtime (linear n u1 u176)))

(define-read-only (cost_sha512t256 (n uint))
    (runtime (linear n u1 u188)))

(define-read-only (cost_keccak256 (n uint))
    (runtime (linear n u1 u221)))

(define-read-only (cost_secp256k1recover (n uint))
    (runtime u14344))

(define-read-only (cost_secp256k1verify (n uint))
    (runtime u13540))

(define-read-only (cost_print (n uint))
    (runtime (linear n u3 u1413)))

(define-read-only (cost_some_cons (n uint))
    (runtime u230))

(define-read-only (cost_ok_cons (n uint))
    (runtime u230))

(define-read-only (cost_err_cons (n uint))
    (runtime u230))

(define-read-only (cost_default_to (n uint))
    (runtime u287))

(define-read-only (cost_unwrap_ret (n uint))
    (runtime u339))

(define-read-only (cost_unwrap_err_or_ret (n uint))
    (runtime u339))

(define-read-only (cost_is_okay (n uint))
    (runtime u287))

(define-read-only (cost_is_none (n uint))
    (runtime u287))

(define-read-only (cost_is_err (n uint))
    (runtime u287))

(define-read-only (cost_is_some (n uint))
    (runtime u287))

(define-read-only (cost_unwrap (n uint))
    (runtime u287))

(define-read-only (cost_unwrap_err (n uint))
    (runtime u287))

(define-read-only (cost_try_ret (n uint))
    (runtime u287))

(define-read-only (cost_match (n uint))
    (runtime u287))

(define-read-only (cost_or (n uint))
    (runtime (linear n u3 u149)))

(define-read-only (cost_and (n uint))
    (runtime (linear n u3 u149)))

(define-read-only (cost_append (n uint))
    (runtime (linear n u71 u176)))

(define-read-only (cost_concat (n uint))
    (runtime (linear n u75 u244)))

(define-read-only (cost_as_max_len (n uint))
    (runtime u475))

(define-read-only (cost_contract_call (n uint))
    (runtime u153))

(define-read-only (cost_contract_of (n uint))
    (runtime u13400))

(define-read-only (cost_principal_of (n uint))
    (runtime u999))


(define-read-only (cost_at_block (n uint))
    {
        runtime: u210,
        write_length: u0,
        write_count: u0,
        read_count: u1,
        read_length: u1
    })


(define-read-only (cost_load_contract (n uint))
    {
        runtime: (linear n u1 u157),
        write_length: u0,
        write_count: u0,
        ;; set to 3 because of the associated metadata loads
        read_count: u3,
        read_length: (linear n u1 u1)
    })


(define-read-only (cost_create_map (n uint))
    {
        runtime: (linear n u1 u1631),
        write_length: (linear n u1 u1),
        write_count: u1,
        read_count: u0,
        read_length: u0
    })


(define-read-only (cost_create_var (n uint))
    {
        runtime: (linear n u7 u2152),
        write_length: (linear n u1 u1),
        write_count: u2,
        read_count: u0,
        read_length: u0
    })


(define-read-only (cost_create_nft (n uint))
    {
        runtime: (linear n u1 u1610),
        write_length: (linear n u1 u1),
        write_count: u1,
        read_count: u0,
        read_length: u0
    })


(define-read-only (cost_create_ft (n uint))
    {
        runtime: u1972,
        write_length: u1,
        write_count: u2,
        read_count: u0,
        read_length: u0
    })


(define-read-only (cost_fetch_entry (n uint))
    {
        runtime: (linear n u1 u1539),
        write_length: u0,
        write_count: u0,
        read_count: u1,
        read_length: (linear n u1 u1)
    })


(define-read-only (cost_set_entry (n uint))
    {
        runtime: (linear n u4 u2204),
        write_length: (linear n u1 u1),
        write_count: u1,
        read_count: u1,
        read_length: u0
    })


(define-read-only (cost_fetch_var (n uint))
    {
        runtime: (linear n u1 u543),
        write_length: u0,
        write_count: u0,
        read_count: u1,
        read_length: (linear n u1 u1)
    })


(define-read-only (cost_set_var (n uint))
    {
        runtime: (linear n u5 u691),
        write_length: (linear n u1 u1),
        write_count: u1,
        read_count: u1,
        read_length: u0
    })


(define-read-only (cost_contract_storage (n uint))
    {
        runtime: (linear n u13 u7982),
        write_length: (linear n u1 u1),
        write_count: u1,
        read_count: u0,
        read_length: u0
    })


(define-read-only (cost_block_info (n uint))
    {
        runtime: u6321,
        write_length: u0,
        write_count: u0,
        read_count: u1,
        read_length: u1
    })


(define-read-only (cost_stx_balance (n uint))
    {
        runtime: u1385,
        write_length: u0,
        write_count: u0,
        read_count: u1,
        read_length: u1
    })


(define-read-only (cost_stx_transfer (n uint))
    {
        runtime: u1430,
        write_length: u1,
        write_count: u1,
        read_count: u1,
        read_length: u1
    })


(define-read-only (cost_ft_mint (n uint))
    {
        runtime: u1645,
        write_length: u1,
        write_count: u2,
        read_count: u2,
        read_length: u1
    })


(define-read-only (cost_ft_transfer (n uint))
    {
        runtime: u612,
        write_length: u1,
        write_count: u2,
        read_count: u2,
        read_length: u1
    })


(define-read-only (cost_ft_balance (n uint))
    {
        runtime: u547,
        write_length: u0,
        write_count: u0,
        read_count: u1,
        read_length: u1
    })


(define-read-only (cost_nft_mint (n uint))
    {
        runtime: (linear n u9 u795),
        write_length: u1,
        write_count: u1,
        read_count: u1,
        read_length: u1
    })


(define-read-only (cost_nft_transfer (n uint))
    {
        runtime: (linear n u9 u795),
        write_length: u1,
        write_count: u1,
        read_count: u1,
        read_length: u1
    })


(define-read-only (cost_nft_owner (n uint))
    {
        runtime: (linear n u9 u795),
        write_length: u0,
        write_count: u0,
        read_count: u1,
        read_length: u1
    })


(define-read-only (cost_ft_get_supply (n uint))
    {
        runtime: u483,
        write_length: u0,
        write_count: u0,
        read_count: u1,
        read_length: u1
    })


(define-read-only (cost_ft_burn (n uint))
    {
        runtime: u612,
        write_length: u1,
        write_count: u2,
        read_count: u2,
        read_length: u1
    })


(define-read-only (cost_nft_burn (n uint))
    {
        runtime: (linear n u9 u795),
        write_length: u1,
        write_count: u1,
        read_count: u1,
        read_length: u1
    })


(define-read-only (poison_microblock (n uint))
    {
        runtime: u29568,
        write_length: u1,
        write_count: u1,
        read_count: u1,
        read_length: u1
    })
```

### Determining runtime cost values

The goal of this proposal is to make the total real runtime of a full
block less than 30 seconds. 30 seconds is a short enough period of
time that prospective miners should be able to process a new block
before the next Bitcoin block 95% of the time (`exp( -1/20 ) ~= 95%`).

To determine a new proposed cost for a Clarity function, we executed a
set of benchmarks for each Clarity cost function in the
[clarity-benchmarking](https://github.com/blockstack/clarity-benchmarking)
Github repository. After running these benchmarks, constant factors in
the runtime functions were fitted using linear regression (given a
transform). These benchmarks produced regression fitted functions for
each Clarity cost function, for example:

```
runtime_ns(cost_secp256k1verify) = 8126809.571429
runtime_ns(cost_or) = 2064.4713444648587 * input_len + 91676.397154
```

The runtime block limit in the Stacks network is `5e9` (unitless), and
the goal of this proposal is that this should correspond to 30 seconds
or `3e10` nanoseconds. So, to convert the `runtime_ns` functions into
runtimes for the Stacks network, we have the simple conversion:

```
runtime_stacks = runtime_ns * 5e9 / 3e10ns
```

For running the benchmarks and analysis in the `clarity-benchmarking`
repository, see the [`README.md`](https://github.com/blockstack/clarity-benchmarking/blob/master/README.md)
file in that repository.



================================================
FILE: sips/sip-012/scripts/README.md
================================================
# SIP 012 Vote Tabulation Script

The main script is `count-votes.sh`.  It will count up the votes for/against SIP 012 for a given reward cycle.  See `count-votes.sh` for detailed usage information.

Sample run:

```
$ cat stackers-19.json delegating.json | ./count-votes.sh /tmp/tally-19 4933b0b002a854a9ca7305166238d17be018ce54e415530540aa7e620e9cd86d 705850
{"yes":"10194020608227","no":"0"}
$ cat stackers-20.json delegating.json | ./count-votes.sh /tmp/tally-20 7ae943351df455aab1aa69ce7ba6606f937ebab5f34322c982227cd9e0322176 707951
{"yes":"77064706545373","no":"0"}
```

To generate the artifacts `stackers-19.json`, `stackers-20.json`, and `delegating.json` from a Stacks node's debug log file, run the following:

```
$ ./generate-artifacts.sh /path/to/node/log.txt
```



================================================
FILE: sips/sip-012/scripts/extract-delegates.sh
================================================
#!/bin/bash

############################################################
# Script to extract all STX addresses that are delegating.
#
# Usage: ./extract-delegates.sh REWARD-CYCLE < DEBUG-LOG-FILE
############################################################

set -oue pipefail

FIRST_BLOCK=666050
REWARD_CYCLE_LENGTH=2100

# DEBG [1635816373.424732] [src/vm/functions/special.rs:81] [chains-coordinator] Handle special-case contract-call to QualifiedContractIdentifier { issuer: StandardPrincipalData(SP000000000000000000002Q6VF78), name: ContractName("pox") } delegate-stack-stx (which returned Response(ResponseData { committed: false, data: Int(3) }))
# DEBG [1635816373.394132] [src/vm/functions/special.rs:81] [chains-coordinator] Handle special-case contract-call to QualifiedContractIdentifier { issuer: StandardPrincipalData(SP000000000000000000002Q6VF78), name: ContractName("pox") } delegate-stack-stx (which returned Response(ResponseData { committed: true, data: Tuple(TupleData { type_signature: TupleTypeSignature { "lock-amount": uint, "stacker": principal, "unlock-burn-height": uint,}, data_map: {ClarityName("lock-amount"): UInt(6000000000000), ClarityName("stacker"): Principal(Standard(StandardPrincipalData(SP2G4JFB3WWBWPVGEDNBTMEVJB6DNDR468G0S03AX))), ClarityName("unlock-burn-height"): UInt(680750)} }) }))
#
# becomes
#
# ""
# {"address": "SP2G4JFB3WWBWPVGEDNBTMEVJB6DNDR468G0S03AX", "delegating": "1", "until": "680750"}
extract_delegate() {
   # stdin: a DEBUG-level logfile
   # stdout: JSON describing each PoX lock event
   gawk '
{
   addr_field = "";
   for (i = 38; i <= NF; i++) {
      if ($i != "") {
          addr_field = addr_field " " $i
      }
   }
   found = 0
   address = ""
   is_contract = match(addr_field, /QualifiedContractIdentifier \{ issuer: StandardPrincipalData\(([^)]+)\), name: ContractName\("([^"]+)"\)/, parts)
   if (is_contract) {
      address = parts[1] "." parts[2]
      found = 1
   }
   else {
      is_standard = match(addr_field, /Standard\(StandardPrincipalData\(([^)]+)\)\)/, parts)
      if (is_standard) {
         address = parts[1]
         found = 1
      }
   }

   found_lock_height = match(addr_field, /ClarityName\("unlock-burn-height"\): UInt\(([0-9]+)\)/, parts)
   if (found && found_lock_height) {
      printf "{\"address\":\"" address "\",\"type\":\"delegation\",\"until\":\"" parts[1] "\"}\n"
   }
}
'
}

grep 'Handle special-case contract-call' | grep 'delegate-stack-stx' | grep 'committed: true' | extract_delegate



================================================
FILE: sips/sip-012/scripts/extract-stackers.sh
================================================
#!/bin/bash

############################################################
# Script to extract all STX addresses that are stacking
# in a particular reward cycle, given access to a node's
# debug log file.
#
# Usage: ./extract-stackers.sh REWARD-CYCLE < DEBUG-LOG-FILE
############################################################

set -oue pipefail

FIRST_BLOCK=666050
REWARD_CYCLE_LENGTH=2100

# DEBG [1635829849.697968] [src/chainstate/stacks/db/accounts.rs:298] [chains-coordinator] PoX lock 604260000 uSTX (new balance 6104) until burnchain block height 689150 for Standard(StandardPrincipalData(SP2WGGG8E7NVFA0W4YZ87M6R09TNJ33CEBAXB9QPB))
# DEBG [1635941010.356021] [src/chainstate/stacks/db/accounts.rs:298] [chains-coordinator] PoX lock 12622260119595 uSTX (new balance 0) until burnchain block height 714350 for Contract(QualifiedContractIdentifier { issuer: StandardPrincipalData(SP2C2YFP12AJZB4MABJBAJ55XECVS7E4PMMZ89YZR), name: ContractName("arkadiko-stacker-v1-1") })
#
# becomes
#
# {"type";"stacker", "locked":"604260000","until":"689150","address":"SP2WGGG8E7NVFA0W4YZ87M6R09TNJ33CEBAXB9QPB"}
# {"type":"stacker", "locked":"12622260119595","until":"714350","address":"SP2C2YFP12AJZB4MABJBAJ55XECVS7E4PMMZ89YZR.arkadiko-stacker-v1-1"}
extract_stacker() {
   # stdin: a DEBUG-level logfile
   # stdout: JSON describing each PoX lock event
   gawk '
{
   num_locked = $7
   until = $16
   addr_field = "";
   for (i = 18; i <= NF; i++) {
      if ($i != "") {
          addr_field = addr_field " " $i
      }
   }
   found = 0
   address = ""
   is_contract = match(addr_field, /QualifiedContractIdentifier \{ issuer: StandardPrincipalData\(([^)]+)\), name: ContractName\("([^"]+)"\)/, parts)
   if (is_contract) {
      address = parts[1] "." parts[2]
      found = 1
   }
   else {
      is_standard = match(addr_field, /Standard\(StandardPrincipalData\(([^)]+)\)\)/, parts)
      if (is_standard) {
         address = parts[1]
         found = 1
      }
   }

   if (found) {
      printf "{\"address\":\"" address "\",\"type\":\"stacker\",\"locked\":\"" num_locked "\",\"until\":\"" until "\"}\n"
   }
}
'
}

block_height_to_reward_cycle() {
   # $1: burnchain block height
   # stdin: none
   # stdout: reward cycle
   local block_height="$1"
   echo $(( ($block_height - $FIRST_BLOCK) / $REWARD_CYCLE_LENGTH ))
}

stacking_in_reward_cycle() {
   # $1: reward cycle number
   # stdin: output from extract_stacker
   # stdout: the JSON blobs that are stacking within this reward cycle
   local target_reward_cycle="$1"
   local json=""
   local reward_cycle=0
   local first_block=0
   local until_ht=0

   while IFS= read -r json; do
      until_ht="$(echo "$json" | jq -rc '.until')"
      reward_cycle="$(block_height_to_reward_cycle "$until_ht")"

      # echo >&2 "Until reward cycle $reward_cycle: $json"

      if (( "$reward_cycle" > "$target_reward_cycle" )); then
         echo "$json"
      fi
   done
   return 0
}

target_reward_cycle="$1"
grep ' PoX lock ' | extract_stacker | stacking_in_reward_cycle "$target_reward_cycle"



================================================
FILE: sips/sip-012/scripts/generate-artifacts.sh
================================================
#!/bin/bash

# NOTE: not tested.  Reconstructed from bash history.

LOGFILE="$1"
if [ -z "$LOGFILE" ]; then
   echo >&2 "Usage: $0 NODE-LOGFILE.out"
   exit 1
fi

# get PoX lockup and delegate-stack-stx events
grep -F '[chains-coordinator] PoX lock ' "$LOGFILE" > ./pox-lock.out
grep -F 'Handle special-case contract-call' "$LOGFILE" | grep 'delegate-stack-stx' > ./delegate-pox-lock.out

# extract log entries to JSON stacker records
./extract-stackers.sh 19 < ./pox-lock.out > stackers-19-raw.json
./extract-stackers.sh 20 < ./pox-lock.out > stackers-20.json

# consider stackers that only stacked in 19, not 20
echo -n "" > stackers-19.json
while read -r json; do
   addr="$(echo "$json" | jq -r -c '.address')"
   if ! grep -F "$addr" stackers-20.json >/dev/null; then
      echo "$json" >> stackers-19.json
   fi
done < ./stackers-19-raw.json

# extract log entries to JSON delegate records
./extract-delegates.sh < ./delegate-pox-lock.out | sort | uniq > delegating.json



================================================
FILE: sips/sip-012/scripts/stackers-19.json
================================================
{"address":"SM14T5JTCX46RXV2RW4QBKYNPFXF5PJGSBD2X7SH2","type":"stacker","locked":"500000","until":"708050"}
{"address":"SM19HFRTPVXMR2BXXFV3M6YHQNBA1APR6CYWX21RP","type":"stacker","locked":"386000000000","until":"708050"}
{"address":"SM2CC48KX8HASDE0BR9HXWCBJMK7T2YV9BFKZ83X2","type":"stacker","locked":"9940000000000","until":"708050"}
{"address":"SM3B4ZX0TM5R27DJ1MGTJX73C7P1V8406M5QGVDC6","type":"stacker","locked":"13000000000000","until":"708050"}
{"address":"SP02A0EY3X890QQRT8KWCFA8YQ5N59SXXC52BEXC","type":"stacker","locked":"595000000","until":"708050"}
{"address":"SP10EN1KAHBF1MECMD6XY6FKYPQXMT6WTPPN9FBHE","type":"stacker","locked":"41666913600","until":"708050"}
{"address":"SP10SYKPCC91PH34CP6KN6K409HT6ARTGFZPYDP1N","type":"stacker","locked":"200000000","until":"708050"}
{"address":"SP11W1YTM3TMR9ZDD7F6FAD53BQJ1ED9N575M5GX8","type":"stacker","locked":"18700000000","until":"708050"}
{"address":"SP1239SRF7MPS2WXYDVTPJ2V4ZBE2TDCV5NY42ZAM","type":"stacker","locked":"13001000000","until":"708050"}
{"address":"SP123TY61PFFAEZBX3PNH7KG3663B3GBW440NMYX0","type":"stacker","locked":"5895000000","until":"708050"}
{"address":"SP129N2D7NMT70Z76FKGPXTJ8Q76D8FGZ5GVXSQN7","type":"stacker","locked":"24700000000","until":"708050"}
{"address":"SP12YQQY1NQ58VCXVEBCDN18NGFACZJ4TPVXAJ14R","type":"stacker","locked":"800000000","until":"708050"}
{"address":"SP1308DQKXZK593BES4GV419HMM3X94MM3TSVFA88","type":"stacker","locked":"750000000","until":"708050"}
{"address":"SP13646A651GQNPJ2VYHB0K12WGQN93Q7GTFV1C8M","type":"stacker","locked":"361073000000","until":"708050"}
{"address":"SP13CM9QN6J23B6T6415SC0T8JQZ3YADPD1TJ27WZ","type":"stacker","locked":"220000000000","until":"708050"}
{"address":"SP143YPY0K388CKX1T5KH79GSW90RH49NSRZVTT0M","type":"stacker","locked":"50000000","until":"708050"}
{"address":"SP14JMK7YAHGS3296HBCMKXJN23WA9EC5BMA8WV2H","type":"stacker","locked":"68000000000","until":"708050"}
{"address":"SP14PMGHFNVXZ3N1V1VG6EJA0WH0G0Q8F0RGMYFE2","type":"stacker","locked":"238100000","until":"708050"}
{"address":"SP14SVGY4HTE0YMMQ3K6YYTPGKGY5V2NN15AY7XNZ","type":"stacker","locked":"99913600","until":"708050"}
{"address":"SP15S478J9ZMR77N501EMJADSEGAFGPT0ZZ9E9R8A","type":"stacker","locked":"1056000000","until":"708050"}
{"address":"SP16Q13XQMWST2Z842WXM0A5PWSNA6TQTPM18PK41","type":"stacker","locked":"1500000000000","until":"708050"}
{"address":"SP17AJ04SD5YYB9G5CPC1GHHC2VN6EA3PPM3SH6YW","type":"stacker","locked":"90000000000","until":"708050"}
{"address":"SP17DGYKZ8GKW8TRKE53WE6B0MVEZGXZQWRGS6SGM","type":"stacker","locked":"330000000","until":"708050"}
{"address":"SP187ERJYDSY1YDRSDTZDD2D6HM64YQB985WQ8QJ2","type":"stacker","locked":"12500000000","until":"708050"}
{"address":"SP1934QK1ZXGCEBB3MN9Y0FNR20GMDWM3Y5P5VV5","type":"stacker","locked":"1340000000","until":"708050"}
{"address":"SP19M6N5ADWN8ABGKTG75GENB99W32S4A7SVV0HJS","type":"stacker","locked":"499000000","until":"708050"}
{"address":"SP19RF4WJTWT149FQB9QGMW9N409GACD9EFVPYHFH","type":"stacker","locked":"4083000000","until":"708050"}
{"address":"SP1A8XCMT0MCX1153T2FSSJ58ESV8JVN9CFEK06DT","type":"stacker","locked":"412045000000","until":"708050"}
{"address":"SP1ABCNVR5VR8ESY2V50DYJFPBFN3TVRQNS0P3JFK","type":"stacker","locked":"1326000000","until":"708050"}
{"address":"SP1AHD995X0SJ8YSQF1FHGW5JG9TTKC5XADTMYPCA","type":"stacker","locked":"253657056","until":"708050"}
{"address":"SP1ASE7R0KDK8Z7E20VH1GQ6CXHFTTKRWZ3C5SH8Y","type":"stacker","locked":"583000000","until":"708050"}
{"address":"SP1AXVHRZMNPE4621HWPSKD18FS4GM96KSAC82RER","type":"stacker","locked":"47688999801","until":"708050"}
{"address":"SP1AYVSC81FQAFDYJ1RRMQAK8TWB40ETKEP1Z6M4Y","type":"stacker","locked":"51000000000","until":"708050"}
{"address":"SP1B35DSEAKN6JCRYYC3161G4CD7P1W7NJGV8HZ89","type":"stacker","locked":"3500000000000","until":"708050"}
{"address":"SP1B717ATWZEZ8GGBAHGSDXDJ3JHADD4R1Q16R1HK","type":"stacker","locked":"140000000000","until":"708050"}
{"address":"SP1BZC0PXGMJEM1972G2ZGEFEDTWKWERXFKWN6QFJ","type":"stacker","locked":"3685570000","until":"708050"}
{"address":"SP1BZEGCBVBZ25N5QS736CC33JM3VRJ9Q6TXG0TDD","type":"stacker","locked":"2840666938","until":"708050"}
{"address":"SP1D1F5XHQ2Y8X04HX66ECHPP27M5V0ZZKSGZXY25","type":"stacker","locked":"120000000000","until":"708050"}
{"address":"SP1D2P4A6EV88CNSKFN9JHXMZ5PN9YQRKBNXBEKA8","type":"stacker","locked":"1500000000","until":"708050"}
{"address":"SP1DZGPXNERQ9PZV92SYZASXK0GS5T3RSAMMF991J","type":"stacker","locked":"1190000000","until":"708050"}
{"address":"SP1E32XK54WWBFM0QTBNT44RV69201CZMRV2ZKKA3","type":"stacker","locked":"102720513","until":"708050"}
{"address":"SP1E9GBZ7VQHRQQMAF89VGRAPBNCYQ7NHRKX1EP6R","type":"stacker","locked":"532540000","until":"708050"}
{"address":"SP1ET0MKG8DZJHC7Q7MVGGYVRM726GBHWMQ6BD1J6","type":"stacker","locked":"222530457","until":"708050"}
{"address":"SP1F5DSY5TBFHXG80RV02N0CMRABSMCSM83A4STR0","type":"stacker","locked":"13690341486","until":"708050"}
{"address":"SP1F7WF2XCPP7Y91FZ16AVZD5Z8EDECW88WR7T1EC","type":"stacker","locked":"500000000","until":"708050"}
{"address":"SP1FBF62CJDWKM6CWVFK3R4R14JWAYNEF95E4Y7XD","type":"stacker","locked":"1000000000","until":"708050"}
{"address":"SP1FS1TV4FXBBH8AHC6Y0F8PHEKAAK8N85A61V35J","type":"stacker","locked":"9284000000","until":"708050"}
{"address":"SP1FV3SN48RVHHQF7456N62G5NW768B8YM44M3AV1","type":"stacker","locked":"40000000","until":"708050"}
{"address":"SP1FZEDKMD9736NAWS1V6Z33KBKKY4WN9JHJXCQX6","type":"stacker","locked":"135864000","until":"708050"}
{"address":"SP1G69A01K850YT1RN5QG822Q2NPTF3QS4YPYSBDZ","type":"stacker","locked":"20000000000","until":"708050"}
{"address":"SP1GDDQCAHQJ9F7WV3953CH4KXS7KMKSSMT0M20AG","type":"stacker","locked":"110330000000","until":"708050"}
{"address":"SP1GRRA4P0VHKPRF3MKNX9XD5CPBTCYQE6P1JZ2W9","type":"stacker","locked":"11999997035","until":"708050"}
{"address":"SP1HB7779C8GNDQ4VT7CTN9APSKK48XJ8PJAKTGFT","type":"stacker","locked":"1300000000","until":"708050"}
{"address":"SP1HMKBV1K727NMYZFDE237RG2NT6G92M3S6868WG","type":"stacker","locked":"50000000","until":"708050"}
{"address":"SP1J8KDC28HTF338MZJ49SNXXM9Z7GGS0KJQ0TSDG","type":"stacker","locked":"8338892899","until":"708050"}
{"address":"SP1JSE79G093C17XZNAQAVBKAX2K551KGVDZC5Z76","type":"stacker","locked":"3325000000","until":"708050"}
{"address":"SP1K9C1C760CSW669YV5J2FJ4K9VNK8J1R9N1GH49","type":"stacker","locked":"3200000000","until":"708050"}
{"address":"SP1K9YACPRZ8PMVA3QX20JN444W1S30QFSEEQ0QWN","type":"stacker","locked":"5779999801","until":"708050"}
{"address":"SP1KMRW2G1ZB200ND2JP1VP99GBBGC4FEFTQ28W6F","type":"stacker","locked":"2518000000","until":"708050"}
{"address":"SP1KPD871XYW30DTWSSG56XPVDC7253P5ZZN363P9","type":"stacker","locked":"1000000000","until":"708050"}
{"address":"SP1KWZ8MQA40FF6EXK4G6SMF06B6SZ5FVKQYC5YQT","type":"stacker","locked":"2020913600","until":"708050"}
{"address":"SP1M1ATHN7NP5ZNFKE4Q53JR7P6FAZT76AJ2VVYXX","type":"stacker","locked":"150000000","until":"708050"}
{"address":"SP1ME1TS4Z46T83K4HPQHGV3Q3VX2NF758FFCBWPW","type":"stacker","locked":"99000000","until":"708050"}
{"address":"SP1MJ8FNYZHE19H8YFJ624ZEEXAEB69B80G3DQ0XK","type":"stacker","locked":"4476638285","until":"708050"}
{"address":"SP1MS7KGA5WESV319PV9GVKW2FFJJ1YNT9ETC6FQC","type":"stacker","locked":"4000000000","until":"708050"}
{"address":"SP1N06Z1498FKVCB9QK4TYEKQ70XCKFCXH4BEYEC4","type":"stacker","locked":"82332000000","until":"708050"}
{"address":"SP1Q3VA4YYDAFY7WQVQGZYGH0D232BM4DV2KF7T1S","type":"stacker","locked":"92406500","until":"708050"}
{"address":"SP1QAHRV4H9X0QTBD4SDF2XTQQZXQG6SQ7XVTE0K8","type":"stacker","locked":"103348000000","until":"708050"}
{"address":"SP1QJBEHS9P9S3D91GWDAV1SQAA9613TWBGCC9EYS","type":"stacker","locked":"7989000000","until":"708050"}
{"address":"SP1R1HND0ZXGFZXQCRKQ1PNR1ADA7ZJHJMKVJ1HCJ","type":"stacker","locked":"324950000","until":"708050"}
{"address":"SP1R6YS229G7TV47ZEZ33CDQBS7AQR3QJSY3MNF4F","type":"stacker","locked":"500000000","until":"708050"}
{"address":"SP1R8NFPFGFPVM7DCCVQ4HBJ83QJA5ZGW50CRK9RB","type":"stacker","locked":"2043918584","until":"708050"}
{"address":"SP1S2EN7AHYH41P9DSYW0VM8FRHSDD77CFA3A7H3T","type":"stacker","locked":"40000000000","until":"708050"}
{"address":"SP1S3K579FJQNHVNBBXT5WZSTFMT95HS018WWB0AT","type":"stacker","locked":"14994000000","until":"708050"}
{"address":"SP1T0NKGCAZZKCKNVMAW60DDZ9QC5XAD8C4QDD3PP","type":"stacker","locked":"100000000","until":"708050"}
{"address":"SP1T2SV6451HSZPJH9YBFWDM69ZPEVXM86HM597XJ","type":"stacker","locked":"99913600","until":"708050"}
{"address":"SP1TD345DMS67CJQJR8S9FQ95M9ZSHDHYTJ4SK4VS","type":"stacker","locked":"442969801","until":"708050"}
{"address":"SP1TQ2BKXYWJ2W8DCKQSP94CTHYC8EKJT7T1Y09D8","type":"stacker","locked":"1200000000","until":"708050"}
{"address":"SP1TWA0K60WB961W7QJQKHTASNQXZEEP36V15TFGQ","type":"stacker","locked":"6256378400","until":"708050"}
{"address":"SP1V7NRPKG7XHGNBZ5HGQ42SM90VNF2Y5YXY0RDA7","type":"stacker","locked":"262190000","until":"708050"}
{"address":"SP1VDP51TS04PWRK4DBPY64T8M1GY85Q1QX8WDVFN","type":"stacker","locked":"186000000","until":"708050"}
{"address":"SP1VM3P7H4N82DK1WDVFT50GDHZKX3ZH7XSN8KNP1","type":"stacker","locked":"500000000","until":"708050"}
{"address":"SP1W8C25TZCXDQTAR7MZQPSNF8C73274DCNT2NWJZ","type":"stacker","locked":"100000000000","until":"708050"}
{"address":"SP1WQ59358VCM82GSVREYF4RZ02QXVZ1WXRCZSCPG","type":"stacker","locked":"2400000000","until":"708050"}
{"address":"SP1X2WX4RS1GBDF3KNS4XXJ718XRPJ77A4XNXH2ZY","type":"stacker","locked":"5000000000","until":"708050"}
{"address":"SP1XDN5MVZ732N4TSPS7A4PGTY2VKBN2VYY823R8D","type":"stacker","locked":"422870303","until":"708050"}
{"address":"SP1XTAXYRTSKMZFV6PTNGHJWKFTS2KVJK5GZYF38J","type":"stacker","locked":"17699618079","until":"708050"}
{"address":"SP1Y5603BG64PND9X5V59FPZATPTFWSQHQMWFHJ9D","type":"stacker","locked":"22575590063","until":"708050"}
{"address":"SP1YFA8FW983BDZXH87KH80795172E3Y9XC5VTTK9","type":"stacker","locked":"98313600","until":"708050"}
{"address":"SP1YYBMTZVG18PBVB4XTSK7TTWDJJ3C6TZXSNMAJ0","type":"stacker","locked":"42710000000","until":"708050"}
{"address":"SP1Z7CW5WDWMJ6WFKE1CRF41V8C4YD911HYGH0WF8","type":"stacker","locked":"600000000","until":"708050"}
{"address":"SP1ZHD36QBDRN42X4X5ZVEVBWKAXTMMA3BKNYWDY1","type":"stacker","locked":"395000000","until":"708050"}
{"address":"SP1ZHDJ95YEJ9PZPYPF95FMWDKWCQSWRAQWQHYWDP","type":"stacker","locked":"505000000","until":"708050"}
{"address":"SP2009K5G8DGFY7F4ZDRT9K1JP9CKTBZC5WFJZAD7","type":"stacker","locked":"205394050000","until":"708050"}
{"address":"SP207D4A7XMNGA7JJ34FD724A0NYV7K7MYDWK9T21","type":"stacker","locked":"200000000","until":"708050"}
{"address":"SP207R9N5VTFS6H2G0CFKZ6JB6AHBYN7E2FR0M0DN","type":"stacker","locked":"24999999801","until":"708050"}
{"address":"SP20BZFPPQMEGSG1NPZRQE0JTFXF68EQW4JZD69EZ","type":"stacker","locked":"100000000","until":"708050"}
{"address":"SP20GSBGFKJZECGP932GQQSZT83KXF4HC7KPF65QF","type":"stacker","locked":"290000000","until":"708050"}
{"address":"SP20J1SD14FXX9VE6GC4QKSPP2F3JNF5WVDZR4TYZ","type":"stacker","locked":"374999000000","until":"708050"}
{"address":"SP20JMXFT8QRYES7Q1ZNTWPAXACETHGSWV9A0EDEP","type":"stacker","locked":"1360000000","until":"708050"}
{"address":"SP221CDNSRGS6CM4BCJGKCQDYG03JTBCF8RX42D01","type":"stacker","locked":"500000000","until":"708050"}
{"address":"SP228WEAEMYX21RW0TT5T38THPNDYPPGGVW2RP570","type":"stacker","locked":"400000000","until":"708050"}
{"address":"SP22J0TQ6YA0EB70YD3GW24A9BEGDEA3XA5TAB9SQ","type":"stacker","locked":"110697000000","until":"708050"}
{"address":"SP22Z57B3PH87F0EAH9AEVP01RDZX9K8JT03G552G","type":"stacker","locked":"543000000","until":"708050"}
{"address":"SP22ZJZ1KETW298FXKV58RF95VB2MQSQ0807BBM5P","type":"stacker","locked":"1306218300","until":"708050"}
{"address":"SP2389QCGHF3EFNSZAKQDA8SS3SW8KR24D7Z06HHC","type":"stacker","locked":"773720000000","until":"708050"}
{"address":"SP23EW35J2RW3JD815W9S53SXX97N679GW221HSSA","type":"stacker","locked":"67000000","until":"708050"}
{"address":"SP246HMXWGY3WF7VRZB3E5E2YPTM0ZRXXMFTTVZ5S","type":"stacker","locked":"2000000000","until":"708050"}
{"address":"SP24AFQEDS4HR26P2NFBYH0VPCXHJ637QMC6ABFK5","type":"stacker","locked":"385229000000","until":"708050"}
{"address":"SP24GQ60GT3G3NSX7090YRR8DBMFF2NXTW1GHD4AD","type":"stacker","locked":"500000000000","until":"708050"}
{"address":"SP24JRWPM2YBXCV0SKR820JPTVEQK9NYNWMZPE7CV","type":"stacker","locked":"1443000000","until":"708050"}
{"address":"SP24TN44EK3MPAPQVGSGQ5EH0DGBKSHT3BKQJB924","type":"stacker","locked":"25000000000","until":"708050"}
{"address":"SP24WE3BZTDPH2M5RF0H8HDETG3V7424R3YR5BSNM","type":"stacker","locked":"33982671446","until":"708050"}
{"address":"SP2570YNWG8EEP37V68KJ3PK35AN8691CDY6GZR2G","type":"stacker","locked":"2500000000","until":"708050"}
{"address":"SP25SQR5GE76ED6KA2ZBVHRDRQ7537R7ZT8J0FD0W","type":"stacker","locked":"672929134","until":"708050"}
{"address":"SP25X4TZBD3GFAZ6ER897QXJ318SBEPT9RCTM03BS","type":"stacker","locked":"2000000000","until":"708050"}
{"address":"SP25ZA03RTFHTDJT9M5GNX8QV1YJRJA2J47PQFBSY","type":"stacker","locked":"101560000000","until":"708050"}
{"address":"SP26Z4AHW28NZQMKYRH2NBCEMN1BMZY2W8ZPDHDWF","type":"stacker","locked":"538000000","until":"708050"}
{"address":"SP272G79GSJB7BZ66PRF3GBS9VKS65J3F9B5VS901","type":"stacker","locked":"200000000000","until":"708050"}
{"address":"SP273XN645XQ35KPGSCYH1R7AFA7D9DSGCM1E66J0","type":"stacker","locked":"1185000000","until":"708050"}
{"address":"SP27EQH5ASYBRMKD7A1RFE7HX44SPXETAB9R8QTVS","type":"stacker","locked":"36500000000","until":"708050"}
{"address":"SP27S5Y9P81XX2PZC28GQ687B8CYWW2E0B54GNXWB","type":"stacker","locked":"300000000","until":"708050"}
{"address":"SP281EDFY54S0GCDTKPEKP6K32Y8VTJ6DC4KXTFY3","type":"stacker","locked":"7089391725","until":"708050"}
{"address":"SP287WSB9DMKVWND9JQKZ3H9TY9MSDV9QEQ8SJ3TP","type":"stacker","locked":"15000000000","until":"708050"}
{"address":"SP28FS6K7XZXJC8NMKV65W65T66C5D76TNFZWECW1","type":"stacker","locked":"4547000000","until":"708050"}
{"address":"SP294GG6MJJCHZ2BDV5PTMPK93MGYB2CY9VV5GG6D","type":"stacker","locked":"1718223659","until":"708050"}
{"address":"SP2A54X7G1JXYK5VQN4C5KHDHJV8RFJ9RJTSCVZGW","type":"stacker","locked":"1300000000","until":"708050"}
{"address":"SP2ABCYTA1WH4KZ9KMERHJP4EQJJCQDME66D5A1HH","type":"stacker","locked":"21874999008","until":"708050"}
{"address":"SP2B8XVVQN16VFKFKX7A5VGBNFE3WE3N8PHAD6HQ1","type":"stacker","locked":"1500000000","until":"708050"}
{"address":"SP2BNP9637394002WP5BSWK2SHS97JGRFRJ71Q394","type":"stacker","locked":"250000000","until":"708050"}
{"address":"SP2BQ782SESAYXACWCWDYP0Y4YVYVW0FBRQ384XX4","type":"stacker","locked":"100000000","until":"708050"}
{"address":"SP2C7EE8T80AHDCYD1HPZMJJXNMCFXGXDK7ME0M4G","type":"stacker","locked":"830000000","until":"708050"}
{"address":"SP2CQPK19120XS71E1D1YAMBSNVSJ3KJS70ABA9TC","type":"stacker","locked":"99913600","until":"708050"}
{"address":"SP2D39N30HS99R8VFKHMQJH1665WZSJPXSSDKSP25","type":"stacker","locked":"200000000","until":"708050"}
{"address":"SP2D784TEAPZH07FC1MY6CCK0R3ACNDGHR3FBSMKJ","type":"stacker","locked":"100086400","until":"708050"}
{"address":"SP2DD4SR9MPBRKCJVMFYFGPM4FY1VJ63E0BT8YA27","type":"stacker","locked":"2499000000","until":"708050"}
{"address":"SP2E15MCQG2HC7RDV5A88HSRTP80DPVYQPHGN1BV9","type":"stacker","locked":"500000000","until":"708050"}
{"address":"SP2EBZB4M75QYAA9XP9XY98PQQCCVMQAVDAT0CXCQ","type":"stacker","locked":"2400000000","until":"708050"}
{"address":"SP2ECKAWK4DRPM6AMP2QH3VFCP5DHKZBFWVEWTDNR","type":"stacker","locked":"40000000000","until":"708050"}
{"address":"SP2FN6XCY6D84YWJQJSBPBDYXPXMAQWP6A61AXE31","type":"stacker","locked":"700000000","until":"708050"}
{"address":"SP2FNPHR7YE49C9B8FNKN1R0RCASHMRDEZ71PZ5JY","type":"stacker","locked":"929841780","until":"708050"}
{"address":"SP2FP6FW5PQY1JWGSMKPD705F7XZSQ4PJ3JD52EG9","type":"stacker","locked":"1427000000","until":"708050"}
{"address":"SP2G6B6ARQ8R5MRE702JPXBDV7PVSW5HTS81GYQ7G","type":"stacker","locked":"5300000000","until":"708050"}
{"address":"SP2GA0B2HMKNV9GKFGGPTKWJHJ8TEYFBVMTC9FX6W","type":"stacker","locked":"3000000000","until":"708050"}
{"address":"SP2H1A16NZ2HS9SGHQ3ZFDV2ETQW5YD777CY9W31X","type":"stacker","locked":"1500000000","until":"708050"}
{"address":"SP2H4HFERWC4208VW51BPGT9C2J74MT1W5JDBGZAZ","type":"stacker","locked":"700000000","until":"708050"}
{"address":"SP2H5VVV8WABA2QZV2ZEJ81FG1P25J4CNB18ETTMD","type":"stacker","locked":"99000000","until":"708050"}
{"address":"SP2JMZ72A6PSENJK32KM86BH8CDA5MX6J841Y7T2S","type":"stacker","locked":"651136400","until":"708050"}
{"address":"SP2JPJED6E76TXTPF8V773VA8Q9Y3T5PFED2XME2J","type":"stacker","locked":"500000000","until":"708050"}
{"address":"SP2JVZ8BKVJE1GY3A6DH0JRAWDSPT0TVPW580RQQ1","type":"stacker","locked":"857000000","until":"708050"}
{"address":"SP2K2Y277FZ48627S2PGDH0Q0J0GBJCYSY4QYNPK6","type":"stacker","locked":"6000000000","until":"708050"}
{"address":"SP2KBD37DQCGGMAG2CKDAXA5AMYCWAH25B2TQ3ZET","type":"stacker","locked":"30972999060","until":"708050"}
{"address":"SP2KZZ20P68NKG1XW2CT98NHWEK5KS1CYCMV3GVF6","type":"stacker","locked":"13703595000","until":"708050"}
{"address":"SP2MAGHWK255EXCQ2ZSVBT31Z3CH702N6N6WSHX9G","type":"stacker","locked":"200000000","until":"708050"}
{"address":"SP2MW6VSVM0J6CTKCEZBCPQNAYAG790K3R0ME0ASZ","type":"stacker","locked":"1000000000","until":"708050"}
{"address":"SP2N27AWKMQEH9S9VDEYMZWS83PD9FKTVNM2MM6Z4","type":"stacker","locked":"550000000","until":"708050"}
{"address":"SP2N3Z3QHHMBEV2EPRZA1P83M213TPTCV5XD5HQ4X","type":"stacker","locked":"297919900","until":"708050"}
{"address":"SP2NK7DRRGAE9ZZ38NFPBGMK39XEA5CWKKKDW03BJ","type":"stacker","locked":"5000000000","until":"708050"}
{"address":"SP2PAZQWB6Y5G0TSMC0EXFDKG5AQEZ2AQTF388D28","type":"stacker","locked":"20000000000","until":"708050"}
{"address":"SP2PRBEX510TSNRT7T1JX8P59MSBSQHRTEM8S06GE","type":"stacker","locked":"8000000000","until":"708050"}
{"address":"SP2PXNWW3EA4WCVQS54E03T969TW51DW3SZBHFNR5","type":"stacker","locked":"300000000","until":"708050"}
{"address":"SP2Q79QN7YYTH4Y0X2H1CH0XKHG78HAPCXYCFPN4A","type":"stacker","locked":"2239000000","until":"708050"}
{"address":"SP2QGS35J9Z77GK73JPQZ080RJ7TWJJ620J9YTJBF","type":"stacker","locked":"95000000","until":"708050"}
{"address":"SP2R8C36A8KVBBWYC4ASD6V36S2E9VJ0FXWV2T4CP","type":"stacker","locked":"2500000000","until":"708050"}
{"address":"SP2RFZA63SZRX5CZRBHKFC01S4QVWP8P0NEZYX54F","type":"stacker","locked":"1314999604","until":"708050"}
{"address":"SP2RW80TCDT7ZQRG95HN5GVS8XQGYR3HN7CZE8SG","type":"stacker","locked":"20832913600","until":"708050"}
{"address":"SP2S0948DSAHCG5J5P2CF5WRW6V1BNJFS7XFRA5ZN","type":"stacker","locked":"450000000","until":"708050"}
{"address":"SP2S3TREKZAZARJ3VYS7Y8QYWKN8C4BBVZR1C4MZ6","type":"stacker","locked":"978584566000","until":"708050"}
{"address":"SP2SSHDSGHHEQN1A7Z0RP0YJ6QECE8TGQTYN594PM","type":"stacker","locked":"50000000","until":"708050"}
{"address":"SP2ST1HP2F24PTKNT2Y4AB19PZ5NY0HCP7M2ZJSEJ","type":"stacker","locked":"1977038245","until":"708050"}
{"address":"SP2SXNTK8H2ZF8Y9CW2EJEHVFBAVH8AK31RNJSZ59","type":"stacker","locked":"1020000000","until":"708050"}
{"address":"SP2TB9BR1WQ8TZTACRY4MWM27KGR85VQAM8BK49NE","type":"stacker","locked":"1300000000","until":"708050"}
{"address":"SP2TDGJZAGJWFSJAWQN2WBGR0TNEVV4CNWJBZ1SNC","type":"stacker","locked":"431000000","until":"708050"}
{"address":"SP2TZBMHPE6C37PAG6VPA1AGT310HCDGBF5GRCH6C","type":"stacker","locked":"50000000","until":"708050"}
{"address":"SP2V9ATCT5AGFSEP3WGCKQHNG26CKE3V3Q6WPRG46","type":"stacker","locked":"818265264","until":"708050"}
{"address":"SP2VCYZFK5JAPHWESXSJXB3CJABMVW3PAX8SWBPYC","type":"stacker","locked":"10000000000","until":"708050"}
{"address":"SP2WBXERYJXSH1RE9BJ9CY4A24R6SY3S1YC7G85AE","type":"stacker","locked":"2635000000","until":"708050"}
{"address":"SP2WKB7YWTPCVPNW5XVWSZQEQK07J91371WYV63TV","type":"stacker","locked":"3212000000","until":"708050"}
{"address":"SP2X40FDFC4GKM5P7ZA22QRAP4E6DVBGJKHXXED9N","type":"stacker","locked":"200000000","until":"708050"}
{"address":"SP2XESVQBJMNFZP4VQEBP3SJB69ANZZ2Y67CY07CP","type":"stacker","locked":"36925999801","until":"708050"}
{"address":"SP2XPYCM9ZYHFM119P57WM50S2CMQQ04G9ENRCPQG","type":"stacker","locked":"2500000000","until":"708050"}
{"address":"SP2XTWNFRKVC580XWRHW7DPCAF7NRQSPZXB0H00G7","type":"stacker","locked":"9668000000","until":"708050"}
{"address":"SP2Y4QYK69BYZV59FGPAFJ6K47MQBMA431YQ8R7ZY","type":"stacker","locked":"200000000","until":"708050"}
{"address":"SP2Y6M02JW7F2EFA4VEJFPN0YRWV6RVYP0J013GET","type":"stacker","locked":"50000000","until":"708050"}
{"address":"SP2YC41386MSKZVWWT0Q4R7YGY85PFTVCQ9QWKV3K","type":"stacker","locked":"200000000","until":"708050"}
{"address":"SP2YSD5XQQDT2P114BEY28H6YMJJ1RKKA4V9EFCE2","type":"stacker","locked":"2083333332","until":"708050"}
{"address":"SP2YSXDXE1E450S61V4VSZMZES3QNRASDH83P9D0D","type":"stacker","locked":"2018632317","until":"708050"}
{"address":"SP2Z6BJJZM6WGFJBRQQHKJPXJVQZEK85DVF96B5EZ","type":"stacker","locked":"79119800","until":"708050"}
{"address":"SP2Z93NTWX2ZC423723P1XXWTR2QNYBRYNZGP6T1M","type":"stacker","locked":"2000000000","until":"708050"}
{"address":"SP2ZBPK3HNMZ1V3Z1J1DDD9QCEEMHBDAPBY0QKQWS","type":"stacker","locked":"333330000","until":"708050"}
{"address":"SP2ZBSDRAYDFVH613N1MMRNGS313S7XKNSCJYZ83P","type":"stacker","locked":"72000000","until":"708050"}
{"address":"SP2ZT0BGFZX5V8DW2RCAJCT7YNNGR2ZXJT091ZBKZ","type":"stacker","locked":"3209000000","until":"708050"}
{"address":"SP3047EGCA1P4Q6FNDQHXJTH7JYWH96TJD21QB74A","type":"stacker","locked":"995000000","until":"708050"}
{"address":"SP30F2QAKR5TEN0FTK4XGPYBB8JHDRMNVE3QFKV47","type":"stacker","locked":"1000000000","until":"708050"}
{"address":"SP30GGD247PAQCS6WYM1QW9H21R1BXZ36A3AH4WZ9","type":"stacker","locked":"224000000","until":"708050"}
{"address":"SP31W6HP3MX51BTM1TM43AE2WEAK0ADE75P7Z871G","type":"stacker","locked":"98841600","until":"708050"}
{"address":"SP31WY87X4BNKJ9N39BW4E0KGR17FRJMB3VFF4ETH","type":"stacker","locked":"100000000","until":"708050"}
{"address":"SP325DAYKWK2AST79G24TTJ9E28CBEESGRG9XWCAF","type":"stacker","locked":"100000000","until":"708050"}
{"address":"SP32W4N2WK6JAHNTV3VZD6B6H29FTBMTY44ZWSMW5","type":"stacker","locked":"17000000000","until":"708050"}
{"address":"SP32X0BRC5J1BTC88MFGHTBQ8ANWN243PVM0HTV9Y","type":"stacker","locked":"30000000000","until":"708050"}
{"address":"SP32XD1F46VPYGWSWFXGBKM2JWNK5TWKSNWB6PK7J","type":"stacker","locked":"50000000000","until":"708050"}
{"address":"SP3335VRW7MEP5PXZ8ZFS7FDJBX2DXX374T0QVZDX","type":"stacker","locked":"2499000000","until":"708050"}
{"address":"SP335WVA3CRKPWH73Z535PRK5995W2QA4BPPSDRSW","type":"stacker","locked":"1000000000","until":"708050"}
{"address":"SP33DF00JSGZHJ2TJSNNCWQQHXMVK0384ZMYBCWJ9","type":"stacker","locked":"354481800","until":"708050"}
{"address":"SP33S5RP1DSNYX9AZJ5C96EA9RQNVM1Y1WJYCDRG1","type":"stacker","locked":"91712000000","until":"708050"}
{"address":"SP34194H4V84A99FR64ZEMSMFPKQWH92XS0X5FRXX","type":"stacker","locked":"120000000000","until":"708050"}
{"address":"SP344FXYA19N7RX3MSBRHKZ8R830ZVP6XB24GT605","type":"stacker","locked":"4997571600","until":"708050"}
{"address":"SP344KKNJ86Q7H592V9VTY4KG2V5QS1CGQFNRP3QZ","type":"stacker","locked":"10000000000","until":"708050"}
{"address":"SP345A685CP2YB3J7WWTQKF3Y9SWCVETXHQNMBXDX","type":"stacker","locked":"477310793","until":"708050"}
{"address":"SP348BNKDH8AFYF04FRKS6FE1DN8YJXNMGQEZDD6X","type":"stacker","locked":"101417697","until":"708050"}
{"address":"SP34BD9Y4F4VVJSVJSET42CWKW6K0A81D1YBC0NVH","type":"stacker","locked":"2000000000","until":"708050"}
{"address":"SP34N4BJVEHDRBFYMR61AQ066474N06XWSJZJXFQK","type":"stacker","locked":"125000000","until":"708050"}
{"address":"SP34V4SST6CRC1X81J4494HJ041NENQ5QSXZ9J1X4","type":"stacker","locked":"601018000000","until":"708050"}
{"address":"SP359XCXKRQYPM5FRN3YY8TQH8EMWQRPCD1KR80CC","type":"stacker","locked":"1106000000","until":"708050"}
{"address":"SP35T2XPRFV930TZ8N3EZ7GA04EHAF4JBYRBK0R17","type":"stacker","locked":"99072000000","until":"708050"}
{"address":"SP36GDZEKRN5RES3PRHVK0V8WKAE35DZEJZJPQG6H","type":"stacker","locked":"1195000000","until":"708050"}
{"address":"SP36Y8XKYDC1KWVZCMVJ34YBQN4XZXTH5KJ5D72TX","type":"stacker","locked":"371896771","until":"708050"}
{"address":"SP37C6HQRQ4GYP1EMEK7KW31HG7G5JNZ5ZPFQMP57","type":"stacker","locked":"25000000000","until":"708050"}
{"address":"SP38HVW2KCREMH2J9HDJR8EZ7EXCJWMZ2M1YACP19","type":"stacker","locked":"90999000000","until":"708050"}
{"address":"SP39K85BYDZ9D34BRBKE60X622MA0JKQAS1NB27S8","type":"stacker","locked":"1500000000","until":"708050"}
{"address":"SP39VZBGWRZQZW3B0K7CHRYXGFKV1MVVVXF7HVWE3","type":"stacker","locked":"8460000000","until":"708050"}
{"address":"SP39W418XW5K075CTXEQYA2R3P3Y552QCCGV96F20","type":"stacker","locked":"111668000000","until":"708050"}
{"address":"SP3B7BNQP8XA9DH5CK6XDYHCAME008D46BD77XBM4","type":"stacker","locked":"99000000","until":"708050"}
{"address":"SP3BA14EBS58TY6MGMV6KQB47YHNPSNWTN4ZTMSFR","type":"stacker","locked":"110000000000","until":"708050"}
{"address":"SP3BZZ4HY118YANTMV7SEBPC98RNTT0CQ5SGGXQ55","type":"stacker","locked":"97776000000","until":"708050"}
{"address":"SP3C049E6CNBTPFQ6GMSWHT0FHQQ0208843MRD67B","type":"stacker","locked":"40000000","until":"708050"}
{"address":"SP3CBKJV78QSSY1MHDHH3E5FDJNEJJVMHAJ3Q9K17","type":"stacker","locked":"416466000000","until":"708050"}
{"address":"SP3CM7FQPGXDH8V23J29QZ025RVR1RBY1BK0BNM82","type":"stacker","locked":"4000000000","until":"708050"}
{"address":"SP3CP1DD0BH9EA9PX08DWBAYV9RCEH2R0PDM90TNT","type":"stacker","locked":"474000000","until":"708050"}
{"address":"SP3CR120Z3QRMQZN9J21QNR663PX7ZVTD3970GRR0","type":"stacker","locked":"123141600","until":"708050"}
{"address":"SP3CVFTJRWMM76GSBWG4WFKAR4P4WQJR7HVB55N8M","type":"stacker","locked":"519000000","until":"708050"}
{"address":"SP3CXP82SP2M920C5XX42RMAJ3Y6FS0KS5ZK1N1BC","type":"stacker","locked":"8000000000","until":"708050"}
{"address":"SP3CZFTS449PGACNX85PAK882PTZK9502PZ70RJ75","type":"stacker","locked":"1000000000","until":"708050"}
{"address":"SP3D5HNRZQDKYS3RRFSCZ33MZ0MH0FCYNMVRV3AWJ","type":"stacker","locked":"2885000000","until":"708050"}
{"address":"SP3D5TAQAMG3DZYKCH3CXCG4RZ4H5DNJ1WV8ZXSBR","type":"stacker","locked":"1100000000","until":"708050"}
{"address":"SP3DJWHZ1A091441XAK7FJAYWS5TNVPNX6DPYG5D5","type":"stacker","locked":"800000000","until":"708050"}
{"address":"SP3DXVQCHKPCADYA1HC82YYC7FVJDT65VRN0RH32H","type":"stacker","locked":"10000000000","until":"708050"}
{"address":"SP3E01HSR8SC25QPK5YXY9R04V2YYMFP34W3ZPPTM","type":"stacker","locked":"32575000000","until":"708050"}
{"address":"SP3E13ZCYW2ZQQCFN6YEN6NXK56HNFRAY3MJ6PGB0","type":"stacker","locked":"3710912828","until":"708050"}
{"address":"SP3E6S7TDY2C19J0VNRPARX454ZWNE63S8HSN2VSZ","type":"stacker","locked":"8080000000","until":"708050"}
{"address":"SP3EHY1QQX1DEJK1HR2DTK5BH92A252ZSZACV3QM8","type":"stacker","locked":"4774000000","until":"708050"}
{"address":"SP3EXTHZ7PHAJ8DDJB7AMVQXDZ6T68364EZ01WB20","type":"stacker","locked":"959030356","until":"708050"}
{"address":"SP3FEHH7WAWGNDTXC6CMX1NV4S8331BK55CQ04XGV","type":"stacker","locked":"261988000000","until":"708050"}
{"address":"SP3FJ31S46NS9XJEXK40ACV2MNFFKV421095ZWDQW","type":"stacker","locked":"580000000","until":"708050"}
{"address":"SP3GDZH3XEN81H6PWDA7WN6KW7E8V2C219X10NRTN","type":"stacker","locked":"1050000000","until":"708050"}
{"address":"SP3GSKXZWRXZ6Z42M6M7CYN4FTPJFQHXVNCNN1TBR","type":"stacker","locked":"12619000000","until":"708050"}
{"address":"SP3H3BJ7H35QM2RNV5TEAJC6BAY3VQTCCN7HNH1NQ","type":"stacker","locked":"50000000","until":"708050"}
{"address":"SP3H6X82CFV3E3KRNX194Z30DNT9V3KFG2VB2YM4B","type":"stacker","locked":"96962813","until":"708050"}
{"address":"SP3HPDJD9CGSGG7MC2HMFTFAPAJ3VFSQ3Y3FPZXFV","type":"stacker","locked":"1137759100","until":"708050"}
{"address":"SP3J1J8SXVAEFB0YGDFA3CJFM99Q2FKK67B82E10","type":"stacker","locked":"515000000","until":"708050"}
{"address":"SP3J5KNPHSFM9Z751060HEN49PZSZGZ28QAS2SWWD","type":"stacker","locked":"197916000000","until":"708050"}
{"address":"SP3J66FRWD9MP6X2PJD6197YMSYKNGW2MTHA7P2Z2","type":"stacker","locked":"1154000000","until":"708050"}
{"address":"SP3JNTAQVKN7B7521RJRHW9NT37B6BADED6ZG8R79","type":"stacker","locked":"500000000000","until":"708050"}
{"address":"SP3JP38M5S9WG2JXHM3NPGGPZF6CRS7RP5XXSP11M","type":"stacker","locked":"1027000000","until":"708050"}
{"address":"SP3JZ4CDBEWNZEA8EXXNWFQ98FQ0VMZS453VJB2TF","type":"stacker","locked":"760975600","until":"708050"}
{"address":"SP3K264JEZ5C3QRZ51GE167G8X520CCV0M7G08PFV","type":"stacker","locked":"12000000000","until":"708050"}
{"address":"SP3KEDCZ6BNBT1GFTG2XJXR6WZB1Q6NK624EV96GR","type":"stacker","locked":"2847000000","until":"708050"}
{"address":"SP3KWVT3CTP9KDQPGACJVBPR1T22S2AZE77FQ8VEW","type":"stacker","locked":"1000000000","until":"708050"}
{"address":"SP3M7K8GEZ8FCDW922R6P7YZYFMD7C4HJJ5K0R4D3","type":"stacker","locked":"107852941","until":"708050"}
{"address":"SP3M91PQ2VAS67804G7DBMCSFR87V38GTHDWYS6NJ","type":"stacker","locked":"900000000","until":"708050"}
{"address":"SP3MBV19ABTV3ZDY8RC1EKQC1ECN1JRBT0B1KJWEG","type":"stacker","locked":"157000000","until":"708050"}
{"address":"SP3MGK82ZAMSF309ME63SAF9CEW42X5JAMXYFF08S","type":"stacker","locked":"99999784","until":"708050"}
{"address":"SP3MJ8PXRZSYHQX6AYQXGA1GRGA4W2NJKN3NFY3TY","type":"stacker","locked":"2085270000000","until":"708050"}
{"address":"SP3MNXF624DWVA6R4P79XC7HS378BZJC17178SDVF","type":"stacker","locked":"10100000000","until":"708050"}
{"address":"SP3NFAYYF2G6EZD91KDZZFBF94HH13Q9WKRT8DHBS","type":"stacker","locked":"449999000000","until":"708050"}
{"address":"SP3P1ZA7S3QF5QQAMZK3QDKQ9TPX0AZ1ZPKD118RQ","type":"stacker","locked":"23000000000","until":"708050"}
{"address":"SP3P8ZWARDDFEWHEVJ85RR2V89PT4VBEQKFP4KE09","type":"stacker","locked":"990000000","until":"708050"}
{"address":"SP3PEHCWSEZ6D1M3950ZTY71EK8DAK4A5ZQ0B3DTR","type":"stacker","locked":"989000000","until":"708050"}
{"address":"SP3PGB46DX8M0M679J4Z1AETEGMCK7ZJDYJV7MEM9","type":"stacker","locked":"2355000000","until":"708050"}
{"address":"SP3Q0DJE6GPY4V0WBKKAE2GGFJ3W2X7ETVSFRANW7","type":"stacker","locked":"5056000000","until":"708050"}
{"address":"SP3R6JQPJMGNZ49YWB4ZCD9T4SQZCSTQF0YYN8XF1","type":"stacker","locked":"17000000000","until":"708050"}
{"address":"SP3RFER8H3CF3516X77GPTXM7W237BEKPJVE9BQV6","type":"stacker","locked":"1190000000","until":"708050"}
{"address":"SP3RYV2GY2ZCXHD8WKZ1WQD1Z38Q67E82PBV6N5M1","type":"stacker","locked":"754000000","until":"708050"}
{"address":"SP3S8H7JJ1TTRMY28DF46ZJYFHF7GNEJ2PJXP7FPZ","type":"stacker","locked":"2043761200","until":"708050"}
{"address":"SP3SJFERFAW051RK9Q74QZ6G7AC5M9T9ZM5FAZ8N3","type":"stacker","locked":"814899158","until":"708050"}
{"address":"SP3SKGVBYQMQAWSA9FY11P5QC7NVNG55XGQ4VZKSJ","type":"stacker","locked":"1090000000","until":"708050"}
{"address":"SP3SNKQXCTVGQ3Z4VRR443CJT5KX96CX7PZ4F89J1","type":"stacker","locked":"28300000000","until":"708050"}
{"address":"SP3V0YTM40AD2DD0094C6ATT9Y1T4T7TJ8MKPDEFE","type":"stacker","locked":"99999784","until":"708050"}
{"address":"SP3VJN00MMZK90SF5R1BE6BFW5GXH4MDR577S5NS6","type":"stacker","locked":"107913600","until":"708050"}
{"address":"SP3W7P3S6HEHR9ZJ91DZEC683WFYCDACNHVWSAN5K","type":"stacker","locked":"2951388890","until":"708050"}
{"address":"SP3WVC89JPADZQJ0RFQS1D1627NS1AK375RM6E5FR","type":"stacker","locked":"9557000000","until":"708050"}
{"address":"SP3WXNVPY9J007AASZYYTSEWGPXJW1H1MRSC1A9NJ","type":"stacker","locked":"2495000000","until":"708050"}
{"address":"SP3XGET4RTB4W79CHDBG0VPH4J4PM9KNEW7WVE8YP","type":"stacker","locked":"30000000000","until":"708050"}
{"address":"SP3YDEH3QZFCAZWTKT5NF3MYREMNTJEDC94Z3P3SZ","type":"stacker","locked":"50948000000","until":"708050"}
{"address":"SP3Z3YSTD32DQZAD9N9P828B9Y9J4R3556TFRGN4B","type":"stacker","locked":"539000000","until":"708050"}
{"address":"SP3Z8QJH6CVGJ0JK163HZN2N9WYPZGRW1F79KD7B7","type":"stacker","locked":"450000000","until":"708050"}
{"address":"SP3ZJM0P0PRT48V9S5DX8X1BBZVX1HN0P53X3DHCJ","type":"stacker","locked":"1015000000","until":"708050"}
{"address":"SP3ZY5DBKBBXWJPSCV1G7SEMTPAGT7C659A42AF2A","type":"stacker","locked":"4427000000","until":"708050"}
{"address":"SP4GPHGXSRZRS3KP247WCHTQR3KWCVTH1SJCPFG9","type":"stacker","locked":"1150000000","until":"708050"}
{"address":"SP50KZKGN80RFXYX8CGT4B3SSNBC6CM4A65TZX8F","type":"stacker","locked":"168000000000","until":"708050"}
{"address":"SP54PT5NZ6FG8PFWXYE41QDKKS1RMJBM95G3DAT4","type":"stacker","locked":"8847000000","until":"708050"}
{"address":"SP59BTR4KAH1P6DBEN7R3JFYZ64D1D2NFWA6KA09","type":"stacker","locked":"99990000000","until":"708050"}
{"address":"SP5GPBPTA8XGKYFD6HSZZ7FZ24Z274ZKZNDR52F5","type":"stacker","locked":"1507000000","until":"708050"}
{"address":"SP5MFMXM5YGZKCH23Y5TMETED6H115VS1P12GGCV","type":"stacker","locked":"877874000000","until":"708050"}
{"address":"SP5TN2MP8EW41ECDDS9R10AZJAACV5RFBVP6PR6X","type":"stacker","locked":"10000000000","until":"708050"}
{"address":"SP661DNB6KZH6YBT1Y32NCDHNJE042ZY7B8JA9WW","type":"stacker","locked":"60867807","until":"708050"}
{"address":"SP6MQQKG8Z2B3AWWMAWNX07TZV1NJ4YAWGJGER02","type":"stacker","locked":"402020900","until":"708050"}
{"address":"SP7383KRJA9AQAY9WS1AKAPG4KAR9ERQM3586AZ3","type":"stacker","locked":"522000000","until":"708050"}
{"address":"SP779SC9CDWQVMTRXT0HZCEHSDBXCHNGG7BC1H9B","type":"stacker","locked":"420000000","until":"708050"}
{"address":"SP7RKS2TA7SF2WC67CGQTTNX4HNV5D17AT0V52VF","type":"stacker","locked":"590000000","until":"708050"}
{"address":"SP8GC9E9DG0D88C5Y0017KGKAPZY2PTF2486F1KE","type":"stacker","locked":"85848600","until":"708050"}
{"address":"SP8YV7E4J52P3ZQ37FS668GF2283VCQWS1YET8YM","type":"stacker","locked":"800000000","until":"708050"}
{"address":"SP902WD2M3X15KKGH21AGS2TXAQKWHK1WYZSSPW5","type":"stacker","locked":"205000000","until":"708050"}
{"address":"SP9AM4Q82D0PJ94GDKDSP28T5FZFYMZGAVDCH0E8","type":"stacker","locked":"4386149784","until":"708050"}
{"address":"SP9B0JGYFZ264QPTRDGEN40E6YABWZWT130HQ096","type":"stacker","locked":"83332999048","until":"708050"}
{"address":"SP9FBRFC028FW65C6CB8ZWQG2C62Z9DVQGX0DPVD","type":"stacker","locked":"20000000000","until":"708050"}
{"address":"SPAFCC0QT811JJZPXSND3R1B532E2A5PPMS0Q5DB","type":"stacker","locked":"25000000000","until":"708050"}
{"address":"SPB09CGY9D3K3X4CZQH6903J73Z9B0M7J0ZMXF3S","type":"stacker","locked":"229000000000","until":"708050"}
{"address":"SPB2VP5GVD980MERQS4J4H479RGKP1TKSF24BHTM","type":"stacker","locked":"10337618200","until":"708050"}
{"address":"SPB8AQRQEQBQJACHKA7GRQ2ET0ECMH9ZA263Q7HH","type":"stacker","locked":"289000000","until":"708050"}
{"address":"SPBAKJP8T37GHPVMV5RX2N0EDCMX79RQXPGSJSDB","type":"stacker","locked":"2114000000","until":"708050"}
{"address":"SPBRMYM12MZKGRBJWBP3VPT845FGXP58041M7H63","type":"stacker","locked":"9050000000","until":"708050"}
{"address":"SPBZ2DQK8X21XJ3DJGV4XVXDBEVWATF33VDEV4ZA","type":"stacker","locked":"1692000000","until":"708050"}
{"address":"SPC30NARAGTSQ4DEER9NM4CV7CWH2JMJZBKJ90G9","type":"stacker","locked":"99999820","until":"708050"}
{"address":"SPCAMN538MMY913N9GBVGFA7X8R77HYWH3WC9YM2","type":"stacker","locked":"2995000000","until":"708050"}
{"address":"SPCGG9JHFJDRH6BBGAR8GHPDECVAZMRZ87M1BHKV","type":"stacker","locked":"800000000","until":"708050"}
{"address":"SPD63E5WQMR9B2ART8M8HADE7WCW99B12EPSR91F","type":"stacker","locked":"1712000000","until":"708050"}
{"address":"SPDANHG1WBW18ZAKFZJCG58GXGCX8P29ENFPCD1E","type":"stacker","locked":"14027000000","until":"708050"}
{"address":"SPDGHTX6ZC90DFYCWJW8MWVWFHMF8W0TB0B49HCV","type":"stacker","locked":"450000000","until":"708050"}
{"address":"SPDGRNM9BFDXQ4XN9HANT0F7MN2Z97QKDB5ZYB5B","type":"stacker","locked":"100000000","until":"708050"}
{"address":"SPDQXZT4CDB9BCCC53CGW0G0052EQ8ZZYK04FTCM","type":"stacker","locked":"200000000","until":"708050"}
{"address":"SPF13R8KGZ8B1B841X30Y2Q6BNANB2YZC3Z6WV7X","type":"stacker","locked":"100000000","until":"708050"}
{"address":"SPFAT16GY08EJ501BZJEQESREAKWMD3QR5QSQT0B","type":"stacker","locked":"500000000","until":"708050"}
{"address":"SPFY12M55M6BJ4VRKJ58Q4N9TV0P3MPQG460N0FV","type":"stacker","locked":"100000000","until":"708050"}
{"address":"SPGMF8QX45FMB20TAN8YHNYFMZAQWWAD0X2WNX6F","type":"stacker","locked":"167000000","until":"708050"}
{"address":"SPH00JPEQVPRQ87Q3ED2MBH0CY831R5KG645Y849","type":"stacker","locked":"216399346","until":"708050"}
{"address":"SPHSCF96PYMYB7W4WZC7ZBKQ7SECN2AW8J4MNFKJ","type":"stacker","locked":"100000000","until":"708050"}
{"address":"SPJ4SME1JBZ0682X48AJYAP5FPFBVVY4BCAMSRZ4","type":"stacker","locked":"2570000000","until":"708050"}
{"address":"SPJZRVAH1CS8G973V76MS15WZ3WBABVA6YSAE3JP","type":"stacker","locked":"58480000000","until":"708050"}
{"address":"SPKN4AYXSV5VTS1KP4DWKVQMZDHQW2YKP01CP1DZ","type":"stacker","locked":"3016788600","until":"708050"}
{"address":"SPKQVJZM28WJT70G3AP7B0PA5EG4HJ8NH97JK42B","type":"stacker","locked":"4400000000","until":"708050"}
{"address":"SPM4JKECG23CJGXC93BDXX7579WVH5NR7E2XVC5H","type":"stacker","locked":"500000000","until":"708050"}
{"address":"SPM97MPV98TWEKPXS8X5FTVHXY5CJQC24X30SFJV","type":"stacker","locked":"1600000000","until":"708050"}
{"address":"SPN06A0FNBXETTYAM9GAWPNNXFH6ZDYFENMT4S21","type":"stacker","locked":"2000000000","until":"708050"}
{"address":"SPNRPD2W804W5HMNXD5RDCPF5Z5CTZZM8KCSW2ZK","type":"stacker","locked":"9869793234","until":"708050"}
{"address":"SPPW17XYT85QBZJKW6W8KZ3T014JKEAYX2VA4HCC","type":"stacker","locked":"200173858","until":"708050"}
{"address":"SPR30KK2JTWVPM9ZB3EE05H8HFDYVSHDNKVFXJ8G","type":"stacker","locked":"20976470831","until":"708050"}
{"address":"SPRSNP97S0V51DCC4HM6PVW2GNDATY3P58R1689N","type":"stacker","locked":"700000000","until":"708050"}
{"address":"SPS4H96TGHT5JFXC0NF24GHWC4W12VKSSD5B7SC1","type":"stacker","locked":"498800000","until":"708050"}
{"address":"SPSA1SNVCV3ZRE3H3E2C4ABK460F9M91S9VTCR06","type":"stacker","locked":"7990000000","until":"708050"}
{"address":"SPSDGXANQ8E2RPHQ9GG9H189ZMQ77FVJ5HDJ1859","type":"stacker","locked":"15000000000","until":"708050"}
{"address":"SPT977DSCQVH1TZB4RMB3K4C5MKHB3R1KJPR0CAX","type":"stacker","locked":"5800000000","until":"708050"}
{"address":"SPT9D276954SH8V2Q9D45MN39FP3QNA8W9JB69DZ","type":"stacker","locked":"279786875000","until":"708050"}
{"address":"SPTFVW7ZS2E0GBWFHA3SKHN1A8J4RZFGAK6MA6PB","type":"stacker","locked":"969313600","until":"708050"}
{"address":"SPTP2RCF0MQMTHT7NGX5R2N0PHC6K0AEJGW26638","type":"stacker","locked":"83332000000","until":"708050"}
{"address":"SPV34QKJRAYEM871PY5EHGTRCEV6V6HZ5NZEWFJ9","type":"stacker","locked":"25000000000","until":"708050"}
{"address":"SPVNCNJHQPB0197CM5XXSGWWPFT6KEAZ60AJRE4S","type":"stacker","locked":"1500000000","until":"708050"}
{"address":"SPVQ9A57NG0SVWV4E82K8VRJYSZ5Y7AHXP5CB4W7","type":"stacker","locked":"192617000000","until":"708050"}
{"address":"SPVWV1TG5FXE9P8JCJ7BEPD3ZVVKSS1Y1R2T7HDS","type":"stacker","locked":"250372061","until":"708050"}
{"address":"SPW4E0SYAVX4W5X6R25DDYWQX8K8W650YAT0BRZ0","type":"stacker","locked":"700000000","until":"708050"}
{"address":"SPW4KNVH5F7MVDFX1DV79DSC0TMWW90J19D6AJ3P","type":"stacker","locked":"2085000000","until":"708050"}
{"address":"SPWJ5FEYPDR89WQE88TEJBFRP9S0KMA68EY8KZDR","type":"stacker","locked":"112895087","until":"708050"}
{"address":"SPWQZKW4H5SYVTY2TTWVMHVYMKS8JM5J0FMNTGN5","type":"stacker","locked":"47207749133","until":"708050"}
{"address":"SPX5TESXN1S4M12KF4AVF8SBP3H6WE8B55EHKM4F","type":"stacker","locked":"1161784573","until":"708050"}
{"address":"SPXMBS72P8K9M8FBQHCNJT1VYYXTGSSFFFS4MGE8","type":"stacker","locked":"100000000000","until":"708050"}
{"address":"SPY3E69EHH7B21RVSWS1RHPAQMHD9Y2JH8JFXY9K","type":"stacker","locked":"924644489000","until":"708050"}
{"address":"SPYQZBR1RKVCPXAF2AYECPETEV9X6R91ZS4HH8CH","type":"stacker","locked":"5000000000","until":"708050"}
{"address":"SPYYRNV2MFB8X08D0ZJDVBNRWS5E8ZYC4FSDHC0H","type":"stacker","locked":"15000000000","until":"708050"}
{"address":"SPZ3VMYZ4CJV3ADFD0VXT6H7Y1PCCWJ3ZDQGY8FV","type":"stacker","locked":"1105000000","until":"708050"}
{"address":"SPZN4R5HNXA2PY445MMDSA2TKAGZFQ4QXG0GXG8E","type":"stacker","locked":"106725000","until":"708050"}
{"address":"SPZQMR0SB88WX6BW83PP1D5JWDAKA1ERQVX5EA2D","type":"stacker","locked":"130000000000","until":"708050"}



================================================
FILE: sips/sip-013/sip-013-semi-fungible-token-standard.md
================================================
# Preamble

SIP Number: 013

Title: Standard Trait Definition for Semi-Fungible Tokens

Author: Marvin Janssen <https://github.com/MarvinJanssen>

Consideration: Technical

Type: Standard

Status: Ratified

Created: 12 September 2021

License: CC0-1.0

Sign-off: Jude Nelson <jude@stacks.org>, Brice Dobry <brice@hiro.so>

Layer: Traits

Discussions-To: https://github.com/stacksgov/sips

# Abstract

Semi-Fungible Tokens, or SFTs, are digital assets that sit between fungible and
non-fungible tokens. Fungible tokens are directly interchangeable, can be
received, sent, and divided. Non-fungible tokens each have a unique identifier
that distinguishes them from each other. Semi-fungible tokens have both an
identifier and an amount. This SIP describes the SFT trait and provides a
reference implementation.

# License and Copyright

This SIP is made available under the terms of the Creative Commons CC0 1.0
Universal license, available at
https://creativecommons.org/publicdomain/zero/1.0/. This SIP's copyright is held
by the Stacks Open Internet Foundation.

# Introduction

Digital assets commonly fall in one of two categories; namely, they are either
fungible or non-fungible. Fungible tokens are assets like the native Stacks
Token (STX), stablecoins, and so on. Non-Fungible Tokens (NFTs) are tokens
expressed as digital artwork and other use-cases that demand them to be globally
unique. However, not all asset classes can be represented as either exclusively
fungible or non-fungible tokens. This is where semi-fungible tokens come in.

Semi-fungible tokens are a combination of the aforementioned digital asset types
in that they have both an identifier and an amount. A single semi-fungible token
class can therefore represent a multitude of digital assets within a single
contract. A user may own ten tokens of ID 1 and twenty tokens of ID 2, for
example. It effectively means that one contract can represent any combination of
fungible and non-fungible tokens.

Some real-world examples can highlight the value and use-cases of semi-fungible
tokens. People who collect trading cards or postage stamps will know that not
all of them are of equal value, although there may be more than one of a
specific kind. Video games can feature in-game items that have different
economic values compared to others. There are many more such parallels to be
found.

Semi-fungible tokens give operators the ability to create new token classes at
will. They no longer need to deploy a new contract every time new token type is
introduced. It greatly simplifies the flow for applications that require many
new tokens and token types to come into existence.

Benefits of using semi-fungible tokens:
- Art NFTs can have series and be grouped in collections.
- Games can have their in-game currencies and items easily represented.
- DeFi protocols can leverage SFTs to transfer many tokens and settle multiple
  orders at once.
- Easy bulk trades and transfers in a single contract call, saving on
  transaction fees.

# Specification

The Semi-Fungible Token trait, `sip013-semi-fungible-token-trait`, has 8
functions:

## Trait functions

### Balance

`(get-balance ((token-id uint) (who principal)) (response uint uint))`

Returns the token type balance `token-id` of a specific principal `who` as an
unsigned integer wrapped in an `ok` response. It has to respond with `u0` if the
principal does not have a balance of the specified token or if no token with
`token-id` exists. The function should never return an `err` response and is
recommended to be defined as read-only.

### Overall balance

`(get-overall-balance ((who principal)) (response uint uint))`

Returns the overall SFT balance of a specific principal `who`. This is the sum
of all the token type balances of that principal. The function has to respond
with a zero value of `u0` if the principal does not have any balance. It should
never return an `err` response and is recommended to be defined as read-only.

### Total supply

`(get-total-supply ((token-id uint)) (response uint uint))`

Returns the total supply of a token type. If the token type has no supply or
does not exist, the function should respond with `u0`. It should never return an
`err` response and is recommended to be defined as read-only.

### Overall supply

`(get-overall-supply () (response uint uint))`

Returns the overall supply of the SFT. This is the sum of all token type
supplies. The function should never return an `err` response and is recommended
to be defined as read-only.

### Decimals

`(get-decimals ((token-id uint)) (response uint uint))`

Returns the decimal places of a token type. This is purely for display reasons,
where external applications may read this value to provide a better user
experience. The ability to specify decimals for a token type can be useful for
applications that represent different kinds of assets using one SFT. For
example, a game may have an in-game currency with two decimals and a fuel
commodity expressed in litres with four decimals.

### Token URI

`(get-token-uri ((token-id uint)) (response (optional (string-ascii 256)) uint))`

Returns an optional ASCII string that is a valid URI which resolves to this
token type's metadata. These files can provide off-chain metadata about that
particular token type, like descriptions, imagery, or any other information. The
exact structure of the metadata is out of scope for this SIP. However, the
metadata file should be in JSON format and should include a `sip` property
containing a number:

```JSON
{
	"sip": 16
	// ... any other properties
}
```

Applications consuming these metadata files can base display capabilities on the
`sip` value. It should refer to a SIP number describing a JSON metadata
standard.

### Transfer

`(transfer ((token-id uint) (amount uint) (sender principal) (recipient principal)) (response bool uint))`

Transfer a token from the sender to the recipient. It is recommended to leverage
Clarity primitives like `ft-transfer?` to help safeguard users. The function
should return `(ok true)` on success or an `err` response containing an unsigned
integer on failure. The failure codes follow the existing conventions of
`stx-transfer?` and `ft-transfer?`.

| Error code | Description                                      |
|------------|--------------------------------------------------|
| `u1`       | The sender has insufficient balance.             |
| `u2`       | The sender and recipient are the same principal. |
| `u3`       | Amount is `u0`.                                  |
| `u4`       | The sender is not authorised to transfer tokens. |

Error code `u4` is broad and may be returned under different cirumstances. For
example, a token  contract with an allowance mechanism can return `(err u4)`
when the `sender` parameter has no allowance for the specified token amount or
if the sender is not equal to `tx-sender` or `contract-owner`. A token contract
without an allowance mechanism can return `(err u4)` simply when the `sender` is
not what is expected.

Since it is possible for smart contracts to own tokens, it is recommended to
check for both `tx-sender` and `contract-caller` as it allows smart contracts to
transfer tokens it owns without having to resort to using `as-contract`. Such a
guard can be constructed as follows:

```clarity
(asserts! (or (is-eq sender tx-sender) (is-eq sender contract-caller)) (err u4))
```

The `transfer` function should emit a special transfer event, as detailed in the
Events section of this document.

### Transfer with memo

`(transfer-memo ((token-id uint) (amount uint) (sender principal) (recipient principal) (memo (buff 34))) (response bool uint))`

Transfer a token from the sender to the recipient and emit a memo. This function
follows the exact same procedure as `transfer` but emits the provided memo via
`(print memo)`. The memo event should be the final event emitted by the
contract. (See also the events section of this document below.)

## Trait definition

A definition of the trait is provided below.

```clarity
(define-trait sip013-semi-fungible-token-trait
	(
		;; Get a token type balance of the passed principal.
		(get-balance (uint principal) (response uint uint))

		;; Get the total SFT balance of the passed principal.
		(get-overall-balance (principal) (response uint uint))

		;; Get the current total supply of a token type.
		(get-total-supply (uint) (response uint uint))

		;; Get the overall SFT supply.
		(get-overall-supply () (response uint uint))

		;; Get the number of decimal places of a token type.
		(get-decimals (uint) (response uint uint))

		;; Get an optional token URI that represents metadata for a specific token.
		(get-token-uri (uint) (response (optional (string-ascii 256)) uint))

		;; Transfer from one principal to another.
		(transfer (uint uint principal principal) (response bool uint))

		;; Transfer from one principal to another with a memo.
		(transfer-memo (uint uint principal principal (buff 34)) (response bool uint))
	)
)
```
## Events

Semi-fungible token contracts should emit custom events in certain situations
via `print`. These events should be emitted after any built-in token events
(such as those emitted by `ft-transfer?`) and before the memo in the case of
`transfer-memo` and `transfer-many-memo`.

| Event name           | Tuple structure                                                                                 | Description                          |
|----------------------|-------------------------------------------------------------------------------------------------|--------------------------------------|
| `sft_transfer`       | `{type: "sft_transfer", token-id: uint, amount: uint, sender: principal, recipient: principal}` | Emitted when tokens are transferred. |
| `sft_mint`           | `{type: "sft_mint", token-id: uint, amount: uint, recipient: principal}`                        | Emitted when new tokens are minted.  |
| `sft_burn`           | `{type: "sft_burn", token-id: uint, amount: uint, sender: principal}`                           | Emitted when tokens are burned.      |

## Use of native asset functions

Contract implementers should always use the built-in native assets that are
provided as Clarity primitives whenever possible. This allows clients to use
Post Conditions (explained below) and takes advantage of other benefits like
native events and asset balances. However, there are no language primitives
specific to semi-fungible tokens. The reference implementation included in this
SIP therefore leverages the primitives to the extent that Clarity allows for.

The recommended native asset primitives to use:

- `define-fungible-token`
- `ft-burn?`
- `ft-get-balance`
- `ft-get-supply`
- `ft-mint?`
- `ft-transfer?`
- `define-non-fungible-token`
- `nft-burn?`
- `nft-mint?`
- `nft-transfer?`

## Implementing in wallets and other applications

Applications that interact with semi-fungible token contracts should validate if
those contracts implement the SFT trait. If they do, then the application can
use the interface described in this SIP for making transfers and getting other
token information.

All of the functions in this trait return the `response` type, which is a
requirement of trait definitions in Clarity. However, some of these functions
should be "fail-proof", in the sense that they should never return an error. The
"fail-proof" functions are those that have been recommended as read-only. If a
contract that implements this trait returns an error for these functions, it may
be an indication of a faulty contract, and consumers of those contracts should
proceed with caution.

## Use of post conditions

The Stacks blockchain includes a feature known as Post Conditions. By defining
post conditions, users can create transactions that include pre-defined
guarantees about what might happen in a contract. These post conditions can also
be used to provide guarantees for custom fungible and non-fungible tokens that
were defined using built-in Clarity primitives.

There are no Clarity primitive counterparts for semi-fungible tokens, but
contract developers can leverage a combination of post conditions to achieve the
same result.

There are two factors that should be checked by post conditions:

1. The amount of semi-fungible tokens being transferred.
2. The token ID of the semi-fungible token being transferred.

To that end, it is recommended that developers use both Clarity primitives in
their design. Semi-fungible token contracts can achieve complete post condition
coverage by using both `define-fungible-token` and `define-non-fungible-token`.

A minimal and sufficient strategy that provides full post condition coverage is
to create a "burn-and-mint" mechanism for token creation and transfers. Such an
SFT contract tracks quantities using an internal fungible token and token IDs
using an internal non-fungible token. Since token identifiers for assets defined
by `define-non-fungible-token` need to be unique, an additional component is
added to ensure token IDs can be expressed per owner. (As SFTs may have a
quantity of a certain token ID that is larger than one.) The token ID type
identifier thus becomes `{token-id: uint, owner: principal}`. Wallet software
can then easily determine the post conditions for the amount as well as the
token ID.

An example of a burn-and-mint mechanism is provided below. The reference
implementation at the end of the document features a full SFT contract that
includes burn-and-mint.

```clarity
(define-fungible-token semi-fungible-token)
(define-non-fungible-token semi-fungible-token-id {token-id: uint, owner: principal})

(define-public (transfer (token-id uint) (amount uint) (sender principal) (recipient principal))
	(begin
		;; <guards>
		;; <token transfer logic>
		(try! (tag-nft-token-id {token-id: token-id, owner: sender}))
		(try! (tag-nft-token-id {token-id: token-id, owner: recipient}))
		;; <balance updates>
		(print {type: "sft_transfer", token-id: token-id, amount: amount, sender: sender, recipient: recipient})
		(ok true)
	)
)

(define-private (tag-nft-token-id (nft-token-id {token-id: uint, owner: principal}))
	(begin
		(and
			(is-some (nft-get-owner? semi-fungible-token-id nft-token-id))
			(try! (nft-burn? semi-fungible-token-id nft-token-id (get owner nft-token-id)))
		)
		(nft-mint? semi-fungible-token-id nft-token-id (get owner nft-token-id))
	)
)
```

## Post Condition strategies

For strategies on how to best guard a semi-fungible token contract with post
conditions, see the reference implementation included with SIP (contained in
[SIP-013-001.tar.gz](SIP-013-001.tar.gz)), or by following the link at the end
of this document.

# Optional send-many specification

SIP013 Semi-fungible tokens can also optionally implement the trait
`sip013-send-many-trait` to offer a built-in "send-many" features for bulk token
transfers. Adding this to the token contract itself may have runtime cost
benefits as of Stacks 2.0. The send-many trait contains 2 additional functions.

## Send-many functions

### Bulk transfers

`(transfer-many ((transfers (list 200 {token-id: uint, amount: uint, sender: principal, recipient: principal}))) (response bool uint))`

Transfer many tokens in one contract call. Each transfer should follow the exact
same procedure as if it were an individual `transfer` call. The whole function
call should fail with an `err` response if one of the transfers fails.

### Bulk transfers with memos

`(transfer-many-memo ((transfers (list 200 {token-id: uint, amount: uint, sender: principal, recipient: principal, memo: (buff 34)}))) (response bool uint))`

Transfer many tokens in one contract call and emit a memo for each. This
function follows the same procedure as `transfer-many` but will emit the memo
contained in the tuple after each transfer. The whole function call should fail
with an `err` response if one of the transfers fails.

## Send-many trait definition

A definition of the optional send-many trait is provided below.

```clarity
(define-trait sip013-transfer-many-trait
	(
		;; Transfer many tokens at once.
		(transfer-many ((list 200 {token-id: uint, amount: uint, sender: principal, recipient: principal})) (response bool uint))

		;; Transfer many tokens at once with memos.
		(transfer-many-memo ((list 200 {token-id: uint, amount: uint, sender: principal, recipient: principal, memo: (buff 34)})) (response bool uint))
	)
)
```

# Related work

## Ethereum ERC1155

This Semi-Fungible Token standard is similar to the
[EIP-1155](https://eips.ethereum.org/EIPS/eip-1155) standard found in the
Ethereum/EVM space. An ERC1155 token is a semi-fungible token that admits both a
token ID as well as a supply per token ID, just like SIP013. They differ in that
the ERC1155 standard describes an approval mechanism as well as "safe transfer"
functions that are specific to Ethereum/EVM. Although the biggest difference is
the requirement of post condition support, a mechanism that does not exist in
Ethereum.

# Backwards Compatibility

Not applicable.

# Trait deployments

## Mainnet

- Token trait: [SPDBEG5X8XD50SPM1JJH0E5CTXGDV5NJTKAKKR5V.sip013-semi-fungible-token-trait](https://explorer.stacks.co/txid/0x7e9d8bac5157ab0366089d00a40a2a83926314ab08807ab3efa87ebc96d9e20a?chain=mainnet)
- Send-many trait: [SPDBEG5X8XD50SPM1JJH0E5CTXGDV5NJTKAKKR5V.sip013-transfer-many-trait](https://explorer.stacks.co/txid/0x88457278a61b7e59c8a19704932eebb7b46817e0bbd3235436a1d72c956db19c?chain=mainnet)

## Testnet

- Token trait: [STDBEG5X8XD50SPM1JJH0E5CTXGDV5NJTJTTH7YB.sip013-semi-fungible-token-trait](https://explorer.stacks.co/txid/0x37e846cce0d31f34be06d969efbb6ff413308066eefffa0bf1a8669bd4be0a05?chain=testnet)
- Send-many trait: [STDBEG5X8XD50SPM1JJH0E5CTXGDV5NJTJTTH7YB.sip013-transfer-many-trait](https://explorer.stacks.co/txid/0x81ec048b187137ade2fb9519375d22ec96c271d114e79c2d44018434e9009911?chain=testnet)

# Activation

These traits will be considered activated when they are deployed to mainnet
and 3 different implementations of the main trait have been deployed to mainnet,
no later than Bitcoin block 769,950. Additionally, no revisions to the traits
were made after Bitcoin block 756,810.

# Reference Implementations

- https://github.com/MarvinJanssen/stx-semi-fungible-token



================================================
FILE: sips/sip-015/sip015-vote-main.zip
================================================
[Binary file]


================================================
FILE: sips/sip-016/sip-016-token-metadata.md
================================================
# Preamble

SIP Number: 016

Title: Schema Definition for Metadata for Digital Assets

Author: Friedger Müffke (mail@friedger.de), Dan Trevino (dantrevino@gmail.com)

Consideration: Technical

Type: Standard

Status: Ratified

Created: 7 November 2021

License: CC0-1.0

Sign-off: Jude Nelson (jude@stacks.org)

Layer: Traits

# Abstract

Non-fungible tokens - NFTs for short - are digital assets registered on
blockchain with unique identifiers and properties that distinguish them from
each other. SIP-009 defines the trait for how ownership of an NFT is managed.
Fungible tokens - FTs for short - are digital assets where each token can be
replaced by another token (see SIP-010). Semi-fungible tokens are digital assets
where each token has a unique identifier and is dividable into fungible parts
(see SIP-013). This SIP aims to provide a flexible standard to attach metadata
to NFTs, like descriptions or urls to digital files. The same standard is
applicable to fungible tokens.

# License and Copyright

This SIP is made available under the terms of the Creative Commons CC0 1.0
Universal license, available at
https://creativecommons.org/publicdomain/zero/1.0/ This SIP’s copyright is held
by the Stacks Open Internet Foundation.

# Introduction

Tokens are digital assets registered on blockchain through a smart contract. A
non-fungible token (NFT) is a token that is globally unique and can be
identified through its unique identifier. In blockchains with smart contracts,
including the Stacks blockchain, developers and users can use smart contracts to
register and interact with non-fungible tokens.

Some use cases of NFTs are name registration, digital art, certification, media
and entertainment, real-estate. They all require that users associate certain
content with an NFT. In general, it is helpful for the users to have a name,
sound, image that represents this content.

# Specification

Every SIP-016 compliant smart contract in the Stacks blockchain must implement
one or more functions that return a resolvable/retrievable URI referencing
metadata. The metadata provide information e.g. for displaying a digital asset
to users. This type of function is named "metadata URI functions".

Appendix A contains a list of trait functions that must meet the following
requirements for the return value. The appendix can be extended without changing
the ratification status of this SIP. Any changes to that appendix must be noted
in the changelog subsection.

## Return Value of Metadata URI Functions

The return value must be a `some` value if and only if the metadata reference an
existing token, otherwise the value must be `none`. Appendix A specifies the
exact meaning of "existing" for each function.

For existing tokens, the inner value of the return value must be a string
representing a resolvable URI.

The schema of the resolvable URI is not specified and should be a well-known
schema like `https`, `ar`, `ipfs`, `sia`. A `data` URI is also valid, however,
the length is limited by this SIP.

If a metadata URI function expects a parameter of type `uint` that identifies a
token and the resulting strings contain `{id}`, then the `{id}` part must be
replaced by the identifier in decimal format given in the function call.

The resolved data of the URI must be a JSON blob.

## JSON scheme of Metadata

The JSON blob resolved through the URI must follow the following JSON schema.

If metadata were retrieved by a function call containing a token identifier and
the string `{id}` exists in any JSON value, it MUST be replaced with the actual
token id in decimal format, by all client software that follows this standard.

```
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Token Metadata",
    "type": "object",
    "required": ["sip", "name"],
    "properties": {
        "sip": {
            "type": "number",
            "description": "SIP number that defines the JSON schema for metadata. For this SIP, the sip number must be `16`."
        },
        "name": {
            "type": "string",
            "description": "Identifies the asset which this token represents"
        },
        "description": {
            "type": "string",
            "description": "Describes the asset which this token represents"
        },
        "image": {
            "type": "string",
            "description": "A URI pointing to a resource with MIME type image/* representing the asset to which this token represents. Consider making any images at a width between 320 and 1080 pixels and aspect ratio between 1.91:1 and 4:5 inclusive. If the token represents a media file of different MIME type or of higher quality defined in property 'raw_media_file_uri', then this image should be used as preview image like a cover for music, or an low-res image."
        },
        "attributes": {
            "type": "array",
            "description": "Additional attributes of the token that are \"observable\". See section below. Values may be strings, numbers, object or arrays.",
            "items": {
                "type": "object",
                "required": ["trait_type", "value"],
                "properties": {
                    "display_type": {"type": "string"},
                    "trait_type": {"type": "string"},
                    "value": {"anyOf": [{"type": "object"}, {"type": "string"}, {"type": "number"}, {"type": "integer"}, {"type": "boolean"}, {"type": "array"}]}
                }
            }
        },
        "properties": {
            "type": "object",
            "description": "Additional other properties of the token. See section below. Values may be strings, numbers, object or arrays."
        },
        "localization": {
            "type": "object",
            "required": ["uri", "default", "locales"],
            "properties": {
                "uri": {
                    "type": "string",
                    "description": "The URI pattern to fetch localized data from. This URI should contain the substring `{locale}` which will be replaced with the appropriate locale value before sending the request. See section about localization for more rules"
                },
                "default": {
                    "type": "string",
                    "description": "The locale of the default data within the base JSON"
                },
                "locales": {
                    "type": "array",
                    "description": "The list of locales for which data is available. These locales should conform to those defined in the Unicode Common Locale Data Repository (http://cldr.unicode.org/)."
                }
            }
        },
        "image_data": {
            "type": "string",
            "description": "Raw SVG image data. Deprecated. Use `properties.image_data`."
        },
        "external_url": {
            "type": "string",
            "description": "Url to view the item on a 3rd party web site. Deprecated. Use `properties.external_url`."
        },
        "animation_url": {
            "type": "string",
            "description": "URL to a multi-media attachment for the item. Deprecated. Use `properties.animation_url`."
        }
    }
}
```

The length of string values is not restricted. Nowadays, clients should be smart
enough to deal with values of different lengths. Note, that the [sitemap
protocol](https://www.sitemaps.org/protocol.html) and many search engines
support only URLs with less than 2048 characters.

### Example

token101.json

```
{
  "sip": 16,
  "name": "Foo #101",
  "image": "ipfs://somerandomecid",
  "attributes": [
     {
      "trait_type": "hair",
      "value": "red",
    },
    {
      "trait_type": "strength",
      "display_type": "number",
      "value": 99,
    },
  ],
  "properties": {
      "collection":  "Foo Collection",
      "total_supply":  "10000"
  },
  "localization": {
      "uri": "ipfs://somerandomcid/{locale}.json",
      "default": "en",
      "locales": ["en", "pt-BR", "de"]
  }
}
```

de.json

```
{
    "sip": 16,
    "attributes: [
        {
          "trait_type": "Haare",
          "value": "rot",
        },
        {
          "trait_type": "Stärke",
          "display_type": "number",
          "value": 99,
        },
    ]
}
```

pt-BR.json

```
{
    "sip": 16,
    "attributes: [
        {
          "trait_type": "cabelos",
          "value": "vermelho",
        },
        {
          "trait_type": "força",
          "display_type": "number",
          "value": 99,
        },
    ]
}
```

### Properties

Common properties of tokens are described in appendix C. Properties of type
`object` are usually described using the following schema:

```
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Token Metadata Property",
    "type": "object",
    "required": [],
    "properties": {
        "type": {
            "type": "string",
            "description": "type of the property"
        },
        "description": {
            "type": "string",
            "description": "description of the property"
        },
        "value": {
            "type": {"oneOf": [{"type": "object"}, {"type": "string"}, {"type": "number"}, {"type": "integer"}, {"type": "boolean"} {"type: "array"}},
            "description": "value of the property"
        }
    }
}
```

Example:

```
{
    "type": "string",
    "description": "Address of custodian key holder",
    "value": "Casa Inc., P.O. Box 20575, Charleston, S.C. 29413, United States."
}
```

### Attributes

Attributes describe additional elements of tokens that are "observable", usually
represented in the associated image or digital asset of the token. In contrast,
`properties` describe elements of tokens that are more abstract and not visible
in the associated image of the token.

Images of NFTs often have a limited set of traits and each trait has a limited
number of possible values. These values are represented as attributes in the
metadata. They can be used to calculate a score for each NFT in the collection
that could define the rarity of the NFT.

An `attribute` consists of a `trait_type` defining the name of the trait, e.g.
"hair". The `value` is the value of the trait, e.g. "red". The `display_type` is
a field indicating how the trait value should be displayed, e.g. on a
marketplace. If `display_type` is omitted, then `string` is used as default
display type.

Appendix B describes the possible types and display types of attributes.

## Localization

The localized data follow the same JSON schema with property `sip` as required
and all other properties as optional.

The localized data overwrite data provided in the default metadata JSON. The
localized data can provide only partial data.

An array of localized `attributes` overwrites the whole list of default
`attributes`.

A localized properties with partial data overwrites only the provided
properties; the remaining default properties remain as default values.

# Using metadata in applications

An application like a marketplace uses metadata to present tokens to users.
Before doing so, application developers should verify whether the metadata is
compliant with their own application's guidelines, e.g. forbidding bad language
in names or unsuitable images.

We remind implementation authors that the empty string for the token URI is a
valid response. We also remind everyone that any smart contract can use the same
metadata as other NFT contracts. It is out of the scope of this standard to
define how a client may determine which smart contracts are the original,
well-known, canonical ones.

## Graphical representation

The metadata of a token contain several properties that can be used to visually
represent the token. It is recommended to consider the first defined property of
the following ordered list:

1. `image`
2. `properties.image_data`
3. `image_data`

A rich representation should use the first defined property of the following
list:

1. `properties.animation_url`
2. `animation_url`

# Out of Scope

Accessiblity of content is not covered by the standard.

Properties other than resolvability of the token URI are out of scope. This
implies that metadata might change over time (stability).

# Metadata functions

Some contracts have dedicated functions to provide some metadata directly
without resolving the token URI. This is usually necessary, if other contracts
need to use the token metadata. This SIP does not define signatures for these
functions.

Examples of contracts with metadata functions are listed below:

**Boom**

The [NFT contract for
Boom](https://explorer.stacks.co/txid/0x423d113e14791f5d60f5efbee19bbb05cf5e68d84bcec4e611f2c783b08d05aa?chain=mainnet)
implements a variation of this trait using similar naming, but returning other
types than response types.

The function signatures for metadata are:

- `(get-boom-meta () {uri: (string-ascii 35), name: (string-ascii 16),
  mime-type: (string-ascii 9)})` and
- `(get-meta? uint {series-id: uint, number: uint, name: (string-utf8 80), uri:
  (string-ascii 2048), mime-type: (string-ascii 129), hash: (buff 64)})`

**Badges**

The [badges
contract](https://explorer.stacks.co/txid/0xb874ddbb4a602c22bb5647c7a2f8bfcafbbca7c0c663a175f2270ef3665f33de?chain=mainnet)
defines metadata for nfts.

The function signatures for metadata are:

- `(get-badge-meta () {uri: (string-ascii 78111)})` and
- `(get-meta? (uint) (optional {user: principal}))`

# Backwards Compatibility

This SIP defines metadata so that metadata for existing NFTs on other
blockchains like Ethereum, Solana or WAX can be re-used for NFTs on the Stacks
blockchain.

# Related Work

NFTs are an established asset class on blockchains. Read for example
[here](https://www.ledger.com/academy/what-are-nft).

## BNS

The Blockchain Naming System uses native non-fungible tokens. It does define
metadata for a name through attachements. The schema for names owned by a person
follows the definition of (schema.org/Person)[https://schema.org/Person]. This
could be an alternative to token URIs.

## EIP 721 and 1155

Metadata for NFTs on Ethereum are defined in [EIP
721](https://eips.ethereum.org/EIPS/eip-721) and [EIP
1155](https://eips.ethereum.org/EIPS/eip-1155). The JSON schema for SIP-016 has
adopted the EIP 1155 schema with the following differences:

- substitution of `{id}` strings must use the decimal format not the hexdecimal,
  zero-padded format.

- properties of type object should use property `value` for the value, not
  property `description` as used by some EIP-1155 NFTs.

## Metaplex

The tool suite Metaplex for NFTs on Solana defines a [JSON
schema](https://docs.metaplex.com/nft-standard#uri-json-schema). The properties
`category` and `files` in Appendic C were inspired by that schema.

## Hedera

Hedera follows the same schema defined in
[H-10](https://github.com/hashgraph/hedera-improvement-proposal/blob/master/HIP/hip-10.md).

# Activation

This SIP is activated if 10 contracts are deployed that follows this
specification. This must happen before Bitcoin tip #750,000.

# Appendix A

List of trait function define in SIPs and specifications specific to these
functions

| SIP and Trait Function Name                            | Definition of "existing"                                                                        | Additional Specification for Properties                                                                                                                                                                                    | Identifier Parameter |
| ------------------------------------------------------ | ----------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- |
| SIP-009 nft-trait.get-token-uri                        | token must be minted and not burnt                                                              | NFTs belonging to a group of tokens should use property `properties.collection` of type `string` for the collection name. <br/> Optional property `properties.id` of type `integer` describes the identifier of the token. | 1st                  |
| SIP-016 get-contract-uri                               | always                                                                                          | `properties.items` of type array can be used to provide the metadata of all tokens belonging to the collection                                                                                                             | X                    |
| SIP-010 ft-trait.get-token-uri                         | always                                                                                          | The required property `decimals` of type `integer` must be the same number as `get-decimals`.                                                                                                                              | X                    |
| SIP-013 sip013-semi-fungible-token-trait.get-token-uri | token must be minted and not burnt, no requirements on the number of fungible part of the token |                                                                                                                                                                                                                            | 1st                  |

# Appendix B

Attribute types

| Type    | Display types                                | Additional Properties | Comment                  |
| ------- | -------------------------------------------- | --------------------- | ------------------------ |
| Numeric | `number`, `boost_percentage`, `boost_number` | `max_value`           |                          |
| Date    | `date`                                       |                       | As unix timestamp in UTC |
| String  | empty                                        |                       |                          |

# Appendic C

Common Properties with predefined types.

| Name                            | Type      | Description                                                                                                                                                                                                                                                                                                                                                         |
| ------------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `animation_url`                 | `string`  | url to a multi-media attachment for the item. Application might use this to display the token in a richer way than the image of the `image` property. Application might support media types like GLTF, GLB, WEBM, MP4, M4V, OGV, and OGG, MP3, WAV, and OGA as well as HTML. The query `?ext={file_extension}` can be used to provide information on the file type. |
| `artist_name`                   | `string`  | name of the artist, mainly used as attribution.                                                                                                                                                                                                                                                                                                                     |
| `category`                      | `string`  | category of the associated media file, e.g. `image`, `video`, `audio`, `vr`, `html`.                                                                                                                                                                                                                                                                                |
| `collection`                    | `string`  | collection name the token belongs to. See also Appendix A.                                                                                                                                                                                                                                                                                                          |
| `collection_image`              | `string`  | url to an image representing the collection.                                                                                                                                                                                                                                                                                                                        |
| `created`                       | `integer` | creation date of the token in unix timestamp                                                                                                                                                                                                                                                                                                                        |
| `creators`                      | `array`   | list of creators and their shares, represented as `{address: string, share: integer}`. Shares are represented as percentage. The sum of shares of all creators must add up to 100. Shares can be used to define royalties.                                                                                                                                          |
| `decimals`                      | `integer` | number of decimals. See also Appendix A.                                                                                                                                                                                                                                                                                                                            |
| `external_url`                  | `string`  | url that will view the token on an external site                                                                                                                                                                                                                                                                                                                    |
| `files`                         | `array`   | list of all associated files, represented as `{uri: string, type: string, signature: string, signature_type: string}`.                                                                                                                                                                                                                                              |
| `id`                            | `integer` | identifier for NFTs. See also Appendix A.                                                                                                                                                                                                                                                                                                                           |
| `image_data`                    | `string`  | raw SVG image data.                                                                                                                                                                                                                                                                                                                                                 |
| `ip_document_uri`               | `string`  | link to document about intellectual property (IP) rights                                                                                                                                                                                                                                                                                                            |
| `raw_media_file_signature`      | `string`  | signature of the media file represented by the token                                                                                                                                                                                                                                                                                                                |
| `raw_media_file_signature_type` | `string`  | signature type of the media represented by the token, e.g. SHA-256                                                                                                                                                                                                                                                                                                  |
| `raw_media_file_type`           | `string`  | MIME type of the media represented by the token                                                                                                                                                                                                                                                                                                                     |
| `raw_media_file_uri`            | `string`  | uri of the media represented by the token                                                                                                                                                                                                                                                                                                                           |
| `seed`                          | `string`  | a string representing of the uniqueness of the NFT, like a DNA. The seed is usually stored on-chain, but it might be contained in this metadata for convenience.                                                                                                                                                                                                                              |
| `symbol`                        | `string`  | token symbol                                                                                                                                                                                                                                                                                                                                                        |
| `total_supply`                  | `integer` | number of total supply, e.g. minted tokens                                                                                                                                                                                                                                                                                                                          |



================================================
FILE: sips/sip-018/sip-018-signed-structured-data.md
================================================
# Preamble

SIP Number: 018

Title: Signed Structured Data

Author: Marvin Janssen <https://github.com/MarvinJanssen>

Consideration: Technical

Type: Standard

Status: Ratified

Created: 28 December 2021

License: CC0-1.0

Sign-off: Jude Nelson <jude@stacks.org>

Layer: Applications

Discussions-To: https://github.com/stacksgov/sips

# Abstract

The Signed Structured Data specification describes a standard way to
deterministically encode and sign Structured Data. Structured Data is data that
can be represented in human-readable format and used in applications and smart
contracts. The aim of the standard is to produce signatures that are
straightforward and inexpensive to verify by smart contracts.

# License and Copyright

This SIP is made available under the terms of the Creative Commons CC0 1.0
Universal license, available at
https://creativecommons.org/publicdomain/zero/1.0/ This SIP's copyright is held
by the Stacks Open Internet Foundation.

# Introduction

Digital signatures are at the heart of blockchains. They allow users to transfer
assets, invoke smart contracts and more, without a designated trusted third
party. To perform these actions, a user signs a transaction and broadcasts it to
the network. However, there are situations in which it is desirable to produce
signed messages that are not transactions. A few common use-cases include:

1. prove to an external application or entity that a user is in control of an
   address;
2. authorise an action to be performed by a smart contract at a later stage
   (like a meta transaction, see below);
3. participate in an off-chain mechanism that is later settled on-chain.

It is important that signed messages are understandable for humans. For
transactions, this is obvious: wallet applications display whom is receiving how
many tokens of what kind. Likewise, the input parameters, function name, and
target contract of contract calls are properly listed. Signed messages that are
not transactions should be no different.

The language properties of Clarity make producing and verifying such signed
messages intuitive. The specification therefore leverages existing standards and
encoding schemes. Messages are represented as native Clarity values and encoded
in wire format in preparation for signing. It also makes sure that these signed
messages are chain and application specific. There is a focus on ease of
verification on the smart contract level.

Below is an example of what a wallet application could show when signing a
SIP018 message.

![Wallet SIP018 concept](SIP-018-001.png)

# Specification

The challenge lies in producing messages that are both meaningful to humans as
well as easy to be processed on-chain. Luckily, Clarity is a strongly-typed
interpreted language. Structured Data is therefore a Clarity Value expression as
detailed in _[SIP002: Smart Contract Language
](https://github.com/stacksgov/sips/blob/main/sips/sip-002/sip-002-smart-contract-language.md)_.
These value expressions are encoded in Stacks wire format, as detailed in
_[SIP005: Blocks and Transactions](https://github.com/stacksgov/sips/blob/main/sips/sip-005/sip-005-blocks-and-transactions.md)_,
and then hashed with SHA256. The resulting hash is used as the input for
signing.

## Definitions

_Clarity Value_: a native Clarity value as expressed in _[SIP002: Smart Contract
Language](https://github.com/stacksgov/sips/blob/main/sips/sip-002/sip-002-smart-contract-language.md)_.

_Meta Transaction_: a meta transaction can be understood of as a transaction
that contains another "transaction". For example, a user may sign a message
that, when received by a particular smart contract, causes it to transfer
tokens. A transaction carrying the signed message will then trigger the
underlying action when it is broadcast.

_SHA256_: a cryptographic hash function producing hashes with a length of 32
bytes.

_Signature_: a proof produced by a signing algorithm, in this case ECDSA with
the `secp256k1` curve, encoded in RSV order.

_Structured Data_: A structured representation of a message to sign expressed as
a Clarity Value.

_Wire format_: the underlying encoding for Clarity Values when generating a
transaction, as expressed in _[SIP005: Blocks and Transactions
](https://github.com/stacksgov/sips/blob/main/sips/sip-005/sip-005-blocks-and-transactions.md)_.

## Formal specification

To obtain a signature _S_ of structured data _D_ using private key _K_:

- `S = signStructuredData(D, K)`; where,

- `signStructuredData(D, K) = sign(messageHash(D), K)`; where `sign` produces a
  `secp256k1` signature of a message hash using private key _K_; and,

- `messageHash(D) = sha256(structuredDataPrefix || domainHash || structuredDataHash(D))`;
  where `structuredDataPrefix` is a static value of `"\x53\x49\x50\x30\x31\x38"`
  (which spells "SIP018" in ASCII), and `domainHash` and `structuredDataHash`
  are as described below.

**Definition of** `domainHash`

The domain hash ensures that messages are chain and application specific. A
`domainHash` is generated out of a `domain` Clarity Value:

- `domainHash = structuredDataHash(domain)` where `structuredDataHash` and
  `domain` are as described below.

**Definition of** `structuredDataHash`

The `structuredDataHash` function calculates a hash _H_ of the input Clarity
Value _D_.

- `H = structuredDataHash(D)`; where,
- `structuredDataHash(D) = sha256(ToCVWireFormat(D))`; where `ToCVWireFormat` is
  a function that encodes an input Clarity Value to its wire format
  representation as described in
  _[SIP005](https://github.com/stacksgov/sips/blob/main/sips/sip-005/sip-005-blocks-and-transactions.md)_.

**Definition of** `domain`

The `domain` is a `tuple` type Clarity Value that represents the domain in which
messages are signed. Its Clarity type definition is as follows:

```clarity
{
	name: (string-ascii len)
	version: (string-ascii len)
	chain-id: uint
}
```

`name` contains a readable application name for which Structured Data is being
signed.

`version` contains a string representation of the application version. The
application developer may choose to change this value to ensure that signed
Structured Data of one version of the application is incompatible with another
version.

`chain-id` contains the ID of the chain the Signed Structured Data is targeting.

The length `len` of the string fields are not important as long as the resulting
`domain` Clarity Value does not exceed the permitted maximum length. It is
encouraged that wallet applications display this information to the user. Other
fields may be added per the discretion of the application developer. For
example, another differentiating field may be a `verifying-contract` that
contains the principal of the contract performing the signature validation.

**Definition of Structured Data**

Structured Data can be any valid Clarity Value. It is assumed that it will
usually take the form of a `tuple` type, as it allows for multiple fields with
readable names to be encoded. The standard does permit it to be another type to
remain flexible. Still, developers should consider the informational content of
requesting a user to sign a simple type like a `principal`, `int`, `uint`, or
`bool`. A tuple can of course contain any type.

A future SIP may define standard types of Structured Data.

## Collisions and replay attacks

Structured Data hashes do not collide with _presign-sighashes_ as currently no
Clarity Value in wire format forms a valid Stacks transaction. Furthermore, the
`0x534950303138` byte prefix ensures that the input always differs in the first
six bytes, as Stacks transactions start with a version byte of `0x00` (mainnet)
or `0x80` (testnet), a four byte chain ID, and end with an authorisation type
that must be `0x04` or `0x05` in order to be valid. A Clarity Value in wire
format starts with a byte in the range of `[0x00, 0x0C]`. The prefix is easy to
remember because it spells "SIP018" in ASCII.

Replay attacks across applications, forks, and other signature-compatible chains
are mitigated by prepending a `domainHash` to the `messageHash`. A `domainHash`
is calculated by hashing a `domain` Clarity Value tuple containing the
application name, version, and chain ID.

This SIP is about signing and verifying application and chain-specific
structured data. Replay protection on the application level is out of scope for
the standard. Application developers need to make sure that their applications
behave properly when they receive the same signed structured data more than
once.

## TypeScript implementation

A reference implementation using `stacks.js` is as follows. The
`signStructuredData` function takes `StacksPrivateKey` and a `ClarityValue` and
will return a buffer of length `65` containing the signature in RSV order.

```ts
import {
  ClarityValue,
  serializeCV,
  signWithKey,
  StacksPrivateKey,
  stringAsciiCV,
  tupleCV,
  uintCV,
} from "@stacks/transactions";
import { createHash } from "crypto";

const structuredDataPrefix = Buffer.from([0x53, 0x49, 0x50, 0x30, 0x31, 0x38]);

const chainIds = {
  mainnet: 1,
  testnet: 2147483648,
};

function sha256(data: Buffer): Buffer {
  return createHash("sha256").update(data).digest();
}

function structuredDataHash(structuredData: ClarityValue): Buffer {
  return sha256(serializeCV(structuredData));
}

const domainHash = structuredDataHash(tupleCV({
  "name": stringAsciiCV("Dapp Name"),
  "version": stringAsciiCV("1.0.0"),
  "chain-id": uintCV(chainIds.mainnet),
}));

function signStructuredData(
  privateKey: StacksPrivateKey,
  structuredData: ClarityValue,
): Buffer {
  const messageHash = structuredDataHash(structuredData);
  const input = sha256(
    Buffer.concat([structuredDataPrefix, domainHash, messageHash]),
  );
  const data = signWithKey(privateKey, input.toString("hex")).data;
  return Buffer.from(data.slice(2) + data.slice(0, 2), "hex");
}
```

## Clarity implementation

Verifying signed Structured Data on Stacks 2.1 requires only minimal code. As
the Structured Data itself is application-specific, it is left out of this
reference. The `verify-signed-structured-data` function takes a structured data
hash, a signature, and a signer, and returns `true` or `false` depending on
whether the signature is valid.

```clarity
(define-constant chain-id u1)
(define-constant structured-data-prefix 0x534950303138)

(define-constant message-domain-hash (sha256 (to-consensus-buff
	{
		name: "Dapp Name",
		version: "1.0.0",
		chain-id: chain-id
	}
)))

(define-constant structured-data-header (concat structured-data-prefix message-domain-hash))

(define-read-only (verify-signature (hash (buff 32)) (signature (buff 65)) (signer principal))
	(is-eq (principal-of? (unwrap! (secp256k1-recover? hash signature) false)) (ok signer))
)

(define-read-only (verify-signed-structured-data (structured-data-hash (buff 32)) (signature (buff 65)) (signer principal))
	(verify-signature (sha256 (concat structured-data-header structured-data-hash)) signature signer)
)
```

# Related work

- [EIP712](https://eips.ethereum.org/EIPS/eip-712) is a standard in Ethereum
  (and adopted by other EVM-compatible chains) describing a similar mechanism
  that enables signing of structured data. Some aspects of this SIP were loosely
  inspired by the standard.
- [EIP191](https://eips.ethereum.org/EIPS/eip-191) now describes various signing
  schemes used in the EVM space. When `personal_sign` was introduced, it allowed
  users to sign data without running the risk of inadvertently signing a
  transaction by adding a prefix to the message. The authors were inspired by
  Bitcoin and thus settled on a message structure of
  `<varint_prefix_length><prefix><varint_message_length><message>`. For
  Ethereum, it effectively took the form of `\x19Ethereum Signed Message:\n`,
  followed by the message length, followed by the message. The `\x19` byte
  correctly encodes the prefix length, which is `25`. However, the message
  length was [mistakenly](https://github.com/ethereum/go-ethereum/issues/14794)
  encoded as an ASCII string and not an actual `varint`. It makes verifying
  messages signed with `personal_sign` needlessly expensive on-chain, as the
  message byte length has to be converted to an ASCII string representation
  before the message hash can be obtained. What is more, the messages signed
  with `personal_sign` do not have a predefined structure which makes it very
  difficult for wallet applications to display them properly.
  [MetaMask](https://docs.metamask.io/guide/signing-data.html#a-brief-history),
  a popular EVM browser wallet extension, assesses if a message passed to
  `personal_sign` is valid UTF-8, and will display it as human-readable text if
  so. Otherwise, it converts the message to a hex string and displays that
  instead. Complex messages cannot be meaningfully expressed in UTF-8 whilst
  still allowing smart contracts to process them efficiently. Applications
  developers thus often resorted to requesting users to sign hashes of complex
  messages, making the data being signed completely opaque to the user.
  Considering these problems and Clarity's inherent readability, there is no
  reason for there to ever be a `personal_sign` equivalent in Stacks.

# Backwards Compatibility

Not applicable

# Activation

This SIP will be considered activated if the following two conditions are met:

1. `to-consensus-buff` or equivalent functionality is added to Stacks 2.1.
2. At least one popular wallet application implements the standard before or
   within one year of the launch of Stacks 2.1.

# Reference Implementations

- https://github.com/MarvinJanssen/stx-signed-structured-data

# Test vectors

## Structured data hashing

Using `structuredDataHash(CV)` with an input Clarity Value.

- CV = `asciiCV("Hello World")`:
  `5297eef9765c466d945ad1cb2c81b30b9fed6c165575dc9226e9edf78b8cd9e8`
- CV = `asciiCV("")` (empty string):
  `3c8f1b104592e3ebb2b2602b3979a27e77f586fb4c655369fa4eccb6d545a0f8`
- CV =
  `tupleCV({"name": asciiCV("Test App"), "version": asciiCV("1.0.0"), "chain-id": uintCV(1)})`
  (domain tuple):
  `2538b5dc06c5ae2f11549261d7ae174d9f77a55a92b00f330884695497be5065`

## Message hashing

Using `messageHash(CV)`, which is
`sha256(Prefix || structuredDataHash(Domain) || structuredDataHash(CV))`.

- Prefix = `0x534950303138` (constant value)
- Domain =
  `tupleCV({"name": asciiCV("Test App"), "version": asciiCV("1.0.0"), "chain-id": uintCV(1)})`
- CV = `asciiCV("Hello World")`
- Message hash:
  `1bfdab6d4158313ce34073fbb8d6b0fc32c154d439def12247a0f44bb2225259`

## Message signing

Using the following parameters:

- Private key =
  `753b7cc01a1a2e86221266a154af739463fce51219d97e4f856cd7200c3bd2a601`
- Corresponding public key =
  `0390a5cac7c33fda49f70bc1b0866fa0ba7a9440d9de647fecb8132ceb76a94dfa`
- Corresponding address: `ST1PQHQKV0RJXZFY1DGX8MNSNYVE3VGZJSRTPGZGM`

And the following inputs to obtain the message hash for signing:

- Domain =
  `tupleCV({"name": asciiCV("Test App"), "version": asciiCV("1.0.0"), "chain-id": uintCV(1)})`
- CV = `asciiCV("Hello World")`
- (Message hash:
  `1bfdab6d4158313ce34073fbb8d6b0fc32c154d439def12247a0f44bb2225259`)

Produces the following signature:

- `8b94e45701d857c9f1d1d70e8b2ca076045dae4920fb0160be0642a68cd78de072ab527b5c5277a593baeb2a8b657c216b99f7abb5d14af35b4bf12ba6460ba401`

Which can be verified in Clarity:

```clarity
(secp256k1-verify 0x1bfdab6d4158313ce34073fbb8d6b0fc32c154d439def12247a0f44bb2225259 0x8b94e45701d857c9f1d1d70e8b2ca076045dae4920fb0160be0642a68cd78de072ab527b5c5277a593baeb2a8b657c216b99f7abb5d14af35b4bf12ba6460ba401 0x0390a5cac7c33fda49f70bc1b0866fa0ba7a9440d9de647fecb8132ceb76a94dfa)
true
```



================================================
FILE: sips/sip-019/sip-019-token-metadata-update-notifications.md
================================================
# Preamble

SIP Number: 019

Title: Notifications for Token Metadata Updates

Author: Rafael Cárdenas (rafael@hiro.so), Matthew Little (matt@hiro.so)

Consideration: Technical

Type: Standard

Status: Ratified

Created: 17 May 2022

License: GPL-3.0

Sign-off: Jude Nelson (jude@stacks.org), Aaron Blankstein (aaron@hiro.so), Marvin Janssen (http://github.com/MarvinJanssen)

Layer: Traits

# Abstract

As the use of tokens (fungible and non-fungible) has grown in popularity, Stacks developers have
found novel ways to define and use metadata to describe them. This rich data is commonly cached and
indexed for future use in applications such as marketplaces, statistics aggregators, and developer
tools like the [Stacks Blockchain API](https://github.com/hirosystems/stacks-blockchain-api).

Occasionally, however, this metadata needs to change for a number of reasons: artwork reveals, media
storage migrations, branding updates, etc. As of today, these changes do not have a standardized way
of being propagated through the network for indexers to refresh their cache, so the display of stale
metadata is a very common problem.

This SIP aims to define a simple mechanism for developers to notify the Stacks network when metadata
for a token has changed, so interested parties can refresh their cache and display up-to-date
information in their applications.

# Introduction

Smart contracts that declare NFTs, FTs and SFTs conform to a standard set of traits used to describe
each token (see [SIP-009](../sip-009/sip-009-nft-standard.md),
[SIP-010](../sip-010/sip-010-fungible-token-standard.md) and
[SIP-013](https://github.com/stacksgov/sips/blob/main/sips/sip-013/sip-013-semi-fungible-token-standard.md)).
One of these traits is `get-token-uri`, which should return a URI string that resolves to a token's
metadata usually in the form of a JSON file. There is currently no defined structure for this data,
and it is not considered to be immutable.

To illustrate a common use of `get-token-uri`, we'll look at the
[`SPSCWDV3RKV5ZRN1FQD84YE1NQFEDJ9R1F4DYQ11.newyorkcitycoin-token-v2`](https://explorer.stacks.co/txid/0x969192220b1c478ef9d18d1cd413d7c79fe02937a9b33af63d441bd5519d1715?chain=mainnet)
contract which declares the NewYorkCityCoin fungible token.

At the time of writing, the value returned by this contract for `get-token-uri` is the string:
```
"https://cdn.citycoins.co/metadata/newyorkcitycoin.json"
```
When this URI is resolved, it returns a JSON file with the following metadata:
```json
{
  "name": "NewYorkCityCoin",
  "description": "A CityCoin for New York City, ticker is NYC, Stack it to earn Stacks (STX)",
  "image": "https://cdn.citycoins.co/logos/newyorkcitycoin.png"
}
```
Even though the URI string is fixed, this file lives off-chain so it is conceivable that its
contents could change at any point in the future. Additionally, this contract includes a way for its
owners to change this URI via a `var-set` function call:

```clarity
(define-data-var tokenUri (optional (string-utf8 256)) (some u"https://cdn.citycoins.co/metadata/newyorkcitycoin.json"))

;; set token URI to new value, only accessible by Auth
(define-public (set-token-uri (newUri (optional (string-utf8 256))))
  (begin
    (asserts! (is-authorized-auth) ERR_UNAUTHORIZED)
    (ok (var-set tokenUri newUri))
  )
)
```

This setup is very flexible for administrators, but it creates a complex problem for metadata
indexers which now need to figure out if (and when) they should re-index token contracts to avoid
displaying stale metadata in their applications.


## Metadata staleness

Within the Stacks ecosystem, there are a number of applications that need to index token metadata
and struggle with specific challenges caused by changed metadata. For example:

* An NFT marketplace, which needs to display a token's artwork for users to view.
  * Presenting a token's icon correctly is difficult given that the `get-token-uri` on-chain
    variable could change, the off-chain JSON file could change, and/or the image served by the URL
    could change.
* A [blockchain API](https://github.com/hirosystems/stacks-blockchain-api), which needs to serve FT
metadata to return account balances correctly.
  * Wallets require the on-chain decimals value in order to correctly send and receive tokens.
    Critical balance draining is possible when this property is zero at contract launch but updated
    later.

For indexing, developers usually run and maintain a background process that listens for new token
contracts deployed to the blockchain so they can immediately call on their metadata to save the
results. This works for new contracts, but it is insufficient for old ones that may change their
metadata after it has been processed.

To avoid staleness, some indexers resort to a cron-like periodic refresh of all tracked contracts,
but while this may work for individual applications, it does not provide a consistent experience for
Stacks users that may interact with different metadata-aware systems with different refresh periods.
This workaround also adds unnecessary network traffic and creates extra strain on public Stacks
nodes due to aggressively polling contract-read RPC endpoints.

## Metadata update notifications

To solve this problem reliably, contract administrators need a way to notify the network when they
have made changes to the metadata so any indexers may then perform a refresh just for that contract.

The proposed mechanism for these notifications leverages the [`print` Clarity
language function](https://docs.stacks.co/write-smart-contracts/language-functions#print). When
used, its output is bundled inside an event of type `contract_event`:

```json
{
  "type": "contract_event",
  "contract_event": {
    "contract_identifier": "<emitter contract>",
    "topic": "print",
    "value": "<print output>"
  }
}
```

This event is then attached to a transaction object and broadcasted when the same transaction is
included in a block or microblock.

This SIP proposes a standard message structure (similar to a notification payload) that would be
used through `print`. Existing metadata indexers would receive this event through the [Stacks node
event-emitter
interface](https://github.com/stacks-network/stacks-blockchain/blob/master/docs/event-dispatcher.md#post-new_block),
parse and validate its contents, and refresh any contracts that were updated. `print` was also
selected for the following reasons:

1. There is precedent for the use of `print` notifications in the Stacks ecosystem: the BNS
contract, for example, uses it to notify the network when a change to a name or its zonefile has
occurred. The PoX-2 contract for Stacks 2.1 will make heavy use of it to record stacking state
changes across addresses. This SIP aims to continue this trend.
1. For chain indexers, consuming it is practically free if they already process transactions. This
would enable, for example, a notification to be clearly displayed in the Stacks Explorer alongside
its transaction.
1. Adding a `print` notification to a function's Clarity code also serves as self-explanatory
   documentation.
1. If there is a new notification use case in the future, a newer SIP can propose an additional
   `print` structure and indexers would be quick to adopt these if they need to. See [Notification
   structure reusability](#notification-structure-reusability).

# Specification

Notification messages for each token class are specified below. Token metadata update notifications
must be made via a contract call transaction to the [deployed reference
contract](https://explorer.stacks.co/txid/0xe92af2ea5c11e2e6fde4d31fd394de888070efff23bffad04465c549543abfa2?chain=mainnet)
or from a call to `print` within any other contract, including the token contract itself.

## Fungible Tokens

When a contract needs to notify the network that metadata has changed for a **Fungible Token**, it
shall call `print` with a tuple with the following structure:

```clarity
{ notification: "token-metadata-update", payload: { token-class: "ft", contract-id: <token contract id> }}
```

| Key                   | Value                                                                  |
|-----------------------|------------------------------------------------------------------------|
| `notification`        | The string `"token-metadata-update"`                                   |
| `payload.token-class` | The string `"ft"`                                                      |
| `payload.contract-id` | The contract id (principal) of the contract that declared the token    |
| `payload.update-mode` | _[optional]_ Metadata update mode (see section below)                  |
| `payload.ttl`         | _[optional]_ Time-to-live for `payload.update-mode: dynamic`           |

## Non-Fungible Tokens

When a contract needs to notify the network that metadata has changed for a **Non-Fungible Token**,
it shall call `print` with a tuple with the following structure:

```clarity
{ notification: "token-metadata-update", payload: { token-class: "nft", token-ids: (list u100, u101), contract-id: <token contract id> }}
```

| Key                   | Value                                                                  |
|-----------------------|------------------------------------------------------------------------|
| `notification`        | The string `"token-metadata-update"`                                   |
| `payload.token-class` | The string `"nft"`                                                     |
| `payload.contract-id` | The contract id (principal) of the contract that declared the tokens   |
| `payload.token-ids`   | _[optional]_ A list with the uint token ids that need to be refreshed  |
| `payload.update-mode` | _[optional]_ Metadata update mode (see section below)                  |
| `payload.ttl`         | _[optional]_ Time-to-live for `payload.update-mode: dynamic`           |

If a notification does not contain a value for `payload.token-ids`, it means it is requesting an
update for all tokens.

## Semi-Fungible Tokens

When a contract needs to notify the network that metadata has changed for a **Semi-Fungible Token**,
it shall call `print` with a tuple with the following structure:

```clarity
{ notification: "token-metadata-update", payload: { token-class: "sft", token-ids: (list u100, u101), contract-id: <token contract id> }}
```

| Key                   | Value                                                                  |
|-----------------------|------------------------------------------------------------------------|
| `notification`        | The string `"token-metadata-update"`                                   |
| `payload.token-class` | The string `"sft"`                                                     |
| `payload.contract-id` | The contract id (principal) of the contract that declared the tokens   |
| `payload.token-ids`   | A list with the uint token ids that need to be refreshed               |
| `payload.update-mode` | _[optional]_ Metadata update mode (see section below)                  |
| `payload.ttl`         | _[optional]_ Time-to-live for `payload.update-mode: dynamic`           |

Notifications for SFTs must include a value for `payload.token-ids`.

## Metadata update modes

Applications may use tokens for very different purposes. Some of these could require none or very
few metadata updates ever (e.g. digital artwork that never changes except for reveals), while others
could need to alter it several times a day (e.g. NFTs for in-game items that are traded and modded
continuously).

This use-case variety also affects how developers decide to host their metadata JSON files. For
example, they could choose to use IPFS for low-frequency updates and finality, versus Amazon S3 for
high-frequency off-chain updates.

In order to allow creators and app developers to specify how token metadata should be treated by
indexers, notifications support an optional `payload.update-mode` key that may contain one of the
following values:

* `standard`: The new metadata will be valid until the next notification comes.

    This is the default mode if none is specified.
* `frozen`: This token's metadata will never change again, ever.

    Indexers should ignore new notifications for this token, even if valid.
* `dynamic`: The new metadata is expected to change very quickly and many times in the future (even
  off-chain).

    Indexers should not expect to receive explicit notifications for each of these changes and
should consider refreshing this token's metadata frequently. Token developers may suggest a
reasonable amount of time between refreshes by adding an estimated value (defined in seconds) to the
`payload.ttl` notification property.

## Considerations for metadata indexers

For a token metadata update notification to be considered valid by metadata indexers, it must meet
the following requirements:

1. Its payload structure should be correct whether it is updating a [FT](#fungible-tokens), an
   [NFT](#non-fungible-tokens) or an [SFT](#semi-fungible-tokens).
1. Either the `contract_identifier` field of the contract event must be equal to the
   `payload.contract-id` (i.e., the event was produced by the contract that owns the metadata) or
   the transaction's `tx-sender` principal should match the principal contained in the
   notification's `payload.contract-id` (i.e., the STX address that sent the transaction which emits
   the notification should match the owner of the token contract being updated).

Notifications that do not meet these requirements must be ignored.

### Other implications

* Notifications can come at any point in time and are persistent in the Stacks blockchain.
  * When performing a local sync to the chain tip, old notifications for old metadata updates could
    not necessarily have a distinct effect in metadata responses when processed in the present.
* Multiple notifications for the same tokens will not necessarily correspond to multiple metadata
  updates.
  * Refreshing a token's metadata should be an idempotent operation. Repeated refreshes should not
    create distinct records in the internal metadata database.
  * To prevent slow performance and guard against any Denial of Service attack attempts, contract
    call rate limiting should be implemented locally.
* Notifications can be delayed and out of order.
  * A notification transaction's timestamp should not be considered to be the time when the token
    metadata was actually updated.

Given these constraints the notifications this SIP proposes should be taken as _hints_ to metadata
indexers. Metadata indexers are not obliged to follow them.

## Notification structure reusability

Even though establishing a generalized smart contract notification standard is out of scope for this
SIP, the proposed `print` message structure was designed for reusability by future SIPs that wish to
standardize other events.

For example, developers could vary the `notification` and `payload` values to notify the network
when an NFT collection has been fully minted or another important milestone is reached.

# Related work

An alternative considered for token metadata update notifications is for them to be transmitted via
an off-chain notification service that indexer developers may subscribe to, such as:

* An official mailing list
* A forum post
* An authoritative API service

While these channels would have several advantages like being simpler to update, faster to
propagate, and easier to moderate, they have key disadvantages that make them inadequate for this
SIP's intended use:

1. They introduce a third party dependency
    * An off-chain notification service would most likely be maintained by centralized entities
      unrelated to the Stacks ecosystem. As such, they could modify the channel, its reach, or its
      rules at any time while affecting the entire network.
    * Accepting third party solutions would invite developers to use many different hinting service
      APIs and implementations, defeating the standardization purpose of this SIP. Moving
      notifications to the blockchain establishes a canonical way to store and access them.
    * Even if a decentralized off-chain third-party solution is found, it could still add a layer
      of friction for developer adoption.
1. They are not future proof
    * If the selected off-chain service changes at any point, a migration to another notification
      channel will be much more difficult once the Stacks ecosystem has more token applications and
      metadata indexers.

# Backwards compatibility

Developers who need to emit metadata update notifications for tokens declared in older contracts
(that were deployed before this notification standard was established) could do so by either calling
the contract described in [Reference Implementations](#reference-implementations) or by first
deploying a new separate contract containing a public function that prints this notification and
then calling it to have it emitted.

# Activation

This SIP will be activated when the following conditions are met:

1. At least 10 unique contracts have had metadata updates triggered via contract-call transactions
   that print the proposed notification payload.
1. At least 3 metadata indexers (like the Stacks Blockchain API or an NFT marketplace) start
   listening for and reacting to the emitted notifications.

If the Stacks blockchain reaches block height 170000 and the above has not happened, this SIP will
be considered rejected.

# Reference implementations

A [reference contract](./token-metadata-update-notify.clar) has been deployed to mainnet as
[`SP1H6HY2ZPSFPZF6HBNADAYKQ2FJN75GHVV95YZQ.token-metadata-update-notify`](https://explorer.stacks.co/txid/0xe92af2ea5c11e2e6fde4d31fd394de888070efff23bffad04465c549543abfa2?chain=mainnet).
It demonstrates how to send notifications for each token class and it is available for developers to
use for refreshing any existing or future token contract. If the SIP evolves to require a change to
this contract pre-activation, a new one will be deployed and noted here.

```clarity
;; token-metadata-update-notify
;;
;; Use this contract to notify token metadata indexers that an NFT or FT needs its metadata
;; refreshed.

(use-trait nft-trait 'SP2PABAF9FTAJYNFZH93XENAJ8FVY99RRM50D2JG9.nft-trait.nft-trait)
(use-trait ft-trait 'SP3FBR2AGK5H9QBDH3EEN6DF8EK8JY7RX8QJ5SVTE.sip-010-trait-ft-standard.sip-010-trait)

;; Refresh the metadata for one or more NFTs from a specific contract.
(define-public (nft-metadata-update-notify (contract <nft-trait>) (token-ids (list 100 uint)))
  (ok (print
    {
      notification: "token-metadata-update",
      payload: {
        contract-id: contract,
        token-class: "nft",
        token-ids: token-ids
      }
    })))

;; Refresh the metadata for a FT from a specific contract
(define-public (ft-metadata-update-notify (contract <ft-trait>))
  (ok (print
    {
      notification: "token-metadata-update",
      payload: {
        contract-id: contract,
        token-class: "ft"
      }
    })))
```

The [Stacks Blockchain API](https://github.com/hirosystems/stacks-blockchain-api) will also add
compatibility for this standard while this SIP is being considered to demonstrate how indexers can
listen for and react to these notifications.



================================================
FILE: sips/sip-019/token-metadata-update-notify.clar
================================================
;; token-metadata-update-notify
;;
;; Use this contract to notify token metadata indexers that an NFT or FT needs its metadata
;; refreshed.

(use-trait nft-trait 'SP2PABAF9FTAJYNFZH93XENAJ8FVY99RRM50D2JG9.nft-trait.nft-trait)
(use-trait ft-trait 'SP3FBR2AGK5H9QBDH3EEN6DF8EK8JY7RX8QJ5SVTE.sip-010-trait-ft-standard.sip-010-trait)

;; Refresh the metadata for one or more NFTs from a specific contract.
(define-public (nft-metadata-update-notify (contract <nft-trait>) (token-ids (list 100 uint)))
  (ok (print
    {
      notification: "token-metadata-update",
      payload: {
        contract-id: contract,
        token-class: "nft",
        token-ids: token-ids
      }
    })))

;; Refresh the metadata for a FT from a specific contract
(define-public (ft-metadata-update-notify (contract <ft-trait>))
  (ok (print
    {
      notification: "token-metadata-update",
      payload: {
        contract-id: contract,
        token-class: "ft"
      }
    })))



================================================
FILE: sips/sip-020/sip-020-bitwise-ops.md
================================================
# Preamble

SIP Number: 020

Title: Bitwise Operations in Clarity

Authors: Cyle Witruk <https://github.com/cylewitruk>, Brice Dobry
<https://github.com/obycode>

Consideration: Technical, Governance

Type: Consensus

Status: Ratified

Created: 12 November 2022

License: CC0-1.0

Sign-off: Jason Schrader <jason@joinfreehold.com>, Jesse Wiley <jesse@stacks.org>, Jude Nelson <jude@stacks.org>

Layer: Consensus (hard fork)

Discussions-To: https://github.com/stacksgov/sips

# Abstract

This SIP adds bitwise operations to the Clarity language which could simplify
the implementation of smart contracts that require manipulation of bits. The
changes include the addition of the following operations:

- Bitwise Xor (`bit-xor`)
- Bitwise And (`bit-and`)
- Bitwise Or (`bit-or`)
- Bitwise Not (`bit-not`)
- Binary Left Shift (`bit-shift-left`)
- Binary Right Shift (`bit-shift-right`)

# License and Copyright

This SIP is made available under the terms of the Creative Commons CC0 1.0
Universal license, available at
https://creativecommons.org/publicdomain/zero/1.0/ This SIP's copyright is held
by the Stacks Open Internet Foundation.

# Introduction

Bitwise operations are common in other programming languages. Common algorithms,
including many used in encryption, or the ability to set and check flags in a
bit field for example, would be much more difficult to implement without the use
of these operations. When executing a contract using these operations, the
common hardware on which miners and nodes are likely to be running can all
perform these operations very efficiently -- these are typically single cycle
operations. Note that the addition of these bitwise operations commits the
Clarity VM to using 2's complement to represent integers.

# Specification

## Bitwise Xor (`bit-xor`)

`(bit-xor i1 i2...)`

- **Inputs:** int, ... | uint, ...
- **Output:** int | uint

Returns the result of bitwise exclusive or'ing a variable number of integer
inputs.

| Bit in i1 | Bit in i2 | Bit in Output |
| --------- | --------- | ------------- |
| 0         | 0         | 0             |
| 0         | 1         | 1             |
| 1         | 0         | 1             |
| 1         | 1         | 0             |

The following example uses only 8 bits to make it easier to follow. Actual
Clarity values are 128 bits.

```
(bit-xor 17 30) ;; Return 15
;; Binary representation:
;; i1 (17):     00010001
;; i2 (30):     00011110
;; Output (15): 00001111
```

### Examples

```
(bit-xor 1 2) ;; Returns 3
(bit-xor 120 280) ;; Returns 352
(bit-xor -128 64) ;; Returns -64
(bit-xor u24 u4) ;; Returns u28
(bit-xor 1 2 4 -1) ;; Returns -8
```

## Bitwise And (`bit-and`)

`(bit-and i1 i2...)`

- **Inputs:** int, ... | uint, ...
- **Output:** int | uint

Returns the result of bitwise and'ing a variable number of integer inputs.

| Bit in i1 | Bit in i2 | Bit in Output |
| --------- | --------- | ------------- |
| 0         | 0         | 0             |
| 0         | 1         | 0             |
| 1         | 0         | 0             |
| 1         | 1         | 1             |

The following example uses only 8 bits to make it easier to follow. Actual
Clarity values are 128 bits.

```
(bit-and 17 30) ;; Return 16
;; Binary representation:
;; i1 (17):     00010001
;; i2 (30):     00011110
;; Output (16): 00010000
```

### Examples

```
(bit-and 24 16) ;; Returns 16
(bit-and 28 24 -1) ;; Returns 24
(bit-and u24 u16) ;; Returns u16
(bit-and -128 -64) ;; Returns -128
(bit-and 28 24 -1) ;; Returns 24
```

## Bitwise Or (`bit-or`)

`(bit-or i1 i2...)`

- **Inputs:** int, ... | uint, ...
- **Outputs:** int | uint

Returns the result of bitwise inclusive or'ing a variable number of integer
inputs.

| Bit in i1 | Bit in i2 | Bit in Output |
| --------- | --------- | ------------- |
| 0         | 0         | 0             |
| 0         | 1         | 1             |
| 1         | 0         | 1             |
| 1         | 1         | 1             |

The following example uses only 8 bits to make it easier to follow. Actual
Clarity values are 128 bits.

```
(bit-or 17 30) ;; Return 31
;; Binary representation:
;; i1 (17):     00010001
;; i2 (30):     00011110
;; Output (31): 00011111
```

### Examples

```
(bit-or 4 8) ;; Returns 12
(bit-or 1 2 4) ;; Returns 7
(bit-or 64 -32 -16) ;; Returns -16
(bit-or u2 u4 u32) ;; Returns u38
```

## Bitwise Not (`bit-not`)

`(bit-not i1)`

- **Inputs:** int | uint
- **Output:** int | uint

Returns the one's compliment (sometimes also called the bitwise compliment or
not operator) of `i1`, effectively reversing the bits in `i1`.

In other words, every bit that is `1` in `ì1` will be `0` in the result.
Conversely, every bit that is `0` in `i1` will be `1` in the result.

| Bit in i1 | Bit in Output |
| --------- | ------------- |
| 0         | 1             |
| 1         | 0             |

The following example uses only 8 bits to make it easier to follow. Actual
Clarity values are 128 bits.

```
(bit-not u41) ;; Return u214
;; Binary representation:
;; i1 (41):      00101001
;; Output (214): 11010110
```

### Examples

```
(bit-not 3) ;; Returns -4
(bit-not u128) ;; Returns u340282366920938463463374607431768211327
(bit-not 128) ;; Returns -129
(bit-not -128) ;; Returns 127
```

## Bitwise Left Shift (`bit-shift-left`)

`(bit-shift-left i1 shamt)`

- **Inputs:** int, uint | uint, uint
- **Outputs:** int | uint

Shifts all bits in `i1` to the left by the number of places specified in `shamt`
modulo 128 (the bit width of Clarity integers). New bits are filled with zeros.

Note that there is a deliberate choice made to ignore arithmetic overflow for
this operation. In use cases where overflow should be detected, developers
should use `*`, `/`, and `pow` instead of the shift operators.

The following example uses only 8 bits to make it easier to follow. Actual
Clarity values are 128 bits.

```
(bit-shift-left 6 u3) ;; Return 48
;; Binary representation:
;; Input  (6):  00000110
;; Output (48): 00110000
```

### Examples

```
(bit-shift-left 16 u2) ;; Returns 64
(bit-shift-left -64 u1) ;; Returns -128
(bit-shift-left u4 u2) ;; Returns u16
(bit-shift-left 123 u9999999999) ;; Returns -170141183460469231731687303715884105728 (== 123 bit-shift-left 127)
(bit-shift-left u123 u9999999999) ;; Returns u170141183460469231731687303715884105728 (== u123 bit-shift-left 127)
(bit-shift-left -1 u7) ;; Returns -128
(bit-shift-left -1 u128) ;; Returns -1
```

## Bitwise Right Shift (`bit-shift-right`)

`(bit-shift-right i1 shamt)`

- **Inputs:** int, uint | uint, uint
- **Output:** int | uint

Shifts all the bits in `i1` to the right by the number of places specified in
`shamt` modulo 128 (the bit width of Clarity integers). When `i1` is a `uint`
(unsigned), new bits are filled with zeros. When `i1` is an `int` (signed), the
sign is preserved, meaning that new bits are filled with the value of the
previous sign-bit.

Note that there is a deliberate choice made to ignore arithmetic overflow for
this operation. In use cases where overflow should be detected, developers
should use `*`, `/`, and `pow` instead of the shift operators.

The following example uses only 8 bits to make it easier to follow. Actual
Clarity values are 128 bits.

```
(bit-shift-right u170 u1) ;; Return u85
;; Binary representation:
;; Input  (u170): 10101010
;; Output (u85):  01010101
```

### Examples

```
(bit-shift-right 2 u1) ;; Returns 1
(bit-shift-right 128 u2) ;; Returns 32
(bit-shift-right -64 u1) ;; Returns -32
(bit-shift-right u128 u2) ;; Returns u32
(bit-shift-right 123 u9999999999) ;; Returns 0
(bit-shift-right u123 u9999999999) ;; Returns u0
(bit-shift-right -128 u7) ;; Returns -1
(bit-shift-right -256 u1) ;; Returns -128
(bit-shift-right 5 u2) ;; Returns 1
(bit-shift-right -5 u2) ;; Returns -2
```

# Related work

Not applicable

# Backwards Compatibility

Because this SIP introduces new Clarity operators, it is a consensus-breaking
change. A contract that uses one of these new operators would be invalid before
this SIP is activated, and valid after it is activated.

# Activation

This SIP will be a rider on SIP-015. It will be considered activated if and only
if SIP-015 (and Stacks 2.1) is activated.

# Reference Implementations

- https://github.com/stacks-network/stacks-blockchain/pull/3389
- See also discussions in
  https://github.com/stacks-network/stacks-blockchain/pull/3382



================================================
FILE: sips/sip-021/miner-protocol.d2
================================================
shape: sequence_diagram

bitcoin: Bitcoin
miner: Miner
stackers: Stackers

Sortition / Tenure Election : {
  miner -> bitcoin: send block-commit
  bitcoin."sortition"
  bitcoin -> miner: miner observes sortition result
}

Tenured Miner Loop: {
  miner."mine Stacks block"
  miner -> stackers: block to StackerDB
  stackers -> stackers: StackerDB notification
  stackers -> stackers: Stackers validate Block
  stackers -> stackers: Stackers sign block
  stackers -> miner: Ack
}




================================================
FILE: sips/sip-022/sip-022-emergency-pox-fix.md
================================================
# Preamble

SIP Number: 022

Title: Emergency Fix to PoX Stacking Increases

Authors:
    Aaron Blankstein <aaron@hiro.so>,
    Brice Dobry <brice@hiro.so>,
    Friedger Müffke <mail@friedger.de>,
    Jude Nelson <jude@stacks.org>,
    Pavitthra Pandurangan <pavi@stacks.org>,

Consideration: Technical, Governance

Type: Consensus

Status: Ratified

Created: 19 April 2023

License: BSD 2-Clause

Sign-off: Rafael Cárdenas <rafael@hiro.so> (SIP Editor), Jesse Wiley <jesse@stacks.org> (Acting Technical CAB Chair), Jason Schrader <jason@joinfreehold.com> (Governance CAB Chair), Jude Nelson <jude@stacks.org> (Steering Committee Chair)

Discussions-To: https://github.com/stacksgov/sips

# Abstract

On 19 April 2023, it was discovered that there was a bug in the PoX smart
contract which would allow a user to claim that they have stacked far, far more
STX than they had locked.  Exploiting this bug both allows the user to increase
their PoX reward slot allotment, while also driving up the stacking minimum.
Furthermore, it creates the conditions for a network-wide crash:  if the total
amount of STX stacked as reported by the PoX smart contract were to ever exceed
the total amount of liquid STX, then the node would crash into an irrecoverable
state.  This bug has already been triggered in the wild.

This SIP proposes **two immediate consensus-breaking changes** that both prevents this bug
from being triggered in subsequent reward cycles, and replaces the current PoX
implementation with a new PoX implementation without the bug.  If ratified, this
SIP would activate two hard forks 200 Bitcoin blocks prior to the start of
reward cycles #58 and #59.

This SIP would constitute two consensus-rules version bumps.  During cycle #58, the system 
version would be Stacks 2.2.  During and after cycle #59, the system would be
Stacks 2.3.

# Addendum

*The following was added after this SIP was accepted, where some version number changes were necessary. The following section addresses these changes **without** changing the ratified text* 

[SIP-023](./sips/sip-023/sip-023-emergency-fix-traits.md), which was accepted by the required CAB's on May 2nd, 2023 necessitates some changes to this SIP. The changes introduced in [SIP-023](./sips/sip-023/sip-023-emergency-fix-traits.md) are in response to a bug introduced by the first hard fork, referred to later in this SIP as `Stacks 2.2`. To address the issue, an intermediary version `Stacks 2.3` was created which supercedes the second hard fork as defined here. 
As a result, the second hard fork defined later in this SIP, `Stacks 2.3` **is now changed to `Stacks 2.4`** due to the intermediary release required as a result of the first hard fork `Stacks 2.2`. 

In addition to the version number change, [SIP-023](./sips/sip-023/sip-023-emergency-fix-traits.md) also necessitates a change to the peer network version defined later in this SIP as follows:

* Change the mainnet peer network version bits from `0x18000008` to `0x18000009`. 
* Change the testnet peer network version bits from `0xfacade08` to `0xfacade09`. 

# Addendum II

_The following was added after this SIP was accepted to reflect the updated activation height for cycle 60, where the current text addresses cycle 59 activation height. The following section addresses these changes **without** changing the ratified text_

[SIP-023](./sips/sip-023/sip-023-emergency-fix-traits.md), which was accepted by the required CAB's on May 2nd, 2023 defines specific [activation criteria](./sips/sip-022/sip-022-emergency-pox-fix.md#activation) for cycle #59. As a result of more testing being done prior to the release, this window shall be missed and the new target activation will be in cycle #60, or Bitcoin block `792051`.

Current text:
> The second hard fork will take effect 200 Bitcoin blocks prior to the start of reward cycle #59, which is Bitcoin block height 789751.

Is now changed to the following:
> The second hard fork will take effect 400 Bitcoin blocks prior to the start of the prepare phase for cycle #60, which is Bitcoin block height 791551.


The 3 values changed:

- Reward cycle is changing from `59` to `60`
- Activation height is change from `789751` to `791551 `
- Blocks prior to activation height for the start of the reward cycle is changed from `200` to `400` to allow more time for contract deployments and stacking transactions



# Introduction

[SIP-015](./sips/sip-015/sip-015-network-upgrade.md) proposed a new PoX smart
contract, `pox-2`, which included a new public function `stack-increase`.  This
function allows a user to increase the amount of STX locked for PoX while the
account has locked STX.  The `stack-increase` function calls an internal function
`increase-reward-cycle-entry` to update the PoX contract's data space to record
the increase.

The `increase-reward-cycle-entry` function has a bug in this code path.  The bug
itself is annotated with comment lines starting with "(BUG)".

```clarity
(let ((existing-entry (unwrap-panic (map-get? reward-cycle-pox-address-list { reward-cycle: reward-cycle, index: reward-cycle-index })))
      (existing-total (unwrap-panic (map-get? reward-cycle-total-stacked { reward-cycle: reward-cycle })))
      (total-ustx (+ (get total-ustx existing-total) (get add-amount data))))
    ;; stacker must match
    (asserts! (is-eq (get stacker existing-entry) (some (get stacker data))) none)
    ;; update the pox-address list
    (map-set reward-cycle-pox-address-list
             { reward-cycle: reward-cycle, index: reward-cycle-index }
             { pox-addr: (get pox-addr existing-entry),
               ;; (BUG) ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
               ;; (BUG) `total-ustx` is the amount of uSTX locked in this cycle, not
               ;; (BUG) the stacker's total amount of uSTX. This value ought to be
               ;; (BUG) `(+ (get total-ustx existing-entry) (get add-amount data))`
               ;; (BUG) ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
               total-ustx: total-ustx,
               stacker: (some (get stacker data)) })
    ;; update the total
    (map-set reward-cycle-total-stacked
             { reward-cycle: reward-cycle }
             { total-ustx: total-ustx })
    (some { first-cycle: first-cycle,
            reward-cycle: (+ u1 reward-cycle),
            stacker: (get stacker data),
            add-amount: (get add-amount data) })))))
```

The bug is reachable by any solo Stacker who calls `stack-increase`.  Any solo
Stacker who increases their total STX locked will erroneously set the amount of
uSTX backing their PoX address to be equal to the current total number of uSTX
locked in this cycle (the value `total-ustx`), instead of the sum of their
current locked uSTX amount and their added amount.  The act of triggering this
bug is an unavoidable consequence of calling the `stack-increase` function --
individuals who call `stack-increase` are not thought to be deliberately
exploiting the system.

This bug was first triggered in the wild by Stacks transaction
`20e708e250bad3fb5d5ab84a70365c3c1cf0520c7a9f67cd5ff6b9fa94335ea5`.

The immediate consequences for PoX of this bug being triggered are as follows:

* The total STX locked to the PoX address owned by the caller of `stack-increase`
  will be potentially higher than the amount of STX that the caller possesses.
The caller will receive PoX payouts _as if_ they had locked that much STX.  So,
the caller receives undue BTC.

* The stacking threshold is raised to account for the PoX contract's reported
  increase in STX locked.

Similar consequences are expected when a Stacker contributes to two different PoX addresses and 
at least one PoX address would benefit from auto-unlocking. This behavior has not been seen in the wild.

Furthermore, if this bug is triggered enough times, the Stacks network will crash.  This is
because of a runtime assertion in the PoX reward set calculation logic that
verifies that the total locked STX does not exceed the total liquid STX.  This
would no longer be true due to this bug.  The offending assertion is detailed
below:

```rust
pub fn get_reward_threshold_and_participation(
    pox_settings: &PoxConstants,
    addresses: &[RawRewardSetEntry],
    liquid_ustx: u128,
) -> (u128, u128) {
    let participation = addresses
        .iter()
        .fold(0, |agg, entry| agg + entry.amount_stacked);

    assert!(
        participation <= liquid_ustx,
        "CORRUPTION: More stacking participation than liquid STX"
    );
```

The `RawRewardSetEntry` data are pulled directly from the
`reward-cycle-pox-address-list` data map, and the `.amount_stacked` field is
equal to the `total-ustx` field that was erroneously set in `stack-increase`.

Considering these consequences with respect to the [draft blockchain catastrophic
failure and recovery guidelines](https://github.com/stacksgov/sips/pull/10),
this bug would be categorized as requiring an _immediate_ hard fork to rectify.
The network has not yet crashed, but it is in imminent danger of crashing and
there is insufficient time to execute a Stacker-based SIP vote as has been customary for
past hard forks.  This SIP instead proposes that this hard fork activate at the
start of the next reward cycle (#58) at the time of this writing.

There is less than one reward cycle remaining to fix this
problem, and yet a Stacker vote would require at least one complete reward cycle
to carry out a vote (not accounting for any additional time required for
sending out adequate public communications and tabulating the vote afterwards).
A subsequent hard fork to re-enable PoX would have the effect of restoring
Stacker voting.

# Specification

Given the lack of time to conduct a Stacker vote to activate this SIP, the
proposed fix in this SIP is as parsimonious and discreet as possible.  It will
execute as a set of **two hard forks**.

The first hard fork, which activates before the start of reward cycle #58, will disable PoX beginning with cycle #58.
The `pox-2` contract will be considered defunct, just as the pre-2.1 `pox`
contract is.  This hard fork would do the following:

* Prevent all stacking functions from being called in `pox-2`.  The `pox-2`
  contract would be considered defunct, like the `pox` contract is now.

* Set the minimum required block-commit memo bits to `0x07`.  All block-commits
  after the Bitcoin block activation height must have a memo value of at least
`0x07`.  This ensures that miners that do not upgrade from Stacks 2.1 will not
be able to mine in Stacks 2.2.

* Set the mainnet peer network version bits to `0x18000007`.  This ensures that follower
  nodes that do not upgrade to Stacks 2.2 will not be able to talk to Stacks
2.2 nodes.

* Set the testnet peer network version bits to `0xfacade07`.  This ensures that
  testnet follower nodes that do not upgrade to Stacks 2.2 will not be able to
talk to Stacks 2.2 nodes.

The second hard fork will instantiate a new PoX
implementation `pox-3`. The `pox-3` contract code will:

* Fix the aforementioned `stacks-increase` bug.

* Prevent Stackers from contributing to two or more PoX addresses. In particular,
    * Add a `delegated-to` field in the `stacking-state` data map, so that the 
    `stacking-state` entry for a PoX user will indicate the principal to which 
    their STX are delegated (if they are using delegated stacking).

    * Add checks to the delegated stacking public functions that validate the 
    `delegated-to` field in the Stacker's `stacking-state` map entry.

* Set the minimum required block-commit memo bits to `0x08`.  All block-commits
  after the Bitcoin block activation height must have a memo value of at least
`0x08`.  This ensures that miners that do not upgrade from Stacks 2.2 will not
be able to mine in Stacks 2.3.

* Set the mainnet peer network version bits to `0x18000008`.  This ensures that follower
  nodes that do not upgrade to Stacks 2.3 will not be able to talk to Stacks
2.3 nodes.

* Set the testnet peer network version bits to `0xfacade08`.  This ensures that
  testnet follower nodes that do not upgrade to Stacks 2.3 will not be able to
talk to Stacks 2.3 nodes.

## Alternative Approaches Considered

It is unusual that this SIP proposes two hard forks in rapid succession without 
a Stacker-based vote for activating the new rules.  The
reason for this is because PoX must first be disabled prior to the start of
reward cycle #58 in order to avert a network-wide
crash.  This cannot be delayed, but there is insufficient time to prepare `pox-3`
or even execute a Stacker-based vote before this bug must be addressed.
Therefore, the first hard fork must happen immediately.

A second hard fork is necessary to instantiate `pox-3`, which must also happen
as soon as possible (no more than one reward cycle later) in order to restore
critical functionality to the Stacks blockchain.  Because PoX would be disabled
before `pox-3` would activate, there would not exist a means of carrying out a
Stacker-based vote to upgrade the system (as had been the case in all prior
hard forks).  Beyond receiving a BTC yield, **the lack of a functioning PoX contract
prevents consensus-level SIPs from being voted upon**, which necessitates an
expedient restoration.

A less-disruptive alternative approach of repairing the
`reward-cycle-pox-address-list` data map was considered.  This would have only
required a single hard fork, and no disruption of PoX payouts (however,
`stack-increase` would have been disabled).  This approach was ultimately dropped
because of the interactions between delegated stacking and solo stacking -- it
would not be possible to retroactively compute the correct values for the
`reward-cycle-pox-address-list` data map.  This, in turn, meant that any repair
tactic would require the node to calculate the correct values for
`reward-cycle-pox-address-list` as the blocks in reward cycle #57 were
processed, which in turn meant that nodes would need to boot from genesis to
derive the correct data with which to repair the data map at the start of reward
cycle #58.  There is insufficient time to implement, test, and deploy this
approach.

# Related Work

Consensus bugs requiring immediate attention such as this
have been detected and fixed in other blockchains.  In the
absence of a means of gathering user comments on proposed fixes, the task of
activating these bugfixes has fallen to miners, exchanges, and node runners.  As
long as sufficiently many participating entities upgrade, then a chain split is
avoided and the fixed blockchain survives.  A prominent example was Bitcoin
[CVE-2010-5139](https://www.cvedetails.com/cve/CVE-2010-5139/), in which a
specially-crafted Bitcoin transaction could mint arbitrarily many BTC well above
the 21 million cap.  The [developer
response](https://bitcointalk.org/index.php?topic=823.0) was to quickly release
a patched version of Bitcoin and rally enough miners and users to upgrade.  In a
matter of hours, the canonical Bitcoin chain ceased to include any transactions
that minted too much BTC.

# Backwards Compatibility

There are no changes to the chainstate database schemas in this SIP.  Everyone
who runs a Stacks 2.1 node today will be able to run a Stacks 2.2 node off of
their existing chainstates at the start of reward cycle #58,
as well as a Stacks 2.3 node off of a Stacks 2.2 chainstate at the start of
reward cycle #59.

Stacks 2.2 nodes will not interact with Stacks 2.1 nodes on the peer network
after the Bitcoin block activation height passes.  In addition, Stacks 2.2 nodes
will ignore block-commits from Stacks 2.1 nodes.  Similar changes were made for
Stacks 2.05 and Stacks 2.1 to ensure that the new network cleanly separates from
stragglers still following the old rules.  This also applies to Stacks 2.3 nodes
and Stacks 2.2 nodes.

# Activation

This SIP shall be considered Activated if the Stacks 2.3 network is live at the
start of reward cycle #59.

The Bitcoin block activation height for the first hard fork will need to pass prior to the selection of
the PoX anchor block for reward cycle #58 (Bitcoin block height 787851).  This
SIP proposes Bitcoin block height 787651, which is 200 Bitcoin blocks prior.  In
other words, the Bitcoin block that is mined 100 blocks prior to the start of
the prepare phase for reward cycle #58 shall be the activation height.

The second hard fork will take effect 200 Bitcoin blocks prior to the start of reward cycle #59,
which is Bitcoin block height 789751.

The node software for Stacks 2.2 and 2.3 shall be merged to the `master` branch of the
reference implementation no later than three days prior to the activation
height.  This means that everyone shall have at least three days to upgrade
their Stacks 2.1 nodes to Stacks 2.2, and at least three days to upgrade from
2.2 to 2.3.

# Reference Implementation

The reference implementation of this SIP can be found in the
`feat/sip-022-pox-disable` branch of
the Stacks blockchain reference implementation.  It is available at
https://github.com/stacks-network/stacks-blockchain.



================================================
FILE: sips/sip-023/sip-023-emergency-fix-traits.md
================================================
# Preamble

SIP Number: 023

Title: Emergency Fix to Trait Invocation Behavior

Authors:
    Aaron Blankstein <aaron@hiro.so>,
    Brice Dobry <brice@hiro.so>,
    Jude Nelson <jude@stacks.org>,

Consideration: Technical, Governance

Type: Consensus

Status: Ratified

Created: 1 May 2023

License: BSD 2-Clause

Sign-off: Rafael Cárdenas <rafael@hiro.so> (SIP Editor), Jesse Wiley <jesse@stacks.org> (Acting Technical CAB Chair), Jason Schrader <jason@joinfreehold.com> (Governance CAB Chair), Jude Nelson <jude@stacks.org> (Steering Committee Chair)

Discussions-To: https://github.com/stacksgov/sips

# Abstract

On 1 May 2023, it was discovered that smart contracts deployed prior to Stacks 2.1
that exposed public methods with
trait arguments could not be invoked with previously working trait-implementing
contract arguments.

This bug was caused by the activation of Stacks Epoch 2.2 (https://github.com/stacksgov/sips/blob/main/sips/sip-022/sip-022-emergency-pox-fix.md).

This SIP proposes an **immediate consensus-breaking change** to
introduce a new Stacks epoch 2.3 that corrects this regression.

**This SIP proposes a Bitcoin activation height of 788,240**

# Introduction

Clarity 2, introduced in Stacks 2.1, includes a new type checker and type system which
impacts trait invocations. In order for existing contracts to remain
compatible, their types must be _canonicalized_. In the context of traits,
the type canonicalization rules implement the new trait semantics introduced in
[SIP-015](./sips/sip-015/sip-015-network-upgrade.md).

## Epoch 2.2 Bug Behavior

The type canonicalization method performed an exact check for the current epoch:

```rust
    pub fn canonicalize(&self, epoch: &StacksEpochId) -> TypeSignature {
        match epoch {
            StacksEpochId::Epoch21 => self.canonicalize_v2_1(),
            _ => self.clone(),
        }
    }
```

Therefore, a pre-2.1 function with trait arguments that is invoked in Stacks 2.2
will fail to canonicalize its trait arguments, and abort with a
runtime analysis error. Specifically:

* If a miner includes a contract call transaction with trait arguments in a block, the transaction will abort with a runtime error.

* If a user submits a contract call transaction with trait arguments to the
  mempool, it will be rejected.

* A read-only contract-call with trait arguments will fail with a runtime
  analysis error.

# Specification

This hard fork will do the following:

* In epoch 2.2, the current buggy behavior will be preserved.  All
  contract-calls with trait arguments must fail with a runtime analysis error.

* In epoch 2.3, the desired behavior will be restored.  The trait semantics
  described in SIP-015 will be restored, and trait arguments in
  contract-calls will be treated as they were in Stacks 2.1.

* Set the minimum required block-commit memo bits to `0x08`.  All block-commits
  after the Bitcoin block activation height must have a memo value of at least
`0x08`.  This ensures that miners that do not upgrade from Stacks 2.2 will not
be able to mine in Stacks 2.3.

* Set the mainnet peer network version bits to `0x18000008`.  This ensures that follower
  nodes that do not upgrade to Stacks 2.3 will not be able to talk to Stacks
2.3 nodes.

* Set the testnet peer network version bits to `0xfacade08`.  This ensures that
  testnet follower nodes that do not upgrade to Stacks 2.3 will not be able to
talk to Stacks 2.3 nodes.

The reference implementation will update the `canonicalize()` method to match on all epochs, setting
the epoch 2.3 behavior to `self.canonicalize_v2_1()`, and the epoch 2.2 behavior to `self.clone()`.
This will preserve the buggy 2.2 behavior during the 2.2 epoch (so that the
hard fork does not require rollback), but fix the behavior after activation
of the 2.3 epoch.

# Related Work

Several potential workarounds were explored first to try to solve this issue without a hard-fork. 
Unfortunately, attempts to wrap pre-2.1 contracts with 2.2 contracts can avoid the mempool rejection, 
but still hit the same error in the form of a runtime type-checker error.
Upon further inspection into the code paths, a hard-fork option was determined to be the only viable option in this case.

Consensus bugs requiring immediate attention such as this
have been detected and fixed in other blockchains.  In the
absence of a means of gathering user comments on proposed fixes, the task of
activating these bugfixes has fallen to miners, exchanges, and node runners.  As
long as sufficiently many participating entities upgrade, then a chain split is
avoided and the fixed blockchain survives.  A prominent example was Bitcoin
[CVE-2010-5139](https://www.cvedetails.com/cve/CVE-2010-5139/), in which a
specially-crafted Bitcoin transaction could mint arbitrarily many BTC well above
the 21 million cap.  The [developer
response](https://bitcointalk.org/index.php?topic=823.0) was to quickly release
a patched version of Bitcoin and rally enough miners and users to upgrade.  In a
matter of hours, the canonical Bitcoin chain ceased to include any transactions
that minted too much BTC.

# Backwards Compatibility

There are no changes to the chainstate database schemas in this SIP.  Everyone
who runs a Stacks 2.2 node today will be able to run a Stacks 2.3 node off of
their existing chainstates before the activation height.

Stacks 2.3 nodes will not interact with Stacks 2.2 nodes on the peer
network after the Bitcoin block activation height passes.  In
addition, Stacks 2.3 nodes will ignore block-commits from Stacks 2.2
nodes.  Similar changes were made for Stacks 2.05, Stacks 2.1, and
Stacks 2.2 to ensure that the new network cleanly separates from
stragglers still following the old rules.

# Activation

This SIP shall be considered Activated if the Stacks 2.3 network is live at the
Bitcoin block activation height.

The node software for Stacks 2.3 shall be merged to the `master` branch of the
reference implementation no later than two days prior to the activation
height. This means that everyone shall have at least two days to upgrade
their Stacks 2.2 nodes to Stacks 2.3.

# Reference Implementation

The reference implementation of this SIP can be found in the
`feat/2.3-traits-only-fix` branch of
the Stacks blockchain reference implementation.  It is available at
https://github.com/stacks-network/stacks-blockchain.



================================================
FILE: sips/sip-024/sip-024-least-supertype-fix.md
================================================
# Preamble

SIP Number: 024

Title: Emergency Fix to Data Validation and Serialization Behavior

Authors:
    Aaron Blankstein <aaron@hiro.so>,
    Brice Dobry <brice@hiro.so>,
    Jude Nelson <jude@stacks.org>,
    Pavitthra Pandurangan <pavitthra@stacks.org>,

Consideration: Technical, Governance

Type: Consensus

Status: Ratified

Created: 11 May 2023

License: BSD 2-Clause

Sign-off: Jason Schrader <jason@joinfreehold.com> (Governance CAB Chair), Brice Dobry <brice@hiro.so> (Technical CAB Chair), Jude Nelson <jude@stacks.org> (Steering Committee Chair)

Discussions-To: https://github.com/stacksgov/sips

# Abstract

On 8 May 2023, a critical Denial-of-Service vulnerability manifested
in the Stacks network. While the initial DoS threat was remedied
through a non-consensus breaking hotfix, the underlying bug that
triggered the vulnerability requires consensus changes to fix.
This underlying bug has existed in the Stacks blockchain implementation
since the launch of Stacks 2.0, and has the potential to impact the
functionality of contracts even if they do not currently rely on the
buggy behavior.

This SIP proposes a **consensus-breaking change** to be included in
the SIP-022 hardfork (Epoch 2.4) to remediate this negative impact.

# Introduction

Stacks 2.0 allows contracts to include tuple types with _extra_ fields
to be included in lists with tuples with fewer fields:

```clarity
(list (tuple (a 1)) (tuple (b 1) (a 1)))
```

The Clarity runtime will treat each item of this list as if it only
had the field `a`, which creates an issue for the database on reads and writes.
On database reads, the Clarity database checks if the found type
matches the expected type, and discovers a mismatch. This mismatch
led to a DoS on 8 May 2023, and was fixed by converting the node
crash into a transaction invalidation.

However, transaction invalidation is _not_ sufficient as a long-term
solution due to the following:

1. Miners must be able to charge for these kinds of failures
2. Contracts which do not directly rely on this behavior could still
   receive buggy values because of the behavior (which could lead to storage failures).

# Specification

The proposed changes to the Epoch 2.4 hard fork will do the following:

* Add a value sanitization routine which eliminates any of these extra
  fields from the in-memory representation of a Clarity value.
* Invoke the sanitization routine on contract-call arguments and
  return values.
* Invoke the sanitization routine on database reads.
* Invoke the sanitization routine during Clarity value constructors
  which relied on the buggy type check behavior.

This will preserve the existing type system behavior, but it will ensure
that values constructed this way _match_ the expected type.

# Related work
The Stacks network has precedent for fixing consensus bugs through hard forks, some being released on 
short timelines. 

Other blockchains have also detected and fixed consensus critical bugs quickly. A prominent example of 
this happened on Bitcoin, which had a bug that would allow the minting of an arbitrary amount of BTC 
above the 21 million cap. A patched version was quickly released, and the network upgraded in a 
matter of hours. 

# Backwards Compatibility 
Everyone who runs a 2.3 node will be able to run a Stacks 2.4 node 
off of their existing chainstate. There are no changes to the chainstate database schemas in this SIP.

Stacks 2.4 nodes will not interact with Stacks 2.3 nodes on the peer network (defined in SIP-022)
after the Bitcoin block activation height of `791551`. In addition, Stacks 2.4 nodes
will ignore block-commits from Stacks 2.3 nodes (as well as from nodes on prior versions). 
Similar changes were made for Stacks 2.05 and Stacks 2.1 to ensure that the new network
cleanly separates from stragglers still following the old rules.

# Activation 
The changes described in this SIP will ship in the same release as the changes described in SIP-022, which discusses
and proposes a fix to the proof of transfer protocol.

This release will ship 500 blocks prior to reward cycle 60, which is Bitcoin block height 791,551. 
This gives stackers ample time (~3 days) to stack through the new contract. 

The node software for Stacks 2.4 shall be merged to the `master` branch of the
reference implementation no later than four days prior to the activation
height.  This means that everyone shall have at least three days to upgrade
their Stacks 2.3 nodes to Stacks 2.4. This change does not require a sync from genesis.

# Reference Implementation
The reference implementation of this SIP can be found in the
`feat/epoch-2.4-sanitize` branch of the Stacks blockchain reference implementation.  It is available at
https://github.com/stacks-network/stacks-blockchain.



================================================
FILE: sips/sip-025/sip-025-iterating-towards-weighted-schnorr-threshold-signatures.md
================================================
# Preamble

SIP Number: 025

Title: Iterating towards Weighted Schnorr Threshold Signatures

Authors:

* Aaron Blankstein (aaron@hiro.so)
* Brice Dobry (brice@hiro.so)
* Crypt0jan (jan@alumlabs.io)
* Jacinta Ferrant (jacinta@trustmachines.co)
* Jude Nelson (jude@stacks.org)
* Hank Stoever (hank@trustmachines.co)
* Joey Yandle (joey@trustmachines.co)

Consideration: Technical

Type: Consensus

Status: Ratified

Created: 14 May 2024

License: BSD 2-Clause

Sign-off: Brice Dobry (Technical CAB), Jude Nelson (SC)

Discussions-To:

# Abstract

SIP-021 defines a threshold signature scheme called Weighted Schnorr Threshold
Signatures (WSTS), a Schnorr signature scheme based on FROST whereby a set of
mutually-distrustful parties produce a single Schnorr signature from shares of a
private key.  No party knows the private key; a signature can only be produced
if a threshold of parties agree to produce a signature.

WSTS is used in SIP-021 to provide a means for Stackers to collectively append
blocks to the Stacks blockchain in a way that achieves Bitcoin finality for
Stacks.  Because a block can only be attached if a large fraction of the stacked
STX votes for the block, the Stacks blockchain will not fork on its own as long
as at least 30% of STX votes are honest.  In the absence of network partitions,
Stackers always see the same Stacks chain tip and thus can compel Stacks miners
to build atop it (and refuse to sign blocks from miners that do not do this).

This SIP describes an incremental approach to achieving this end (Bitcoin
finality) via a simpler, but less efficient means:  have each Stacker append a
signature to the block, and do not aggregate them.  This approach makes blocks
bigger (but tolerably so), and does not meaningfully slow down validation.  By
implementing this means first, before WSTS is ready, SIP-021 can be ratified
sooner than later.

# Introduction

WSTS, being a variant of FROST, requires that signers designate a particular
signer as a coordinator to facilitate both the _distributed key generation_ (DKG)
and _signing round_ steps of the protocol.  But because signers are distributed
and mutually distrustful, the setting for WSTS coordinator selection is
fundamentally a Byzantine setting.  Not only can individual signers be faulty,
but also the coordinator may be faulty.  This necessitates a Byzantine
fault-tolerant (BFT) protocol for making forward progress on DKG and signing
rounds (something that the FROST authors leave as an exercise to the
implementer), in which faulty signers and coordinators can be identified by a
BFT majority and excised from the next round of the protocol.

Excluding a Byzantine signer from WSTS is trivial if the coordinator is honest:
the coordinator restarts the protocol without including the Byzantine signer.
Other signers do not communicate with the Byzantine signer, because the
coordinator has not designated that signer as part of the signer set.

But what happens when the coordinator is faulty?  To oust a Byzantine
coordinator, signers must execute a BFT protocol amongst themselves to select a
new coordinator.  But in order to deal with this problem, coordinator selection
will:

* be a best-effort process that could result in an unrecoverable signer split
  (and subsequently a chain stall),
* implement leader election with BFT Paxos (or something equivalent), or 
* implement some "in between" solution. 

The first option is a non-starter, because signers work in a Byzantine setting.

The third option is a false option.  The history of distributed systems should
teach us that any such half solution is either broken, or eventually becomes a
(bad) implementation of BFT Paxos anyways.

Of these options, it should be clear that the second option is the best -- it
applies a well-known protocol to solve the exact kinds of problems it was
designed to solve. However, implementing BFT Paxos is a serious undertaking, and
applicable libraries are not readily available.

Why propose this SIP at all, then, if the only path to a viable WSTS
implementation is to implement coordinator selection via BFT Paxos?  The reason
is that WSTS is not an end but a _means_ of achieving Bitcoin finality.  There are
other, simpler means to achieving this in a Byzantine setting that are less
efficient, but simpler to implement and more robust to failure than WSTS which
can be used to implement the goals of SIP-021 while a complete WSTS with
BFT-Paxos implementation is developed.

To achieve this, we propose an iterative approach to signer-set signatures in
Nakamoto, spread across two hard forks:  one to implement a simpler but
less-efficient signer-set signature which can be delivered sooner, and one to
implement the complete WSTS scheme with BFT Paxos coordinator selection.

# Specification

Nakamoto signer-sets would be implemented in two iterations, where each
iteration takes effect with a hard fork.  The first iteration would activate
with SIP-021 if this SIP is ratified before SIP-021 activates.

## Iteration 1 

In Epoch 3.0, the signer set does not use WSTS to aggregate a signature, but
instead simply provides a concatenation of signatures (like Bitcoin's P2SH
multisig). Each signer binary listens to their paired Stacks node for block
proposals, and individually computes a signature over the block if they approve
it. This signature is sent to the miner via StackerDB, which gathers and
includes the signatures in their block. Each 3.0 block header includes all of
the signatures required to reach the signer set approval threshold (as discussed
in SIP-021). Apart from the signature scheme, the rest of Nakamoto's consensus
rules would be identical. This allows for a simpler signature scheme to
implement the rest of the Nakamoto system. 

## Iteration 2

Once iteration 1 is stable and SIP-021 activates, WSTS will be used to improve
the efficiency of the system. Leader election with BFT Paxos will be implemented
during this iteration.  This iteration will require some significant design
work, and will be fully specified in a future SIP which describes the hard fork
in total.

Figure 1: Nakamoto Block Header in Iterations 1 and 2

```diff
--- a/stackslib/src/chainstate/nakamoto/mod.rs
+++ b/stackslib/src/chainstate/nakamoto/mod.rs
@@ -305,8 +305,8 @@ pub struct NakamotoBlockHeader {
     pub state_index_root: TrieHash,
     /// Recoverable ECDSA signature from the tenure's miner.
     pub miner_signature: MessageSignature,
-    /// Schnorr signature over the block header from the signer set active during the tenure.
-    pub signer_signature: ThresholdSignature,
+    /// The set of recoverable ECDSA signatures over
+    ///   the block header from the signer set active during the tenure.
+    ///   (ordered by reward set order)
+    pub signer_signature: Vec<MessageSignature>,
     /// A bitvec which represents the signers that participated in this block signature.
     /// The maximum number of entries in the bitvec is 4000.  The ith bit represents
     /// the participation of the ith signer, in reward set order.
     pub signer_bitvec: BitVec<4000>,
```

The primary impact on the Stacks protocol is in the block header (Figure 1). The
Nakamoto block header must include a vector of recoverable ECDSA signatures.
This is variable length, depending on the number of signers who participated in
the block's construction. Validation of a Nakamoto block header requires
validating each of these signatures against the reward cycle's signing set,
summing their weights until the threshold is reached. If any signature in the
header is invalid, the block is invalid; if there are duplicate signatures in
the header, the block is invalid; if the total weight of the signatures is not
greater than or equal to the signing threshold, the block is invalid.

## Impact on Chainstate

Each signature will occupy 65 bytes of the block header. This is a small, but
decidedly not negligible overhead in the block header. In the worst case
scenario (i.e., there are 4000 distinct signers in the set), this would be 182
KB. Depending on the size of each block in the network, this could represent an
overhead of 5%-50% in terms of network bandwidth. However, if the signer set
distribution is similar to stacker set distributions in pre-3.0 epochs, we
expect around 100 distinct signers, meaning an overhead of ~4.5KB (the most
distinct PoX addresses in a reward set was 270, but fewer signatures than 270 is
required to clear the threshold). This is still not an ideal block header size:
WSTS is still an important feature for Nakamoto, however, concatenated
signatures is a worthwhile step along the way.

## Benchmarks

To confirm that this change does not meaningfully impact chain validation, one
of the authors tested an implementation of Iteration 1 block header.  In this
experiment, it took about 12.38ms to verify 300 signatures sequentially.  For
1400 signatures -- 70% of 2000, the maximum possible number of signatures --
the time to validate is 58.62ms.  Thus, validation time is not a concern.


## Stacks Signer Binary

The stacks signer binary is still responsible for signing block proposals. It
does not need to perform the WSTS DKG protocol for generating the signer set's
aggregate public key, but it still needs to perform Stacks and Bitcoin state
tracking in order to monitor correct miner behavior and prevent any
miner-initiated forking. Because the signer binary no longer needs to perform
DKG or distributed signing, coordinator selection is no longer necessary.
Practically speaking, this also obviates the need for signers to vote for an
aggregate public key in the prepare phase (which eliminates the failure
conditions arising from a vote failure), and it obviates the need for signers to
send Stacks transactions and spend STX (or require the signer to compel miners
to admit these transactions for free).

While signers and miners continue to operate in a Byzantine setting, the
consequences of Byzantine activity remain as they are in SIP-021:

| Condition             | Honest miner                      | Faulty miner |
| --------------------- | --------------------------------- | -----------  |
| >= 70% honest signers | Liveness and safety are preserved | Safety is preserved, but not liveness |
| >= 30% honest signers, but less than 70% | Safety is preserved, but not liveness | Safety is preserved, but not liveness |
| < 30% honest signers | Safety is preserved, but not liveness | Catastrophic failure (see SIP-011) |

# Related Work

The signature scheme presented in iteration 1 is
essentially the same as a Bitcoin p2sh script.  The signers each produce a
signature over a _sighash_ -- a hash over the block header besides the
signatures.  Signers can sign in any order.

BFT Paxos is a well-understood and widely-used BFT agreement protocol.  This SIP
proposes (but does not specify in detail) that it be used for WSTS coordinator
selection in iteration 2 of the Nakamoto signer-set signature.

# Backwards Compatibility

This change does not alter the goals of SIP-021, but it does alter
the means.  However, SIP-021 is not activated, so there is no consideration for
backward compatibility above and beyond that prescribed in SIP-021.

# Activation

This SIP is only meaningful if SIP-021 activates, and only
meaningfully affects the workloads of Stackers.  As such, this SIP activates if
(1) SIP-021 activates, and (2) the Stackers demonstrate that they agree with
these changes.

To demonstrate signer agreement, it is sufficient for signers to produce a
SIP-018 signed structure data payload indicating a yes or no vote.  The domain
tuple shall be

```clarity
{
   "name": "SIP-025",
   "version": "1",
   "chain-id": u1
}
```

The structured data to sign will either be the ASCII string `yes` (for a
yes-vote) or `no` (for a no-vote).

Signer agreement will be demonstrated if and only if there exists a reward cycle
N between the current one (cycle 84) and the second-to-last cycle of Stacks 2.5,
such that:

* at least 70% of the signers vote "yes" (as weighted by STX) in cycle N
* fewer than 30% of the signers vote "no" (as weighted by STX) in cycle N+1

This scheme allows signers who feel strongly against this SIP to reject it in
cycle N+1, even if they are not stacked in cycle N.

The vote results are supplied in a supplementary `votes.csv` file.

# Reference Implementation

This SIP is implemented in the Stacks blockchain repository, available at
https://github.com/stacks-network/stacks-core. 



================================================
FILE: sips/sip-025/votes.csv
================================================
Please Verify Signer Key,SIP Vote Choice,Vote Hash,Signer Entity Name
034df3feda207a1cd4f31ae2b58f136a0d382d23419ef8d06569fa538202ba8aed,Yes,014959b57f14e0ac5c1e5e9544f77149508585ba7f5555445c789a17f242f562c5141636b82eb977e79ef8872e2c51a8458e4e60d0c0f974dd54466c28a5424ecd,Chorus One
02b20a0603a409270d4421d89a831e8f7b2fa7c5f2d8872d7aa94737334d10c194,Yes,014ae940f533560c03f3c035c260e08911a6c9fe0ced596cd9c8a4a381ad92104b087e9de3fa39d7f3877120681820e7bacbe0f28a6217bde66f0134da39c08c1c,luxor-stacks-signer
e076e4d2e24f,Yes,017019bcba419b6c825cf54992cc28f513f58e121a6c8ef496fdb3f0056b52b6306cb33d75d9619b2172c4e5c4524a26c1e635c6c194acae0702ebdef93b165e0d,Stacking DAO
02c54d8b1ba4b7207f78f861c60f8a67433c264a11ac9b6b7773476e9f6c008e49,Yes,0128f2e99304106a322f3ea54f71fc3a9f5b9d33bf6c4565bd4efaa6ab74b4e4f25231a9a2cb773f2e1b74eddd27a40fdc2d38beb3edba4e1f05ddb9add7854996,InfStones
0215245613e31de2ec2e7f2c4facb45724be2e49d9d42abb0a5e571322593b36bf,Yes,01dcbc8aacb7777435340a1f634e36a54751f6436e341ae790a0b48fcb6a130c5a5392fc4a267df006143fbd6c38a4f163faf60f7e99a2d79794cc44f626b78d3a,Kiln*
039dc5297b92c1f6b48f4a68e180b853ff6e8188fb78422652a90b8fe14941adce,Yes,012ac5c792ee205fb359ed3062d0e52ae907a37ff1195f0aaf215902c7f9aab54979a99b2f0269264054ef9314c09375eec45c4909f6657315811d31786a6fb1e5,Kiln
02254a34747123978819f2a90506f76cb057fe3fbff6d8721a0d9cf8e9412d0e60,Yes,0024e00247214e8184631ce78f2990f269b06801e87ce88d764f3fb1f1ec0fda0c657dd028522cd8406bd1200cf3eae90f4ab517951ab816cf290806539237b061,Chorus One
03cef32afac202346ac76a28e81e77ed497c3f22ce20ac54b496950b4ef0b74b2e,Yes,01ab8beeb22bd4db2b34c90c17b313d1774fed3458808548b0c81425c9dc7ad1390234239a302e7144c07006b1dafd13616d6ca68c9fcb0962cda4dc016caaa040,Staking Defense League
03a541c1ec2cfb32da48cfadf439c9b2f27d166bbffa18a178c7a6a0d54cfa7813,Yes,01f4f9ad555cdbfcf7b1a77a3ea9291103bc936d137c2e4624ac7e80b4f31cf41e079abc3bbc79f8daaaffadaf2e6c8d49215f761db2d053ac7587a376fc4121a5,Blockdaemon
03e0df37e83e43847625a0320456cb9758050a61ce76c2c130bf50242f27ba6d54,Yes,012223040a6a808515956a509a4b44e656e6fab0f9e788c6eff14ff66274086f481ad1094f3ddd1c558f586acc31c15943ab294857bbe859987520522874e91cb1,Alum Labs
03ed732eab6b99b90315f9b58ce9c3e2d1991bc4e9cfa59841535c0ef7dbba38e0,Yes,013a514ea2da121cac2a81e5881eedcee1a2aeceb89b8a0bc539627928c3f5e8bb7f76eb82ce6c8dd229fb173087b5dfe45c57dee01e08acd62dd40dcc4a2d953a,Planbetter Pool
03fb8ad634c6cd072a5dfb0a3b237e3134cfee64b2adb8246c168bb4f6b0aa220c,Yes,01284bf5da25407e672e0bcce293c1844d4e3b287982f9f1de39ee47cbf7d406b33545eb9ca46cbbb2ec9035c5d6aefd51b16f4dd9bf77984f2f47c7d6e7b292ef,
029e1245f007bd8f76d5ce67e759acd21f8b0f2538a80713468f7524bf3fff6136,Yes,017c8aa1b486b5c5ee0a49d05ce993649696624a83293599a1ede5443f1bf8ba4d7791ccd227336b20e40804cd619ac1fb176bc6bcfcd30f1f58ca809d84b61837,Luganodes
0321129d7a3e14cce66abef68b9a3d31d998f14e9a18b09d66aa1110fc604a3b1f,Yes,0170ef0c17704a69b65440778b36aeb347860457077a07da9dd1f60698bc6d36c240d6f39181ac897d9c9d35b4d6601694187ecb14a49d66c9811363dd95204eef,
03cc1da6f6235699284987f7d3a98a950b0c693cdbed87ab33c04f61e2dfb6a177,Yes,01612e9945ec7731a40f906781076dab396508da714f641045c1dd24d009a4d1370412073a2f44ff828a4f72728df50a6370626956d4f1c6fe538595d9c316cdfb,Despread
023d6ecdc36fa1e1c6a9f116c7f13ae843001ed9d617f66f6c68cabf751bf82555,Yes,00231bfd8c638cf3f7eb9ef92cf4742e7c352c3b328c45606f1588de9a0ec8c577532326710d61e2b413014e172feb59192c5848fa4974f000b5402ad9236e1f5a,Fast Pool
024f164c6e73df283d34d7d9cc86553a82dce76045ba7dfbf4de0004f89eabb8e0,Yes,0103258e9590279cf9c6d9b711f1cb78938b6220c89ca984af7a9ac57681437c197d47d37914b67babd862160c2868990d7dcc24e822de686150087a94ccedcca9,SenseiNode
0244869db071d334ff8e5cd94956ae7b60a4abd41f83f3c9d66ab314718151d94d,Yes,00c7468ed99e8f67e3bc95ab04d4228df05b4c48a1c776996e1eaa767e432e614a0ce4f4c7a667c59d042fb1863e01f9a1a073a0bbca0db2c359e8cb6ed72cb352,Restake
0284df4505c6318a0017a7848aa0a95bf8cd3db697a89d2ec1978a027bece770ef,Yes,007efbe5ff9022e9cd8eb5f51c1b9b026392d26cc6883eaaba29c472b0e01f09436d59c4ea428fe49a059380caf9f468cc0cb90b406e32bd1885058053824d0380,Degen Lab
0303144ba518fe7a0fb56a8a7d488f950307a4330f146e1e1458fc63fb33defe96,Yes,0112b2bd6204e543ca5c88036311f62273674cf677a80db1c484c4d1ade3fd4e16219cc8fc12bcdae725d9c0afeb5cb7f0086d7d7bbf48347531a5f967b67170db,



================================================
FILE: sips/sip-027/sip-027-non-sequential-multisig-transactions.md
================================================
# Preamble

SIP Number: 027

Title: Non-sequential Multisig Transactions

Authors: Jeff Bencin <jbencin@hiro.so>, Vlad Bespalov <vlad@asigna.io>

Consideration: Technical

Type: Consensus

Status: Ratified

Created: 2023-08-30

License: BSD 2-Clause

Sign-off:

Discussions-To: https://github.com/stacksgov/sips

# Abstract

This SIP proposes a new multisig transaction format which is intended to be easier to use than the current format described in SIP-005.
It does not remove support for the current format, rather it is intended to co-exist with the old format and give users a choice of which format to use.

The issue with the current format is that it establishes a signer order when funds are sent to multisig account address, and requires signers to sign in the same order to spend the funds.
In practice, the current format has proven difficult to understand and implement, as evidenced by the lack of Stacks multisig implementations today.

This new format intends to simplify the signing algorithm and remove the requirement for in-order signing, without comprimising on security or increasing transaction size.
It is expected that this will lead to better wallet support for Stacks multisig transactions.

# Introduction

Currently, a multisig transaction requires the first signer to sign the transaction itself, and subsequent signers to sign the signature of the previous signer.
For a transaction with *n* signers, the final signature is generated in the following way:

```
signature_n(...(signature_2(signature_1(tx))))
```

There are a few drawbacks to doing it this way:

- The order in which the signers must sign is fixed as soon as funds are sent to a multisig account, which limits flexibility when creating a spending transaction from a multisig account
- The process of signing a transaction requires each signer to validate the entire signature chain before signing, in order to make sure it matches the transaction.
  This means the time to fully sign a transaction is `O(n^2)`
- This does not reduce the size of a transaction, as each intermediate signature must still be included
- The algorithm for doing this is complex, and several developers have a hard time understanding and implementing it correctly

This document proposes having each signer sign the transaction directly:

```
signature_1(tx), signature_2(tx), ..., signature_n(tx)
```

This would address all of the concerns listed above, and would not increase transaction size or make it easier to forge a signature

## Examples

Imagine a DAO that has a management team comprised of five members.
They create a 3 out of 5 multisig account on Stacks.
The existing multisig standard mandates that all transactions from this account be signed in an order which is established upon account creation.
The ordering requirement creates a hierarchy where keys near the start of the sequence have more flexibility than those near the end.
To illustrate some of the limitations this creates:

- In a scenario where the 1st member initiates a transaction and the 4th signs it, it prohibits the 2nd and 3rd members from signing. The responsibility then falls solely on the 5th member to finalize the transaction.
- Once the 5th member has signed a transaction, no further signatures are possible.
- If the 3rd member initiates a transaction, only the 4th and 5th members are eligible to provide subsequent signatures.
- Initiating a transaction by the 4th or 5th member is impossible, as there are insufficient subsequent members to complete the signing process.

While such a multisig setup might suffice for smaller teams, as the number of required signers increases, it becomes increasingly difficult to create a transaction. This SIP aims to remove these limitations.

# Specification

This is intended to be an update and replacement for the existing
"[Transaction Authorization](https://github.com/stacksgov/sips/blob/main/sips/sip-005/sip-005-blocks-and-transactions.md#transaction-authorization)" and
"[Transaction Signing and Verifying](https://github.com/stacksgov/sips/blob/main/sips/sip-005/sip-005-blocks-and-transactions.md#transaction-signing-and-verifying)" sections of SIP-005.
For anything not mentioned here, the rules from SIP-005 still apply.

### Transaction Encoding

#### Transaction Authorization

Each transaction contains a transaction authorization structure, which is used
by the Stacks peer to identify the originating account and sponsored account, to
determine the fee that the spending account will pay, and to
and determine whether or not it is allowed to carry out the encoded state-transition.
This SIP affects the spending condition encoding described in SIP-005.

Per SIP-005, a spending condition is encoded as a 1-byte hash mode, a 20-byte
public key hash, an 8-byte nonce (big-endian), an 8-bit fee (big-endian), and a
condition-specific payload, depending on the hash mode.

In addition to the hash modes specified in SIP-005, this SIP adds two new hash modes: `0x05` and `0x07`.
These numbers were chosen in order to maintain the following relationships:
 - `is_multisig = hash_mode & 0x1`
 - `is_p2wsh_p2sh = hash_mode & 0x2`
 - `is_non_sequential_multisig = hash_mode & 0x4`

| Hash mode | Spending Condition | Mainnet version | Hash algorithm |
| --------- | ------------------ | --------------- | -------------- |
| `0x05` | Non-sequential multi-signature | 20 | Bitcoin redeem script P2SH |
| `0x07` | Non-sequential multi-signature | 20 | Bitcoin P2WSH-P2SH |

The corresponding testnet address versions are:
*  For 22 (`P` in the c32 alphabet), use 26 (`T` in the c32 alphabet)
*  For 20 (`M` in the c32 alphabet), use 21 (`N` in the c32 alphabet).

The hash algorithms are described below briefly, and mirror hash algorithms used
today in Bitcoin.  This is necessary for backwards compatibility with Stacks v1
accounts, which rely on Bitcoin's scripting language for authorizations.

_Hash160_:  Takes the SHA256 hash of its input, and then takes the RIPEMD160
hash of the 32-byte

_Bitcoin P2PKH_:  This algorithm takes the ECDSA recoverable signature and
public key encoding byte from the single-signature spending condition, converts them to
a public key, and then calculates the Hash160 of the key's byte representation
(i.e., by serializing the key as a compressed or uncompressed secp256k1 public
key).

_Bitcoin redeem script P2SH_:  This algorithm converts a multisig spending
condition's public keys and recoverable signatures
into a Bitcoin BIP16 P2SH redeem script, and calculates the Hash160
over the redeem script's bytes (as is done in BIP16).  It converts the given ECDSA
recoverable signatures and public key encoding byte values into their respective
(un)compressed secp256k1 public keys to do so.

_Bitcoin P2WPKH-P2SH_:  This algorithm takes the ECDSA recoverable signature and
public key encoding byte from the single-signature spending condition, converts
them to a public key, and generates a P2WPKH witness program, P2SH redeem
script, and finally the Hash160 of the redeem script to get the address's public
key hash.

_Bitcoin P2WSH-P2SH_:  This algorithm takes the ECDSA recoverable signatures and
public key encoding bytes, as well as any given public keys, and converts them
into a multisig P2WSH witness program.  It then generates a P2SH redeem script
from the witness program, and obtains the address's public key hash from the
Hash160 of the redeem script.

The resulting public key hash must match the public key hash given in the
transaction authorization structure.  This is only possible if the ECDSA
recoverable signatures recover to the correct public keys, which in turn is only
possible if the corresponding private key(s) signed this transaction.

#### Transaction Signing and Verifying

Per SIP-005, signing a transaction is performed after all other fields in the transaction are
filled in.  Summarizing, the high-level algorithm for filling in the signatures in a spending
condition structure is as follows:

0. Set the spending condition address, and optionally, its signature count.
1. Zero the other spending condition fields, using the appropriate algorithm below.
   If this is a sponsored transaction, and the signer is the origin, then set the sponsor spending condition
   to the "signing sentinel" value (see below).
2. Serialize the transaction into a byte sequence, and hash it to form an
   initial `sighash`.
3. Calculate the `presign-sighash` over the `sighash` by hashing the
   `sighash` with the authorization type byte (0x04 or 0x05), the fee (as an 8-byte big-endian value),
   and the nonce (as an 8-byte big-endian value).

See SIP-005 for definitions of `sighash` and `presign-sighash`.

For non-sequential hash modes `0x05` and `0x07`:

4. Calculate the ECDSA signature over the `presign-sighash` by treating this
   hash as the message digest.  Note that the signature must be a `libsecp256k1`
   recoverable signature in VRS format. Store the message signature and public key encoding byte as a signature auth field.
5. Repeat step 4 until the signer threshold is reached.

The algorithms for clearing an authorization structure are as follows:
* If this is a single-signature spending condition, then set the fee and
  nonce to 0, and set the signature bytes to 0 (note that the address is _preserved_).
* If this is a multi-signature spending condition, then set the fee and
  nonce to 0, and set the vector of authorization fields to the empty vector
  (note that the address and the 2-byte signature count are _preserved_).

When sponsoring a transaction, the sponsor uses the same algorithm as above to
calculate its signatures.  This way, the sponsor commits to the signature(s) of
the origin when calculating its signatures.

When verifying a transaction, the implementation verifies the sponsor spending
condition (if present), and then the origin spending condition.  It effectively
performs the signing algorithm again, but this time, it verifies signatures and
recovers public keys.  Per SIP-005:

0. Extract the public key(s) and signature(s) from the spending condition.
1. Zero the spending condition.
2. Serialize the transaction into a byte sequence, and hash it to form an
   initial `sighash`.
3. Calculate the `presign-sighash` from the `sighash`, authorization type byte,
   fee, and nonce.
4. Use the `presign-sighash` and the next (public key encoding byte,
   ECDSA recoverable signature) pair to recover the public key that generated it.

For non-sequential hash modes `0x05` and `0x07`:

5. Repeat step 4 for each signature, so that all of the public keys are
   recovered.
6. Verify that the sequence of public keys hash to the address, using
   the address's indicated public key hashing algorithm, and the number of signatures
   is **at least** the required number of signatures.

When verifying a sponsored transaction, the sponsor's signatures are verified
first.  Once verified, the sponsor spending condition is set to the "signing
sentinel" value in order to verify the origin spending condition.

#### Additional Recommendations

While this SIP allows signers to sign in any order, the ordering of public keys in the transaction auth fields still affects multisig account address generation.
When funding a multisig account or creating a transaction, it is strongly recommended, but not required, to order public keys from least to greatest (equivalant to lexographically sorting the hex-encoded strings).
This will remove the requirement to remember key order and result in consistent address generation.

# Related Work

[PR #139](https://github.com/stacksgov/sips/pull/139): This draft SIP was created earlier but lacked the technical specifications for implementation. The author has since closed this PR in favor of this draft

# Layer

Consensus (hard fork)

# Requires

[SIP-005](https://github.com/stacksgov/sips/blob/main/sips/sip-005/sip-005-blocks-and-transactions.md)

# Backwards Compatibility

The Stacks Blockchain will continue to treat multisig transactions using the current format as valid.
Existing multisig accounts will be able to use the new transaction types to spend previously recieved funds.

# Activation

Since this SIP requires a change to the stacks consensus rules a community vote is additionally required.

## Process of Activation
Users can vote to approve this SIP with either their locked/stacked STX or with unlocked/liquid STX, or both. The criteria for the stacker and non-stacker voting is as follows.

## For Stackers:

In order for this SIP to activate, the following criteria must be met by the set of Stacked STX:

- At least 80 million Stacked STX must participate in the vote to activate this SIP.
- Of the Stacked STX that vote, at least 80% of them must vote "yes."

The voting addresses will be:

- Bitcoin **YES** Address: 399iMhKN9fjpPJLYHzieZA1PfHsFxijyVY
- Bitcoin **NO** Address: 31ssu69FmpxS6bAxjNrX1DfApD8RekK7kp
- Stacks **YES** Address: SPA17ZSXKXS4D8FC51H1KWQDFS31NM29SKZRTCF8
- Stacks **NO** Address: SP39DK8BWFM2SA0E3F6NA72104EYG9XB8NXZ91NBE

which encode the hashes of the following phrases into Bitcoin / Stacks addresses:

- **YES** to Non-sequential Multisig Transactions
- **NO** to Non-sequential Multisig Transactions

Stackers (pool and solo) vote by sending a dust stacks to the corresponding stacks address **from the account where their STX are locked**.

Solo stackers only, can also vote by sending a Bitcoin dust transaction (6000 sats) to the corresponding bitcoin address.

## For Non-Stackers:

Users with liquid STX can vote on proposals using the Ecosystem DAO. Liquid STX is the users balance, less any STX they have locked in PoX stacking protocol, at the block height at which the voting started (preventing the same STX from being transferred between accounts and used to effectively double vote). This is referred to generally as "snapshot" voting.

For this SIP to pass, 66% of all liquid STX committed by voting must be in favour of the proposal.

The act of not voting is the act of siding with the outcome, whatever it may be. We believe that these thresholds are sufficient to demonstrate interest from Stackers -- Stacks users who have a long-term interest in the Stacks blockchain's successful operation -- in performing this upgrade.

If the majority vote is **YES**, order-independent multisig transactions will be enabled upon reaching Stacks Epoch 3.0.

# Activation Status
At the end of cycle 90, the following vote was calculated. A total of 118,632,231 STX participated.

- For solo stacking, 100% voted 'Yes.' Total voting power is 3,449,000 STX balance with votes cast from 1 account. 
- For pool stacking, 100% voted 'Yes.' Total voting power is 114,914,556 STX balance with votes cast from 75 accounts. 
- For non-stackers, 99.9933% voted 'Yes.' Total voting power of ‘Yes’ is 268,674 STX balance with votes cast from 157 accounts.  For non-stackers, 0.0067% voted ’No.’ Total voting power of ‘No’ is 17 STX balance from 3 account.
    268,691.89

All voting criteria from STX holders have been met. A breakdown of the transactions can be found [here](https://stx.eco/dao/proposals/SP3JP0N1ZXGASRJ0F7QAHWFPGTVK9T2XNXDB908Z.sip-027-multisig-transactions/results).
A copy of the scripts used to tabulate the solo and pool stacking can be found [here](https://github.com/stacksgov/sips/blob/main/sips/sip-027/scripts).

# Reference Implementations

To be implemented in Rust. See https://github.com/stacks-network/stacks-blockchain/pull/3710.



================================================
FILE: sips/sip-027/results/multisig-dao-votes.csv
================================================
voter,txid,for,power
SP360XZY8BAEV22YC2E1S7STRBRZWN8WEP07MFPV6,0x6b589e691f9172ee0e25eddb20b7fcc8b900d4b66a1cd96c352440341eb42877,true,1100000
SP3YAYV2F7GQV833K0J72ESAVD92MXE46N7SZN58R,0x34bcde19f393565deb8eab26cb10cac72f5342ccfdd60b79441230f27ef3c545,true,1419822
SP243QG2P4SY34JVGDRGGVW5FNE9XWQZJ77PRFHRP,0xd4a819f99c6ac9fab2a8b6e2c330cd3cd13528487de36865b8a15172e32c9e28,true,1275413
SP39YBTTN2VV61F6AZRVT9F75SDPCTKH0TV313CEN,0xe6ad85f0c9496e88000e02b684dfe5a726058b59a9f4431c8ca2ad81147e124f,true,1100000
SP3HWZB4KFBSWK886D6CK4ZBZ6CTFM2EXJKVDETZ7,0xe385bf4b9a7f5875ee3d5f30ea818c53957882c67c79bb80c3cbb16bdba3ec9c,true,1100000
SP1A6SG4G6FCJCP10QK9NKDH2KD6KW1WPG1J354ZP,0x6f01701c77352261a4ab82dd6af7a051d3135151411b0e370d84cc98d72a4a1c,true,1150000
SP2SACH111M97FZWN2Z8XMJ1FCKSJM3NGE37MGXAT,0xf784396f0f315a495fce9d945bcfbfb689cf5e073c93b6332bcabbd9651a2f4c,true,149124536
SP28F5HQ6KKNJ2ZG8016BGB2VJHBW9ESFC3RAHQP7,0x6b24eaf250e937b205dc56533aa4eba55fe21249daf54e048f4bb98d62558476,true,10808425
SP2CEBH7PWF2SJ1CBH94TMT0D08P462HRGBKHFM6D,0x8b864356d9d6d5f520705adc83009f1a8b717b415665770f2d82aca55a7a704e,true,2285260
SP3X8T8SA3FPRK6S8RD5XZEH9K44SP3KFJFEP4SQM,0xf88659464d5fb413388b2600b17269e7ca8055d9ef9589cab791cd9b43a7e529,true,1574211
SP2Y6PN1W5F97RZ2ENNSAADVWBFDF3GCVC4YZ71CN,0x80993eed69eaf82076a097a6205a637f6c9c495b733bdea053e93f7b8b5085e2,true,199662565
SP1M2KY35ND63DRY71WNSRH5JA2Q5VHZ0HXF8M6RJ,0x6d8d1a34794fe7871de30b4ed5edcef8108764d5dc62531d88ed059c70c56ce1,true,2000000
SP2FGK1JPBZ25SXCV7Y3F9B5RTW9EB5R4VVQPB0SC,0xe2d67e72aafeb1d5d53c7c5ce55bbef7cde5ca35964c89b4f80dda4b1d42e50d,true,14598090
SP32X4AF7D5JNA0PRFBEVRRT8K57C5B6WFV130Z5A,0x2b6dad48e03326a4e05d1d427ade5053a14bef0ec307af5f5e30aa4aa8aad122,true,3043660
SP3G0FTJARHAF89P14SX1P9E3E9E4HT008VX2PNRZ,0x673ffb5999adaaf2e79789eead5f2bbf1ccc553ac7643315d490ae98567995e8,true,2130613
SP18DGDASP836GWESYYRBCF3S6XZBWPV8GBV82TJS,0x5ab4363f85bf926005db51653614d3dbb096b60980e062b94b3d07c19294779b,true,2050975
SP1JDYRCVFCQ3DTXM1G6Z5ZDPJ9BB205RBQ7BKW7B,0x7355f7132a7b991fc54185e4cecf64881ca6aaba06eb720421dfb7ee99267b2d,true,3170063
SP3ZQ9D23C0A5S2QC7AR7WDFRWFW0CVF3KC07HTP5,0x66d2ec46f5f7fb45dcef73c82b5b371c43e082c1e583dcaf7dc4a5f9c445d334,true,1900000
SP2SDZ8CB9G3KQ0A5ZRXJBWQ38TTG45AR1957PDFP,0xcd356668c8d2508f9c8c5a29a243754e3b3e26706735097827dacafba2a9317b,true,2477234
SP1T07GK9H4M0WP4N1DSSA7NJ7GNTQZ0GBZM0GAR2,0x16fab55123e197aba0cc5b61966ca57fc20b419e37c5f724ca9bad13516756cc,true,100381915
SP1YS34MP7V0DPYSXD80C42M36D5TJKFCZ60B3AEM,0xc4fdcab3d5852be1b7d9d4e87a909fcb00a02734e71a132739585eeebfc03ab0,true,1989920
SP38WCGSSQJBFAKH77R93AMTHBBEF83DQ6EJ358F2,0x135de50022a20706c5a33634604981e1a1d54afb66eac0af7925f52ebb155000,true,792210062
SP26STSDW5X5YY5N5DRPR4VDJY86FPMB4NZ0RNBW,0xc1194852e9e75208d47933d0bd07472ec3c16c539fe6ec8e65091836fdb4312c,true,44225357
SP2W4AH8RHNHQB9C1600D6QVCF59NCREBW7YEC8VF,0x3119743f6debbde26f85f517c41693d77fb649eb44b64a97bab562959d1657c8,true,4451447
SP6SVZRG52SS35ANKZR0RTBE0CN982E3AJZZKZF3,0x1c9b1aab039017a0fa74f11a15f26afeb0c700b87dcd2fc2b1364de16530aed5,true,12620962
SP1P882HWHCTBKEPPEDZ1MY2CPKF1JJT2XMFNT289,0x7a60a26e51d3493386aef7bb41a4d7d7d15293af4c25607c35d510ac78f46a7e,true,23037346
SP2RBTTFGDXSH54SYBKZ0XEXAAWEY4DWTVNXGD7XM,0x916cc328fb5b005301a8e4679c574a0ce08767a8ed238f0f4d8c22d72bce3d62,true,6881872
SP223G8A01JPHS4PKHEK8AMPKGKGRT5YKQF7VVA4E,0x44377b4e2cd03b6033dc7c319cd99cb8f57949bfe990106dd9aec09ac3ee3421,true,11044433
SP19ABGPHMYDK6PA9D9NE0FCCG8NF0TYEM74MVQQ8,0x6cf1e24e59a4350e37a66b505394626dd6701df99f7efcd9c285b7b7ec58f9bb,true,6932974
SP1B46TPZD8Y3ETHGZYJAPHD9GHJK81K08WRB127X,0x22ee15655bf20b3720b6ac5d435edc030a174e6b9ee78312d098728147dcfc28,true,2653141
SP3AMF8Q1X1THMT6YJ8D7B65NRT7ZN7YD92QG27MY,0xa10229ae62509fb04427f23546ca80be870460bdd3dcda5046f3847166cec5ee,true,2302773
SPTV5V2TS7H726FBHQB04RF905XS16QH2DQE065J,0x031a8e8c55ec4cd19fff5f8dc127889648c499f902919f7690423ab203edea9a,true,2059926
SP30QCGX85MZVBAMH0CH024CXAVA6F4T30PBXN67A,0x7c7ee7f754b057ddd1632bcc83574bf5ee3b3d10aa7dfda2e8ecf3bb50faa5cd,true,4299058
SPJNGNX5RBR9RDWWANG1AJ6A5RJKXMY32M0YK4SD,0x6ffddfdc3d232fd7426fd0383cc0e4af38f10ae23ed812417b884e678b7ba11a,true,1391896
SP1PAGYEDF35JACKPBBTDRYDTV84ZAT0FAMCC38V9,0xfa16a6d35cdf908f085d002122d8c816954116bddee92ee86a8d747c782b0a2d,true,8969819
SP216Y4DYSSBMMEACTMNRFYAWQZ1GWY49DJWH54PC,0x51751fb0d4d3fc2ee9feb4918cc499a4a659f64373c3cd32c6c81975945d1b2e,true,1475030
SP1K30YJE3K05ETW7MBQP8VM2ZC5DFPECT2ATXDPF,0x34641dc4439c406ea15b5fdd07f57c416f5f6cd207584fa3d4de07751efc9a0e,true,18438824
SP1B09WJ17REKAASWXMHN49Z7Z993G71Y4P7MVX7T,0xdc496a1109a0d23624900f2189281e624ca96aa1b27291e1c82d77ecbaffca9b,true,5420429
SP1A4ZE8AKBVWHCN72CM6018XCRZSR6ED8VD8Q7S6,0xeb156e804eb842cbb1b2f8839fadb5d245c631a35a2743f2e7bc42942e4a0c4d,true,50746561
SP2PFT921TWX6G1S9S70FMTYB3X3YJD4NC8WFMKBF,0x7e617f9e0944df9cc9d7e6874e10cfee986636bdaf6addd12771369234e156cd,true,2011839
SP1W5XQ730V53A4CTW8DK5KD1DSMEGN4ZK3FW6NBF,0x086dc96ec55ef32a98191b5198e04813c4b54556e6956a817465be6e4f58b401,true,2125916
SP2TWFDGSTC741C2RKGG6X2RNZ3TZASTJPHQQF0M0,0xe0624a10a09f0b9882f5cb7a06b80adcbde272cce78229309e80845c41aba745,true,7002142
SP3XN8VRCGT78C7CTBEXJZ9EB2AECQ6E5WY4QT8YR,0x9fc008dafac490fb3c6a2e0a771c60f50c9c25a893afcb6eca012fdbe2f946bd,true,5997023
SP2GP1FQ7TPTTHJYCCJKE5C9MT2VXRN50KZ4MJ63N,0xe765839d20a8267757ef62656eb08f2b3949544ab6703dce643079df2dc9e521,true,11371407
SP3CTQWREGFB5FSFH4BF7F0637ECECXX06QDBVBF,0xfbceee700edf14ff7269b45d340bfde2fbc19d634d78addf824652300b8e2085,true,6219698
SP27G4BAETJAXHDNCGVAC2036476MC3BE9K87CJ2D,0xe10880b801a501b886c33b46aa484be684d5462b8d338d89ac23898ec7943315,true,281975036
SP3ATPYJHSG4C9H48RWGXJN913QSY8KZ09KSD88GS,0x39caa83ab3bf245a9ae04c95d2686ec830e55b1f63963764cb69fae637630d34,true,14696377060
SP14ZYP25NW67XZQWMCDQCGH9S178JT78QJYE6K37,0x0630455c720bea171468c8d7ddb689089fe45143e5fc344e20fd29101ee855b4,true,389439881
SP1B91MKXWMBQP50YWCNR08XZKBJJVSJRHB72SBX,0x427b2021a3e0b847028d9e6ab19127e13dc02ac98da4db87c73907a7e4cf855d,true,1875446
SPQ3STDA3G4Q6QD716425BE7A2G378QFQ10RJK3V,0x4c24606902bba331c47e56a88ba665fa0794a183caafdacc450ef351384a0781,true,306061104
SPBWF76FHRNA9C1A6ZZ896B3XRRK5TGGW7X9A55A,0xed7c02ea1483450bf214d2670926dc2fb821c35d40a8b3434081bb876a6a6e3f,true,9467197
SP3N8ZJBY5R6V4QNW7GR7GA6VG73WAYXAFPEMF69X,0x96f0c1a7511657cb231c240c23c95e5ad5ed9ad0eff3fb119fe377214bbb23fa,true,42916333
SP37Q561WR22AXA3EC9GJDN9QGK9K97Z3H940EV9Z,0xb423291333bf40bca78316624ca81c7e6bb24e9f72c8ebde9d70a0ea7e384d28,true,58684073811
SPYMQGWH0SXVZQY2R46CYWVX1CEVHHV34H76DC49,0x5a023c36563a47b13f95994457df838c5c1611136586736deb28fa65e1560b48,true,136599000000
SP3VCX5NFQ8VCHFS9M6N40ZJNVTRT4HZ62WFH5C4Q,0x63c503a1c0226de1684a734b0ae871dd711cddfa79efbbd3b87e4e891bb58e54,true,2900880575
SP7PSDAPGQ2A36G1EPX363AZFWS017Q6FXFFF2BX,0xb647255da1daa688063352f3dfcca6d5566105b7c34228e20f9b532d157d8c15,true,35792584
SP2944D80P2TQY1EY4E5RFWP3NZFGM3N6DEWPDTGX,0x286366ef1dd1fdeb0a657cfad67570370c505cd96968eb9af9a25a3d0c0c2406,true,1033986
SP2NHZDAMMEEASE4DKHYYCVAG8RF8PA7YHPPW40BX,0xe59e178490bbae99d864881a37f5acb4bea7fa66dcc152ecf676664b463a9fcf,true,515963211
SP34R4W2E28ZFF4NS3DXW1CJSP89BK07PC6GNXGNX,0xb0df1806fb668c760e57a385e9a75967cc207a3f32d00dfb152a06ebf216d3a0,true,5187547
SP2C1WREHGM75C7TGFAEJPFKTFTEGZKF6DFT6E2GE,0xc10ef54a4a385cf459d9b85370239a6051759b3d18789d8ae897fa486676cf88,true,1962188
SP3QGW69T7Q2BBB6RCCXGN6MCJCH10N0958W3GZ9Z,0x285e5360a798257679797411e7e4d421a2a789b453c10d0a0e3c2b477298eaeb,true,285597743
SP25DP4A9QDM42KC40EXTYQPMQCT1P0R5243GWEGS,0xa3bed0a79545678d321405f159ed287c655c201f72bcae50832f1e5d2f3ff9c6,true,19206167
SP3YS4Q6P6J2QF8K581V5E3GFAZWZ5YN6CMJY73QK,0xdc30f616eeccd486a6703d3fd88a585aeeb9196c6d4283b9ab090266209abfad,true,5641599
SP28PKVZSWRYRKCP10FTS2FXK3DN3F76VPYPVHMSE,0x57d534f824d6ae950347f0034ca27331c6838ca307e99a4ddcf930a583d592c9,true,1786096318
SP2NTAVRBEVVMDJJD0VV9FHDFY27DQCHG4RKP5A7F,0xa5757d27e27cbb8734e55129c884804a40ccde0f61d3bc4363d00864f67d4a2e,true,1494430
SP3GBCZAYVMYVAC5GN5MJXTK1PJ3XVYKYD25R0FJJ,0x1b3dab8c37a15e63ac50e834e0cd19c063b232826c177323677c2eb48ddca4ae,true,88997970
SP7T6J7JRKSAZH02G283M8GNCXT96BACHDRQ6B4C,0x8552b399f7c40c4095b2aba08e7e9ff5ad4ff5de3195669cfe92a61db9c3d361,true,2076695779
SP31A0B5K60KHWM3S3JD0B47TG3R43PT1KRV7V53B,0x8425def76fed01cb059f8e1a4a85277df53dc432d327000d25559d7040dea550,true,2097466832
SP393GB5D7ZYMH7AM6RMACBJMW5DMJ1JM6A7BRXCZ,0x491746e750d3b1924f93a4d261023b53a1bc6e0896ecfc276d0508504216cad1,true,1924917
SP25HV48GJREWX3CSGTTV6J9CY2TYCXP3JNHK2NTG,0x0d513cfc4d76f2ee398debb213c51ce67300ba4d954f42aabeb5749bc974f749,true,67390824
SP1R0X4XT4B3731JYXM52BZ7HSYHNREFCGY12W9N0,0x2576c45583204a31206c3f38772e211abfd1995374b8650cb46da77d705f8fa2,true,2510115
SP23S4KHTBQADHS6Q0EQVHTC7Q9YRGBSD0F3X6QY,0x29f504fab7863323ec2cc6b35162f79474cbfce4cd2926ded502a3cf1da0102e,true,1158376
SP2ARFMQ4BXJ5K7M28QDCH6JV3WY51TJ14054AENV,0xf234da697a5de48784f59d4d4f4bc42f5e1764185dfe41461a350adfd2988f59,true,7927820
SP34HBB15K9P54ZRK2PEARGG0PW98QGSV92YKQHEW,0xa5ecebc041672d186e74175bee5c446e375ad4a50ebafe1feccb13fcc17a4100,true,14009107
SP2KZ24AM4X9HGTG8314MS4VSY1CVAFH0G1KBZZ1D,0x6d6ac6139a7935a36e7c48ef4c0b59892278ad63fbd686178cdd9735a98f38dc,true,19226715
SP5NSFTWED17R0HG8K44YBS4QZ3WW1N9WXGA167P,0x7cf9b2a276f5c61c1d4935c03c526f1d52c2b905b2338d69461987652cfe3980,true,30993050
SP37MBZPJBVGVCDCBEA6EVKCY748VC48N7GZ842M4,0xb47caecc4dc02509e0293f30b335565d02e956e1e39ca2af2d7737e3f11f2ec7,true,3011540
SP35J1CM4FFGW6JRVJ53QR45AECB3H6W1BEVR5N3H,0x9159e84c59ca524f805da9a1cf01368a740c6cf5531bd86043db962f357418e1,true,3166827
SP2NPJCP8RY6ZSX7WZATECHTSQBNZ08WJ8JCW048C,0x7c2db30e12b127fad5888bdae20bed73a14a58f3fd7fa94d2a2ccdc45e264bdf,true,11159322
SP2GPSRRW1MXYM5N1011W17EZ8HWPYXMDY1X9Z00Z,0x935295afaa092ea00aea2c980798a31028214e213f57134562e617d24dc8f1d0,true,2561033
SP3SAYJ9YPDS3MK76QH9BAFR27DA86E3H1EATGDTG,0x955e2f30eb2050837dabd5ddaaaa1ec78da3fae87d5baf957787e2c524fd4529,true,3221610
SP28ZTJS8Q58ERK8MDNFGQA85CHQRP4SYH85B95SG,0x83718228706422b6b3e6a5de8ed6c974743d6a63af7d8fd6bf9c8b616cd6b659,true,179469834
SP3F0Z7QSRDR8GK66A714DPBDSE429N9RKV4MR0J0,0x1aeeed2960eb1453f00a4c790c5f70ae6413f561cbd5b482c9837f848a5e28b9,true,30078078
SP2J1NM0YR9S2SD6VKHCTQ18C0ZB3EEDXY1VN2ZPF,0xf5826bb4685e4624a76c6a040014a7abb2686041e33392344c3affeefd2a2b1a,true,23691902
SP10FVY8H3ZHKPERY1DYZNF0XNM1P7J8F1RAH70QD,0x836682b21cda2423f799831a7926623a73e45d340823eff7333bf3aae565bbed,true,2337541
SPRSECC45ZWE1MKDT8CMH5Y3MG4NRQ4TJQXWAKE2,0x1515faf1b9f195510e5b1af924de0bdc4eb573083ae7e80bf16237c53bb26efc,true,12984370
SPAN3P3RA2QRGM8V1J8JFDX583EFFT2V9RDCVTZC,0x6391bdcae175ed82fbc10eff92c240aa7ea8321e4537a520551208c81ea547bf,true,7228399
SP2XT9VQ08317BJQH0EXCK1HE01CBEC9B69XSTE1D,0x69f9e8b876134e7f389ff66c10e5849b275d9d89899732df8a67faa297795788,true,4000411857
SP1YAVCV34TT37ACR0ZD9JTASMF915MJMHCN8ENCQ,0xc10a2362fabf78b7a4c90054000f184e9e9a8385146519826686aa55ec931269,true,33655202
SPQGBGEETB0DG0P6S125WBR6HCX1TNFHDB065AY5,0x70d2ae8c12a01c66707d060c36431d2f502adf91dbcc134434ed45e02e42ad64,true,97864435
SP2881ZP80PJMGKVM6P4C37KHN6F8G044HAVR884K,0x5dca26cfc1905d0efa37269d3cd4b5c73b750814ba0bd1fc9486bb0645d9d2b8,true,99995585
SP22682J0RP4AJSJ1JYFBQ1Q79Q880BVJDD28BPTR,0xa28931e47657d275e7df83c2eac96e90fe1d8d223dfd4783eec3d4aca223b41f,true,8096272790
SP3GNQC2QSD5B3YGH3AASXZE30D4T040JWW8KBNPC,0x0b0ad925e077b1264d6ef0d13a8df32bccffbdda68296937ba9c9b961dd25c07,true,30868350864
SP264K42S3AGW5ZHWPTY2XZ1YYX7CBQPYVPD5SSXQ,0x44298828276898ca0758341d1fa2aeec80288c5cdd45a877c811e5828daaf9c8,true,98648635
SP1EPWNPPGEZMGKHFZ6WXEZHTVTKH0CT77NM32X43,0x8b67b8ab409c91c6609d9df0881e79d7b6a93ed443cb26c6a6fb2cbc87f7deec,true,6724828
SP2EK6MPWJYXM0JE3K19AWCDT0041DFPMJERAPP9Y,0xd827bc26a076eca2e98e2820cdf287a4d2244759d9c70974903d2e03c417f189,true,1000000
SP68C69NS28RKRZ4TTVEN538287T5BXH22M5HGE1,0x593aa596aee7d12e8dce73f6480f51716a1cf381be1cc813d68f866c48f7779c,true,6570296
SP1P458Q2Z3CZY9CHDJ3GS5THDHCYD7PR0BM5JFZ3,0x07a673d61903c466b94ee135a32d2a42b3fb92c536e0528843683d4b9be2d191,false,1000000
SP23BJCKF48J19360XQ31Q7D3E07ST9J5H5E1HMK7,0xcf4b3c223df6997eccc82c097d074fffc903671fec7155f7de0b4f7bf2f38d87,true,55939087
SP3QC4R6M7M0DAZBXSZCW4FWGDCNDD05FV8Y0AY8C,0xfc196b7b1847e56b7751896bbfe5233f8e6aad0dce4c710dfb5d3860a78aef00,true,6024689
SP330R59339Q2WQNVX43Z5AN1GCYMFJ9PN3K66YQD,0x2193120f378db28f230674f322c3416c7ac0f08cdbac044de9d59b5b3da9f57c,true,23786718
SP327AMYAAJFHDSDGE6AD0HTACYQ4CCXJGT47M2H3,0x8ec8a6d0d5fa42922c7aa544b584103ee782e085100b00aa2649f9b08ba774b1,true,7370511
SPM2JZ5R7M6AZQTXKEM94K63E2CN95TT6AMMA5PP,0xdee509d866df34653d33a1bf4bc168c2b2490e77b623d6a6043fd63feee20163,true,4668675
SP2EDRYCPGTS32HZAGWV54RAVA2GTW0WPBP4HGCXR,0xca069edecfdd31a86a5b756cf4d6c3feb422e7e580543ef26b8c8883c9e66566,true,78040928
SPBP4KDPZJJYV8N8JRHS9135V0YXBZDSA5MYMREV,0xbbea7173e7faed12b722ced51e18bdd34ccfbea62afc4392318382c91ed19416,true,2079187
SP3EN2WMVAP7SNVV1QJA0ZZ6TC3R0044FZXE8PQTX,0x2faa9541de7804cab36469b21ff3771c0a552ad308040622761baf260d5768c4,true,20704274
SP2HJVJQS0TRBTQ1WAWWN9H9W2HKGDZ7H5EZCEAQC,0x9ff584b12bc07a03a2e4ebac46b12cf72ac9c1423f5c06df0c7b34509d8f06b1,true,38329473
SP376Y7METTJAT372GYDGD225YE20A01GAV7KJFKN,0xe17d80aa58dbf4862443d4c91a7b89b02a79d21398222ff53dc762443a67e50f,true,377899383
SPAFRYT831WS7ZRHGZBPMNCBJRBC0ZT884HFXERA,0x147b7f2b8244915b97d53c1ee2a7b17fa82fa5faace72a252cd46412557ef885,true,1000000
SP12V92X9H9C6F04AFX4C7NDRRMF4WD0S2EX33865,0x6528f0715d222d915de09a56295566a66e311b0235f8b2c24626bed3e830a2ff,true,5274622
SP1VETYCVMJCCBNYXB0YYAWKGFA4MKMW2C21SR72A,0xdfbe828d66584220243f4affe024afda5d691ccb72e8364fc76d6db3e01e5e30,true,4676800
SP1ZCGABS83EZGVNRNBANM585EKFH018GNB1X06DT,0x876fa585d65937dae8ca1ca3302fb6b917c7426f60ef9f5c03ec57e622b0450c,true,4376800
SP1PV390R5TW2PHCCJT1D0621WP9VXQD4J7SGMNQT,0x54ef411aef1087782986d1850f0bec89e486846d1d79aeebecd8e24813479700,true,5076800
SP18APAH9C1EPBD7QVGMNEF298CB9C95CMVW3M21P,0x2a4082f1e9a3be0616dc50a5e1b9c38b4a1cb9fad6a295e6881edb5372431bf1,true,5570232
SP3D5H0YZZBAY3XBFVRDT8AJEK6XDM3X623SHHQ81,0x9c732f5e4704e9d3d1688f4ce3e516c4ff49a681f03906d2be2e9493fe307a25,true,2441354
SP2J3F35AAWDTT52RDFR437D32TPAEE10NF9K0ZH8,0x8677cb2efe8ca2dd7b4e1d9320096ec16f63e0f4b0a19b6fbeef4a41ce8f1b62,true,2440668
SP3D9XBW1Y39W3X2KK5GAF4KYTGW3KVPNS4R2H2K7,0x8005add3b23709f4aee5dd6271bee639247f811ea5b34403823b153d1db1135a,true,2240668
SP3D4E8CVDPE7YVQAYAGRD9B43F53E13NYX5K0JVX,0x7b2435259b68b57b615df7314840ed8f17fdaf90e0363bb90d638955db987d95,true,2340668
SPFDXVD3GQFS77A112E95QTC7Z0JHC3W5G6C3PH5,0x9e3893e9cb98ffcd54879f9c52f40b65e8e2f6920f31472655a1c9c83a8a6f1e,true,3132715
SP2C9K1150C6E900YWGETMBZP6R4J1JMR3TWN2SHT,0xe9c8cd25893c318a2267536fb7fd4685672cbdc316a6ab94bf75ba9c82fb464e,true,3100051
SP1N6DW24K1SWHV6A4QYZGCJ9E9EHG0X7Y0MYAQ00,0x288488e59fbf3a86d4575292e0e2c2b4f0329812a20cd368a88cc0cd85529f1c,true,2100051
SPRW9XNCTE0RDS04D0Y5HHA5PDKR2A41CBAR3PB6,0x2072e90ed3d7adc208b40ec8d00fcbb97cf98eb2a1218462b1549b492881efdf,true,3100051
SP1GPX3ZYJNDX1509F4SENPEGT2EC4PV8AAZDAYPM,0xe37d0a31771d22ee41a34ab5e7f2505442dda4284584640dbe8d3115699e4b3e,true,3138673
SP3ESSFQ8Y0ZXBZB5XA60BFVV9NMTFR8Y1NCNMBGP,0xb45c612c8ff55b17a2630ec432d489fc3ed986dc67ea1fbf83b29e37d33d4c4a,true,1263785
SP3GPV7YEVS2VNFYYXEJA4HWXA0HFX4SMFK9F12P7,0xbb8e43a55aa7ecdb02df524286d0743d6ccd8072ace302e9846c46f0a969cf6e,true,165210513
SP2N7VSJ2DT9NY438G3VDWYFP3WWBKYN46GQPHH6T,0x1702a8613357c712683815424d5b8db2449b91f70aca1c01226da977b5c0aebc,true,18314864
SP19NPW1QYFAVJ4DFY9C29X9MMVD1RA3SGK033EZ8,0xf4d7cfd80c37cc7e0c7074120c9b0df34194d34ec02e5ed05fbc60662f775276,true,3153952
SPSEBFRZZEZSHGRKRR1Z55RX5AWHER3CYM0H9BMW,0x3df0996ef298010aa2fbabb280b326fc526eded19d5db84393ef6d9424f06866,true,996167964
SPXZJPEQ3P0721P7HTP2Y27DAY216Z3ZNQYXAWFR,0x37139a5435f6ff0fd9bcf7a7da528db377f822b38cfee6980befa336f9b3bbac,true,1865528
SP281NBPA7H99TPEBB22J1Y360GE3Z6735NN92C4D,0x410954df701dc226ea822a0c703ef77c2f17c00078b70991b0872e4f06767933,true,1464317
SPQ2AT2319NV91VDRXV1M6CJKKCBTBJ6RZYN6RE6,0x17c5ce3209c69f641099feab61783a8fde1ba3730b14dbd3a43f4306efd2349d,true,1991244
SP1Q1R96THZA9THXF2F0ZAJ7332Q1GHAPD97B5HF0,0xd6123d89b19dd0226dcbeea313e76a3266437ccca14ebb4c95546b7b9eb18bd4,true,1947299
SP29X2GDNP6SJBCS50W5C45WW3WZKENCHCR2TWCTJ,0x0925ffeb47e92cb4fe8e9f8ec00fdb56460e660d656c8220c52bf4f78457e605,true,2247299
SP25SWAJ0NXMH2EHEWE02VRW8VSY0SF7SQ9BFM0BK,0x831cdd24d7cb6947b57b2db56513ac8aa9816df95f1c9024fc951c4b5a80ec2e,true,2749477
SP3DGEBES323CX9KV5GAJGC8SRNWFKC1NK0GK6BH,0xd28f1dcf8f15a3f16cff71a19202f8a82aa43c0ecfcfcb8cf7871ecbcd3e9b07,true,2949477
SP1W2FZTH00ZEYDTCD62A7M5QFERRDHCH260B0QXF,0xb732c8117503b267ac8ba2c2a0b2cae133fd8553054d318148a247b43aa97d6e,true,2749477
SP13R0ZZW68NH96DF1JZ65B543TBRM6FPTCC05G39,0xbff981631fcdc08478151bdee0ab6f19f857419a24a9cbe554ae0d5bfd9d90e0,true,3420963
SP2F02FRWRSG74NH8CDWNHSRWS8YHBH04451R3ZXT,0xf9ac4dfb6bd1f47a7be605d79dda78d6c3de4c26e5cb3ada40d23f36cd104e18,true,2849477
SP8170ZRP66BQEQVYBNVK4F5R8QQ0B4S24XC27YR,0xc326ec0a7cb3c81ede1edb13274eae0b889abbd3a2c875dde74f67358d9c89d0,true,3100051
SP2HZMNKXP8JJGZ8W2B90CAZWP83ARH10BXNBKBGK,0x85ae320802b5bc026fd74d42952c316b7c1e66c609ffb41e5ba6e5e0d6620536,true,102804699
SP1YP3RVGRKV3F0PBC1ZQHGV1ACZT05087ZTPRZAQ,0xcf113f35955fe7895feba5eaaf9d91ce45df2db3d62a957623aaf1b2c7468eff,true,7071291
SP2ASZVDCGMZXC9RF8ZD3ED2JBMDM4TX87CGV8EN7,0xd033bdd2970bb12cdddae6b0abce892b72f8cfaae144cc776e4b963f13a0ac5b,true,8923415
SP2F0DP9Z3KSS0DABDBJN0DA0SHMCVWHXPVTH3PJJ,0xd04c803133cd880144efe75ad58b9f20b53f2fdc6fc910e78b21df411132c16b,true,71094069
SP1PHAGEQ5RWM8G84DFGMRPENKQGFC4QJ9YWXAYKF,0x83a4e75f67f6d3e1ee3a87659155895159ff0ba63d86406875cc6dfc3b33097f,true,23000000
SP36P3B159T3KFD8KM63HQXR3G2TW6AA1114Z8ZVJ,0xcec102199bb47dedf9a397e64bdb6073ed28243345f1acdf0537d53fd3bfaa30,false,3820540
SP1E4NAGDG5C42694ZZNQJDK7VJ41CVCYV1W1W148,0xddbfa143e4e489f9611a2a67cf339051bb4d824b1cb727887f4d24648b3f20e0,true,1876631
SP65J08Y7DX8FTDJKQVWCPPN8BRSQF5KMT2K4CD5,0xc5f031f3b53e31cfa79f2c6b119f6a89db7c0b44486f83380aaeb2914d81a0a8,true,1000021
SP25RK61425QBXW105M85SY22WJ46T6T6G5D1XJ9,0x22432a7819db13468e80329cff322610dfe48ca2c7436a95f4fbb16fc7768375,true,1077000
SP284MQ5HZJ22NQRWVMT2MB9YXCF7S1DDZRDPXB7Z,0xe85ce3e74512f154d992b3af7376a2ae526ae4aec82224652d153fd18ce3d56c,true,1819651
SP779SC9CDWQVMTRXT0HZCEHSDBXCHNGG7BC1H9B,0x5fc22b2580e027d3256b0e1a2fe32b4fb03a61e7f3bd742db2340c0c3c6181a1,true,5111448
SP16JSP1JMTBNV3GN5Y3JYEEPG5WK3SGSYDZSM7VJ,0xb22b20fce8d9581965fab81f94eee1832b3ce7950c655e33a41b5b8587f42258,true,1000000
SP3GGNDQASTXH0SVTSWVSNS7BP3RZ4MDXX25YW80J,0xe0c146e39e2ccef3d89424688f0f154265fdea1c568d70d60a71509e1d707062,true,17625139
SP12VTBRY3M9X3HKZH1ST668METTXR452V29XF7QJ,0x3944e08b6831555d79e6dc7542f256e581d21da0004ede2f9a031c76b943b5ca,true,89580230
SPFW2GN3FJPZRS7G2WS3VHJSGKKAWX2TS9BHKVHW,0xff251277c3c7854d27492b5014319e1bb8509148373b71c24f84064e29342e17,true,5787160
SPBGX7PWC5719ZSPCMA8YJGXM08HVV93SR5PQ102,0xaa6a94c0e505176e94e845ed3d5d814acdeedc741f41090c2cc69c9df10ff0d6,true,9213316
SP1ERZZ0G7KERNCXQDJF4GTHCF8DGZB8001YCNPQG,0xb11b5daebdfa16a75bcaf93baa0de25dffe16d8beac47a0087c310c3e6716d37,true,1457459
SPZ0JWFD70SD70QQ5YP9AHNFHCJXZG7ZB3QN6FYP,0xcf525fbbfbac298ca6f867d2a769c953335638aef7cc839024c40446b049ef29,false,13072584
SP25ZD9H455D2DMMPVGBADB0JDBFHJS1BTSGD9KYS,0x59d4647a239ca1cb172a359aa99857772592c4cb5d043a84de4596c8b85158dd,true,202099056
SP1NXBK3K5YYMD6FD41MVNP3JS1GABZ8TRTH2ZTMX,0x5e6497f0cf3ae2dedd5c2bacac403b7f3123b354df0188a67966235b6f9ba8d1,true,35783412
SP3JP0N1ZXGASRJ0F7QAHWFPGTVK9T2XNXDB908Z,0x5f4e75f7cf952b117c8053b4efb42d0049d80b8779f1de4d86da20e8c965a8c8,true,106531197


================================================
FILE: sips/sip-027/results/multisig-pool-votes.csv
================================================
voter,txid,for,power
SP2Z2CBMGWB9MQZAF5Z8X56KS69XRV3SJF4WKJ7J9,0xfcb85e802e3fb55a712589f27771b0ba06807e2dfde5bb63123dee2cc0f0d446,true,1999000000
SP39ZYHN0GRAA9FBE43QGQ2HFS3PRWZGE1JCQRWYH,0x722c3009c9446f1ad01b6f542100ba359afd35033d751e691704a98bf2b6e459,true,298000000
SP1NX4J8WPXR8KYVYMV2AF97Q5R6XJ8VVFSXMEDQ3,0xb22895e5ac0e2aecb8fd9ef16aa347a0836a52e2b281d271336b82c50e9a0464,true,24822000000
SP2JCF3ME5QC779DQ2X1CM9S62VNJF44GC23MKQXK,0x6e490a6cdb58a6ab885927abe09300a549bac71f331e8b77decf12713cf55d47,true,279996000000
SPKS1G7EQHP6FCFPFQW9S1913EAHHGHX0493F14V,0xe78ab7a0da4b986c83c25bf3d1709b793459054fa8991101f7703c2717bae279,true,62954000000
SPQZ94RC1JB4YQYDD17WSH397G83RP21G8Z9CHSM,0xbb1c26ff2d339cea72eeff51ea4cc2585c35deac7af5c0d7a329381915f03f2d,true,20398000000
SP760GCSGE6K8EX9EMW9QE12NY6QAPVAHFHNVZYA,0x221da41fefb27565dc682efbcc04a0e5ed3d905ec9d138ea2eaa23819512073e,true,4665000000
SP26HQEB01J47QGKGSDP6XJ6Z5TCM7ZEGAB6TXQPN,0xd983591ab70d8c91aa50bd172e24f2b4613ee16a00441b73bfb008d9ae2bcecc,true,4665000000
SPP74WS833MY99FXA1H2QC64RFMVCNZ37765FM3R,0x9616daa15b9676689587b5ad3cd9459ecdfbbd262751d116a7524c2f535e5aab,true,119000000
SP2F0DP9Z3KSS0DABDBJN0DA0SHMCVWHXPVTH3PJJ,0xb732b3a063a788ef076859a833cdfeb4eb89614d30adc5e6578719c29645af90,true,99000000
SP3S3X4WCNPTDZW0623D5MGFK6K8WR8PSQAXTY505,0x679962316ec535cb60c97d247fa49cee3d765f57893fc624343bb5c5ec927877,true,1053996000000
SP3N2RARPZ4FZP7JHJTXF30NAHQ0T9EYG4QZG4DJ5,0xbdf0a3d6fcb284a13d5cf1c18160d3d19d829fb63ded4a909de780bf6304df54,true,1680000000
SP2CM2RVAAKEJ4BF8AD5KV7B84FN2KPRM0A578AE6,0x93dad6e055d2fd40553acb6157f69ca94fd5ea200983b18b7a4e8839db3ac294,true,499999999519
SP2W7WXBSVXGQGDBM03C691T5ZGTV9EQ7NVJH9H19,0x1d6695f3b2bfd5e3f21c42ff71e705fc6da639b8a6ebc025118915e70050d168,true,1044412696452
SP2KW6DXVTR0SJGY3GN8GMPRP0KK2J8B9T4PMJWEP,0xd9f9198c3b3b361e131dbf36c3def9c5b3e019016cc7ef7e619e7d7df7ebb847,true,799999000000
SPZFXRQMCWCYJWM0MCJ6RVRX1AX6297SJ50VE41R,0x812ea10afd1254f220362d9053f4fec22e277b94e8f8dabce8aa68fba35c4d5f,true,5048000000
SP329M6CS0S3738Z0T268FXQXBSX0ZD1FZVBZS037,0x26690a514edd9bb8f928589fd5c5d5cef1b40133a70b98e2ff6f9ee7f12c0cd5,true,747000000
SPSTE5R54386QDCDNJJWH2EXQFST44QYZW3RPMD3,0x9a5cd39860cc26634377562d4b8719e32e10ebb4b1bddc2e13e9bb2e2402e8c5,true,299000000
SP12RR3Q6P9RAM5C4MJNFQ2PP17QRNNJ81VC9MEW2,0x48d58940464170fe2ecfae5b07624508b2f07422237fbec6dfde309d59030ca7,true,198000000
SP2Q5WHA9NAGWQV500HSV93SEG8PJDNC6FAH88EP4,0x9996688c703ba74ca7def85b6f196520ae9dbd1b12ee1a24ca0bf26435953666,true,219999000000
SPGTGMQWQ24S4SDZE9QV7TH6J2M9PEPQX6DKRTX4,0x5c4b4179ff3e009eb6e45546c95d7f7afa455afbd43a36fcc453d6bc29a073c8,true,970741646
SP30JZHPM23NN4KRNBZWCKRW6HGKN7EYKFKP9HBBN,0x5cb28fbcf7157ef4598c07ae242ae0641ac874cef7cb8f38e3819b581b1eed07,true,59997000000
SP3BNT6YEYFMVTT9V8MMY8ZKM4P9M3SY9X9PDJVEB,0xa1cd335ea715d27d035792e9b88df71e59ad56a0a4b6234e7ba535653bb34a98,true,11998000000
SP1WYMS04HEP4V5RQQ51JJ4D9S1Z15RTJ3GPR0HDK,0x5d34743e97b3c9f15277c714f7b6dd95221c5fec7496c6c716960aea2ee79cdf,true,303982000000
SP9XX1CEWA7JVG98P888VMYD4X5YBQ6H3ST516HG,0x2562412014bfcde5be7e58084f464c67ee819a0446071b0a6544aad1f6118e39,true,498000000
SP8R8AT0HS12MRKHMZ22J05DMTBDHRW9XJBKE5DG,0x689847ef5774f935758bd1c6a2edab820cad72683ce3d572f329053af03de927,true,579000000
SP3N0TH3N7BDG4WBSYV6FE2ASSAPEGWK47EEWD9TV,0x986513eb0bac134231cf1066f6e95577bb4081f64fb792fb402c59cd294199e3,true,1749000000
SP2TZE09GHARKG0B8NTT9X77QXBTQPQ2J1579T0D8,0x12e413f9aac2902816bb051ed4459feb5feff858abc108f760b968984887f514,true,49999000000
SP27Z5KCV5QGFH255ZWGMF0RVSRGZ9RTNAEE1X28,0x356ce4cdb75e3065f082b2e62bf52375d80b54c3635eeb76e076656fd9df551b,true,299000000
SP20D7NAJPTDS8AVTFE88VWQ5QQTYB29HYNEHZZGA,0xed50aa5e6de4ffe26c5301cb79300d4c309b096fb16e2fcd48bc5f57332a5f8c,true,128999000000
SP2EJSKCAD26AKPNYBQACSX9AY2JX6V27D3F9BW56,0x19b766dfaffc506f48fd62c2c907e9030fe4a8f923bdf8d39e1e74d2047dd045,true,740000000
SPP3HM2E4JXGT26G1QRWQ2YTR5WT040S5NKXZYFC,0xf880b92b162e387c4ba7bced7fbc494de7a18f10d61852c294150f8d3c56c72a,true,5399000000
SP39DC776TVRWSPSXNXCCM80APY6EBV4J1Y3HAZYJ,0xca79dae630eec22105e5ce819a223aa96b3faa60601f96adaf6384f640aeabf5,true,600049000000
SP2G67CTZDK869T8E25W3M6AAF1MNJ5GNEJVZA6A4,0x6e64dcf5b82e97a15c05dce1421a83e6455b08b5a7c0e11c424612a6d32f41a9,true,103000000
SP35MER4PHM6XGB99YDRQAK0M0JQ8F9CVF04VZ1VX,0x00dbd5315926e62fcf29222d4803443d4dcc41e67a9f166efbfbd07e9c925056,true,11999000000
SP29902VVK134BEFGP0F3QT7W2H5CFY2BVWAKSN7E,0xfbaedaecbadd396b0e43491f849286c690c214801eda8825f1a52fdf5910b1a9,true,2000000000
SP2ZRF8JCSA852P2K4ZB7RS21M43NYFKPSQ7DG1N8,0xdc3b4efdd644f2a291f5217f851563f8e67862785571d50ebc2b27a51aca93bf,true,6993000000
SP2DC8W3DB139SWGHCZ173ZRQJKY05BCXMC2KGXX7,0x7a58649ecc03e4ce143ae6650b120c48b06e9df66ad5c01820bed9838b2a740c,true,2799000000
SPF4682V9B3SNAYRTGWX6H3MWDRVM1VC4ETDC3MS,0x62f3c199fe1b0ee6db9a713282e26ea9aace4fc560c293d775a4695c965d0ba4,true,9999000000
SP10Y2X7RMBZPDH64Y49KFDPG4WK3YY6QN7XE8KHD,0xcb5c8e7ad2a51155fee1ed48bf9e251fb1539bf2875b3f8c62e614785fa4f38d,true,24005930751
SP3J9J71T02XB5C4PJJT3FZ1FASYJ4V8XMR6QY8D0,0x9620034d7ddce6a3410d719dcca63d73e058a832c0d9de4c825fbab9a3b88303,true,599000000
SP1RJC76DDEGTXEA21MNVDAV40Y4HW845C9J46RJS,0xe0f1680ed983daa208f4f0c53e34629b3c72976681ac7ee92b3118d32d261e19,true,101000000
SP22B1M07CY1TTC683V4P6VPTCCWCX21BES7DD35M,0x3a14072db68af796f7a15e0ccf91969f3125caca3be950699a48a7597929644f,true,39404300660
SP3CHC5CKZGPZ3W4Q4JASMM5ZSMD3P7TQWNSE6BQ8,0x5e4b7e919b6ddc8f2119bec977ce051a003d98d40023c97c57e4c056d91b3f1a,true,36198000000
SMX5RPBHKPF4M2WG14K8W8D9M7Y58A20N6GY9VBB,0xbe16eda8ff0dc9d726aabd730d28574a809be3ea7f4fc59509d0214456456b14,true,125000000000
SM375112TJX2XDBKV31HTS7Y96681KDSJ9VV4PQKV,0xd5a4a61768251919163d70ed0b17e1243b9382b9fa6f8039d8168fd38e9ea55c,true,150000000000
SM28MZMVW2W1PK9EGY0MWVTKKW5C8H8FGPNZY3Z6H,0x40c09fc8f40a56ffa4a477a5a8c9f91b8b849a580e90dac97310f1b7ec49c2da,true,125000000000
SMSTT1YVA10J7PFKWT9C8C4Y0TRQX14KGKQDXJX6,0x0941b7e05981cbe36f524a40047bf997fd4fb3df623253e94dbbe64991e57401,true,120000000000
SM11TJG7ZZJMERTMFZBRQF26WJBHJ1ES5TXWDEKJM,0xb06da129bf654fdbe3e3042986bea17f2293fc2d036859e9147d793dcc297ed3,true,125000000000
SM43APJS7JJXJVF53RDH8AAA1561QZ127NWG6AQX,0xe664ad4a6f223457a9cd27d33f838d9428a10709bbdb7ec96ebbfb3babfe01bd,true,19000000000000
SM4AETMATXSD8XKGV0J39JJ088XVEQXGD8287P8H,0x9ff5a426248dc98592088370382d381871fbdc302bbe61d1fefbc6a4e770e49f,true,120000000000
SM2VPH5Q2S14DY67M0NBSW6GSY47Z5WRHRWDGB0RK,0xd72c6980c46e4c3b2bab532432dfa93daec3b1b9f858d4b1f7c1e088b5beef3a,true,125000000000
SMFZTYFFXVZJNBX21ZZB0FZFTTBQT9RBNEZ5FZ01,0x7d8a010fa1024539690f56da86962a43a8b9c142cdea003d40046c62c6c2d16a,true,120000000000
SM2BMD7QNSDDZXQXXGFNPD8EGSQ69GZF2CQ8Z1XN9,0x253ba5316e8c923fb2e581aa43b4a0e14837072955d6b711565e6a3f2132deb2,true,120000000000
SM1JFZTVCX1RZCCHWMGWCZ3TY37KVEJZJKFEWP8F7,0xc9046bab41eeead77ac6b916c4818bb43731cbb535de21ab7d2e698ed46de331,true,15000000000000
SM17AB7JPYHX1BJ0NGPR8TJ8GAQ5E7R65RJPX9EM,0xe44f2b14fbf2f1e80a2fe87d55b9ccd0278613b8999afec6fe90661c94d60ebe,true,5390000000000
SM39S3W3ADQ5NP68N9R4FWMWBC1NQAS4VWXWWTZYM,0x772fee8ddaa0ad78d3e272b4bf205e91061e94333916836c99484ec6ba224eb4,true,3000000000000
SP2NHZDAMMEEASE4DKHYYCVAG8RF8PA7YHPPW40BX,0x34383c87108696b62980ba95575bad6d2f41121ed888fcbe11ae284e2d59d902,true,5199000000
SP3TA7SMY7APYR9SFKDT0527NC0GWR84S3AHEM0NE,0xe21ea78992fc21282803bbededfcd8a215341c83890a531040a790551aea9509,true,50054927941
SP2C7E0N4PNV1E55SZ0QBHHXYTHHKJ7GTD5T17JGW,0x81100751b3cfdc00716e8d34f4eb0ae0b453830f0e675906bc4645ed55db912d,true,50052337860
SP6WS2G1W2XHYXHX30PSPS25GDNB3DF7610SFZJC,0xf4b30ba2a3a19649063688fef392e5de32bee0a243ee0cdabf518504006beb91,true,140799000000
SPG34S51QV6YTZQGVRPZY9323MY4BTCFAFP1HR25,0xf89bd1db3860ae92b1d2ac696ead1c729af49329862ca2ef7dcb1e75a8c2a2ec,true,1204000000
SP37Q561WR22AXA3EC9GJDN9QGK9K97Z3H940EV9Z,0xff332cb55ca0e6b9e7ab417c052b43f7abbbb485b25261bc33b313e983a9e603,true,59999000000
SM2CDAXV570733P3K1HAF54C6D63FXQ7X24SJTHVC,0x5c2dc7b668f8d87a2b0545dd0e26afeffb69d9c5ce67cfc04fb3e7f50fbacfab,true,15000000000000
SP1G2V19PMG1HDAXZP7DY4Z59VSG2SR1BRGDZEGGG,0x0e5896916d38a201f7675bb6bde19abb1a5a66bd1548f9f3326d7f6d8f45aa09,true,238848000000
SPTF7TRK58APKSPTRFK7N66RSCWE7MZ559A0A88J,0x06409ed827b0875d8d6a24c6ece78b4e59c25c2e36ca27a0b8a37587312ae97e,true,299000000
SP1SJ7PGM3M7D7J60C39FGXJ29ES1JWVJGJ3XCX75,0x504ead937c63f2bfe790aac500218bbf079d7a3c03ea3e307fdfade45a6c54a0,true,79999000000
SP103BZSXCX2YF8HXMN8DDP5Z46DN4A0HPRDYJXDD,0xfa3a1312e5d074c8b6d261234f0f53bb3041839c3a69ec65d24c4d9b6fc7e2b1,true,100000000
SP3N4E7VQVRZVPVARD6QTYCCM3VBMDPNP53TM39AN,0x1cfeb40246c0a76797f29f3fe58863c44bda58c091a0a9a8ad8dc252faa319c2,true,76999000000
SPETRC149CY5PSKEK1K2Q160MR8YQ924GETDJRSS,0xe52371e373ad1ba353cf9e8a3e7eb953d6c7056dc0f0c4b9efa5794ff6c9466f,true,419998000000
SP3H4VWAJ9A2468RVKWCGMV33PGJC1Z8CFZZ19ZTR,0xc8ea0db9a9bd10da9fc8a9ac987b85a253149a7d9be2710c9e23735f01fb7194,true,30666000000
SP2EM86AM2AYGGNJX562AY6BDTKWXQMQVQ0T863M6,0x5be52b38bf9c1270dd6977bd60a597a1965bb47556ea5f1cfe1399e68d11b3d1,true,92490000000
SP2HCKXC6GAWMAHWH06XGJBTS7JVA6YFRJJB2PCWA,0xac40e60f38d4c8c467066861a149f9f85c0e9a11513eb565303827573624e995,true,2996000000


================================================
FILE: sips/sip-027/results/multisig-solo-votes.csv
================================================
voter,txid,for,power
SP3573HMB9SPCTMT85YS85KEPYCX33E6MZGQ5QB2A,0x0bd70b5b1c95c87790644beedaa1b0141aed4e1f8a154f075771049d74bce1e1,true,3449000000000


================================================
FILE: sips/sip-027/scripts/validate-and-count-votes/index.js
================================================
import { poxAddressToBtcAddress, poxAddressToTuple } from '@stacks/stacking';
import axios from 'axios';
import { cvToJSON } from '@stacks/transactions';
import { writeFileSync } from 'fs';

const MULTISIG_POOL_VOTES_FILE = 'multisig-pool-votes.csv';
const MULTISIG_SOLO_VOTES_FILE = 'multisig-solo-votes.csv';

function convertVotesToCsv(votes) {
  const headers = 'voter,txid,for,power\n';
  const rows = votes.map(vote => 
    `${vote.voter},${vote.txid},${vote.for},${vote.power}`
  ).join('\n');
  
  return headers + rows;
}

const YES_STX_ADDRESS = "SPA17ZSXKXS4D8FC51H1KWQDFS31NM29SKZRTCF8";
const NO_STX_ADDRESS = "SP39DK8BWFM2SA0E3F6NA72104EYG9XB8NXZ91NBE";

const YES_BTC_ADDRESS = "399iMhKN9fjpPJLYHzieZA1PfHsFxijyVY";
const NO_BTC_ADDRESS = "31ssu69FmpxS6bAxjNrX1DfApD8RekK7kp";

const CYCLE_TO_CHECK_FOR = 90;

const GET_EVENTS_API_URL = `https://api.mainnet.hiro.so/extended/v1/tx/events`;
const POX_INFO_URL = `https://api.mainnet.hiro.so/v2/pox`;
const SIGNERS_IN_CYCLE_API_URL = (cycle) => `https://api.hiro.so/extended/v2/pox/cycles/${cycle}/signers`;
const POX_4_ADDRESS = 'SP000000000000000000002Q6VF78.pox-4';
const LIMIT = 100;

async function fetchData(offset) {
  try {
    const response = await axios.get(GET_EVENTS_API_URL, {
      params: {
        address: POX_4_ADDRESS,
        limit: LIMIT,
        offset: offset,
      },
    });

    return response.data.events;
  } catch (error) {
    if (error.response) {
      if (error.response.status !== 404) {
        await new Promise((resolve) => setTimeout(resolve, 10000));
        return fetchData(offset);
      } else {
        console.error(`Error: ${error}`);
      }
    } else {
      console.error(`Error: ${error}`);
    }
    return null;
  }
}

async function fetchAddressTransactionsStacks(offset, address) {
  try {
    const response = await axios.get(`https://api.hiro.so/extended/v2/addresses/${address}/transactions?limit=50&offset=${offset}`);

    return response.data.results;
  } catch (error) {
    if (error.response) {
      if (error.response.status === 429) {
        await new Promise((resolve) => setTimeout(resolve, 10000));
        return fetchAddressTransactionsStacks(offset, address);
      } else {
        console.error(`Error: ${error}`);
      }
    } else {
      console.error(`Error: ${error}`);
    }
    return null;
  }
}

async function fetchAddressTransactionsBitcoin(address) {
  try {
    const response = await axios.get(`https://mempool.space/api/address/${address}/txs`);

    return response.data;
  } catch (error) {
    if (error.response) {
      if (error.response.status === 429) {
        await new Promise((resolve) => setTimeout(resolve, 10000));
        return fetchAddressTransactionsBitcoin(address);
      } else {
        console.error(`Error: ${error}`);
      }
    } else {
      console.error(`Error: ${error}`);
    }
    return null;
  }
}

async function fetchPoxInfo() {
  try {
    const response = await axios.get(POX_INFO_URL);
    return response.data;
  } catch (error) {
    if (error.response) {
      if (error.response.status === 429) {
        await new Promise((resolve) => setTimeout(resolve, 10000));
        return fetchPoxInfo();
      } else {
        console.error(`Error fetching PoX info: ${error}`);
      }
    } else {
      console.error(`Error fetching PoX info: ${error}`);
    }
    return null;
  }
}

async function fetchSignersInCycle(cycle) {
  try {
    const response = await axios.get(SIGNERS_IN_CYCLE_API_URL(cycle));
    return response.data;
  } catch (error) {
    if (error.response) {
      if (error.response.status === 429) {
        await new Promise((resolve) => setTimeout(resolve, 10000));
        return fetchPoxInfo();
      } else {
        console.error(`Error fetching signers info: ${error}`);
      }
    } else {
      console.error(`Error fetching signers info: ${error}`);
    }
    return null;
  }
}

function parseStringToJSON(input) {
  function parseValue(value) {
    if (value.startsWith('(tuple')) return parseTuple(value);
    if (value.startsWith('(some')) return parseSome(value);
    if (value === 'none') return null;
    if (value.startsWith('u')) return parseInt(value.slice(1), 10);
    if (value.startsWith('0x')) return value;
    if (value.startsWith("'") && value.endsWith("'")) return value.slice(1, -1);
    if (value.startsWith("'")) return value.slice(1);
    if (value.startsWith('"') && value.endsWith('"')) return value.slice(1, -1);
    if (value.startsWith('"')) return value.slice(1);
    return value;
  }

  function parseTuple(value) {
    const obj = {};
    const tupleContent = value.slice(7, -1).trim();
    const entries = splitEntries(tupleContent);

    entries.forEach((entry) => {
      const spaceIndex = entry.indexOf(' ');
      const key = entry.slice(1, spaceIndex);
      const val = entry.slice(spaceIndex + 1).trim().slice(0, -1);
      obj[key] = parseValue(val);
    });

    return obj;
  }

  function parseSome(value) {
    const someContent = value.slice(5, -1).trim();
    return parseValue(someContent);
  }

  function splitEntries(content) {
    const entries = [];
    let bracketCount = 0;
    let startIdx = 0;

    for (let i = 0; i < content.length; i++) {
      if (content[i] === '(') bracketCount++;
      if (content[i] === ')') bracketCount--;
      if (bracketCount === 0 && (content[i] === ' ' || i === content.length - 1)) {
        entries.push(content.slice(startIdx, i + 1).trim());
        startIdx = i + 1;
      }
    }

    return entries;
  }

  function parseMain(input) {
    const mainContent = input.slice(4, -1).trim();
    if (mainContent.startsWith('(tuple')) return parseTuple(mainContent);
    const entries = splitEntries(mainContent);
    const result = {};

    entries.forEach((entry) => {
      const spaceIndex = entry.indexOf(' ');
      const key = entry.slice(1, spaceIndex);
      const val = entry.slice(spaceIndex + 1).trim().slice(0, -1);
      result[key] = parseValue(val);
    });

    return result;
  }

  return parseMain(input);
}

function getEventsForAddress(address, allEvents) {
  let events = [];
  let isDelegator = false;
  let delegatedTo = [];
  let isSoloStacker = false;

  for (const entry of allEvents) {
    if (entry.contract_log.value.repr.includes(address)) {
      const result = parseStringToJSON(entry.contract_log.value.repr);
      if (result.name == "stack-stx") {
        events.push({
          name: result.name,
          stacker: result.stacker,
          startCycle: result.data["start-cycle-id"],
          endCycle: result.data["end-cycle-id"],
          poxAddress: result.data["pox-addr"] != null ? 
            poxAddressToBtcAddress(
              parseInt(result.data["pox-addr"].version, 16),
              Uint8Array.from(Buffer.from(result.data["pox-addr"].hashbytes.slice(2), 'hex')),
              'mainnet',
            ) :
            null,
          signerKey: result.data["signer-key"],
          amountUstx: result.data["lock-amount"],
        });
        isSoloStacker = true;
      } else if (result.name == "stack-extend") {
        events.push({
          name: result.name,
          stacker: result.stacker,
          startCycle: result.data["start-cycle-id"],
          endCycle: result.data["end-cycle-id"],
          poxAddress: result.data["pox-addr"] != null ? 
            poxAddressToBtcAddress(
              parseInt(result.data["pox-addr"].version, 16),
              Uint8Array.from(Buffer.from(result.data["pox-addr"].hashbytes.slice(2), 'hex')),
              'mainnet',
            ) :
            null,
        });
      } else if (result.name == "stack-increase") {
        events.push({
          name: result.name,
          stacker: result.stacker,
          startCycle: result.data["start-cycle-id"],
          endCycle: result.data["end-cycle-id"],
          poxAddress: result.data["pox-addr"] != null ? 
            poxAddressToBtcAddress(
              parseInt(result.data["pox-addr"].version, 16),
              Uint8Array.from(Buffer.from(result.data["pox-addr"].hashbytes.slice(2), 'hex')),
              'mainnet',
            ) :
            null,
          amountUstx: result.data["total-locked"],
        });
      } else if (result.name == "delegate-stx") {
        events.push({
          name: result.name,
          stacker: result.stacker,
          amountUstx: result.data["amount-ustx"],
          startCycle: result.data["start-cycle-id"],
          endCycle: result.data["end-cycle-id"],
          poxAddress: result.data["pox-addr"] != null ? 
            poxAddressToBtcAddress(
              parseInt(result.data["pox-addr"].version, 16),
              Uint8Array.from(Buffer.from(result.data["pox-addr"].hashbytes.slice(2), 'hex')),
              'mainnet',
            ) :
            null,
        });
        if (result.stacker === address) {
          isDelegator = true;
          delegatedTo.push(result.data["delegate-to"]);
        }
      } else if (result.name == "revoke-delegate-stx") {
        events.push({
          name: result.name,
          stacker: result.stacker,
          startCycle: result.data["start-cycle-id"],
          endCycle: result.data["end-cycle-id"],
        });
      } else if (result.name == "delegate-stack-stx") {
        events.push({
          name: result.name,
          stacker: result.data.stacker,
          amountUstx: result.data["lock-amount"],
          startCycle: result.data["start-cycle-id"],
          endCycle: result.data["end-cycle-id"],
          poxAddress: result.data["pox-addr"] != null ? 
            poxAddressToBtcAddress(
              parseInt(result.data["pox-addr"].version, 16),
              Uint8Array.from(Buffer.from(result.data["pox-addr"].hashbytes.slice(2), 'hex')),
              'mainnet',
            ) :
            null,
        });
      } else if (result.name == "delegate-stack-extend") {
        events.push({
          name: result.name,
          stacker: result.data.stacker,
          startCycle: result.data["start-cycle-id"],
          endCycle: result.data["end-cycle-id"],
          poxAddress: result.data["pox-addr"] != null ? 
            poxAddressToBtcAddress(
              parseInt(result.data["pox-addr"].version, 16),
              Uint8Array.from(Buffer.from(result.data["pox-addr"].hashbytes.slice(2), 'hex')),
              'mainnet',
            ) :
            null,
        });
      } else if (result.name == "delegate-stack-increase") {
        events.push({
          name: result.name,
          stacker: result.data.stacker,
          startCycle: result.data["start-cycle-id"],
          endCycle: result.data["end-cycle-id"],
          increaseBy: result.data["increase-by"],
          totalLocked: result.data["total-locked"],
          poxAddress: result.data["pox-addr"] != null ? 
            poxAddressToBtcAddress(
              parseInt(result.data["pox-addr"].version, 16),
              Uint8Array.from(Buffer.from(result.data["pox-addr"].hashbytes.slice(2), 'hex')),
              'mainnet',
            ) :
            null,
        });
      } else if (result.name == "stack-aggregation-commit-indexed" || result.name == "stack-aggregation-commit") {
        events.push({
          name: result.name,
          amountUstx: result.data["amount-ustx"],
          cycle: result.data["reward-cycle"],
          poxAddress: result.data["pox-addr"] != null ? 
            poxAddressToBtcAddress(
              parseInt(result.data["pox-addr"].version, 16),
              Uint8Array.from(Buffer.from(result.data["pox-addr"].hashbytes.slice(2), 'hex')),
              'mainnet',
            ) :
            null,
          signerKey: result.data["signer-key"],
        });
      } else if (result.name == "stack-aggregation-increase") {
        events.push({
          name: result.name,
          amountUstx: result.data["amount-ustx"],
          cycle: result.data["reward-cycle"],
          rewardCycleIndex: result.data["reward-cycle-index"],
          poxAddress: result.data["pox-addr"] != null ? 
            poxAddressToBtcAddress(
              parseInt(result.data["pox-addr"].version, 16),
              Uint8Array.from(Buffer.from(result.data["pox-addr"].hashbytes.slice(2), 'hex')),
              'mainnet',
            ) :
            null,
        });
      };
    };
  };

  return {events, isDelegator, delegatedTo, isSoloStacker};
}

function getStackerForBtcAddress(address, allEvents) {
  let print = false;
  if (address == "bc1p7l2cywf6qr9gwca3vsv6mwdlkfl3f7agw9kdm98re7jmn087q86suc2lpk" || address == "bc1p6dm28490l7yxl935yplp2pd92psj5yt82sfp2tpqc93ah3u6gges97q9sw") {
    print = true;
  };
  const addressDeserialized = cvToJSON(poxAddressToTuple(address));
  const version = addressDeserialized.value.version.value;
  const hashbytes = addressDeserialized.value.hashbytes.value;

  for (const entry of allEvents) {
    if (entry.contract_log.value.repr.includes(version) && entry.contract_log.value.repr.includes(hashbytes)) {
      if (print == true) {
        console.log(address, entry);
      }
      const result = parseStringToJSON(entry.contract_log.value.repr);
      if (result.name == "stack-stx") {
        return result.stacker;
      }
    }
  }

  return "Could not find BTC address";
}

async function fetchAllData() {
  const poxInfo = await fetchPoxInfo();
  if (poxInfo === null) return;

  let offset = 0;
  let moreData = true;
  let allEvents = [];

  while (moreData) {
    const data = await fetchData(offset);

    if (data && data.length > 0) {
      for (const entry of data) {
        allEvents.push(entry);
      }
      offset += LIMIT;
    } else {
      moreData = false;
    }
  }

  offset = 0;
  moreData = true;
  const ADDRESSES = [];

  // 854,950 until 857,050

  while (moreData) {
    const data = await fetchAddressTransactionsStacks(offset, YES_STX_ADDRESS);

    if (data && data.length > 0) {
      for (const entry of data) {
        if (entry.tx.burn_block_height >= 854950 && entry.tx.burn_block_height < 857050) {
          ADDRESSES.push({
            address: entry.tx.sender_address,
            time: entry.tx.burn_block_time,
            nonce: entry.tx.nonce,
            vote: "yes",
            txid: entry.tx.tx_id,
          });
        };
      }
      offset += 50;
    } else {
      moreData = false;
    }
  }

  offset = 0;
  moreData = true;

  while (moreData) {
    const data = await fetchAddressTransactionsStacks(offset, NO_STX_ADDRESS);

    if (data && data.length > 0) {
      for (const entry of data) {
        if (entry.tx.burn_block_height >= 854950 && entry.tx.burn_block_height < 857050) {
          ADDRESSES.push({
            address: entry.tx.sender_address,
            time: entry.tx.burn_block_time,
            nonce: entry.tx.nonce,
            vote: "no",
            txid: entry.tx.tx_id,
          });
        };
      }
      offset += 50;
    } else {
      moreData = false;
    }
  }

  const btcYesData = await fetchAddressTransactionsBitcoin(YES_BTC_ADDRESS);
  if (btcYesData && btcYesData.length > 0) {
    for (const entry of btcYesData) {
      if (entry.status.confirmed == true) {
        if (entry.status.block_height >= 854950 && entry.status.block_height < 857050) {
          ADDRESSES.push({
            btcAddress: entry.vin[0].prevout.scriptpubkey_address,
            address: getStackerForBtcAddress(entry.vin[0].prevout.scriptpubkey_address, allEvents),
            time: entry.status.block_time,
            nonce: null,
            vote: "yes",
            txid: entry.txid,
          });
        };
      };
    }
  }

  const btcNoData = await fetchAddressTransactionsBitcoin(NO_BTC_ADDRESS);
  if (btcNoData && btcNoData.length > 0) {
    for (const entry of btcNoData) {
      if (entry.status.confirmed == true) {
        if (entry.status.block_height >= 854950 && entry.status.block_height < 857050) {
          ADDRESSES.push({
            btcAddress: entry.vin[0].prevout.scriptpubkey_address,
            address: getStackerForBtcAddress(entry.vin[0].prevout.scriptpubkey_address, allEvents),
            time: entry.status.block_time,
            nonce: null,
            vote: "no",
            txid: entry.txid,
          });
        };
      };
    }
  }

  ADDRESSES.sort((a, b) => {
    if (a.time === b.time) {
      return a.nonce - b.nonce;
    }
    return a.time - b.time;
  });

  // SM3QS5GHTHQ7HZ1P04XWQJXK5B5HN1V24BEMWM7Q9 and SM14HV23Z50KK8WBK84C3KPJG78EZWPHYHQB584NQ are counted as valid votes - voted with pool reward address, no time left to do STX

  let totalVotes = 2; // SM3QS5GHTHQ7HZ1P04XWQJXK5B5HN1V24BEMWM7Q9 + SM14HV23Z50KK8WBK84C3KPJG78EZWPHYHQB584NQ
  let validVotes = 2; // SM3QS5GHTHQ7HZ1P04XWQJXK5B5HN1V24BEMWM7Q9 + SM14HV23Z50KK8WBK84C3KPJG78EZWPHYHQB584NQ
  let yesVotes = 2; // SM3QS5GHTHQ7HZ1P04XWQJXK5B5HN1V24BEMWM7Q9 + SM14HV23Z50KK8WBK84C3KPJG78EZWPHYHQB584NQ
  let noVotes = 0;
  let yesVotesInvalid = 0;
  let noVotesInvalid = 0;
  let notStacking = 0;
  let notStackingInCycle = 0;

  let soloStackerVotes = 0;
  let delegatorVotes = 2; // SM3QS5GHTHQ7HZ1P04XWQJXK5B5HN1V24BEMWM7Q9 + SM14HV23Z50KK8WBK84C3KPJG78EZWPHYHQB584NQ
  let totalSoloStackerAmountYes = 0;
  let totalDelegatedAmountYes = 29819000000000 + 20000000000000; // SM3QS5GHTHQ7HZ1P04XWQJXK5B5HN1V24BEMWM7Q9 + SM14HV23Z50KK8WBK84C3KPJG78EZWPHYHQB584NQ
  let totalSoloStackerAmountNo = 0;
  let totalDelegatedAmountNo = 0;

  let soloStackerVotesForCsv = [];
  let poolStackerVotesForCsv = [];

  const verifiedAddresses = [];

  for (const {address, btcAddress, vote, txid} of ADDRESSES) {
    console.log("Processing PoX data for", btcAddress !== undefined ? btcAddress : address + ":");

    if (address == "SM3QS5GHTHQ7HZ1P04XWQJXK5B5HN1V24BEMWM7Q9" || address == "SM14HV23Z50KK8WBK84C3KPJG78EZWPHYHQB584NQ") {
      continue;
    };

    if (verifiedAddresses.includes(address)) {
      console.log("This address already voted!");
      console.log();
      continue;
    };

    if (address !== "Could not find BTC address") {
      verifiedAddresses.push(address);
    };

    let {events, isDelegator, delegatedTo, isSoloStacker} = getEventsForAddress(address, allEvents);

    let wasStacking = false;
    let stackingSignerKey = null;
    let delegatedAmount = 0;
    let stackedAmount = 0;

    totalVotes++;

    if (isDelegator === true) {
      for (const delegator of delegatedTo) {
        events = getEventsForAddress(delegator, allEvents).events;
        events.reverse();

        let delegations = new Map();
        let acceptedDelegations = new Map();
        let committedDelegations = new Map();

        let wasAccepted = false;
        let acceptedToAddress;
        let wasCommitted = false;

        let delegatedAmountLocal = 0;

        for (const event of events) {
          const { name, stacker, startCycle, endCycle, poxAddress, amountUstx, increaseBy, totalLocked, cycle, signerKey } = event;
  
          switch (name) {
            case 'delegate-stx':
              delegations.set(stacker, { startCycle, endCycle, poxAddress, amountUstx });
              break;
            case 'revoke-delegate-stx':
              delegations.delete(stacker);
              break;
            case 'delegate-stack-stx':
              acceptedDelegations.set(stacker, [{ startCycle, endCycle, poxAddress, amountUstx }]);
              break;
            case 'delegate-stack-extend':
              if (acceptedDelegations.has(stacker)) {
                const existingList = acceptedDelegations.get(stacker);
                const lastEntry = existingList[existingList.length - 1];
      
                lastEntry.endCycle = endCycle;
                acceptedDelegations.set(stacker, existingList);
              }
              break;
            case 'delegate-stack-increase':
              if (acceptedDelegations.has(stacker)) {
                const existingList = acceptedDelegations.get(stacker);
                const lastEntry = existingList[existingList.length - 1];
      
                if (lastEntry.amountUstx + increaseBy === totalLocked) {
                  if (lastEntry.startCycle === startCycle) {
                    lastEntry.amountUstx += increaseBy;
                  } else {
                    const newEntry = {
                      startCycle: startCycle,
                      endCycle: lastEntry.endCycle,
                      poxAddress: lastEntry.poxAddress,
                      amountUstx: lastEntry.amountUstx + increaseBy,
                    };

                    lastEntry.endCycle = startCycle;
                    existingList.push(newEntry);
                  }
                  acceptedDelegations.set(stacker, existingList);
                }
              }
              break;
            case 'stack-aggregation-commit':
            case 'stack-aggregation-commit-indexed':
              if (poxAddress) {
                if (!committedDelegations.has(poxAddress)) {
                  committedDelegations.set(poxAddress, [{ startCycle: cycle, endCycle: cycle + 1, amountUstx, signerKey }]);
                } else {
                  const existingList = committedDelegations.get(poxAddress);
                  existingList.push({
                    startCycle: cycle,
                    endCycle: cycle + 1,
                    amountUstx,
                    signerKey,
                  });
                  committedDelegations.set(poxAddress, existingList);
                }
              }
              break;
            case 'stack-aggregation-increase':
              if (poxAddress) {
                const existingList = committedDelegations.get(poxAddress);
                if (existingList) {
                  const entry = existingList.find(e => e.startCycle === cycle);
                  if (entry) {
                    entry.amountUstx += amountUstx;
                  }
                }
              }
              break;
          }
        }

        acceptedDelegations.forEach((value, key) => {
          if (key == address) {
            for (const acceptation of value) {
              if (acceptation.startCycle <= CYCLE_TO_CHECK_FOR && acceptation.endCycle > CYCLE_TO_CHECK_FOR) {
                wasAccepted = true;
                acceptedToAddress = acceptation.poxAddress;
                delegatedAmountLocal += acceptation.amountUstx;
                break;
              }
            }
          }
        });

        committedDelegations.forEach((value, key) => {
          if (key === acceptedToAddress) {
            for (const commitment of value) {
              if (commitment.startCycle == CYCLE_TO_CHECK_FOR) {
                wasCommitted = true;
                stackingSignerKey = commitment.signerKey;
                break;
              }
            }
          }
        });

        if (wasAccepted === true && wasCommitted === true) {
          wasStacking = true;
          delegatedAmount += delegatedAmountLocal;
        }
      }
    } else if (isSoloStacker === true) {
      events.reverse();

      let soloStacking = new Map();

      for (const event of events) {
        const { name, stacker, startCycle, endCycle, poxAddress, signerKey, amountUstx } = event;

        switch (name) {
          case 'stack-stx':
            if (!soloStacking.has(stacker)) {
              soloStacking.set(stacker, [{ startCycle, endCycle, poxAddress, signerKey, amountUstx }]);
            } else {
              const existingList = soloStacking.get(stacker);
              existingList.push({ startCycle, endCycle, poxAddress, signerKey, amountUstx });
              soloStacking.set(stacker, existingList);
            }
            break;
          case 'stack-extend':
            if (soloStacking.has(stacker)) {
              const existingListExtend = soloStacking.get(stacker);
              const lastEntryExtend = existingListExtend[existingListExtend.length - 1];

              if (lastEntryExtend.endCycle === startCycle) {
                lastEntryExtend.endCycle = endCycle;
                soloStacking.set(stacker, existingListExtend);
              }
            }
            break;
          case 'stack-increase':
            if (soloStacking.has(stacker)) {
              const existingList = soloStacking.get(stacker);
              const lastEntry = existingList[existingList.length - 1];

              if (lastEntry.startCycle === startCycle) {
                lastEntry.amountUstx = amountUstx;
              } else {
                const newEntry = {
                  startCycle: startCycle,
                  endCycle: lastEntry.endCycle,
                  poxAddress: lastEntry.poxAddress,
                  signerKey: signerKey,
                  amountUstx: amountUstx,
                };
  
                lastEntry.endCycle = startCycle;
                existingList.push(newEntry);
              }
              soloStacking.set(stacker, existingList);
            }
            break;
        }
      }

      soloStacking.forEach((value, key) => {
        for (const stack of value) {
          if (stack.startCycle <= CYCLE_TO_CHECK_FOR && stack.endCycle > CYCLE_TO_CHECK_FOR) {
            wasStacking = true;
            stackingSignerKey = stack.signerKey;
            stackedAmount += stack.amountUstx;
            break;
          }
        }
      });
    } else {
      console.log("This address is neither a solo stacker, nor a delegator");
      notStacking++;
      if (vote === "yes") {
        yesVotesInvalid++;
      } else if (vote === "no") {
        noVotesInvalid++;
      };
      console.log();
      continue;
    }

    if (wasStacking === true) {
      console.log("This address was a stacker in cycle", CYCLE_TO_CHECK_FOR);
    } else {
      console.log("This address was not a stacker in cycle", CYCLE_TO_CHECK_FOR);
      notStackingInCycle++;
      if (vote === "yes") {
        yesVotesInvalid++;
      } else if (vote === "no") {
        noVotesInvalid++;
      };
      continue;
    };

    let wasActive = false;

    const signersInCycle = (await fetchSignersInCycle(CYCLE_TO_CHECK_FOR)).results;
    for (const signer of signersInCycle) {
      if (signer.signing_key === stackingSignerKey) {
        wasActive = true;
      }
    }

    if (wasActive === true) {
      console.log("The vote of this address is valid");
      console.log(delegatedAmount, stackedAmount);
      validVotes++;

      if (vote === "yes") {
        yesVotes++;
        totalDelegatedAmountYes += delegatedAmount || 0;
        totalSoloStackerAmountYes += stackedAmount || 0;
      } else if (vote === "no") {
        noVotes++;
        totalDelegatedAmountNo += delegatedAmount || 0;
        totalSoloStackerAmountNo += stackedAmount || 0;
      };

      if (isDelegator === true) {
        delegatorVotes++;
        poolStackerVotesForCsv.push({
          voter: btcAddress !== undefined ? btcAddress : address,
          txid: txid,
          for: vote === "yes" ? true : false,
          power: delegatedAmount || 0 + stackedAmount || 0,
        });
      };

      if (isSoloStacker === true) {
        soloStackerVotes++;
        soloStackerVotesForCsv.push({
          voter: btcAddress !== undefined ? btcAddress : address,
          txid: txid,
          for: vote === "yes" ? true : false,
          power: delegatedAmount || 0 + stackedAmount || 0,
        });
      }
    } else {
      if (vote === "yes") {
        yesVotesInvalid++;
      } else if (vote === "no") {
        noVotesInvalid++;
      };
      console.log("This vote is invalid");
    };

    console.log();
  }

  console.log("Blocks left of cycle", poxInfo.current_cycle.id + ":", poxInfo.next_cycle.blocks_until_prepare_phase);
  console.log("Total number of votes (unique addresses):", totalVotes);
  console.log("Number of invalid votes:", totalVotes - validVotes);
  console.log("Number of valid votes:", validVotes);
  console.log("Number of valid YES votes:", yesVotes);
  console.log("Number of valid NO votes:", noVotes);
  console.log("Number of invalid YES votes:", yesVotesInvalid);
  console.log("Number of invalid NO votes:", noVotesInvalid);
  console.log("Number of invalid votes (address not stacking at all):", notStacking);
  console.log("Number of invalid votes (address not stacking in cycle 90):", notStackingInCycle);
  console.log("Out of the valid votes,", delegatorVotes, "were delegators, and", soloStackerVotes, "were solo stackers.");
  console.log("Amount delegated YES:", totalDelegatedAmountYes / 1000000 + " STX");
  console.log("Amount solo stacked YES:", totalSoloStackerAmountYes / 1000000 + " STX");
  console.log("Amount delegated NO:", totalDelegatedAmountNo / 1000000 + " STX");
  console.log("Amount solo stacked NO:", totalSoloStackerAmountNo / 1000000 + " STX");

  const poolVotesCsv = convertVotesToCsv(poolStackerVotesForCsv);
  const soloVotesCsv = convertVotesToCsv(soloStackerVotesForCsv);

  writeFileSync(MULTISIG_POOL_VOTES_FILE, poolVotesCsv);
  writeFileSync(MULTISIG_SOLO_VOTES_FILE, soloVotesCsv);

  console.log('CSV files have been saved successfully.');
}

fetchAllData();



================================================
FILE: sips/sip-027/scripts/validate-and-count-votes/nonStackerVotes.js
================================================
import axios from "axios";
import { writeFileSync } from "fs";

const STX_ADDRESS = "SP3JP0N1ZXGASRJ0F7QAHWFPGTVK9T2XNXDB908Z.bde001-proposal-voting";
const MULTISIG_DAO_VOTES_FILE = 'multisig-dao-votes.csv';

async function fetchAddressTransactionsStacks(offset, address) {
  try {
    const response = await axios.get(`https://api.hiro.so/extended/v2/addresses/${address}/transactions?limit=50&offset=${offset}`);

    return response.data.results;
  } catch (error) {
    if (error.response) {
      if (error.response.status === 429) {
        await new Promise((resolve) => setTimeout(resolve, 10000));
        return fetchAddressTransactionsStacks(offset, address);
      } else {
        console.error(`Error: ${error}`);
      }
    } else {
      console.error(`Error: ${error}`);
    }
    return null;
  }
}

function convertVotesToCsv(votes) {
  const headers = 'voter,txid,for,power\n';
  const rows = votes.map(vote => 
    `${vote.voter},${vote.txid},${vote.for},${vote.power}`
  ).join('\n');
  
  return headers + rows;
}

async function fetchAllData() {
  let moreData = true;
  let offset = 0;

  let noAmount = 0;
  let noCount = 0;

  let yesAmount = 0;
  let yesCount = 0;

  let daoVotesForCsv = [];

  while (moreData) {
    const data = await fetchAddressTransactionsStacks(offset, STX_ADDRESS);

    if (data && data.length > 0) {
      for (const entry of data) {
        if (entry.tx.burn_block_height >= 854950 && entry.tx.burn_block_height < 857050) {
          if (entry.tx.tx_status == "success" && entry.tx.tx_type == "contract_call" && entry.tx.contract_call.function_name == "vote" && entry.tx.contract_call.function_args[2].repr == "'SP3JP0N1ZXGASRJ0F7QAHWFPGTVK9T2XNXDB908Z.sip-027-multisig-transactions") {
            if (entry.tx.contract_call.function_args[1].repr == "true") {
              const amount = parseInt(entry.tx.contract_call.function_args[0].repr.slice(1));
              yesAmount += amount;
              yesCount++;
              daoVotesForCsv.push({
                voter: entry.tx.sender_address,
                txid: entry.tx.tx_id,
                for: true,
                power: amount,
              });
            } else if (entry.tx.contract_call.function_args[1].repr == "false") {
              const amount = parseInt(entry.tx.contract_call.function_args[0].repr.slice(1));
              noAmount += amount;
              noCount++;
              daoVotesForCsv.push({
                voter: entry.tx.sender_address,
                txid: entry.tx.tx_id,
                for: false,
                power: amount,
              });
            } else {
              console.log("Wrong data:", entry.tx.contract_call);
            };
          };
        };
      }
      offset += 50;
    } else {
      moreData = false;
    }
  }

  console.log("Amount against:", noAmount);
  console.log("Amount for:", yesAmount);
  console.log("Count against:", noCount);
  console.log("Count for:", yesCount);

  const daoVotesCsv = convertVotesToCsv(daoVotesForCsv);

  writeFileSync(MULTISIG_DAO_VOTES_FILE, daoVotesCsv);

  console.log('CSV files have been saved successfully.');
}

fetchAllData()


================================================
FILE: sips/sip-027/scripts/validate-and-count-votes/package.json
================================================
{
  "name": "validate-and-count-votes",
  "version": "1.0.0",
  "main": "index.js",
  "type": "module",
  "scripts": {
    "start": "node index.js"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "dependencies": {
    "@stacks/stacking": "^6.15.0",
    "@stacks/transactions": "^6.15.0",
    "axios": "^1.7.2",
    "dotenv": "^16.4.5"
  }
}



================================================
FILE: sips/sip-028/sip-028-sbtc_peg.md
================================================
# Preamble

**SIP Number:** 028  

**Title:** Signer Criteria for sBTC, A Decentralized and Programmable Asset Backed 1:1 with BTC  

**Authors:**  
- Adriano Di Luzio ([adriano@bitcoinl2labs.com](mailto@adriano@bitcoinl2labs.com))
- Andre Serrano ([andre@bitcoinl2labs.com](mailto:andre@bitcoinl2labs.com))  
- Ashton Stephens ([ashton@trustmachines.co](mailto:ashton@trustmachines.co)) 
- Daniel Jordon ([daniel@trustmachines.co](mailto:daniel@trustmachines.co))
- Friedger Müffke ([friedger@ryder.id](mailto:friedger@ryder.id))  
- Jesus Najera ([jesus@stratalabs.xyz](mailto:jesus@stratalabs.xyz))  
- Joey Yandle ([joey@trustmachines.co](mailto:joey@trustmachines.co))  
- Jude Nelson ([jude@stacks.org](mailto:jude@stacks.org))  
- Mårten Blankfors ([marten@trustmachines.co](mailto:marten@trustmachines.co))  
- Tycho Onnasch ([tycho@zestprotocol.com](mailto:tycho@zestprotocol.com))  

**Consideration:** Governance 

**Type:** Operation  

**Status:** Ratified 

**Created:** 2024-06-21

**License:** BSD 2-Clause

**Sign-off:**
- Jason Schrader jason@joinfreehold.com (Governance CAB)
- Jude Nelson jude@stacks.org (Steering Committee)

**Discussions-To:**
- [sBTC Working Group Discussions](https://github.com/stacks-network/sbtc/discussions) 

## Abstract

This SIP proposes a new wrapped Bitcoin asset, called sBTC, which would be implemented on Stacks as a SIP-010 token. sBTC enables seamless and secure integration of Bitcoin into the Stacks ecosystem, unlocking decentralized applications and expanding Bitcoin's utility through smart contracts. Stacks today offers a smart contract runtime for Stacks-hosted assets, and the forthcoming Stacks [3.0 release](https://github.com/stacksgov/sips/blob/main/sips/sip-021/sip-021-nakamoto.md) provides lower transaction latency than Bitcoin for Stacks transactions. By providing a robust BTC-wrapping mechanism based on [threshold signatures](https://eprint.iacr.org/2020/852.pdf), users would be able to lock their real BTC on the Bitcoin chain, instantiate an equal amount of sBTC tokens on Stacks, use these sBTC tokens on Stacks, and eventually redeem them for real BTC at 1:1 parity, minus the cost of the relevant blockchain transaction fees.

This is the first of several SIPs that describe such a system. This SIP describes the threshold signature mechanism and solicits from the ecosystem both a list of signers and the criteria for vetting them. These sBTC signers would be responsible for collectively holding all locked BTC and redeeming sBTC for BTC upon request. Given the high-stakes nature of their work, the authors of this SIP believe that such a wrapped asset can only be made to work in practice if the Stacks ecosystem members can reach broad consensus on how these signers are chosen. Thus, the first sBTC SIP put forth for activation concerns the selection of sBTC signers.

This SIP outlines but does not describe in technical detail the workings of the first sBTC system. A separate SIP will be written to do so if this SIP successfully activates.

## Introduction

### Glossary
| Term                | Definition                                                                                                                                                            |
|---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **.sbtc contract**  | A smart contract (or a collection of contracts) defining the sBTC token and functions related to it.                                                                    |
| **Deposit API**     | A third-party API that communicates with the sBTC Signers via the sBTC Signer API.                                                                                      |
| **SIP-10 Token**    | A token on the Stacks blockchain that adheres to the fungible token standards outlined in [SIP-10](https://github.com/stacksgov/sips/blob/main/sips/sip-010/sip-010-fungible-token-standard.md).                                                                       |
| **Stacks Signer**   | An entity that receives PoX payouts for stacking their STX tokens and actively participating in the Stacks protocol by signing mined blocks.                            |
| **sBTC**            | A SIP-10 token on the Stacks Blockchain that can be turned back into BTC on the Bitcoin Blockchain. 1 sBTC is equivalent to 1 BTC on the Bitcoin Blockchain.           |
| **sBTC operation**  | A smart contract function call that initiates some action from the sBTC protocol.                                                                                                        |
| **sBTC Peg Wallet** | The single UTXO holding the entire BTC balance that’s pegged into sBTC. This peg wallet is managed and maintained by the sBTC Signers.                                  |
| **sBTC Signer**     | An entity that will sign sBTC operations and communicate with contracts on the chain to make that feasible. This entity has partial access to spending the sBTC UTXO.   |
| **sBTC Signer API** | An API exposed by the sBTC Signer that handles basic low-level commands.                                                                                                |
| **sBTC Signer Set** | The set of all sBTC signers. Each is registered with the .sbtc contract and these entities as a group collectively maintain the sBTC's Bitcoin UTXO.      |
| **Two-way peg**     | A two-way peg allows assets to move between two blockchains in a trustless manner. This proposal focuses on implementing such a peg between Bitcoin and Stacks, enabling users to lock BTC on Bitcoin and mint an equivalent amount of sBTC on Stacks. |
| **Wrapped Bitcoin** | A tokenized version of Bitcoin on another blockchain, designed to maintain a 1:1 peg with BTC. It acts as a derivative asset that allows Bitcoin to be utilized in various decentralized applications and ecosystems. |


## Problem Statement

Bitcoin Script's computational expressiveness is limited, such that developers who want to build non-trivial decentralized applications must first build and maintain non-trivial off-chain services to make up the difference. Namely, because Bitcoin Script programs can neither store nor read arbitrary chain state (up to VM-imposed size limits), applications that maintain state across Bitcoin transactions must not only provide the means of storing it themselves but also somehow make it available to subsequent Bitcoin transactions.

Doing this in an open-membership peer-to-peer setting has been shown to be a difficult task (given the size and complexity of systems like Lightning, Taro, Bisq, and BitVM), which imposes a high barrier to entry for building decentralized applications on Bitcoin. Our key insight is that existing applications built on Bitcoin have built up most of the workings of an L2 blockchain like Stacks, but have done so implicitly within their interior components. This SIP makes this design choice explicit: the act of building non-trivial applications on Bitcoin is the act of building on a Bitcoin L2, and therefore the act of providing a rich programming environment for BTC is the act of implementing a wrapped BTC asset (sBTC) on a Bitcoin L2 with smart contracts. Indeed, this has been realized already with systems like Rootstock's RBTC.

## Proposed Solution

sBTC aims to mitigate Bitcoin’s limitations by combining the capability of the Stacks Blockchain with the reliability and security of Bitcoin. By enabling the secure movement of BTC in and out of the Stacks Blockchain via the sBTC protocol, users can interact with their BTC on Stacks using Clarity smart contracts which will benefit from faster block times than Bitcoin. The protocol is “secure” in that it is operated by a decentralized signer network, removing the risk of a single point of failure and trust in a single custodian. Users can deposit BTC into the protocol, seamlessly transact using sBTC on the Stacks blockchain, and have the freedom to redeem sBTC tokens for the underlying BTC at any time.

### Programmability

[Clarity](https://docs.stacks.co/clarity/overview) is the smart contract language on Stacks, which allows developers to encode essential business logic on a blockchain. Using smart contracts, developers can build more expressive decentralized applications that interact with sBTC, such as DeFi protocols, stablecoins, payments, and many others.

### Fast Blocks

The Stacks Nakamoto Upgrade, proposed in [SIP-021](https://github.com/stacksgov/sips/blob/main/sips/sip-021/sip-021-nakamoto.md#proposed-solution), enables fast blocks where user-submitted transactions will now take on the order of seconds, instead of tens of minutes. Thus, sBTC on Stacks will offer an improvement to Bitcoin’s current transaction times.

The sBTC protocol not only addresses the limitations of Bitcoin's scripting system but also provides a secure and decentralized solution for utilizing Bitcoin in various applications.

## Design

While the first sBTC implementation is under development, the wrapped nature of the sBTC token means that any such system would have the following properties:

- sBTC is a SIP-10 token backed 1:1 by BTC.
- The sBTC peg wallet is maintained by the set of sBTC signers. These signers are responsible for the security and maintenance of the wallet, ensuring that sBTC is redeemable for BTC.
- Bitcoin can be converted into sBTC within 3 Bitcoin blocks, and sBTC can be converted into Bitcoin within 6 Bitcoin blocks. sBTC relies on the forking behavior guaranteed by [SIP-021](https://github.com/stacksgov/sips/blob/main/sips/sip-021/sip-021-nakamoto.md) in order to maintain the peg wallet correctly across forks.

## Specification

Management of the sBTC peg wallet on the Bitcoin blockchain shall be managed by the proposed set of signers through a democratic process, involving the sBTC Signer Set rather than a single custodian. At launch, the sBTC protocol will be maintained by 15 independent entities that make up the sBTC Signer Set and each unique signer is allocated exactly one vote. The system requires at least 70%, or 11 out of 15 signatures, for an sBTC operation to be fulfilled. The eligibility criteria to become an sBTC Signer are determined through the community governance process of ratifying this SIP. For this release, sBTC will not be part of Stacks consensus.

sBTC Signers are responsible for accepting or rejecting all sBTC deposit and withdrawal operations submitted to the network. For a transaction to be fulfilled, at least 70% of the signers need to approve the transaction. This means that the liveness and reliability of the signers is crucial to the success of the protocol. The system is live ("resilient") if at least 70% of the sBTC Signer voting power are online and honest. Then (and only then), deposits and withdrawals happen in a timely manner. The system is safe ("trustworthy") if at least 30% of the sBTC Signer voting power is honest. Then, no theft of funds can occur. Additionally, more details on sBTC deposit and withdrawals are included in the appendix of this SIP. 

While up to 30% of the signers can be offline without a user impact on the functioning of the protocol, it becomes more critical for the rest of the signers to approve sBTC operations because operations necessarily still need to meet 70% of the original signing power. If more than 30% of signers become unavailable, no sBTC operations will be approved until at least 70% come back online and operational. In the event that 30% of signer set goes permanently offline, the BTC in the peg wallet will become locked. While not currently planned for the initial sBTC release, it is possible to add a clawback mechanism that would allow recovering the BTC. To protect users from a liveness failure during deposit, a deposit UTXO shall be made satisfiable by one of two spending conditions: (1) the signer set spends the UTXO, or (2) the user spends the UTXO after a fixed number of Bitcoin blocks have passed. Then, if there is an indefinite liveness failure, users will be able to reclaim their in-flight BTC [3]. 


### sBTC Signer Responsibilities
The sBTC signers play a critical role in the security and operations of the sBTC system. Their responsibilities can be grouped into two categories: tasks mandated by the sBTC protocol and operational best practices to effectively manage the sBTC system.

**Protocol-Mandated Tasks:**
- Signers must accept and process BTC deposit requests.
- They must fulfill BTC withdrawal requests in a timely manner, ensuring accurate execution.
- Signers are responsible for moving BTC to a new UTXO when private keys are rotated.
- Signers must perform UTXO consolidation as BTC is deposited to optimize the number of unspent outputs [1].
- Signers are required to deduct transaction fees from users to fund BTC withdrawal transactions. This includes:
  - Ensuring that the transaction fee is deducted from the user.
  - Setting a minimum sBTC withdrawal amount to cover the estimated transaction fees.
  - Estimating the transaction fee proportionally based on the requested operation [2].
 
**Operational Best Practices:**
- Signers must maintain industry-standard operational security (opsec) around hosts and private data, including private keys.
- They should collectively coordinate to calculate and advertise the fee parameters of the system, including:
  - The minimum sBTC peg-out amount.
  - The STX transaction fee for minting sBTC. This fee is paid by the user and can be sponsored by a 3rd party.

### sBTC Signer Eligibility Criteria

Signers will run the sBTC binary in addition to the core Stacks signer software and must meet certain criteria in order to facilitate the reliable functioning of the sBTC protocol at all times.

The following eligibility criteria will be used to identify the sBTC Signers:

- Does the proposed sBTC signer have a demonstrable operating history which shows their experience and reliability in running blockchain services?
- Has the proposed sBTC signer participated in running a Stacks signer instance on Stacks 2.5 testnet or mainnet, and can they provide metrics showing this (ex: amount of stacks stacked over past several cycles)?
  * Note: The sBTC signer is a Stacks event observer, meaning that the experience of running a Stacks node signer directly translates to running an sBTC signer.
- Does the proposed sBTC signer agree to use reasonable efforts to maintain >99% uptime on the sBTC Signer? 
  * Note: This metric may be self-affirmed if independent verification is not possible, or confirmed by on-chain voting/stacking activity.
- Does the proposed sBTC signer commit to a direct communication channel to be set up with the sBTC core engineers in order to respond to urgent updates within 24 hours?
- Has the signer made contributions to Bitcoin or the Stacks network over the past year that demonstrate their commitment to the growth and success of the network? Examples include, but are not limited to: publishing independent research, marketing, co-authoring a SIP, submitting a Stacks pull request/issue, providing feedback on Stacks core development, or contributing to a Stacks Working Group.
- Does the geographic distribution of the proposed sBTC signer support a diverse and distributed signer set?

The criteria described above will be used to identify sBTC Signers that are able to meet some or all of the responsibilities described in the previous section.

### Selection Process
The sBTC Signer Set will be finalized from the list of eligible Signers, based on the above criteria. The [sBTC Working Group](https://github.com/orgs/stacks-network/discussions/508) will conduct the vetting process and the results will be published as a discussion in the [sBTC Github repository](https://github.com/stacks-network/sbtc/discussions/624). 

The selection process is as follows:
1. **Nomination Phase**: Open a call for nominations within the community.
2. **Evaluation & Community Feedback**: The proposed signer set will be published to provide transparency.
3. **SIP Vote**: The community will vote on the sBTC signer criteria.
4. **Final Selection**:  If SIP-028 is ratified, then the proposed signer set voted upon in step 3 shall be the initial signing set for sBTC. If the signer set changes during the vote, such as by the withdrawal of one or more candidates, then the vote will be restarted in a subsequent reward cycle (to be determined if this comes to pass).

   
### Updating The sBTC Signer Set
In the event that the sBTC Signer Set needs to be updated (for example, if a signer is no longer available to complete their responsibilities) sBTC Signers can perform a threshold vote to agree on the updated set, which would require the same 70% approval threshold as sBTC operations. This process will also be performed if a signer needs to rotate their cryptographic keys.


## Related Work

### [WBTC](https://wbtc.network/assets/wrapped-tokens-whitepaper.pdf)

**WBTC** is a closed membership system made up of 50+ merchants and custodians with keys to the WBTC multisig contract on Ethereum. WBTC deposits and withdrawals can only be performed by the authorized merchants, and end users purchase WBTC directly from the merchants. Until recently, BTC was held in a Bitcoin multi-sig wallet secured solely by BitGo. Now, two of the three multi-sig keys are held by BitGo, while one is held by BiT Global.

### [tBTC v2](https://whitepaper.io/document/691/tbtc-whitepaper)

**tBTC** is an ERC-20 wrapped asset launched in May 2020. BTC is currently held and secured by a permissioned set of 35 Beta Staker Nodes from the Threshold Network. Seven DeFi protocols including Aave and Synthetix manage the minting and burning process, with Guardians monitoring to veto suspicious behavior. tBTC is natively minted on Ethereum and Arbitrum.

### [RBTC](https://rootstock.io/static/a79b27d4889409602174df4710102056/RS-whitepaper.pdf)

**rBTC** is a wrapped BTC asset natively minted on Rootstock, an EVM-compatible sidechain. BTC is secured by a 5-of-9 multi-sig Bitcoin wallet controlled by the Powpeg Federation. Peg operations settle to Bitcoin via merge mining. Instead of collateralizing the system with a new token, peg operators are incentivized by earning a portion of transaction fees. PowPeg operators keep specialized hardware called PowHSMs active and connected to special types of Rootstock full nodes. Since the Bitcoin blockchain and the Rootstock sidechain are not entangled in a single blockchain or in a parent-child relation, peg-in and peg-out transactions require a high number of block confirmations. Peg-ins require 100 Bitcoin blocks, and peg-outs require 4000 Rootstock blocks (roughly 200 Bitcoin Blocks).

The following table summarizes the main design differences between these systems:

| Feature                | WBTC            | tBTC             | rBTC             | sBTC (this SIP)    |
|------------------------|-----------------|------------------|------------------|--------------------|
| Spending threshold      | 2 of 3          | 51 of 100        | 5 of 9           | 11 of 15           |
| Bitcoin finality        | No              | No               | Yes              | Yes                |
| Expected Peg-in speed   | 1 hour          | 1-3 hours        | 16 hours         | 0.5 hours          |
| Expected Peg-out speed  | 1 hour          | 3-5 hours        | 33.3 hours       | 1 hour             |
| Custodian rotation      | No              | Yes              | No               | Yes                |
| Fee structure           | % of BTC moved  | % of BTC moved   | Transaction fees | Transaction fees   |


In conclusion, the sBTC system shares similarities with existing models but introduces some key distinctions:
- **Bitcoin Finality:** sBTC inherits Bitcoin finality from [Stacks 3.0](https://github.com/stacksgov/sips/blob/feat/sip-021-nakamoto/sips/sip-021/sip-021-nakamoto.md), which ensures that sBTC transactions receive the same level of security provided by the Bitcoin network.
- **Faster Deposit & Withdrawal Times:** sBTC enables BTC withdrawals without the long delays associated with block confirmations in other systems. This is achieved through the finality rules described in [Stacks 3.0](https://github.com/stacksgov/sips/blob/feat/sip-021-nakamoto/sips/sip-021/sip-021-nakamoto.md).


## Activation

sBTC is designed to activate on Stacks 3.0 as defined in [SIP-021](https://github.com/stacksgov/sips/blob/feat/sip-021-nakamoto/sips/sip-021/sip-021-nakamoto.md). Therefore, this SIP is only meaningful when SIP-021 activates. The sBTC Working Group plans to observe at least 2-4 weeks of network behavior on Stacks Nakamoto to ensure a stable release. After this period, sBTC can be activated on the Stacks network without requiring a separate hard fork.

### Process of Activation

Users can vote to approve this SIP with either their locked/stacked STX or with unlocked/liquid STX, or both. The SIP voting page can be found at [sbtc.vote](https://sbtc.vote). The criteria for the stacker and non-stacker voting is as follows.

#### For Stackers:

In order for this SIP to activate, the following criteria must be met by the set of Stacked STX:

- At least 80 million Stacked STX must vote, with least 70% (56 million) voting "yes".

The voting addresses will be:

| **Vote** | **Bitcoin Address**              | **Stacks Address**                    | Message      | ASCII-encoded message                      | Bitcoin script                                                                                  |
| -------- | -------------------------------- | ------------------------------------- | ------------ | ------------------------------------------ | ----------------------------------------------------------------------------------------------- |
| yes      | `11111111111mdWK2VXcrA1e7dnvidC` | `SP00000000001WPAWSDEDMQ0B9J72P0KAK2` | `yes-sip-28` | `000000000000000000007965732d7369702d3238` | `OP_DUP` `OP_HASH160` `000000000000000000007965732d7369702d3238` `OP_EQUALVERIFY` `OP_CHECKSIG` |
| no       | `111111111111ACW5wa4RwyeKYEAzMD` | `SP000000000006WVSDEDMQ0B9J73E2TN78`  | `no-sip-28`  | `00000000000000000000006e6f2d7369702d3238` | `OP_DUP` `OP_HASH160` `00000000000000000000006e6f2d7369702d3238` `OP_EQUALVERIFY` `OP_CHECKSIG` |

The addresses have been generated as follows:

- Encode `<message>` in ASCII, with 0-padding.
- Use the resulting `<encoding>` in the Bitcoin script`OP_DUP` `OP_HASH160` `<encoding>` `OP_EQUALVERIFY` `OP_CHECKSIG`.
- The Bitcoin address is the `base58check` of the hash of the Bitcoin script above.
- The Stacks address is the `c32check-encoded` Bitcoin address.

Stackers (pool and solo) vote by sending Stacks dust to the corresponding Stacks address from the account where their Stacks are locked.

Solo stackers only can also vote by sending a bitcoin dust transaction (6000 sats) to the corresponding bitcoin address.

#### For Non-Stackers:

Users with liquid STX can vote on proposals directly at [sBTC.vote](https://sbtc.vote) using the Ecosystem DAO. Liquid STX is the user’s balance, less any STX they have locked in the PoX stacking protocol, at the block height at which the voting started (preventing the same STX from being transferred between accounts and used to effectively double vote). This is referred to generally as "snapshot" voting.

For this SIP to pass, 70% of all liquid STX committed by voting must be in favor of the proposal. 

We believe that these thresholds are sufficient to demonstrate interest from Stackers -- Stacks users who have a long-term interest in the Stacks blockchain's successful operation -- in performing this upgrade.

### Activation Status

At the end of Bitcoin block height 869,749, the following vote was recorded: **A total of 135,940,943 STX participated, with 135,801,729 STX (99.90%) voting 'Yes' and 139,214 STX (0.10%) voting 'No'.**

A breakdown of the vote is as follows:
- For STX locked in stacking, a total of 126,084,232 STX participated. Of this, 125,945,571 STX (99.89%) from 77 accounts voted 'Yes', while 138,661 STX (0.11%) from 1 account voted 'No'.
- For unlocked STX, a total of 9,718,049 STX participated. Of this, 9,717,496 STX (99.99%) from 1,175 accounts voted 'Yes', while 553 STX (0.01%) from 40 accounts voted 'No'.

All voting criteria from STX holders have been met. A breakdown of the transactions can be found [here](https://stx.eco/dao/proposals/SP3JP0N1ZXGASRJ0F7QAHWFPGTVK9T2XNXDB908Z.sip028-signer-criteria-for-sbtc/results2).

The API where results come from can be found [here](https://github.com/radicleart/stxeco-api-vote).

## Appendix
[1] https://github.com/stacks-network/sbtc/issues/52

[2] https://github.com/stacks-network/sbtc/pull/186

[3] https://github.com/stacks-network/sbtc/issues/30

### Specification

#### Deposits

The main steps of the sBTC Deposit flow will be as follows:

1. **Deposit request:** A bitcoin holder creates a transaction on Bitcoin.
  - The deposit transaction contains a UTXO (deposit UTXO) spendable by sBTC Signers, with an OP_DROP payload.
  - The payload contains the recipient address of the sBTC and the maximum fee the depositor is willing to have go towards the consolidation of the deposits into a single UTXO.
2. **Proof of deposit:** The bitcoin holder submits a proof of deposit on Stacks by invoking the Deposit API.
3. **Deposit accept:** 
  - **Deposit redeem:** The sBTC Signers redeem the deposit by consuming the deposit UTXO, consolidating it into the sBTC UTXO.
  - **Mint:** The sBTC Signers finalize the deposit acceptance making a Clarity contract call that mints the sBTC on the Stacks Layer.

#### Withdrawals (Redeeming sBTC)

The main steps of the sBTC withdrawal flow are as follows:

1. **Withdrawal request:** An sBTC holder calls the `withdraw-request` function in the `.sbtc` contract.
   - This transfers the requested amount of sBTC to the `.sbtc` contract & mints the user a non-transferable locked-sBTC as a placeholder.
2. **Withdrawal accept:** If accepted, the following happens:
   - The signers create a transaction on Bitcoin which returns the requested amount to the designated address.
   - Once the Bitcoin transaction is confirmed, the signers make a smart contract call to one of the `.sbtc` contracts to mark the transaction as fulfilled.
   - If successful, the resulting Stacks transaction will record the withdrawal request as complete & will accordingly burn the user’s locked-sBTC.
3. **Withdrawal reject:** If instead the request is rejected, the sBTC signers will call the `withdraw-reject` function in the `.sbtc` smart contract. This function does the following:
   - Returns the sBTC to the holder.
   - Records the signer votes.



================================================
FILE: sips/sip-029/sip-029-halving-alignment.md
================================================
# Preamble

**SIP Number:** 029

**Title:** Preserving Economic Incentives During Stacks Network Upgrades

**Authors:**
- Alex Miller (alex@hiro.so)
- Andre Serrano (andre@bitcoinl2labs.com)
- Brittany Laughlin (brittany@lattice.vc)
- Jesse Wiley (jesse@stacks.org)
- Jude Nelson (jude@stacks.org)
- Philip De Smedt (philip@stackingdao.com)
- Tycho Onnasch (tycho@zestprotocol.com)
- Will Corcoran (will@stacks.org)

**Consideration:** Economics, Technical, Governance

**Type:** Consensus (hard fork)

**Status:** Ratified

**Created:** 2024-11-06

**License:** BSD 2-Clause

**Sign-off:**
- j2p2 i.digg.tech@gmail.com (SIP Editor)
- Mike Cohen mjoecohen@gmail.com (Technical CAB)
- Jason Schrader jason@joinfreehold.com (Governance CAB)
- MattySTX mattystx@gmail.com (Economics CAB)

**Discussions-To:**
- Stacks Forum Post: [Aligning with Bitcoin Halving and Incentives after Nakamoto](https://forum.stacks.org/t/aligning-with-bitcoin-halving-and-incentives-after-nakamoto/17668)


# Abstract

The first Stacks halving is expected to take place 210,384 Bitcoin blocks after the Stacks 2.0 starting height, 666,050, which is Bitcoin height 876,434, which is set to occur during Reward Cycle 100 in December 2024, cutting the STX block reward from 1,000 STX to 500 STX. This SIP proposes a modification to the emissions schedule given that the network is going through two major launches (Nakamoto and sBTC) which rely on predictable economic incentives. The proposed schedule modification and associated STX emission rate would create time for Nakamoto and sBTC to launch and settle in, but, being mindful of supply, would still result in an overall reduced target 2050 STX supply (0.77% lower) and a reduced tail emission rate (50% lower).

# License and Copyright

This SIP is made available under the terms of the BSD-2-Clause license,
available at https://opensource.org/licenses/BSD-2-Clause.  This SIP’s copyright
is held by the Stacks Open Internet Foundation.

# Introduction

STX halvings were originally designed to happen every 4 years, similar to Bitcoin. The first Stacks halving is expected to take place at Bitcoin block 876,434, which is set to occur during Reward Cycle 100 in December 2024, cutting the STX block reward from 1,000 STX to 500 STX, thereby significantly altering the economic incentives of mining on the Stacks blockchain. At the same time, the Stacks network is going through two major upgrades/changes, both of which are highly dependent on economic incentives.

First, the role of Stackers is changing. The role of Stackers in the Nakamoto blockchain (SIP-021) differs from their role in the original Stacks blockchain in that they must now collectively sign Stacks blocks. This is required to prevent Stacks forks from arising, and to secure the chain tip before it can be fully anchored to the Bitcoin chain. This also means that Stackers must run and maintain signing nodes with high availability in order to ensure that blocks always reach the requisite signature threshold. The PoX payouts (SIP-007) granted to Stackers by miners provide a positive monetary incentive for Stackers to carry out this task.

Second, the release of the Nakamoto blockchain unblocks sBTC (SIP-028), a wrapped Bitcoin asset on the Stacks blockchain which benefits from Nakamoto’s newfound resistance to forks. Because inducing a chain reorganization (a reorg) in Nakamoto is at least as hard as doing so in the Bitcoin blockchain, applications can rely on Nakamoto to ensure that each sBTC token is backed 1:1 by a BTC token – there is no feasible way to double-spend sBTC through a Stacks blockchain reorg.

Because of how important both of these upgrades are to the future of the Stacks blockchain and the dependency of all blockchains on economic incentives for security, changing the incentives while the system is going through a transition could have negative impacts. In particular, given that miners bid BTC in order to win the STX coinbase reward (and that BTC is what provides PoX payouts for Signers), it is highly likely that a 50% reduction in the STX coinbase reward would lead to a corresponding 50% reduction in PoX payouts, thereby dramatically decreasing incentives for signers while Nakamoto and sBTC are gaining adoption. Additionally, as discussed in the 7th Avenue Group report [1][2], by reducing the gross value of the block rewards and corresponding PoX payouts, it is likely that some miners and signers may choose to cease their work on the Stacks blockchain, reducing competition and economics further.

While ultimately halvings do need to happen, for those reasons, it would be highly preferable to not change the economic incentives until both Nakamoto and sBTC have been live for some time, as well as to have reductions in the STX block reward happen at the same time as reductions in the BTC block reward given their links.

Therefore, this SIP proposes altering the token emission schedule to preserve the existing incentive structure while ensuring no increase in the 2050 target supply, and incorporating these principles:

* All STX holders would see a reduced 2050 target STX supply by 0.77%, thereby making STX more scarce
* All STX holders would see a reduced tail inflation (from 125 STX to 62.5 STX) after the final halving
* Stacks miners and signers’ economic incentives would remain consistent with the existing incentives for the next 16 months
* The new Stacks halving schedule would align with Bitcoin halvings starting in 2028 to strengthen the connection the Stacks L2 has to Bitcoin and also synchronize the economic adjustments of both assets, reducing changes in incentives for miners and signers at each halving, as further outlined in the Forum post [3]

# Specification

Applying these upgrades to the Stacks blockchain requires a consensus-breaking network upgrade, in this case, a hard fork. Like other such changes, this will require a new Stacks epoch. In this SIP, we will refer to this new epoch as Stacks 3.1.

The _current_ STX emission schedule is presented as follows.  Note that the **first STX halving is in December 2024**.  The tail emission after the final halving in 2032 would be 125 STX per block.

| Coinbase Reward Phase | Bitcoin Height | Approx Date | STX Supply at Block | STX Reward | Annual Inflation |
|--------------------|----------------|----------------------|-------------------|------------|-----------------|
| Current            | 870,100        | -                    | 1,552,452,847    | 1000       | -               |
| 1st                | 876,434        | Dec 2024             | 1,558,786,847    | 500 (50%)  | 3.37%          |
| 2nd                | 1,086,818      | Dec 2028             | 1,663,978,847    | 250 (50%)  | 1.58%          |
| 3rd                | 1,297,202      | Dec 2032             | 1,716,574,847    | 125 (50%)  | 0.77%          |
| -                  | 2,197,560      | Jan 2050 (17.08y)    | 1,829,119,597    | 125 (0%)   | 0.36%          |


The _proposed_ STX emission schedule is presented as follows.  In particular, this SIP proposes preserving the 1000 STX coinbase until April 2026.  After this, there would be a halving to 500 STX after two years, aligning the remaining Stacks halving block heights with Bitcoin's halving schedule. Four years later, emissions halve again to 125 STX, and the tail emission after the final halving in 2036 would be 62.5 STX. This brings the total supply in 2050 to 1,804,075,347, or about 0.77% lower than the original 1,818,000,000 estimate.

| Coinbase Reward Phase | Bitcoin Height | Approx Date           | STX Supply at Block | STX Reward | Annual Inflation |
|--------------------|----------------|---------------------|-------------------|------------|-----------------|
| Current            | 870,100        | -                   | 1,552,452,847    | 1000       | -               |
| 1st                | 945,000        | Apr 2026 (+1.33y)   | 1,627,352,847    | 500 (50%)  | 3.23%          |
| 2nd                | 1,050,000      | Apr 2028 (2y)       | 1,679,852,847    | 250 (50%)  | 1.57%          |
| 3rd                | 1,260,000      | Apr 2032 (4y)       | 1,732,352,847    | 125 (50%)  | 0.76%          |
| 4th                | 1,470,000      | Apr 2036 (4y)       | 1,758,602,847    | 62.5 (50%)   | 0.37%          |
| -                  | 2,197,560      | Jan 2050 (13.83y)   | 1,804,075,347    | 62.5 (0%)   | 0.18%          |


With these changes, miner incentives and PoX yield remain unchanged for another 16 months, which we believe is sufficient time for the nascent Nakamoto signer set to develop into a set of stable, professional block signers, and for the sBTC project to attract sufficient initial liquidity.

The model for both the current and proposed emissions schedules can be found in the SIP-029 Stacks Emission Model[4].

# Related Work

While many blockchain protocols implement token emission schedules with periodic reductions in block rewards, we are not aware of any precedent for modifying an emission schedule specifically to maintain economic incentives during major protocol upgrades.

# Backwards Compatibility

This change requires a hard fork of the Stacks blockchain

# Activation

## Voting Timeline

Voting will begin at bitcoin block height 870,750, which occurs ~ Sunday, November 17th, 2024.
Voting will conclude at bitcoin block height 872,750, which occurs ~ Sunday, December 1st, 2024.

## Activation

The SIP-029 STX emission schedule is designed to activate on Stacks 3.0 as defined in [SIP-021](https://github.com/stacksgov/sips/blob/main/sips/sip-021/sip-021-nakamoto.md).  The SIP-029 emission schedule will be active starting at bitcoin block height 875,000, which is in the middle of stacking cycle 99.

### Process of Activation

Users can vote to approve this SIP with either their locked/stacked STX or with unlocked/liquid STX, or both. The SIP voting page can be found at [stx.eco](https://stx.eco). The criteria for the stacker and non-stacker voting is as follows.

#### To Vote:

In order for this SIP to activate, the following criteria must be met:

- At least 80 million stacked STX must vote, with at least 80% of all stacked STX committed by voting must be in favor of the proposal (vote "yes").
- At least 80% of all liquid STX committed by voting must be in favor of the proposal (vote "yes").

The voting addresses will be:

| Vote | Bitcoin Address | Stacks Address | Msg | ASCII-encoded msg | Bitcoin script |
| - | - | - | - | - | - |
| yes      | `11111111111mdWK2VXcrA1e7in77Ux` | `SP00000000001WPAWSDEDMQ0B9J76GZNR3T` | `yes-sip-29` | `000000000000000000007965732d7369702d3239` | `OP_DUP` `OP_HASH160` `000000000000000000007965732d7369702d3239` `OP_EQUALVERIFY` `OP_CHECKSIG` |
| no       | `111111111111ACW5wa4RwyeKgtEJz3` | `SP000000000006WVSDEDMQ0B9J76NCZPNZ`  | `no-sip-29`  | `00000000000000000000006e6f2d7369702d3239` | `OP_DUP` `OP_HASH160` `00000000000000000000006e6f2d7369702d3239` `OP_EQUALVERIFY` `OP_CHECKSIG` |

The addresses have been generated as follows:

- Encode `<message>` in ASCII, with 0-padding.
- Use the resulting `<encoding>` in the Bitcoin script`OP_DUP` `OP_HASH160` `<encoding>` `OP_EQUALVERIFY` `OP_CHECKSIG`.
- The Bitcoin address is the `base58check` of the hash of the Bitcoin script above.
- The Stacks address is the `c32check-encoded` message.

All STX holders vote by sending Stacks dust to the corresponding Stacks address from the account where their Stacks are held (stacked or liquid). To simplify things, user's can create their votes by visiting the [stx.eco](https://stx.eco/) platform. Voting power is determined by a snapshot of the amount of STX (stacked and un-stacked) at the block height at which the voting started (preventing the same STX from being transferred between accounts and used to effectively double vote).

Solo stackers only can also vote by sending a bitcoin dust transaction (6000 sats) to the corresponding bitcoin address.

#### For Miners

There is only one criterion for miners to activate this SIP: they must mine the Stacks blockchain up to and past the end of the voting period (bitcoin block height 872,750). In all reward cycles between cycle 97 & 98 and the end of the voting period, PoX must activate.

# Reference Implementation

The reference implementation can be found at https://github.com/stacks-network/stacks-core/pull/5461.

# References

[1] Soslow, J (2023) Review of Mining Emissions and Risks of the Halving. Available at https://stx.is/emissions-report-1 [Verified 5 November 2024]

[2] Soslow, J (2023) Halving Proposals. Available at https://stx.is/emissions-report-1 [Verified 5 November 2024]

[3] Laughlin, B (2024) Aligning with Bitcoin Halving and Incentives after Nakamoto. [Online forum post] forum.stacks.org https://forum.stacks.org/t/aligning-with-bitcoin-halving-and-incentives-after-nakamoto/17668 [Verified 5 November 2024]

[4] Müffke, F & Corcoran, W (2024) SIP-029 Stacks Emission Model. [Online spreadsheet] docs.google.com https://docs.google.com/spreadsheets/d/1ZRQgQV99kWvcSjkmZWKgldflcB2ytaN6sjo2RiHcjnk/edit?gid=0#gid=0 [Verified 13 November 2024]


