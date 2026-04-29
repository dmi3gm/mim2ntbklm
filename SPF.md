

# SOURCE_FILE: process/README.md
---
# /process/ — Knowledge Creation Process

## Purpose of This Directory

This directory contains the **normative process for creating and evolving SPF packs**. It describes the activity of knowledge production, not the knowledge itself.

| Directory | Contains |
|-----------|----------|
| `/pack/` | Domain knowledge (second principles) |
| `/process/` | Activity of producing that knowledge |

These are fundamentally different:
- `/pack/` answers "What does the domain know?"
- `/process/` answers "How is that knowledge created, validated, and maintained?"

---

## Knowledge vs. Knowledge-Creation Process

| Aspect | Domain Knowledge (pack) | Knowledge-Creation Process |
|--------|------------------------|---------------------------|
| **Subject matter** | Distinctions, methods, products of a domain | Activity of formalizing knowledge |
| **Changes when** | Domain understanding evolves | Process methodology improves |
| **FPF type** | Content of second principles | Meta-process for producing them |
| **Can be wrong about** | Domain facts | Procedure effectiveness |

The process is **not part of the pack**. A medical SPF pack contains medical knowledge; this process describes how any SPF pack (medical, engineering, personal development) is created.

---

## Relationship to FPF and SPF

```
FPF (First Principles)
    ↓ provides meta-language
/process/ (Knowledge Creation)
    ↓ produces
SPF Pack (Second Principles)
    ↓ consumed by
Downstream (courses, guides, AI agents)
```

- **FPF** provides the language of distinctions (method vs. tool, role vs. person, etc.)
- **This process** uses FPF distinctions to formalize domain knowledge
- **SPF pack** is the output of this process
- **Downstream** uses the pack but does not modify it

---

## Mandatory Use

This process is **not optional**. Any modification to `/pack/` must follow this process.

| Action | Required Process Steps |
|--------|----------------------|
| Adding a method | 03 → 06 → 07 → 10 |
| Adding a distinction | 03 → 10 |
| Adding a failure mode | 06 → 08 → 10 |
| Updating SoTA status | 09 → 10 |
| Expanding domain scope | 01 → 02 → 03 → ... |

Skipping steps produces:
- Incoherent distinctions
- Methods without proper boundaries
- Missing failure modes
- Outdated knowledge presented as current

---

## Process Files

| File | Stage |
|------|-------|
| [00-process-overview.md](00-process-overview.md) | What this process is |
| [01-domain-selection.md](01-domain-selection.md) | Selecting and bounding the domain |
| [02-bounded-context.md](02-bounded-context.md) | Establishing context boundaries |
| [03-distinctions-work.md](03-distinctions-work.md) | Working with distinctions |
| [04-domain-entities-identification.md](04-domain-entities-identification.md) | Identifying stable entities |
| [05-information-ingestion.md](05-information-ingestion.md) | Admitting information for analysis |
| [06-analysis-and-formalization.md](06-analysis-and-formalization.md) | Analyzing through distinctions |
| [07-method-and-product-extraction.md](07-method-and-product-extraction.md) | Extracting methods and products |
| [08-failure-modes-extraction.md](08-failure-modes-extraction.md) | Extracting failure modes |
| [09-sota-annotation.md](09-sota-annotation.md) | Assigning SoTA status |
| [10-map-maintenance.md](10-map-maintenance.md) | Maintaining the navigation map |
| [11-review-and-evolution-cycle.md](11-review-and-evolution-cycle.md) | Ongoing review and evolution |

---

## Process Lint (Mandatory)

**Every change to `/pack/` must pass process lint before commit.**

Process lint is NOT a process stage — it is a **cross-cutting verification protocol** that ensures compliance with the SPF constitution.

| When Applied | By Whom |
|--------------|---------|
| Pre-commit | Author (human or AI) |
| PR Review | Reviewer |
| Agent work | AI after each modification |

### Lint Document

**See: [process-lint.md](process-lint.md)** for:
- Change-type matrix (what to check for each type of change)
- Universal bans (didactics, scenarios, method/tool confusion)
- Hard gates (conditions that block commit)
- Lint report format

### Quick Reference

| Change Type | Key Checks |
|-------------|------------|
| Method | No scenarios, has WP link, has distinction link |
| Work Product | Has existence criteria, links to method |
| Failure Mode | Has detection test, links to distinction |
| Distinction | Has contrast, has test, has consequence |
| SoTA | Has status, has revision criterion |
| Any structural | Map updated |

### Hard Gates

These block commit. No exceptions:
- Method without work product link
- Work product without existence criteria
- Failure mode without detection test
- Structural change without map update
- Didactic language detected

---

## For AI Agents

AI agents working on this repository:
1. Must identify current process stage before modifying pack files
2. Must produce the work products specified for that stage
3. Must not skip to later stages without completing earlier ones
4. Must update the map after any structural change
5. **Must run process lint and report results before committing**

See [CLAUDE.md](/CLAUDE.md) for explicit working rules and lint requirements.


# SOURCE_FILE: README.md
---
# SPF — Second Principles Framework

> **Repository type:** `Base/Principles`

> A framework for formalizing second principles of domain areas into engineering knowledge.

## What is this

**SPF (Second Principles Framework)** is a framework of requirements and processes that defines **how second principles** of a specific domain area can be captured and stabilized as **engineering knowledge**.

SPF answers the question:
> What form and criteria are needed so that second principles become a verifiable core of the domain?

## Key concepts

| Term | Definition |
|------|------------|
| **Second principles** | Stable domain-specific patterns and distinctions within a specific area |
| **Pack (domain passport)** | Formalized engineering core of a domain — the result of applying SPF |
| **FPF** | First Principles Framework — meta-ontology and base distinctions on which SPF is built |

## What SPF defines

**Minimum mandatory elements for an engineering description of a domain:**

| Element | FPF code | Description |
|---------|----------|-------------|
| Bounded context | A.1.1 | Domain boundaries, vocabulary |
| Distinctions | A.7 | Key distinctions |
| Characteristics | A.17-A.19 | Characteristics and indicators |
| Methods | A.3.1-A.3.2 | Assessment/verification methods |
| Work Products | A.15.1 | Work products |
| Failure modes | — | Typical interpretation errors |
| SoTA | Part G | Statuses and revision criteria |

**Structure requirements:**
- Identifier and reference rules
- Canonical pack structure

**Process gates:**
- Process lint: correctness checks
- Contracts between source-of-truth and downstream

## Repository structure

```
SPF/
├── README.md              # This file
├── ontology.md            # Base SPF ontology (SPF.SPEC.002)
├── REPO-TYPE.md           # Repository type
├── docs/                  # Conceptual documentation
│   └── conceptual-model.md
├── process/               # Pack creation process
│   ├── 00-process-overview.md
│   ├── 01-domain-selection.md
│   ├── 02-bounded-context.md
│   ├── 03-distinctions-work.md
│   ├── 04-domain-entities-identification.md
│   ├── 05-information-ingestion.md
│   ├── 06-analysis-and-formalization.md
│   ├── 07-method-and-product-extraction.md
│   ├── 08-failure-modes-extraction.md
│   ├── 09-sota-annotation.md
│   ├── 10-map-maintenance.md
│   ├── 11-review-and-evolution-cycle.md
│   ├── material-ingestion-protocol.md
│   └── process-lint.md
├── spec/                  # Specifications
│   ├── ai-view.md
│   ├── downstream-contract.md
│   ├── f-g-r-trust.md        # FPF B.3 — optional pattern
│   ├── human-guides.md
│   └── SPF.SPEC.001-entity-coding.md
└── pack-template/         # Pack structure template
    ├── 00-pack-manifest.md
    ├── 01-domain-contract/  # + 01C-ontology.md (SPF.SPEC.002)
    ├── 02-domain-entities/
    ├── 03-methods/
    ├── 04-work-products/
    ├── 05-failure-modes/
    ├── 06-sota/
    └── 07-map/
```

## What SPF does NOT do

- **Does not add domain content** — SPF does not know which second principles are valid in your domain
- **Does not build courses** — training is downstream
- **Does not replace research/expertise** — SPF defines form, not content

## Level hierarchy

```
FPF (Level 1)  →  first principles framework (meta-ontology + distinctions)
       ↓
SPF (Level 2)  →  second principles framework (form + process)  ← YOU ARE HERE
       ↓
Pack           →  formalized knowledge of a specific domain
       ↓
Downstream     →  derived representations (courses, AI agents, guides)
```

## SPF universality

SPF is **universal in form and process**, but **not in content**:
- Pack structure is the same for any domain
- Knowledge creation process is the same
- Lint and gates are the same
- But pack content is always domain-specific

## Related repositories

| Repository | Type | Role |
|------------|------|------|
| [ailev/FPF](https://github.com/ailev/FPF) | Framework | First Principles Framework (upstream) |
| [PACK-digital-platform](https://github.com/TserenTserenov/PACK-digital-platform) | Pack | Digital platform domain |
| Pack repositories (downstream) | Pack | Created following SPF |

## How to start creating a pack

1. Study the [conceptual model](docs/conceptual-model.md)
2. Follow the [process](process/README.md)
3. Use the [pack template](pack-template/)
4. Run [lint](process/process-lint.md) checks

---

*SPF — Second Principles Framework*


# SOURCE_FILE: CLAUDE.md
---
# CLAUDE.md — SPF (Second Principles Framework)

> **General instructions:** see `/Users/tserentserenov/IWE/CLAUDE.md`
>
> This file contains only specifics of this repository.

---

## 1. Repository type

**Framework** — second principles framework (form + process for Packs).

**Source-of-truth:** Yes (for the SPF specification).

---

## 2. What is SPF

**SPF (Second Principles Framework)** defines:
- **Form** — canonical Pack structure
- **Process** — how to create and evolve a Pack
- **Contracts** — link between source-of-truth and downstream

SPF **does NOT define** domain content — only form and process.

---

## 3. Hierarchy

```
FPF (Level 1)   →  First Principles Framework (meta-ontology)
       ↓                   ↑ upstream
SPF (Level 2)   →  YOU ARE HERE (form + process)
       ↓                   ↓ downstream
Pack            →  (downstream pack repositories)
```

---

## 3.1. Working with FPF

**Local path:** `~/IWE/FPF/FPF-Spec.md` (4.6 MB, ~50000 lines)

**When to read FPF while working with SPF:**
- When clarifying base distinctions (A.7: Role ≠ Method ≠ Work)
- When working with Bounded Context (A.1.1)
- When verifying process correctness (B.4: Evolution Loop, B.5: Reasoning Cycle)
- When working with SoTA (FPF Part G: SoTA Kit)
- When terminology is unclear (FPF Part F: UTS, Bridges)

**How to read the large FPF file:**
1. Do NOT read it in full — the file is too large
2. First read the table of contents (first 200 lines) — understand the structure
3. Search for specific patterns via Grep: `A.7`, `B.5`, `Part G`
4. Read only the needed section

**FPF structure (for navigation):**

| Part | Content | When needed |
|------|---------|-------------|
| **A** | Kernel: Holon, BoundedContext, Role-Method-Work | Base distinctions |
| **B** | Aggregation (Γ), Trust (F-G-R), Evolution Loop | Processes, trust |
| **C** | Domain extensions: Sys-CAL, KD-CAL, NQD-CAL | Extensions |
| **D** | Ethics & Conflict | Ethics |
| **E** | Constitution & Authoring | Authoring rules |
| **F** | Terminology: UTS, Bridges | Terminology |
| **G** | SoTA Kit | Working with SoTA |

**Updating FPF:** `cd ~/IWE/FPF && git pull`

---

## 4. Repository structure

```
SPF/
├── docs/               # Conceptual documentation
│   ├── conceptual-model.md
│   └── fpf-spf-pack.md   # Full conceptual model
├── process/            # Pack creation process
│   ├── 00-process-overview.md
│   ├── 01-domain-selection.md
│   ├── 02-bounded-context.md
│   ├── 03-distinctions-work.md
│   ├── ...
│   ├── process-lint.md
│   └── material-ingestion-protocol.md
├── spec/               # Specifications
│   ├── ai-view.md
│   ├── downstream-contract.md
│   ├── human-guides.md
│   ├── SPF.SPEC.001-entity-coding.md
│   ├── SPF.SPEC.003-pack-scalability.md
│   └── SPF.SPEC.004-service-clauses.md  # SC vs UC distinction
└── pack-template/      # Pack structure template
    ├── 00-pack-manifest.md
    ├── 01-domain-contract/
    ├── 02-domain-entities/
    ├── 03-methods/
    ├── 04-work-products/
    ├── 05-failure-modes/
    ├── 06-sota/
    ├── 07-map/
    └── 08-service-clauses/  # User-facing promises (SC)
```

---

## 5. Hard Bans

### 5.1 Didactics ban
**BANNED in SPF and Pack:** "step", "lesson", "in N days", "implement", "first/then", "exercise", "module", "week 1"

**REASON:** Didactics is downstream. Pack captures **what exists**, not **how to teach**.

### 5.2 Domain content ban in SPF
**SPF defines form**, not content. Content belongs in Packs.

### 5.3 Entity type confusion ban (FPF A.7: Strict Distinction)

| ❌ Confusion | ✅ Distinction | FPF code |
|-------------|---------------|----------|
| Method = Tool | Method — way of acting, tool — means | A.3.1, A.3.2 |
| Method = Scenario | Method — what, scenario — step-by-step how | A.3.1 |
| Work Product = Description | WP — artifact, description — narrative | A.7 |
| System = Episteme | System — physical entity, episteme — knowledge domain | A.1 |
| Role = Actor | Role — function, actor — performer | A.2 |
| Object = Description = Carrier | Object ≠ description ≠ carrier | A.7 |

---

## 6. Claude's role in SPF

### 6.1. What Claude DOES

| Role | Description |
|------|-------------|
| **Spec Guardian** | Ensures compliance with SPF specifications |
| **Process Guide** | Helps follow the Pack creation process |
| **Template Maintainer** | Keeps templates up to date |
| **Lint Runner** | Checks correctness of changes |

### 6.2. What Claude does NOT do

- ~~Domain Expert~~ — does not determine what is true in a domain
- ~~Content Creator~~ — does not generate knowledge from nothing
- ~~Downstream Builder~~ — courses/code belong to other repos

---

## 7. Key documents

| Document | Path | Description |
|----------|------|-------------|
| Conceptual model (brief) | `docs/conceptual-model.md` | FPF → SPF → Pack → Downstream |
| Conceptual model (full) | `docs/fpf-spf-pack.md` | Detailed description of the full architecture |
| Process overview | `process/00-process-overview.md` | Process overview |
| Process lint | `process/process-lint.md` | Validation rules |
| Downstream contract | `spec/downstream-contract.md` | Contract with downstream |
| F-G-R Trust (opt.) | `spec/f-g-r-trust.md` | FPF B.3 — trust pattern |
| Pack template | `pack-template/` | Canonical Pack structure |

---

## 8. Procedures

### 8.1 Changing an SPF specification

1. Identify which spec is affected (`spec/`, `process/`, `pack-template/`)
2. Check whether the change will break existing Packs
3. Update the specification
4. Update `process-lint.md` if needed
5. Notify downstream (Pack repositories)

### 8.2 Changing pack-template

1. Changes must be backwards-compatible
2. If breaking change — Pack migration is required
3. Update `spec/SPF.SPEC.001-entity-coding.md` if IDs are affected

---

## 9. Pre-Commit Checklist

- [ ] Changes do not add domain content
- [ ] Changes do not add didactics
- [ ] Changes are backwards-compatible (or breaking change is documented)
- [ ] `process-lint.md` is updated if needed
- [ ] References are valid

---

## 10. Relationships with other repositories

| Repository | Relationship |
|------------|-------------|
| ailev/FPF | Upstream — SPF follows FPF |
| Pack repositories | Downstream — Pack follows SPF |


# SOURCE_FILE: docs/conceptual-model.md
---
# FPF, SPF and Pack: Conceptual Model

This document establishes the **conceptual model** for knowledge organization within SPF.

---

## 1. Why all this: knowledge, learning and the AI era

### 1.1. Professionals have a picture of their domain

In any applied field, strong specialists have a **picture of their domain**: what matters here, what risks are typical, where the "weak spots" are, which distinctions must not be confused.

This picture almost always emerges from practice, standards, mistakes and their analysis. It exists sometimes parallel to any textbooks and courses as "professional reality".

### 1.2. Why formalization became critical in the AI era

AI can significantly accelerate domain understanding **when a knowledge structure exists**, but without a formalized structure AI reinforces confusion.

---

## 2. Concepts and distinctions: full glossary

### 2.1. Object, description, carrier

| Term | Definition | Example |
|------|-----------|---------|
| **Object** | What exists "in the domain reality" | Car; construction object |
| **Description** | Model/text/diagram about an object | Characteristic card, specification |
| **Carrier** | File/page/video/site where the description resides | Markdown file, PDF, web page |

**Must not confuse**: object ≠ description ≠ carrier.

### 2.2. Knowledge, learning, representation

| Term | Definition | Example |
|------|-----------|---------|
| **Knowledge** | Structured domain content | Pack |
| **Learning** | A way to guide a person through knowledge | Course, training |
| **Representation (view)** | A specific assembly of knowledge for an audience | Guide, course, RAG index |

**Must not confuse**: knowledge ≠ course/textbook ≠ any publication.

### 2.3. Method, tool, practice, scenario

| Term | Definition | Example |
|------|-----------|---------|
| **Method** | A way of acting/evaluating | Time tracking |
| **Tool** | A means of execution | Toggl, Excel spreadsheet |
| **Practice** | A reproducible pattern of applying methods | Daily time recording |
| **Scenario/route** | A step-by-step plan | "30-day program" |

**Must not confuse**: method ≠ tool; method ≠ scenario.

### 2.4. Characteristic, metric, indicator

| Term | Definition | Example |
|------|-----------|---------|
| **Characteristic** | An evaluation axis for an object | "Safety", "agency" |
| **Metric** | A measurable quantity | Response time, % completion |
| **Indicator** | An observable sign/measure | Number of initiatives per week |

### 2.5. State

**State** — a class/mode of an object based on characteristic/indicator values.

**Must not confuse**: state ≠ learning stage. State is "how it is now", not "how to get there".

### 2.6. Work product

**Work product** — an observable, verifiable result of a method/evaluation.

### 2.7. Typical interpretation errors (failure modes)

**Failure mode** — a typical misunderstanding/substitution error.

### 2.8. SoTA status

**SoTA status** — a marker of the currency of a statement/interpretation.

| Status | Meaning |
|--------|---------|
| `current` | Current, confirmed by practice |
| `hypothesis` | New, requires verification |
| `deprecated` | Outdated |

### 2.9. Domain and bounded context

| Term | Definition |
|------|-----------|
| **Domain** | An applied field with language, objects, methods |
| **Bounded context** | Explicitly fixed boundaries and vocabulary of the domain |

---

## 3. First Principles

### 3.1. What are first principles

**First principles** — universal distinctions and requirements for correct thinking about knowledge:

- method ≠ tool
- result ≠ description of result
- characteristic ≠ way to change it
- state ≠ action plan
- object ≠ model
- knowledge ≠ learning

### 3.2. Universality of first principles

First principles are **universal in content**: the same in construction, cooking, medicine, management.

---

## 4. FPF — First Principles Framework

### 4.1. First principles exist before formalization

First principles "have always existed". **FPF does not invent first principles.**

FPF does three things:

| Function | Description |
|----------|-------------|
| **Explication** | Makes first principles explicit |
| **Normativity** | Turns them into correctness requirements |
| **Discipline** | Sets the language and constraints |

### 4.2. What FPF defines

- universal entity types (role, method, work product, process, description, carrier)
- permissible and impermissible distinctions
- rules for working with contexts (bounded context)
- principles of multi-view description
- requirements for verifiability, SoTA and trustworthiness

### 4.3. What FPF does NOT do

- **does not describe specific domains**
- does not contain second principles
- is not a course
- does not provide "step-by-step scenarios"

---

## 5. Second Principles

### 5.1. What are second principles

**Second principles** — stable domain regularities and distinctions within a specific field:

> What really matters here? Which distinctions are critical? What are the typical errors?

### 5.2. They exist before formalization

Second principles live in professionals's experience, standards, craft, "feel of the domain".

### 5.3. Their universality

Second principles:
- **are not universal in content** (different domains have different ones)
- but are **"universal in type"**: they exist in any domain and can be brought to engineering form

---

## 6. SPF — Second Principles Framework

### 6.1. What SPF is

**SPF** — a framework that defines **how to formalize second principles** of a domain so that engineering knowledge results.

### 6.2. What SPF does

**Minimum required elements:**
- bounded context
- key distinctions
- characteristics
- evaluation/verification methods
- work products
- failure modes
- SoTA statuses and revision criteria

**Structural requirements:**
- identifier and reference rules
- canonical pack structure

**Process gates:**
- process lint
- contracts between source-of-truth and downstream

### 6.3. What SPF does NOT do

- does not add domain content
- does not decide which second principles are correct
- does not build courses
- does not replace expertise

### 6.4. How SPF relates to FPF

| FPF | SPF |
|-----|-----|
| Defines correctness of types and distinctions | Defines engineering format for capturing domain content |
| Prevents logical confusion | Prevents knowledge from becoming a "collection of tips" |

---

## 7. Pack — domain passport

### 7.1. What it is

**Domain passport** (also **pack**) — a formalized and stabilized engineering description of a domain.

> Pack = domain passport

### 7.2. Pack is a result, not a process

Pack is a **knowledge artifact** (source of truth), not a process.

### 7.3. What a pack includes

| Element | Description |
|---------|-------------|
| Bounded context | Fixed semantic frame of the domain |
| Distinctions | Conceptual boundaries of the domain |
| Domain entities | Roles, objects of attention, constraints |
| Methods | Ways of acting (not scenarios) |
| Work products | Verifiable results of methods |
| Failure modes | Typical interpretation errors |
| SoTA annotations | Currency statuses |
| Map | Graph of connections between pack elements |

### 7.4. What a pack is NOT

| Pack is NOT | Where it should be |
|-------------|-------------------|
| Course, textbook | Downstream |
| Development route | Downstream |
| "How to implement" | Downstream |
| Embeddings/index | Downstream |

---

## 8. How a pack is created

### 8.1. Logical order

1. **First principles** explicated in FPF
2. **Second principles** fixed according to SPF requirements
3. **Pack** — the result of formalization

### 8.2. Practical process (iterations)

#### Iteration 0: Domain contract
- Bounded context
- Core distinctions
- Truth criteria

#### Iteration 1: Engineering structure
- Characteristic catalog
- Card template
- Top-level map

#### Iteration 2: MVP characteristic
- Definition and distinctions
- Indicators/metrics
- Evaluation methods
- Work products
- Typical errors
- SoTA status

#### Iteration 3+: Expansion

#### Continuously: Evolution

### 8.3. Process stages

```
01. Domain Selection
02. Bounded Context
03. Distinctions Work
04. Domain Entities Identification
05. Information Ingestion
06. Analysis & Formalization
07. Method & Product Extraction
08. Failure Modes Extraction
09. SoTA Annotation
10. Map Maintenance
11. Review & Evolution Cycle
```

---

## 9. How FPF helps SPF and pack

### 9.1. What FPF gives to SPF

FPF ensures **basic correctness**: we don't confuse types, don't mix tool/method, don't substitute result for description.

### 9.2. What FPF gives to pack

FPF makes the pack consistent, traceable, stable.

### 9.3. How SPF helps create a pack

SPF defines the "engineering form" and process gates (lint).

---

## 10. Typical errors (anti-patterns)

### 10.1. Pack-level errors

| Error | How to avoid |
|-------|-------------|
| Pack turns into learning | Didactics go downstream |
| States become "stages" | States are classes, not sequences |
| Tools are declared methods | Method ≠ tool |
| Artifact substitutes fact | Work product ≠ description |
| SoTA becomes "literature review" | SoTA = status + revision criterion |
| Downstream becomes source-of-truth | Pack is the sole source-of-truth |

### 10.2. Forbidden formulations

- Mixing SPF and pack
- Treating SPF as universal knowledge by content
- Treating pack as learning material
- Turning methods into scenarios
- Treating AI representations as source of truth

---

## 11. Level hierarchy and three dimensions

### 11.1. Canonical hierarchy

```
FPF (Level 1)  →  first principles framework
       ↓
SPF (Level 2)  →  second principles framework
       ↓
Pack           →  formalized domain knowledge
       ↓
Downstream     →  derivative representations
```

| Level | Universality |
|-------|-------------|
| **FPF** | Universal in content |
| **SPF** | Universal in form and process |
| **Pack** | Domain-specific |
| **Downstream** | Free form |

### 11.2. Three orthogonal dimensions

| Dimension | What it defines |
|-----------|----------------|
| **Content** | What is inherited semantically |
| **Form** | How the repository is structured |
| **Process** | How it is produced and maintained |

Dimensions are **independent of each other**.

### 11.3. Downstream: document structural protocols

Downstream repositories (projects, governance, surfaces) may follow various structural protocols for organizing their documents:

- "Systems × roles" matrix — project documents organized by intersection of system levels and role perspectives
- Thematic sections — documents organized by subject areas
- Chronological — decision logs, logs, journals

SPF does not prescribe a specific structure for downstream repositories. SPF defines the **contract** between Pack (source-of-truth) and downstream: downstream references Pack but does not duplicate or substitute it.

**Key distinction:** document structural protocol (form) and Pack (content) are **orthogonal**. One Pack can be used by documents from different structural cells, and one document may reference multiple Packs.

---

## 12. Relationship to other methodologies

### 12.1. Domain-Driven Design (DDD)

**Key difference**: DDD is about code. FPF/SPF/Pack is about formalizing knowledge before code.

### 12.2. Ontology Engineering

**Difference**: Formal ontologies are for machine reasoning. Pack is for human-readable knowledge.

### 12.3. Knowledge Graphs

**Difference**: Knowledge Graphs are data-centric. Pack is methodology-centric.

### 12.4. What makes FPF/SPF/Pack unique

1. Explicit separation of content, form and process
2. Process-driven knowledge production
3. Failure Modes as first-class citizens
4. SoTA as an attribute, not a literature review
5. Downstream contract
6. AI-ready, human-readable

---

## 13. Brief glossary

| Term | Definition |
|------|-----------|
| **Bounded context** | Fixed semantic frame of the domain |
| **Distinction** | A distinction preventing confusion |
| **Method** | A way of acting, not a scenario |
| **Work product** | A verifiable result of a method |
| **Failure mode** | A typical interpretation error |
| **SoTA annotation** | Currency status of a statement |
| **Map** | Graph of connections between pack elements |
| **Downstream view** | A derivative representation of a pack |
| **Characteristic** | An evaluation axis for an object |
| **Indicator** | An observable sign for evaluation |
| **State** | Class/mode of an object by characteristics |
| **Practice** | A reproducible pattern of applying methods |

---

## 14. Final formula

> **First principles** — universal distinctions of correct thinking about knowledge; they exist independently of formalization.

> **FPF (First Principles Framework)** — a framework that explicates first principles, makes them explicit and normative.

> **Second principles** — stable domain regularities of a specific field; they exist before formalization in professional experience.

> **SPF (Second Principles Framework)** — a framework of requirements and processes for engineering fixation of second principles.

> **Pack / domain passport** — formalized engineering core of a specific domain: source of truth.

---

## Key distinction: information vs knowledge

| Information | Knowledge (Pack) |
|-------------|-----------------|
| Raw data | Formalized through distinctions |
| Not verified | Has gone through SPF process |
| No SoTA status | Has SoTA + revision criterion |
| Input for process | Output of process |

---

*This document is normative for SPF.*


# SOURCE_FILE: docs/ddd-mapping.md
---
---
type: doc
status: draft
created: 2026-02-10
updated: 2026-02-10
---

# DDD and FPF/SPF/Pack: Full Mapping

> **Purpose:** Formalize knowledge of how the FPF→SPF→Pack→Downstream methodology relates to Domain-Driven Design. What DDD does, what it rejects, the pros and cons of both approaches, and how DDD ideas live in our architecture.
>
> **Short version:** [fpf-spf-pack.md § 14.1](docs/fpf-spf-pack.md)
> **Downstream:** club post — [DS-Knowledge-Index-Tseren/posts/2026-02-10-ddd-vs-fpf-spf-pack.md](https://github.com/TserenTserenov/DS-Knowledge-Index-Tseren/blob/main/posts/2026-02-10-ddd-vs-fpf-spf-pack.md)

---

## 1. What DDD is

**Domain-Driven Design** — a software development approach proposed by Eric Evans (2003). Core idea:

> *"The heart of software is its ability to solve domain problems for the user."*

DDD asserts: software complexity lies in the domain, not the technology. Design must be driven by domain understanding: deep immersion in the business, constant collaboration between experts and developers, a Ubiquitous Language across all artifacts.

### 1.1. Two levels of DDD

| Level | What it does | Scale |
|-------|-------------|-------|
| **Strategic DDD** | How to decompose a large domain and how the parts relate | Organization, system of systems |
| **Tactical DDD** | How to implement a domain model within a single context | One service, one module |

### 1.2. Key books

| Book | Author | Year | Focus |
|------|--------|------|-------|
| *Domain-Driven Design: Tackling Complexity in the Heart of Software* | Eric Evans | 2003 | Foundational "blue book" — all patterns |
| *DDD Reference* | Eric Evans | 2015 | Condensed reference for all patterns (free PDF) |
| *Implementing Domain-Driven Design* | Vaughn Vernon | 2013 | "Red book" — practical guide |
| *Domain-Driven Design Distilled* | Vaughn Vernon | 2016 | Brief introduction (170 p.) |

---

## 2. DDD work products

DDD produces artifacts of **two kinds**: descriptions (non-code) and code.

### 2.1. Descriptive artifacts (non-code)

These artifacts exist **before** and **independently of** code. A team can run Event Storming and build a Context Map without writing a single line.

| # | Work product | What it is physically | Who does it |
|---|-------------|----------------------|-------------|
| 1 | **Ubiquitous Language Glossary** | Document/wiki: table of terms with definitions | Experts + developers together |
| 2 | **Bounded Context Definitions** | Document: boundary, inside — terms and rules | Architect + experts |
| 3 | **Context Map** | Diagram: all contexts and connections between them | Architect |
| 4 | **Subdomain Classification** | Table: Core / Supporting / Generic | Strategist/architect |
| 5 | **Domain Vision Statement** | 1 page: why this domain, where the value lies | Product + expert |
| 6 | **Event Storming Board** | Stickers/Miro: events → commands → aggregates → policies | Whole team |

### 2.2. Code artifacts

| # | Work product | What it is | Example |
|---|-------------|-----------|---------|
| 7 | **Entity** | Class with unique ID and lifecycle | `class Order(id: OrderId)` |
| 8 | **Value Object** | Immutable class without ID, defined by values | `class Money(amount, currency)` |
| 9 | **Aggregate** | Root Entity + nested objects with shared invariants | `Order` → `OrderLine[]`, accessed only through `Order` |
| 10 | **Domain Event** | Notification object: something happened in the domain | `class OrderPlaced(orderId, timestamp)` |
| 11 | **Domain Service** | Stateless operation, does not belong to one entity | `PricingService.calculate(order, discounts)` |
| 12 | **Repository** | Abstraction for storing/retrieving aggregates | `OrderRepository { find(id), save(order) }` |
| 13 | **Factory** | Encapsulation of complex object creation | `OrderFactory.createFromCart(cart)` |
| 14 | **Layered Architecture** | Structure: UI → Application → Domain → Infrastructure | 4 layers, dependencies only downward |

### 2.3. Important clarification: descriptions in DDD serve code

In DDD descriptive artifacts are **intermediate**:
- Glossary is needed so classes are named correctly
- Context Map — so microservices are sliced correctly
- Event Storming — to find aggregates for code

The ultimate goal of all descriptions in DDD is **code**. This is Evans's deliberate decision (see §3).

---

## 3. Evans's position: "The model is the code"

### 3.1. What Evans rejects

Evans explicitly opposes the "model on the shelf" — a document written by analysts, handed to developers, and thereafter living separately from code.

> *"The model is not the diagram. The model is not the document. The model IS the code."*

### 3.2. Evans's arguments

| Argument | Essence |
|----------|---------|
| **Model = code** | The domain model materializes directly in the code of the domain layer. Aggregates, entities, Value Objects, domain events — all of this IS the "formalization" |
| **UL is oral, not documentary** | Ubiquitous Language is maintained through constant communication, pair programming, discussions. The glossary is a supporting, not central, artifact |
| **Context Map is informal** | May be a drawing on a whiteboard, a diagram in a wiki. DDD prescribes no strict format |
| **Document inevitably becomes outdated** | Any document disconnected from code will sooner or later diverge from reality. Better to make code so expressive that it itself is a readable model |

### 3.3. The logic of this position

Evans solves a specific problem: in 2003 a typical project looked like this:
1. Analyst writes a requirements document
2. Architect draws diagrams
3. Developer writes code that matches neither
4. Documents become outdated the next day

DDD says: **throw away the intermediate documents, make the code the model**.

---

## 4. Pros and cons of the DDD approach

### 4.1. Pros

| Pro | Why it is valuable |
|-----|-------------------|
| **Code = model → no desync** | The single source-of-truth (code) cannot become outdated relative to itself |
| **Deep domain understanding** | Knowledge crunching forces developers to understand the business |
| **Expressive code** | Intention-revealing interfaces, ubiquitous language in class names — code reads like a domain description |
| **Bounded Context** | Clear boundaries prevent "Big Ball of Mud" — modularity at the architectural level |
| **Rich integration taxonomy** | 9 Context Map patterns (Partnership, ACL, Conformist...) — precise tools for describing connections |

### 4.2. Cons

| Con | Consequences |
|-----|-------------|
| **Knowledge locked in code** | A business expert who cannot read code cannot independently validate the model. UL works only while the team communicates regularly |
| **No knowledge transfer without people** | A key developer/expert leaves — knowledge of *why* the model is structured this way is lost. Code shows *what*, but not *why* |
| **No formal verification** | Cannot check that code matches domain rules because those rules are nowhere fixed separately from code in structured form |
| **Scaling through people, not artifacts** | DDD works well in one team with live communication. As teams multiply, oral UL stops scaling |
| **Mixing domain and implementation** | Code is an implementation in a specific language, specific framework, with technical compromises. Domain knowledge inevitably mixes with implementation decisions |
| **No meta-level** | No way to formalize rules for creating models. Every team invents its own approach |

### 4.3. Attempts to compensate for cons

There were attempts to supplement DDD with formal artifacts, but none became a standard:

| Attempt | What it does | Why it does not solve the problem |
|---------|-------------|----------------------------------|
| **Event Storming** (Brandolini) | Visual event map on stickers | Informal, becomes outdated quickly |
| **Domain Story Telling** | Visual narratives | No strict format |
| **BDD (Given-When-Then)** | Executable specifications | Tied to a test framework |
| **ADR** (Architecture Decision Records) | Records decisions | Records decisions, not the model |

---

## 5. Pros and cons of the FPF/SPF/Pack approach

### 5.1. Pros

| Pro | Why it is valuable |
|-----|-------------------|
| **Knowledge as an independent artifact** | Pack exists and has value without code. A domain expert can read, validate and improve Pack |
| **Knowledge transfer via artifact** | Pack can be handed to another team, another project, an AI agent — without verbal explanation |
| **Formal verification** | Distinctions with tests, failure modes, trust metrics — structured ways of verifying correctness |
| **Scaling through Pack** | A new team reads Pack and gets formalized domain knowledge. No human mentor needed |
| **Meta-levels** | FPF → SPF ensure portability of patterns across domains. Rules for creating Packs are the same for any domain |
| **Explicit evolution tracking** | SoTA + revision criteria show when knowledge has become outdated. In DDD the model is refactored as needed, without a system |
| **Downstream contract** | Explicit interface between knowledge and application. Code, courses, agents — all use one Pack |

### 5.2. Cons

| Con | Consequences |
|-----|-------------|
| **Two sources of truth** | Pack (text) and Code (downstream) can desync — the very problem Evans was solving. Requires an explicit synchronization process (see §6) |
| **Formalization overhead** | Creating a Pack with IDs, frontmatter, distinctions, failure modes — significant effort. May be excessive for a small team |
| **No runtime patterns** | Aggregate, Domain Event, Repository — code organization patterns not in Pack. When transitioning to code, DDD must be additionally applied |
| **Risk of "model on the shelf"** | If the Pack→Code synchronization process does not work, Pack becomes the very outdated document Evans opposed |
| **Young methodology** | No wide community, no validation at scale, little tooling |

---

## 6. The two-source-of-truth problem: Pack vs Code

### 6.1. Problem statement

Evans is right: a document disconnected from code becomes outdated. We accept this problem but solve it differently.

In DDD the solution: **remove the document, keep the code**.
In FPF/SPF/Pack the solution: **keep both, introduce a synchronization process**.

### 6.2. When Pack and Code diverge

Divergence of Pack and Code is a normal situation. The question is: **what to update?**

| Situation | What to update | Why |
|-----------|---------------|-----|
| New domain knowledge discovered during code development | **Pack** (then Code follows) | Pack is source-of-truth. Knowledge is formalized in Pack, code follows |
| Technical compromise in code forces deviation from model | **Code** (with an ADR record of why) | Implementation may require compromises, but Pack remains the "ideal" model |
| Business expert found an error in the model | **Pack** (then Code follows) | Expert validates Pack directly |
| Code refactoring reveals a better structure | **Both**: Pack is refined, Code consolidates | Code refactoring is a form of knowledge crunching |
| AI agent is working with outdated Pack | **Pack** (update to current understanding) | Agent must work with current knowledge |

### 6.3. Synchronization rule

> **When Pack and Code diverge — do not automatically update one of them. Determine where the truth lies and update the one that is wrong.**

This differs from DDD (where code is always right) and from traditional waterfall (where the document is always right). Our approach: **truth is determined by analysis**, not convention.

### 6.4. Mechanisms to prevent desync

| Mechanism | How it works | Status |
|-----------|-------------|--------|
| **Capture-to-Pack** (Work protocol) | When developing code, discovered knowledge is recorded in Pack | Implemented |
| **Downstream contract** (SPF spec) | Explicit Pack→Code interface with traceability rules | Implemented |
| **SoTA + revision criteria** | Each Pack entity has a revision criterion | Implemented |
| **Process lint** | Automated check of Pack against SPF | Partial |
| **Code lint → Pack** | Check that Code references Pack entities | Not implemented (potential) |

---

## 7. How DDD ideas live in FPF/SPF/Pack

### 7.1. Ideas we took and generalized

| DDD idea | How it lives with us | What we added |
|----------|---------------------|--------------|
| **Bounded Context** | U.BoundedContext (FPF A.1.1) → Pack (SPF) | Generalization to any domain (not just code). 4 required components: Glossary, Invariants, Roles, Bridges |
| **Ubiquitous Language** | Glossary + Distinctions (SPF 01A, 01B) | Tests for violations, failure modes, formal IDs |
| **Knowledge Crunching** | 11-step process (SPF process/) + Capture-to-Pack | Formalized process instead of informal workshops |
| **Model-Driven Design** | Pack-driven Downstream | Code is generated/written based on Pack, not the reverse |
| **Explicit boundaries** | Pack Manifest (scope: in/out) + Bridges | upstream/downstream dependencies, loss/fit annotations |

### 7.2. Ideas we did NOT take (and why)

| DDD idea | Why we did not take it | Consequence |
|----------|----------------------|------------|
| **"Model = code"** | We treat knowledge as an independent artifact, not tied to implementation | Synchronization process required (§6) |
| **Aggregate** (runtime boundary) | Pack is knowledge-time, no runtime | No pattern for "a group of entities updated together". Potentially useful to introduce **Knowledge Aggregate** |
| **Domain Events** (runtime notifications) | Pack is not executed | No way to describe "what happened". But this is not needed at knowledge-time |
| **Value Objects** (immutable, no ID) | All Pack entities have IDs | Some elements (metrics, characteristics) could be value objects, but we do not distinguish |
| **Repository** (storing aggregates) | This is an implementation pattern | Lives in downstream/instrument (code) |

### 7.3. Ideas we could take

| What | Why | Where to place | Priority |
|------|-----|---------------|---------|
| **Context Map Integration Patterns** (9 patterns) | Extend Bridge types: Partnership, ACL, Conformist, Open Host, Shared Kernel, etc. | FPF Bridges or SPF spec | High |
| **Core/Supporting/Generic** | Prioritize investment in Pack formalization | Pack Manifest: `subdomain_type` field | Medium |
| **Knowledge Aggregate** | Groups of Pack entities that MUST be updated together | SPF process | Medium |
| **Knowledge Storming** (Event Storming adaptation) | Method for discovering entities, distinctions and failure modes | SPF process (steps 3-4) | Low |

---

## 8. Summary table: DDD vs FPF/SPF/Pack

### 8.1. By capabilities

| Capability | DDD | FPF/SPF/Pack |
|------------|-----|-------------|
| Domain knowledge formalization | Through code (runtime) | Through structured text (knowledge-time) |
| Bounded Context | Yes | Yes (generalized) |
| Ubiquitous language | UL (oral + in code) | Glossary + Distinctions (formal, with tests) |
| Context integration patterns | 9 patterns (ACL, Partnership...) | Bridges (less developed) |
| Meta-level | No | FPF → SPF (2 meta-levels) |
| Runtime patterns | Aggregate, Event, Service, Repository | No (in downstream) |
| Failure modes | No | Yes (SPF 05, first-class citizens) |
| Trust/readiness metrics | No | Yes (F, G, R) |
| SoTA tracking | No | Yes (status + revision criteria) |
| Downstream contract | No | Yes (explicit knowledge→application interface) |
| Domain classification | Core/Supporting/Generic | No (can be taken) |
| Tooling and community | Mature (20+ years) | Young |

### 8.2. By source-of-truth

| Aspect | DDD | FPF/SPF/Pack |
|--------|-----|-------------|
| **Source-of-truth** | Code | Pack (text) |
| **If text ≠ code** | Update text (code is right) | Determine where truth lies and update the wrong one |
| **Who validates** | Developer (reads code) | Expert (reads Pack) + developer (reads code) |
| **Scaling** | Through people (communication) | Through artifact (Pack) |
| **Risk** | Knowledge locked in code | Desync between Pack and Code |

### 8.3. By work products

| DDD artifact | FPF/SPF/Pack analog | Match |
|-------------|--------------------|----|
| Ubiquitous Language Glossary | Glossary + Distinctions | High (ours are stricter) |
| Bounded Context Definition | Pack = Bounded Context | High (ours are more general) |
| Context Map | Bridges + Pack Manifest | Medium (DDD is richer) |
| Domain Vision Statement | Pack Manifest (scope) | Medium |
| Subdomain Classification | — | No (can be taken) |
| Entity | Domain Entity (DP.XXX.NNN) | Medium |
| Value Object | — | No analog |
| Aggregate | — | No (→ Knowledge Aggregate) |
| Domain Event | — | No (runtime vs knowledge-time) |
| Domain Service | Method (SPF 03) | Medium |
| Repository | Downstream/instrument | Low |
| Layered Architecture | 4-level hierarchy | Analogy (different layers) |

---

## 9. Positioning: what we are relative to DDD

### 9.1. Formulation

> **FPF/SPF/Pack is a generalization of key DDD patterns (Bounded Context, Ubiquitous Language, explicit boundaries) beyond code, to the formalization of domain knowledge as an independent artifact.**
>
> DDD formalizes the domain **through code**. We formalize the domain **before code**, in structured text (Pack), and code is a downstream product of Pack.
>
> At the same time we add what DDD lacks: meta-levels (FPF/SPF), failure modes, trust metrics, SoTA, downstream contracts.
>
> DDD and FPF/SPF/Pack **do not compete — they are sequential**:
>
> ```
> Domain (reality)
>     ↓  FPF/SPF/Pack: knowledge formalization
> Pack (source-of-truth)
>     ↓  DDD: code design based on knowledge
> Code (downstream/instrument)
> ```

### 9.2. Can we say "we do DDD"?

**No** — that would be imprecise. DDD is about code. We are about knowledge before code.

**Yes** — one can say: "we use DDD patterns (Bounded Context, UL), generalized to knowledge management".

**Most precisely:** "Our approach includes and extends the strategic patterns of DDD, but adds an independent domain knowledge artifact (Pack) that DDD does not create."

---

## 10. The core problem we are solving

DDD in effect proposes: "let the code be the model." But code is an implementation in a specific language, in a specific framework, with technical compromises. It inevitably mixes domain knowledge with implementation decisions.

A full-fledged domain knowledge artifact — independent of implementation, verifiable, readable by both business and developers and AI agents — DDD does not create. This is Evans's deliberate decision, not an oversight. But it has consequences:

- **Knowledge locked in code** — business expert cannot validate
- **No transfer without people** — developer leaves, knowledge of "why" leaves with them
- **No formal verification** — domain rules are nowhere fixed separately
- **Scaling through people** — oral UL does not scale to many teams

Pack solves these problems by creating an independent domain knowledge artifact. At the cost of needing to maintain Pack and Code synchronization (§6).

---

## Sources

- Evans, Eric. *Domain-Driven Design: Tackling Complexity in the Heart of Software.* 2003.
- Evans, Eric. *Domain-Driven Design Reference.* 2015. (CC-licensed)
- Vernon, Vaughn. *Implementing Domain-Driven Design.* 2013.
- Vernon, Vaughn. *Domain-Driven Design Distilled.* 2016.
- Fowler, Martin. [BoundedContext](https://martinfowler.com/bliki/BoundedContext.html), [DomainDrivenDesign](https://martinfowler.com/bliki/DomainDrivenDesign.html).
- FPF-Spec.md, A.1.1 (U.BoundedContext): *"FPF generalizes the proven DDD idea of a Bounded Context from software into a universal modeling primitive."*
- SPF/docs/fpf-spf-pack.md, §14.1.


# SOURCE_FILE: docs/fpf-spf-pack.md
---
# FPF, SPF and Pack: Conceptual Model

> **FPF Reference:** The full FPF specification is available locally: `~/IWE/FPF/FPF-Spec.md`
> Codes like `A.1`, `B.5` refer to FPF patterns.

This document captures the **conceptual model** of knowledge organization used in this repository.
It is **normative**: the definitions and demarcations below are mandatory for interpreting the repository structure, working process, and role of downstream artifacts.

---

## Quick navigator

1. [Why all this: knowledge, learning, and the AI era](#1-why-all-this-knowledge-learning-and-the-ai-era)
2. [Concepts and distinctions: full vocabulary](#2-concepts-and-distinctions-full-vocabulary)
3. [First principles: what they are and their universality](#3-first-principles)
4. [FPF: what it is, what it's for, and what it does NOT do](#4-fpf--first-principles-framework)
5. [Second principles: what they are, how they exist before formalization](#5-second-principles)
6. [SPF: what it is, what it's for, and how it relates to FPF](#6-spf--second-principles-framework)
7. [Domain passport (pack): what it is and what it is NOT](#7-pack--domain-passport)
8. [How a pack is created: logical order and practical process](#8-how-a-pack-is-created)
9. [How FPF helps SPF and pack](#9-how-fpf-helps-spf-and-pack)
10. [Typical errors (anti-patterns)](#10-typical-errors-anti-patterns)
11. [Binding to domain: "Characteristics and states of a creator"](#11-binding-to-domain-characteristics-and-states-of-a-creator)
12. [Readiness checklists (Definition of Done)](#12-readiness-checklists-definition-of-done)
13. [Level hierarchy and three dimensions](#13-level-hierarchy-and-three-dimensions)
14. [Relationship to other methodologies](#14-relationship-to-other-methodologies)
15. [Mapping to repository structure](#15-mapping-to-repository-structure)
16. [Brief glossary](#16-brief-glossary)
17. [Final formula](#17-final-formula)

---

## 1. Why all this: knowledge, learning, and the AI era

### 1.1. Professionals have a picture of their domain

In any applied area (construction, culinary arts, medicine, logistics, industrial safety) strong specialists have a **picture of their domain**: what matters here, what risks are typical, where the "thin spots" are, which distinctions must not be confused.

This picture almost always emerges from practice, standards, mistakes, and their analysis. It sometimes exists in parallel with any textbooks and courses as "professional reality", while textbooks/courses are most often an attempt to package this reality for learning purposes.

### 1.2. Why formalization became critical in the AI era

Previously one could "get by" on experience and intuition: they lived in the specialist's head, and transfer happened through mentorship and years of practice.

Now AI can significantly accelerate domain understanding **given a knowledge structure**, while in the absence of a formalized structure AI reinforces confusion (beautifully, confidently, but incorrectly for your context).

Therefore, formalization matters above all to those who want to:
- maintain professional relevance,
- train and scale faster,
- build AI assistants that "understand your domain specifics", not just generic platitudes.

---

## 2. Concepts and distinctions: full vocabulary

A strict language is used below. If word meanings are not fixed, subsequent descriptions will inevitably be read "colloquially".

### 2.1. Object, description, carrier (FPF A.7: Strict Distinction)

| Term | Definition | Example |
|------|------------|---------|
| **Object** | That which exists "in the reality of the domain" | Car; construction site; person as assessment object |
| **Description** | Model/text/diagram about the object | Characteristic card, specification |
| **Carrier** | File/page/video/website where the description resides | Markdown file, PDF, web page |

**Must not be confused**: object ≠ description ≠ carrier. (FPF A.7)

### 2.2. Knowledge, training, representation

| Term | Definition | Example |
|------|------------|---------|
| **Knowledge** | Structured domain content (distinctions, characteristics, methods, verification criteria, typical errors) | Pack |
| **Training** | A way to guide a person through knowledge (learning path, exercises, sequence) | Course, workshop |
| **Representation (view)** | A specific assembly of knowledge for an audience or task | Guide, course, hints, RAG index |

**Must not be confused**: knowledge ≠ course/textbook ≠ any publication.

### 2.3. Method, tool, practice, scenario (FPF A.3)

| Term | Definition | Example | FPF |
|------|------------|---------|-----|
| **Method** | Way of acting/assessing (what to do in principle) | Time tracking | A.3.1 |
| **Tool** | Means of execution (app, timer, template, device) | Toggl, Excel spreadsheet | — |
| **Practice** | Reproducible pattern of applying methods in context | Daily time logging | A.15 |
| **Scenario/path** | Step-by-step plan for reaching a state | "30-day program" | — |

**Must not be confused**: method ≠ tool; method ≠ scenario. (FPF A.7)
A practice is often "assembled" from methods + context + habits.

### 2.4. Characteristic, metric, indicator

| Term | Definition | Example |
|------|------------|---------|
| **Characteristic** | Axis of object assessment | "Car safety", "creator's agency" |
| **Metric** | Measurable quantity related to a characteristic | Braking reaction time, % of fulfilled commitments |
| **Indicator** | Observable sign/measure for assessment (can be input/computed/derived) | Number of initiatives per week |

**Must not be confused**: characteristic ≠ metric ≠ indicator.

### 2.5. State

**State** — class/mode of an object based on characteristic/indicator values.

| State examples | Context |
|---------------|---------|
| "Overloaded", "stable", "at risk" | Systems |
| "Random", "practicing", "systematic" | Learner |

**Must not be confused**: state ≠ learning stage.
State — "how it is now", not "how to get there".

### 2.6. Work product

**Work product** — an observable, verifiable result of a method/assessment.

| Examples | Context |
|----------|---------|
| Protocol, profile, risk map | Documents |
| Time budget, test report | Assessment results |

**Must not be confused**: work product ≠ unverifiable description; work product ≠ promise.

### 2.7. Typical interpretation errors (failure modes)

**Failure mode** — a typical error of understanding/substitution.

| Examples |
|----------|
| "Confusing method with tool" |
| "Substituting fact with report" |
| "Optimizing for a single test" |

### 2.8. SoTA status

**SoTA status** — a currency mark on a statement/interpretation.

| Status | Meaning |
|--------|---------|
| `current` | Up to date, confirmed by practice |
| `hypothesis` | New, requires verification |
| `deprecated` | Outdated, a better interpretation exists |

**SoTA is not a "literature review"** — it is currency management for statements with revision criteria.

### 2.9. Domain area and bounded context (FPF A.1.1)

| Term | Definition | FPF |
|------|------------|-----|
| **Domain area** | Applied sphere with its own language, objects, metrics, methods | A.1 |
| **Bounded context** | Explicitly fixed boundaries and vocabulary of that area (what's in/out; term meanings) | A.1.1 |

**Must not be confused**: "domain" ≠ "course" ≠ "community of people". (FPF A.7)
A domain is defined through boundaries, language, and object types.

---

## 3. First principles

### 3.1. What are first principles

**First principles** — universal distinctions and requirements for correct thinking about knowledge, the same for any domain. They answer the question:

> How to think about and describe knowledge so as not to destroy meaning?

**Examples of first principles (FPF A.7: Strict Distinction):**
- method ≠ tool (A.3)
- result ≠ description of result (A.7)
- characteristic ≠ way to change it (A.17)
- state ≠ action plan (A.19)
- object ≠ model (A.7)
- knowledge ≠ training (A.7)

### 3.2. The universality of first principles

First principles are **universal in content**:
- the same in construction, culinary arts, medicine, management
- independent of subject matter — they define correctness of thinking

### 3.3. When first principles are absent or violated

Then "knowledge decay" occurs:
- methods turn into rituals and advice
- tool is presented as method ("installed the app → became disciplined")
- report substitutes for result ("document exists → therefore done")
- training substitutes for knowledge ("course exists → therefore domain is described")
- errors become invisible (no language of distinctions)
- AI scales confusion

---

## 4. FPF — First Principles Framework

### 4.1. First principles exist before formalization

First principles have "always existed" as a practice of humanity. **FPF does not invent first principles.**

FPF does three things:

| Function | Description |
|----------|-------------|
| **Explication** | Makes first principles explicit (describes distinctions) |
| **Normativity** | Turns them into correctness requirements (what counts as a confusion error) |
| **Discipline** | Provides language and constraints to maintain correct description |

### 4.2. What FPF defines

FPF defines:
- universal entity types (A.1-A.3): role, method, work product, process, description, carrier
- permissible and impermissible distinctions (A.7: Strict Distinction)
- rules for working with contexts (A.1.1: Bounded Context)
- strict demarcations (A.7):
  - object / description / carrier
  - knowledge / representation / publication
  - method / scenario
  - system / process
- multi-view description principles (E.17: MVPK)
- requirements for verifiability, SoTA (Part G) and trust (B.3: F-G-R)

FPF answers the question:
> "How is it fundamentally permissible to describe knowledge and thinking?"

### 4.3. What FPF does NOT do

FPF:
- **does not describe specific domain areas**
- does not contain second principles
- is not a course (for human training)
- does not provide "step-by-step scenarios"

### 4.4. FPF universality

FPF is **universal in content**:
- it is equally applicable to any knowledge domain
- its types and distinctions are subject-independent
- it provides a meta-ontology and description language

FPF is universal in the same way as logic, type theory, basic ontology.

---

## 5. Second principles

### 5.1. What are second principles

**Second principles** — stable domain-specific patterns and distinctions within a specific area. They answer the question:

> What really matters here? Which distinctions are critical? What are the typical errors?

### 5.2. They exist before formalization

Second principles live:
- in professional experience
- in standards
- in craft
- in "domain sense"

They exist **before any description**.

### 5.3. Their universality

Second principles:
- are **not universal in content** (different domains have different ones)
- but are **"universal in type"** in this sense:
  - every domain has them
  - in every domain they can be brought to engineering form
  - and the requirements for that form are defined by first principles discipline (FPF)

---

## 6. SPF — Second Principles Framework

### 6.1. What is SPF

**SPF** is a framework that defines **how to formalize second principles** of a domain area so that engineering knowledge is produced.

SPF answers the question:
> What form and criteria are needed so that second principles become a verifiable core of the domain?

### 6.2. What SPF does

SPF defines:

**Minimum mandatory elements for an engineering description of a domain:**
- bounded context
- key distinctions
- characteristics
- assessment/verification methods
- work products
- failure modes
- SoTA statuses and revision criteria

**Structure requirements:**
- identifier and reference rules (to make knowledge traceable)
- canonical pack structure

**Process gates:**
- process lint: checks that didactics were not introduced, entity types were not mixed
- contracts between source-of-truth and downstream

SPF answers the question:
> "How, following FPF rules, to produce and maintain second principles?"

### 6.3. What SPF does NOT do

SPF:
- does not add domain content
- does not decide for you which second principles are valid
- does not build courses
- does not replace research/expertise

### 6.4. How SPF relates to FPF

| FPF | SPF |
|-----|-----|
| Defines correctness of types and distinctions ("how to think") | Builds on this and defines the engineering format for capturing domain knowledge ("how to formalize second principles") |
| Prevents logical and ontological confusion | Prevents domain knowledge from turning into "a collection of tips" |

### 6.5. SPF universality

SPF is **universal in form and process**, but **not in content**:
- pack structure is the same for any domain
- knowledge creation process is the same
- lint and gates are the same
- but pack content is always domain-specific

SPF is universal like an engineering standard, a production framework, a normative methodology.

---

## 7. Pack — domain passport

### 7.1. What it is

**Domain passport** (aka **pack**) — an already assembled, formalized, and stabilized engineering description of a domain, where second principles have been brought to the state of engineering knowledge.

> Pack = domain passport

### 7.2. Pack is a result, not a process

**Important**: a pack is not a process and not "a way to assemble". A pack is a **result, a knowledge artifact** (source of truth).

### 7.3. What a pack includes

| Element | Description |
|---------|-------------|
| Bounded context | Fixed semantic frame of the domain |
| Distinctions | Conceptual boundaries of the domain |
| Domain entities | Roles, objects of attention, constraints |
| Methods | Ways of acting (not scenarios) |
| Work products | Verifiable results of methods |
| Failure modes | Typical interpretation errors |
| SoTA annotations | Currency statuses |
| Relationship map | Graph of links between elements |

**Pack is the source-of-truth** for the given domain.

Pack answers the question:
> "What does the stabilized knowledge of this specific domain look like?"

### 7.4. What a pack is NOT

| Pack is NOT | Where it belongs |
|-------------|-----------------|
| Course, textbook | Downstream (training systems) |
| Development path | Downstream (guides, coaching) |
| "How to implement" | Downstream (implementation) |
| Embeddings/index | Downstream (AI implementations) |
| Collection of publications | Downstream (content) |

A pack can **generate** (downstream) courses/guides/indexes, but is not one itself.

### 7.5. Non-universality of packs

Each pack:
- is tied to one domain area
- contains domain-specific distinctions and methods
- cannot be directly transferred to another domain

Universality is achieved **not through pack content**, but through the fact that *all packs are built following one SPF and on top of one FPF*.

---

## 8. How a pack is created

### 8.1. Logical order

1. **First principles** exist independently and are explicated in FPF as normative distinctions for correct thinking about knowledge. The principles exist independently of FPF.

2. **Second principles** of a specific domain area exist in professional experience; SPF defines requirements and the process for their engineering capture in a Pack.

3. **Pack** — these are the second principles of a domain area, formalized as an engineering knowledge core in compliance with FPF and SPF requirements.

### 8.2. Practical process (iterations)

In practice, a pack is created iteratively, "together with" capturing second principles:

#### Iteration 0: Domain contract

| Task | Artifact |
|------|----------|
| Fix bounded context (domain name, boundaries, vocabulary) | `01-domain-contract/01A-bounded-context.md` |
| Fix core distinctions (bans on type confusion) | `01-domain-contract/01B-distinctions.md` |
| Fix truth criteria (what counts as verification/artifact) | In bounded context |

#### Iteration 1: Engineering structure

| Task | Artifact |
|------|----------|
| Create characteristics catalog (like safety/reliability in automotive) | `02-domain-entities/02E-characteristics-registry.md` |
| Create characteristic card template | `_template/03-characteristics/` |
| Create top-level map (role/state/characteristic/indicator) | `07-map/PD.MAP.002.md` |

#### Iteration 2: MVP characteristic

Pick 1 characteristic (e.g., agency) and build a minimum set:

| Element | Artifact |
|---------|----------|
| Definition and distinctions | Characteristic card |
| Indicators/metrics | In the card |
| Assessment methods and test scenarios | `03-methods/PD.METHOD.NNN.md` |
| Assessment work products | `04-work-products/PD.WP.NNN.md` |
| Typical errors | `05-failure-modes/PD.FAIL.NNN.md` |
| SoTA status | `06-sota/PD.SOTA.NNN.md` |

#### Iteration 3+: Expansion

- Add next characteristic (caliber of personality)
- Later: stress resilience and others

#### Continuously: Evolution

- SoTA review
- Update criteria, metrics, tests
- Check "haven't we slipped into training"

### 8.3. Process stages (detailed)

The detailed process is described in [`/process/`](/process/):

```
01. Domain Selection
02. Bounded Context
03. Distinctions Work
04. Domain Entities Identification
05. Information Ingestion
06. Analysis & Formalization
07. Method & Product Extraction
08. Failure Modes Extraction
09. SoTA Annotation
10. Map Maintenance
11. Review & Evolution Cycle
```

---

## 9. How FPF helps SPF and pack

### 9.1. What FPF provides for SPF

FPF ensures **base correctness**:
- don't confuse statement types
- don't mix tool/method
- don't substitute result with description
- don't describe "domain as a system" (without specifying which)
- don't confuse states with learning paths

FPF is the "protective grammar" for everything else.

### 9.2. What FPF provides for pack

FPF makes a pack:
- type-consistent
- suitable for tracing and verification
- resistant to "content sprawl"

### 9.3. How SPF helps create a pack

SPF:
- defines the "engineering form" and minimum mandatory elements
- introduces process gates (lint) to ensure:
  - pack doesn't turn into a course
  - doesn't become a collection of lifehacks
  - doesn't lose verifiability
  - doesn't mix levels

---

## 10. Typical errors (anti-patterns)

### 10.1. Pack-level errors

| Error | Symptom | How to avoid |
|-------|---------|--------------|
| **Pack turns into training** | Steps, lessons, "how to pass a stage" appear | Didactics is downstream |
| **States become "stages"** | A linear path appears instead of state classes | States are classes, not a sequence |
| **Tools declared as methods** | App, timer, template = "method" | Method ≠ tool (D.001) |
| **Artifact substitutes for fact** | Report = "quality ensured" | Work product ≠ description (D.005) |
| **SoTA turns into "literature review"** | Instead of statuses and revision criteria — a lit review | SoTA = status + revision criterion |
| **Downstream becomes source-of-truth** | Course/index/embeddings start "overriding" the core | Pack is the only source-of-truth |

### 10.2. Banned formulations

| Banned | Why |
|--------|-----|
| Mixing SPF and pack in formulations | Different levels |
| Considering SPF universal knowledge by content | SPF is universal by form, not content |
| Considering a pack training material | Pack ≠ course |
| Turning methods into scenarios | Method ≠ scenario |
| Considering AI representations a source of truth | Embeddings ≠ knowledge |
| "Creator is a system" | Which system? Specify the object of description! |

---

## 11. Binding to domain: "Characteristics and states of a creator"

### 11.1. Domain area

**Domain name**: Characteristics and states of a creator

**Engineering analogy**: just as in the automotive industry a product has characteristics (safety, reliability) and test methods, a "creator" also has characteristics (agency, caliber of personality, etc.) and assessment/verification methods.

**Bounded context**: [01A-bounded-context.md](/pack/personal-development/01-domain-contract/01A-bounded-context.md)

### 11.2. Creator roles

The pack captures creator roles as participation modes:

| Role | Description |
|------|-------------|
| Learner | Learning acquisition mode |
| Intellectual | Analysis and reflection mode |
| Professional | Productive activity mode |
| Researcher | New knowledge discovery mode |
| Enlightener | Knowledge transfer mode |

### 11.3. Learner states

States are **state classes**, not a trajectory or training program:

| State | Description |
|-------|-------------|
| Random | No regularity, chaotic actions |
| Practicing | Regularity appears |
| Systematic | Has a system, follows it |
| Disciplined | Sustained adherence to the system |
| Proactive | Anticipatory actions, initiative |

### 11.4. Characteristics

Characteristics catalog by analogy with engineering specs:

| Characteristic | Category | Priority |
|---------------|----------|----------|
| Agency | Core | High |
| Caliber of personality | Core | High |
| Stress resilience | Resilience | Medium |

### 11.5. Digital twin

**DS-twin** acts as an external "measurement circuit":
- indicators and their types
- derived score computation (e.g., stage/mastery/agency/risk)
- while generative texts/interpretations do not become truth in themselves

In the pack, this is formalized as an **interface contract**: which indicators are used and how they link to characteristics/states.

---

## 12. Readiness checklists (Definition of Done)

### Phase A: Domain contract stabilization

Done when:
- [ ] Bounded context exists
- [ ] Core distinctions exist
- [ ] Reference/ID rules exist
- [ ] No didactics or "transitions"

### Phase B: Catalog layer

Done when:
- [ ] Characteristics registry exists
- [ ] Characteristic card template exists
- [ ] Top-level map exists
- [ ] Digital twin interface exists

### Phase C: MVP characteristics

Done when for one characteristic:
- [ ] Definition/distinctions exist
- [ ] Indicators/metrics exist
- [ ] Assessment methods + test scenarios exist
- [ ] Work products exist
- [ ] Failure modes exist
- [ ] SoTA status and revision criterion exist

---

## 13. Level hierarchy and three dimensions

### 13.1. Canonical hierarchy

```
FPF (Level 1)  →  first principles framework (meta-ontology + distinctions)
       ↓              Part A-G: Holon, BoundedContext, Γ, F-G-R, SoTA Kit
SPF (Level 2)  →  second principles framework (form + process)
       ↓              process/, pack-template/, spec/
Pack           →  formalized knowledge of a specific domain
       ↓              source-of-truth
Downstream     →  derived representations (courses, AI agents, guides)
```

| Level | What | Universality | FPF Parts |
|-------|------|-------------|-----------|
| **FPF** | Meta-level (ontology and distinctions) | Universal in content | A-G |
| **SPF** | Level of form, process, and guardrails | Universal in form and process | builds on A, B, G |
| **Pack** | Second-level domain knowledge | Domain-specific | uses A.1.1, A.7 |
| **Downstream** | Derived representations (not source-of-truth) | Free form | — |

### 13.2. Three orthogonal dimensions

Knowledge organization is described by three **independent** dimensions:

| Dimension | What it determines | Examples |
|-----------|-------------------|----------|
| **Content** | What is inherited semantically | FPF → SPF → Pack → Downstream |
| **Form** | How the repository is structured | S2R, custom layout |
| **Process** | How knowledge is produced and maintained | ingestion, lint, gates |

### 13.3. Orthogonality of dimensions

Dimensions are **independent of each other**:
- **Content** (knowledge level) does not dictate storage form
- **Form** (repository structure) does not determine the working process
- **Process** (knowledge production) is applicable to different forms

This means:
- A Pack can use S2R structure or another one
- A Downstream repository can use the same S2R as a Pack
- The SPF process applies regardless of the chosen form

### 13.4. S2R — structure format, not knowledge level

**S2R** (Structured Second-level Repository) — is a **form** specification, not a content level:
- S2R defines *how to organize files and folders*
- S2R does NOT define *what level of knowledge is stored in them*
- S2R can be applied to both Pack and Downstream

**Related repositories**:
- [ailev/FPF](https://github.com/ailev/FPF) — First Principles Framework (level 1)
- [TserenTserenov/FMT-S2R](https://github.com/TserenTserenov/FMT-S2R) — structure format specification
- [aisystant/DS-ecosystem-development](https://github.com/aisystant/DS-ecosystem-development) — downstream, uses S2R

### 13.5. What "framework" means in this architecture

In this context, a **framework** is **not a content set** and **not a knowledge library**.

A framework is:
- a set of mandatory distinctions
- a canonical structure
- a normative process
- correctness verification rules
- contracts between levels

---

## 14. Relationship to other methodologies

The FPF → SPF → Pack architecture does not exist in isolation. Below is a comparison with well-known approaches.

### 14.1. Domain-Driven Design (DDD)

| Aspect | DDD | FPF/SPF/Pack |
|--------|-----|--------------|
| **Focus** | Software code and architecture | Formalized knowledge (not code) |
| **Bounded Context** | Model boundary in code | Pack boundary (semantic frame) |
| **Ubiquitous Language** | Shared language of team and code | Distinctions as shared language |
| **Entity/Value Object** | Objects in code | Roles, Objects of Attention, Work Products |

**Key difference**: DDD is about code and software architecture. FPF/SPF/Pack is about knowledge formalization before code.

**Level analogy**:
- FPF ≈ Strategic DDD patterns (conceptual level)
- SPF ≈ Tactical DDD patterns (structural patterns)
- Pack ≈ Bounded Context implementation (concrete implementation)

### 14.2. Ontology Engineering (OWL, SKOS)

| Concept | OWL/SKOS | FPF/SPF/Pack |
|---------|----------|--------------|
| Upper Ontology | DOLCE, BFO, SUMO | FPF (meta-ontology) |
| Domain Ontology | Specific domain ontology | Pack (domain knowledge) |
| Classes/Properties | Types and relationships | Distinctions, Roles, Methods |
| Reasoning | Logical inference | SoTA + revision criteria |

**Difference**: Formal ontologies are for machine reasoning. Pack is for human-readable knowledge with AI support.

### 14.3. Knowledge Graphs

| Concept | Knowledge Graphs | FPF/SPF/Pack |
|---------|------------------|--------------|
| Schema | Graph schema | SPF (_template) |
| Entities | Graph nodes | Pack elements (Methods, WPs, FMs) |
| Relations | Graph edges | Links in Map, cross-references |
| Provenance | Data source | SoTA annotations + material ingestion |

**Difference**: Knowledge Graphs are data-centric (facts). Pack is methodology-centric (how domain knowledge is structured).

### 14.4. What makes FPF/SPF/Pack unique

1. **Explicit separation of content, form, and process** — most frameworks mix these dimensions

2. **Process-driven knowledge production** — SPF defines not only structure but also the knowledge creation process

3. **Failure Modes as first-class citizens** — typical interpretation errors are explicitly modeled

4. **SoTA as attribute, not literature review** — currency status is attached to specific statements with revision criteria

5. **Downstream contract** — explicit interface between source-of-truth and derived representations

6. **AI-ready, human-readable** — Pack is human-readable and suitable for AI agents without losing structure

---

## 15. Mapping to repository structure

### 15.1. FPF (interface to first principles)

- `/fpf/README.md` — describes how this repository builds on FPF
- FPF itself is not implemented here, but connected as an external source of norms

### 15.2. SPF (second principles framework)

| Component | Path |
|-----------|------|
| Pack template | `/pack/_template/` |
| Knowledge-creation process | `/process/` |
| Process lint | `/process/process-lint.md` |
| Downstream specs | `/spec/` |
| Constitution | `CLAUDE.md` |

This is the **universal part**, independent of the domain area.

### 15.3. Pack "Characteristics and states of a creator"

| Path | Purpose |
|------|---------|
| `/pack/personal-development/` | All pack content |
| `00-pack-manifest.md` | Metadata and scope |
| `01-domain-contract/` | Domain contract |
| `02-domain-entities/` | Roles, objects of attention |
| `03-methods/` | Methods |
| `04-work-products/` | Work products |
| `05-failure-modes/` | Typical errors |
| `06-sota/` | SoTA annotations |
| `07-map/` | Relationship maps |

**Note**: The folder is named `personal-development` for historical reasons. The pack's domain name is "Characteristics and states of a creator".

### 15.4. Downstream (explicitly not here)

The following things **are not part of the pack and are not stored in this repository**:
- courses
- guides
- learning paths
- implementation checklists
- AI embeddings and indexes
- publications (PDF, websites)

---

## 16. Brief glossary

| Term | Definition |
|------|------------|
| **Bounded context** | Fixed semantic frame of a domain |
| **Distinction** | A demarcation preventing ontological confusion |
| **Method** | Way of acting, not a scenario |
| **Work product** | Verifiable result of a method |
| **Failure mode** | Typical interpretation error |
| **SoTA annotation** | Currency status of a statement |
| **Map** | Graph of links between pack elements |
| **Downstream view** | Derived representation of a pack |
| **Characteristic** | Axis of object assessment |
| **Indicator** | Observable sign for assessment |
| **State** | Class/mode of an object based on characteristic values |
| **Practice** | Reproducible pattern of applying methods in context |

---

## 17. Final formula

> **First principles** — universal distinctions for correct thinking about knowledge; they exist independently of formalization and define which entity types are permissible in description and what must not be confused in any domain area.

> **FPF (First Principles Framework)** — a framework that explicates first principles, makes them explicit and normative, provides language and correctness criteria for knowledge description, but contains no domain content.

> **Second principles** — stable domain-specific patterns and distinctions of a specific area; they exist before formalization in professional experience, practice, and implicit rules, and are not universal in content.

> **SPF (Second Principles Framework)** — a framework of requirements and processes that defines how second principles can be captured and stabilized as engineering knowledge (through domain boundaries, distinctions, characteristics, verification methods, work products, failure modes, and currency management), building on FPF discipline.

> **Pack / domain passport** — an already assembled and formalized engineering core of a specific domain area: second principles brought to an engineering state in compliance with FPF and SPF requirements; it is a knowledge artifact (source of truth), not a process and not training.

---

## Key distinction: information vs knowledge

| Information | Knowledge (Pack) |
|-------------|-----------------|
| Raw data, materials | Formalized through distinctions |
| Not verified | Passed SPF process |
| No SoTA status | Has SoTA + revision criterion |
| Input to the process | Output of the process |

---

*This document is normative for the spf-personal repository.*


# SOURCE_FILE: docs/spf-sota-mapping.md
---
---
id: SPF.DOC.SOTA-MAPPING
name: SPF ↔ SOTA Mapping
status: draft
created: 2026-02-13
---

# SPF ↔ SOTA Mapping

> Correspondence table: SPF slots and the SOTA practices that fill them.
> Source: Pack DP `06-sota/DP.SOTA.*` + SPF.SPEC.003

## Positioning

| Level | What | Role |
|-------|------|------|
| FPF | Meta-principles of correct thinking | First principles |
| SPF | Core domain specification | Second principles |
| SOTA | Best practices from industry | SPF slot fillers |
| DDD | Method for extracting and engineering the core | SPF operationalization |

> SPF defines SLOTS. SOTA fills slots with METHODS. DDD is the bridge between them.

## Mapping: SPF slot → SOTA practice

| SPF slot | SOTA practice | ID | What it provides |
|----------|---------------|----|-----------------|
| Bounded Context | DDD Strategic | DP.SOTA.001 | Context Mapping, ACL, Published Language |
| Vocabulary (Kinds, terms) | DDD (Ubiquitous Language) | DP.SOTA.001 | UL permeates everywhere: code, UI, docs, tickets |
| Invariants / second principles | DSL→DSLM | DP.SOTA.010 | Machine-checkable domain rules |
| Boundary Statements | Open API Specs | DP.SOTA.003 | OpenAPI + AsyncAPI + CloudEvents |
| Multi-View representations | Multi-Representation Arch | DP.SOTA.012 | viewOf, compositionViewOf, projectionView |
| Projection into Downstream | Multi-Representation Arch | DP.SOTA.012 | Pack → multiple views |
| Context integration | Coupling Model | DP.SOTA.011 | knowledge/distance/volatility coupling |
| Evidence / Assurance | DDD + Open Specs | DP.SOTA.001/003 | Domain tests + contract testing |
| Model evolution | DDD Strategic | DP.SOTA.001 | Refactoring toward deeper insight |
| Policy/mechanism separation | Context Engineering | DP.SOTA.002 | Write/Select/Compress/Isolate |

## Mapping: SPF Layer → SOTA method (Pack Architecture)

| SPF Layer | SOTA method | What it does |
|-----------|-------------|-------------|
| Layer 0 (manifest) | llms.txt, MemGPT/Letta (core) | Machine-readable index, always-in-context |
| Layer 0 (summary) | Contextual Chunking | Retrieval without reading the full file |
| Layer 1 (MAP, indices) | RAPTOR, MemGPT/Letta (recall) | Hierarchical navigation |
| Layer 2 (entity cards) | MemGPT/Letta (archival) | Point load by ID |
| Cross-entity links | LightRAG | Typed `related:` = graph for traversal |
| Semantic search | Hybrid Retrieval | Vector (summary) + exact (ID-codes) |

## Mapping: Operational cycle → SOTA practice

| Operation | SOTA practice | ID | How it is applied |
|-----------|---------------|----|------------------|
| Pack creation | DDD Strategic | DP.SOTA.001 | BC identification, UL extraction |
| Knowledge extraction | AI-Accelerated OE | DP.SOTA.007 | LLM first pass, human validates |
| Capture (during work) | Real-Time KM | DP.SOTA.008 | At checkpoints, not after session |
| Agent design | Agentic Development | DP.SOTA.006 | BC + IPO + contracts |
| Agent context | Context Engineering | DP.SOTA.002 | Write/Select/Compress/Isolate |
| Agent organization | AI-Native Org | DP.SOTA.005 | Each agent = org unit with accountability |
| Coupling assessment | Coupling Model | DP.SOTA.011 | 3 dimensions: knowledge/distance/volatility |
| Retrieval | GraphRAG | DP.SOTA.004 | Vector + graph traversal |
| Digital Twin | KB Digital Twins | DP.SOTA.009 | Pack + data + agents |

## What is NOT applicable (with rationale)

| Practice | Why not SOTA / not applicable |
|----------|-------------------------------|
| Tactical DDD (Entity, VO, Aggregate) | OOP-specific, not universal beyond Java/C# (DP.D.017) |
| Formal domain specifications (academic) | Not mainstream; replaced by ontologies + KG |
| Full GraphRAG (Microsoft) | Excessive for structured Pack; LightRAG is sufficient |
| Static `_index.md` | Become outdated; replaced by auto-MAP |
| Subfolders by entity type | Solves human problem, not AI |

---

*Edition: 2026-02 | Update when SOTA practices in Pack DP change*


# SOURCE_FILE: ontology.md
---
---
id: SPF.SPEC.002
name: Ontology
status: draft
created: 2026-02-10
---

# Ontology Specification

> Ontology architecture: FPF → SPF → Pack → Downstream.
> How concepts are inherited, how Pack describes its ontology, who changes it.

---

## 1. Ontology architecture

### 1.1. Four levels

```
FPF (meta-ontology)      — universal concepts: System, Method, Role, ...
       ↓ inherits
SPF (base ontology)      — fixes FPF concepts + Pack entity types
       ↓ inherits
Pack (domain ontology)   — domain concepts, each linked to an SPF concept
       ↓ references
Downstream               — uses Pack concepts, does not define new ones
```

### 1.2. Inheritance principles

| Rule | Description |
|------|-------------|
| **SPF ← FPF** | SPF ontology is extended **only** from FPF. No domain concepts |
| **Pack ← SPF** | Each Pack concept **must** have a parent concept from the SPF ontology |
| **Downstream ← Pack** | Downstream references Pack concepts. Does not introduce new concepts |
| **Owner of changes** | The ontology at any level is changed **only by the Knowledge Extractor** (DP.AISYS.013) |

### 1.3. Who defines what

| Level | Defines | Does not define |
|-------|---------|----------------|
| FPF | Universal concepts (U.*) | Domain concepts |
| SPF | Fixes FPF concepts + entity types + format | Domain content |
| Pack | Domain concepts linked to SPF | Concepts of other domains |
| Downstream | Nothing new | Does not define, only references |

---

## 2. SPF base ontology (inherited from FPF)

> These concepts are universal — the same for all domains.
> Source: FPF-Spec, Part A (Kernel Architecture Cluster).

### 2.1. Fundamental types

| FPF ID | Concept | EN | Definition |
|--------|---------|-----|-----------|
| U.Entity | Entity | Entity | Primitive of distinction — everything that can be singled out and named |
| U.Holon | Holon | Holon | Composition unit: a whole composed of parts, itself being a part |
| U.System | System | System | Holon with a boundary interacting with its environment |
| U.Episteme | Episteme | Episteme | Unit of knowledge/description as an artifact |
| U.BoundedContext | Bounded Context | Bounded Context | Semantic frame with its own vocabulary, roles and invariants |
| U.Boundary | Boundary | Boundary | Separation of internal and external |
| U.Interaction | Interaction | Interaction | Exchange across a system boundary |

### 2.2. Transformation (action and change)

| FPF ID | Concept | EN | Definition |
|--------|---------|-----|-----------|
| U.Method | Method | Method | Abstract way of acting (capability) that produces a work product |
| U.MethodDescription | Method Description | Method Description | Recipe/instruction for executing a method |
| U.Work | Work | Work | Record of a completed action (occurrence) |
| U.WorkPlan | Work Plan | Work Plan | Schedule of intent |

### 2.3. Roles and capabilities

| FPF ID | Concept | EN | Definition |
|--------|---------|-----|-----------|
| U.RoleAssignment | Role Assignment | Role Assignment | Contextual binding of a role to a holder (Holder#Role:Context) |
| U.Capability | Capability | Capability | Dispositional property — the ability to perform an action |
| U.ServiceClause | Service Clause | Service Clause | Service contract (promise content) |
| U.Commitment | Commitment | Commitment | Deontic object (obligation/permission/prohibition) |

### 2.4. Types and measurement

| FPF ID | Concept | EN | Definition |
|--------|---------|-----|-----------|
| U.Kind | Kind/Type | Kind | Classification unit with intension and extension |
| U.Characteristic | Characteristic | Characteristic | Measurable evaluation axis for an object |
| U.Flow | Flow | Flow | Evolution of constraints (constraint validity) |

### 2.5. Key FPF distinctions (A.7 Strict Distinction)

| Distinction | Meaning |
|------------|---------|
| Object ≠ Description ≠ Carrier | Thing in reality ≠ model of thing ≠ file where the model resides |
| Role ≠ Role holder | Function (Role) ≠ the one who performs it (Holder) |
| Method ≠ Method description ≠ Work | Capability ≠ recipe ≠ fact of execution |
| Characteristic ≠ Metric ≠ Indicator | Evaluation axis ≠ unit of measurement ≠ observable sign |
| Knowledge ≠ Learning ≠ Representation | Pack ≠ course/training ≠ specific assembly for an audience |

> **Update.** When a new concept is added to FPF — it must be added to this table.

---

## 3. SPF entity types

> SPF defines entity types that Pack uses to organize knowledge.
> Each type is linked to one or more FPF concepts.

| Code | Type | FPF concept | Definition |
|------|------|-------------|-----------|
| `M` | Method | U.Method | Description of a capability to produce a work product |
| `WP` | Work Product | U.Work + U.Episteme | Observable result of applying a method |
| `FM` | Failure Mode | — (SPF-specific) | Typical violation of a method with observable symptoms |
| `D` | Distinction | A.7 Strict Distinction | Conceptual boundary whose violation causes confusion |
| `R` | Role | U.RoleAssignment | Contextual function in a bounded context |
| `CHR` | Characteristic | U.Characteristic | Measurable evaluation axis for an entity |
| `SOTA` | SoTA annotation | — (SPF-specific) | Currency status of a statement + revision criterion |
| `MAP` | Map | U.Episteme | Navigation structure of connections between entities |
| `SC` | Service Clause | U.ServiceClause | Service contract: for whom, why, what they receive, acceptance criterion |

---

## 4. Requirements for Pack ontology

### 4.1. Placement

```
<repo>/ontology.md    — in the root of each repo
```

Uniform placement: `ontology.md` in the repo root at **all levels** (SPF, Pack, Downstream). For Downstream the file references Pack and SPF-ontology concepts and introduces no new concepts.

### 4.2. Required sections

#### Section 1: Entity types

All Pack types (base from SPF + extended) linked to SPF:

| Code | Type | FPF/SPF concept | Definition | not (what this is NOT) |
|------|------|-----------------|-----------|------------------------|
| `M` | Method | U.Method | ... | not a scenario |
| `ARCH` | Architecture | U.System + U.Episteme | ... | not an implementation |

**Required column "FPF/SPF concept"** — parent concept from the base ontology (section 2 of this document). Each extended Pack type must specify which FPF concept it belongs to.

#### Section 2: Domain glossary

Key domain concepts linked to the SPF ontology:

| Term | Definition | Parent concept (SPF) | Related to |
|------|-----------|---------------------|-----------|
| Digital platform | Digital ecosystem environment | U.System | DP.ARCH.001 |
| AI system | System using LLM | U.System + U.Capability | DP.ROLE.001 |

**Required column "Parent concept (SPF)"** — which universal concept from the base ontology this domain term belongs to.

#### Section 3: Relations between types

As in the current version (unchanged).

#### Section 4 (opt.): Type hierarchy

#### Section 5 (opt.): Cross-Pack links

### 4.3. Downstream requirements

Downstream repositories (code, bots, courses) contain two kinds of concepts:

#### Reference concepts (from Pack)

Downstream **references** Pack and SPF-ontology concepts. These concepts are not redefined — used as-is with source indicated.

#### Own concepts (implementation)

Downstream **may** introduce its own concepts specific to the implementation (code terminology, UI terms, internal abstractions). Requirements:

1. **Linked to Pack.** Each own concept must be connected to a concept from the upstream Pack's ontology.md
2. **Domain check.** The Knowledge Extractor upon discovering a new concept in downstream checks: is it a domain concept (universal to the subject area)?
   - **Yes, domain** — propose adding to Pack (via Extraction Report), keep a reference in downstream
   - **No, implementation** — keep in downstream ontology.md with a link to the Pack concept
3. **No duplication.** If the concept already exists in Pack — reference it, do not redefine

#### Test: domain vs implementation

| Criterion | Domain (Pack) | Implementation (Downstream) |
|-----------|--------------|------------------------------|
| Used in another downstream? | Yes | No |
| Tied to specific code/UI? | No | Yes |
| Makes sense without this repo? | Yes | No |

#### Required sections of downstream ontology.md

| Section | Content |
|---------|---------|
| Upstream dependencies | Which Packs and SPF are used |
| Concepts used from Pack | Reference concepts with indication of how they are used |
| Implementation terminology | Own concepts linked to Pack |

---

## 5. Rules

1. **Inheritance FPF → SPF.** The base ontology (section 2) is extended only from FPF. No domain concepts should be in the SPF ontology
2. **Parent link.** Each Pack domain concept must have a parent concept from the SPF ontology
3. **Owner of changes — Extractor.** The ontology (`ontology.md`) at all levels is changed only by the Knowledge Extractor (DP.AISYS.013). The user proposes changes; the Extractor formalizes, validates and applies them
4. **Completeness.** The ontology includes ALL Pack entity types
5. **Consistency.** Definitions in the ontology = definitions in the bounded context
6. **No duplication.** Distinctions remain in `01B-distinctions.md`
7. **Coding.** Type codes — per SPF.SPEC.001
8. **Currency.** When adding an entity — update the ontology
9. **Cross-level links.** Concepts between levels are linked, not overlapping:

| Level | Link to level above | Own concepts |
|-------|---------------------|-------------|
| FPF | — | Universal (U.*) |
| SPF | Inherits FPF | Entity types, format |
| Pack | Extends SPF, linked to U.* | Domain concepts |
| Downstream | References Pack + own implementation | Implementation, linked to Pack |

10. **Cascading.** When ontology.md changes at a higher level — check and update lower ones (SPF → Pack → Downstream)
11. **Bilingualism (DDD UL).** The domain glossary (section 2 in Pack, section 2 in downstream) must contain Term (RU) and Term (EN) columns. EN is used in code, files, git. RU — in documents and discourse
12. **Abbreviations.** Each ontology.md contains an Abbreviations section. Abbreviations are inherited top-down (FPF/SPF → Pack → Downstream) with indication of origin level
13. **Language of documents.** Russian is the primary language of all IWE templates, protocols and documents. English is permitted only for: (a) technical keys (YAML frontmatter: `type`, `status`, `date`), (b) established abbreviations from the Abbreviations section, (c) proper names (GitHub, Railway). English phrases with a Russian equivalent are not permitted. Established loanwords are permitted

---

## 6. Abbreviations (FPF/SPF level)

> Abbreviations defined at the FPF and SPF level. Packs inherit them and add their own.

| Abbreviation | Full form (RU) | Full form (EN) | Level |
|-------------|----------------|----------------|-------|
| FPF | First Principles Framework | First Principles Framework | FPF |
| SPF | Second Principles Framework | Second Principles Framework | SPF |
| UL | Ubiquitous Language | Ubiquitous Language | FPF (DDD) |
| BC | Bounded Context | Bounded Context | FPF (DDD) |
| UTS | Unified Terminology System | Unified Terminology System | FPF |
| SoTA | State of the Art | State of the Art | SPF |
| KE | Knowledge Extraction | Knowledge Extraction | SPF |
| FM | Failure Mode | Failure Mode | SPF |
| WP | Work Product | Work Product | SPF |
| M | Method | Method | SPF |
| D | Distinction | Distinction | SPF |
| R | Role | Role | SPF |
| CHR | Characteristic | Characteristic | SPF |
| MAP | Map | Map | SPF |
| IPO | Input-Processing-Output | Input-Processing-Output | SPF |

---

## 7. Relationship to other specifications

| Specification | Relationship |
|--------------|-------------|
| FPF-Spec (Part A) | Source of base ontology (section 2) |
| SPF.SPEC.001 (coding) | Entity type codes |
| 01A-bounded-context | Domain boundaries; ontology defines concepts within boundaries |
| 01B-distinctions | Distinctions; ontology references them |
| 00-pack-manifest | Registration of extended types |
| 07-map | Links between specific entities (ontology — between types) |
| DP.AISYS.013 (Extractor) | Sole agent that changes the ontology |

---

*This document: `SPF.SPEC.002`*


# SOURCE_FILE: pack-template/00-pack-manifest.md
---
# Pack Manifest Template

Use this template to create the manifest file for a new domain pack.

---

## Metadata

```yaml
pack_id: <DOMAIN>
pack_name: <Human-readable name>
version: 0.1.0
fpf_edition: v1.0
status: draft | active | deprecated
maintainers:
  - name: <Name>
    contact: <email or handle>
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
```

---

## Scope

### What This Pack Covers

_Describe the boundaries of this domain. What questions does this pack answer? What practices does it describe?_

-
-
-

### What This Pack Does NOT Cover

_Explicitly list adjacent domains or topics that are out of scope._

-
-
-

---

## Dependencies

### FPF Distinctions Used

_List the core FPF distinctions this pack relies on._

| FPF Distinction | How Used in This Pack |
|-----------------|----------------------|
| method vs tool | ... |
| work product | ... |
| role | ... |

### Other SPF Packs

_List any other SPF packs this pack depends on or relates to._

| Pack | Relationship |
|------|--------------|
| _none_ | |

---

## Content Summary

| Section | Item Count | Status |
|---------|------------|--------|
| Distinctions | _N_ | draft/complete |
| Roles | _N_ | draft/complete |
| Methods | _N_ | draft/complete |
| Work Products | _N_ | draft/complete |
| Failure Modes | _N_ | draft/complete |
| SoTA Annotations | _N_ | draft/complete |
| Maps | _N_ | draft/complete |

---

## Extended Kinds (SPF.SPEC.001)

_Register domain-specific entity kinds here. Leave empty if only using base kinds (M, WP, FM, D, R, CHR, SOTA, MAP)._

| Code | Name | Description | Folder |
|------|------|-------------|--------|
| _KIND_ | _Name_ | _What this kind represents_ | `02-domain-entities/` |

---

## Entity Index (SPF.SPEC.003)

> Auto-generated by `scripts/generate-map.py --manifest`. Do not edit manually.
> This index enables Layer 0 loading: AI agents read manifest to find relevant entities without loading full cards.

| ID | Name | Kind | Summary | Status |
|----|------|------|---------|--------|
| _DOMAIN.KIND.NNN_ | _Name_ | _KIND_ | _One-sentence summary_ | _status_ |

---

## Change Log (Pack-Specific)

| Date | Change | Author |
|------|--------|--------|
| YYYY-MM-DD | Initial creation | ... |


# SOURCE_FILE: pack-template/01-domain-contract/01A-bounded-context.md
---
# Bounded Context: [Domain Name]

---

## Domain Name

**[Domain Name]**

(English: [English Name])

---

## Object of Description

**[Object]** as an object of engineering description.

| Object IS | Object IS NOT |
|-----------|---------------|
| Object of description with characteristics | Concrete individual |
| Carrier of measurable attributes | Subject of teaching |
| Instance of type | Personality with biography |

---

## Scope (What's In)

| Element | Description | Example |
|---------|-------------|---------|
| **[Element 1]** | [Description] | [Example] |
| **[Element 2]** | [Description] | [Example] |
| **[Element 3]** | [Description] | [Example] |

---

## Non-Goals (What's Out)

| Excluded | Reason | Where It Belongs |
|----------|--------|------------------|
| [Item 1] | [Reason] | [Location] |
| [Item 2] | [Reason] | [Location] |

---

## Truth Criteria

Assertions in this pack are considered justified if:

| Criterion | Test |
|----------|------|
| **Observable indicators** | [Description] |
| **Verifiable work products** | [Description] |
| **Distinction test** | [Description] |
| **SoTA + revision criterion** | [Description] |

**Forbidden**:
- Assertions without observable indicators
- Methods without work products
- SoTA without revision criterion

---

## Downstream Note

**[What belongs downstream]** — outside scope of this pack.

| Pack describes | Downstream uses |
|----------------|-----------------|
| [What exists] | [How to use/develop] |

---

## Key Distinctions

| Distinction | In This Pack |
|-------------|--------------|
| [Distinction 1] | [Reference] |
| [Distinction 2] | [Reference] |

---

## Version

| Attribute | Value |
|-----------|-------|
| Bounded context version | 1.0.0 |
| Created | [Date] |
| Last updated | [Date] |
| Pack ID | [ID] |


# SOURCE_FILE: pack-template/01-domain-contract/01B-distinctions.md
---
# Distinctions Template

Use this template to document the core distinctions (concepts) that carve this domain.

---

## How to Use This File

1. Each distinction should clarify a conceptual boundary
2. Distinctions must not contradict FPF (extend only)
3. Include SoTA status for non-obvious distinctions
4. Link to related methods, work products where relevant

---

## Distinction Entry Format

### [D.001] Distinction Name

**Definition**: _One clear sentence defining the concept._

**Contrast with**: _What this is NOT (the other side of the distinction)._

| This Concept | vs. | That Concept |
|--------------|-----|--------------|
| _characteristic 1_ | | _characteristic 1_ |
| _characteristic 2_ | | _characteristic 2_ |

**Why it matters**: _Brief explanation of why making this distinction is useful in practice._

**Related items**:
- Methods: [DOMAIN.M.XXX](link)
- Work Products: [DOMAIN.WP.XXX](link)

**SoTA**: `current` | `deprecated-interpretation` | `hypothesis`
- Revision criterion: _What evidence would change this?_

---

## Distinctions Index

| ID | Distinction | Status |
|----|-------------|--------|
| D.001 | _Name_ | current |
| D.002 | _Name_ | current |

---

## Template Entry (Copy This)

### [D.XXX] _Distinction Name_

**Definition**: _TBD_

**Contrast with**: _TBD_

| This Concept | vs. | That Concept |
|--------------|-----|--------------|
| | | |

**Why it matters**: _TBD_

**Related items**:
- Methods:
- Work Products:

**SoTA**: `current`
- Revision criterion: _TBD_


# SOURCE_FILE: pack-template/02-domain-entities/02A-roles.md
---
# Roles Template

Use this template to document roles relevant to this domain.

---

## What is a Role?

Per FPF: A **role** is a functional position that an agent occupies when performing certain methods. One person may occupy multiple roles; one role may be occupied by multiple people.

A role is NOT:
- A job title (may map to multiple roles)
- A person (person occupies roles)
- A skill (skills enable role performance)

---

## Role Entry Format

### [R.001] Role Name

**Definition**: _What this role does (functional description)._

**Key responsibilities**:
- _Responsibility 1_
- _Responsibility 2_

**Methods performed**:
- [DOMAIN.M.XXX](link) — _brief note_

**Work products owned**:
- [DOMAIN.WP.XXX](link) — _brief note_

**Typical failure modes when this role is absent or poorly performed**:
- [DOMAIN.FM.XXX](link)

**Often confused with**: _Another role, and why they differ._

---

## Roles Index

| ID | Role | Primary Methods |
|----|------|-----------------|
| R.001 | _Name_ | M.001, M.002 |

---

## Template Entry (Copy This)

### [R.XXX] _Role Name_

**Definition**: _TBD_

**Key responsibilities**:
-

**Methods performed**:
-

**Work products owned**:
-

**Typical failure modes when this role is absent or poorly performed**:
-

**Often confused with**: _TBD_


# SOURCE_FILE: pack-template/02-domain-entities/02B-objects-of-attention.md
---
# Objects of Attention Template

Use this template to document what practitioners in this domain attend to.

---

## What is an Object of Attention?

Objects of attention are the entities, states, or phenomena that practitioners observe, measure, or manipulate. They are NOT methods (what you do) but rather what you focus on while doing it.

Examples:
- A doctor attends to: vital signs, symptoms, patient history
- A project manager attends to: deadlines, dependencies, stakeholder concerns
- An engineer attends to: system states, error logs, performance metrics

---

## Object of Attention Entry Format

### [OA.001] Object Name

**What it is**: _Brief description of this object of attention._

**Why practitioners attend to it**: _What decisions or actions does attending to this enable?_

**How it is observed/measured**:
- _Observable indicator 1_
- _Observable indicator 2_

**Related methods** (that involve this object):
- [DOMAIN.M.XXX](link)

**Related work products** (that capture or represent this object):
- [DOMAIN.WP.XXX](link)

**Common mistakes** in attending to this:
- [DOMAIN.FM.XXX](link) — _brief note_

---

## Objects of Attention Index

| ID | Object | Related Methods |
|----|--------|-----------------|
| OA.001 | _Name_ | M.001, M.003 |

---

## Template Entry (Copy This)

### [OA.XXX] _Object Name_

**What it is**: _TBD_

**Why practitioners attend to it**: _TBD_

**How it is observed/measured**:
-

**Related methods**:
-

**Related work products**:
-

**Common mistakes**:
-


# SOURCE_FILE: pack-template/02-domain-entities/02C-methods-index.md
---
# Methods Index Template

This file provides a navigable index of all methods in the pack.

---

## What is a Method?

Per FPF: A **method** (or practice) is a repeatable way of doing something that produces a predictable kind of result. Methods are performed by roles and produce work products.

A method is NOT:
- A tool (tools enable methods)
- A step-by-step scenario (that's an instance/application of a method)
- A work product (that's what the method produces)

---

## Methods by Category

### Category 1: _Category Name_

| ID | Method Name | Produces | Status |
|----|-------------|----------|--------|
| [DOMAIN.M.001](../03-methods/DOMAIN.M.001.md) | _Name_ | WP.001 | current |

### Category 2: _Category Name_

| ID | Method Name | Produces | Status |
|----|-------------|----------|--------|
| [DOMAIN.M.002](../03-methods/DOMAIN.M.002.md) | _Name_ | WP.002 | current |

---

## Full Methods List (Alphabetical)

| ID | Method Name | Category | Produces | SoTA |
|----|-------------|----------|----------|------|
| | | | | |

---

## Methods by Work Product Produced

| Work Product | Produced By Methods |
|--------------|---------------------|
| [DOMAIN.WP.001](../04-work-products/DOMAIN.WP.001.md) | M.001, M.003 |

---

## Adding a New Method

1. Create file: `../03-methods/DOMAIN.M.<NNN>.md` using template
2. Add entry to this index
3. Update `07-map/` navigation
4. Verify pre-commit checklist


# SOURCE_FILE: pack-template/02-domain-entities/02D-tools-index.md
---
# Tools Index Template

This file provides a navigable index of tools relevant to this domain.

---

## What is a Tool?

Per FPF: A **tool** is an artifact (physical or digital) that enables or facilitates the performance of a method. Tools are used; methods are performed.

A tool is NOT:
- A method (tools support methods)
- A work product (work products are outputs; tools are enablers)
- A skill (skills are in the agent; tools are external)

---

## Tools by Category

### Category 1: _Category Name_

| Tool Name | Supports Methods | Type |
|-----------|------------------|------|
| _Tool 1_ | M.001, M.002 | software / physical / conceptual |

### Category 2: _Category Name_

| Tool Name | Supports Methods | Type |
|-----------|------------------|------|
| _Tool 2_ | M.003 | software / physical / conceptual |

---

## Tool Entry Format (If Detailed Descriptions Needed)

### Tool Name

**Type**: software | physical | conceptual

**Purpose**: _What this tool enables._

**Supports methods**:
- [DOMAIN.M.XXX](../03-methods/DOMAIN.M.XXX.md)

**Alternatives**: _Other tools that serve similar purpose._

**Notes**: _Any caveats, versioning, or selection criteria._

---

## Notes on Tool Documentation

- Tools are indexed, not deeply documented (unless domain-specific)
- Generic tools (spreadsheets, text editors) need not be listed
- Focus on tools that are specific to this domain's methods
- Tool recommendations (which tool to use) belong downstream, not here


# SOURCE_FILE: pack-template/02-domain-entities/02E-characteristics-registry.md
---
# Characteristics Registry Template

Use this template to maintain a registry of characteristics relevant to this domain.

---

## What is a Characteristic?

Per FPF (A.17 CHR-NORM): A **characteristic** is a measurable or observable attribute of the object of description within this domain. Characteristics describe **what** is measured or observed, not **how** to develop or change it.

A characteristic is NOT:
- A method (method is how you act; characteristic is what you measure)
- A state (state is a temporary mode; characteristic is a stable attribute)
- A skill (skill enables performance; characteristic is an attribute of the object)
- An indicator (indicator is an observable sign; characteristic is what the indicator measures)

---

## Characteristic Entry Format

### [CHR.NNN] Characteristic Name

**Definition**: _What this characteristic is (without didactics)._

**Category**: _Grouping for navigation (e.g., Core, Resilience, Cognitive, Physical)._

**Indicators**:
- _Observable sign 1_
- _Observable sign 2_

**Measurement/test methods**:
- [DOMAIN.METHOD.XXX](link) — _brief note_

**Related distinctions**:
- [DOMAIN.D.XXX](link) — _brief note_

**Related formalizations**:
- [DOMAIN.FORM.XXX](link) — _brief note_

**Epistemic stage**: `formed` | `evidence` | `hypothesis`

---

## Characteristics Index

| ID | Characteristic | Category | Epistemic Stage | Card |
|----|---------------|----------|-----------------|------|
| CHR.001 | _Name_ | _Category_ | _Stage_ | [link](link) |

---

## Template Entry (Copy This)

### [CHR.XXX] _Characteristic Name_

**Definition**: _TBD_

**Category**: _TBD_

**Indicators**:
-

**Measurement/test methods**:
-

**Related distinctions**:
-

**Related formalizations**:
-

**Epistemic stage**: _TBD_


# SOURCE_FILE: pack-template/03-methods/_method-card-template.md
---
# Method Card Template

Copy this file to create a new method card. Replace all `_TBD_` and `DOMAIN.M.XXX` placeholders.

---

## YAML Frontmatter

```yaml
---
id: DOMAIN.M.XXX
name: _Method Name_
status: draft | active | deprecated
summary: "_One sentence (≤150 chars) describing this method for index and retrieval_"
sota: current | deprecated-interpretation | hypothesis
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
related:                                    # Typed relations (SPF.SPEC.003)
  produces: [DOMAIN.WP.XXX]               # Work products this method produces
  uses: [DOMAIN.D.XXX]                    # Distinctions/entities it relies on
  fails_with: [DOMAIN.FM.XXX]             # Associated failure modes
  requires_role: [DOMAIN.R.XXX]           # Roles needed
  precedes: []                             # Methods that follow
  follows: []                              # Methods that precede
tags: []                                    # Free-form search tags
---
```

---

## [DOMAIN.M.XXX] Method Name

### Definition

_One to three sentences describing what this method is. Focus on what it does, not how to do it._

### Purpose

_Why does this method exist? What problem does it address? What does it enable?_

### Inputs

_What does this method require to begin? (Information, prior work products, conditions)_

| Input | Description | Required? |
|-------|-------------|-----------|
| _Input 1_ | _What it is_ | Yes/No |
| _Input 2_ | _What it is_ | Yes/No |

### Outputs (Work Products)

_What does this method produce?_

| Output | Link | Description |
|--------|------|-------------|
| _Output 1_ | [DOMAIN.WP.XXX](../04-work-products/DOMAIN.WP.XXX.md) | _Brief description_ |

### Roles Involved

| Role | Responsibility in This Method |
|------|------------------------------|
| [DOMAIN.R.XXX](../02-domain-entities/02A-roles.md#r-xxx) | _What they do_ |

### Related Methods

| Method | Relationship |
|--------|--------------|
| [DOMAIN.M.YYY](./DOMAIN.M.YYY.md) | _precedes / follows / alternative to / component of_ |

### Key Distinctions

_What conceptual distinctions are essential to performing this method correctly?_

- [DOMAIN.D.XXX](../01-domain-contract/01B-distinctions.md#d-xxx): _Why it matters here_

### Failure Modes

_What commonly goes wrong when this method is performed poorly?_

| Failure Mode | Link |
|--------------|------|
| _Failure 1_ | [DOMAIN.FM.XXX](../05-failure-modes/DOMAIN.FM.XXX.md) |

### Tools Commonly Used

| Tool | How Used |
|------|----------|
| _Tool 1_ | _Brief note_ |

### SoTA Status

**Status**: `current` | `deprecated-interpretation` | `hypothesis`

**Basis**: _What evidence or consensus supports this method?_

**Revision criterion**: _What would change this status?_

---

## Checklist Before Committing

- [ ] ID follows pattern `DOMAIN.M.NNN`
- [ ] Definition is declarative (not "Step 1: ...")
- [ ] Outputs link to work product cards
- [ ] Failure modes are listed
- [ ] SoTA status and revision criterion specified
- [ ] Added to `02C-methods-index.md`
- [ ] Added to `07-map/`


# SOURCE_FILE: pack-template/04-work-products/_work-product-card-template.md
---
# Work Product Card Template

Copy this file to create a new work product card. Replace all `_TBD_` and `DOMAIN.WP.XXX` placeholders.

---

## YAML Frontmatter

```yaml
---
id: DOMAIN.WP.XXX
name: _Work Product Name_
status: draft | active | deprecated
summary: "_One sentence (≤150 chars) describing this work product for index and retrieval_"
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
related:                                    # Typed relations (SPF.SPEC.003)
  produced_by: [DOMAIN.M.XXX]             # Methods that produce this WP
  consumed_by: [DOMAIN.M.YYY]             # Methods that use this WP as input
  fails_with: [DOMAIN.FM.XXX]             # Associated failure modes
tags: []                                    # Free-form search tags
---
```

---

## [DOMAIN.WP.XXX] Work Product Name

### Definition

_One to three sentences describing what this work product is. A work product is an observable, verifiable output of a method._

### Purpose

_Why is this work product valuable? What decisions or actions does it enable?_

### Produced By

| Method | Notes |
|--------|-------|
| [DOMAIN.M.XXX](../03-methods/DOMAIN.M.XXX.md) | _Primary method_ |
| [DOMAIN.M.YYY](../03-methods/DOMAIN.M.YYY.md) | _Alternative method_ |

### Consumed By

_What methods or roles use this work product as input?_

| Consumer | How Used |
|----------|----------|
| [DOMAIN.M.ZZZ](../03-methods/DOMAIN.M.ZZZ.md) | _As input for..._ |
| [DOMAIN.R.XXX](../02-domain-entities/02A-roles.md#r-xxx) | _For decision-making about..._ |

### Observability Criteria

_How do you know this work product exists and is adequate? Be specific._

**Existence check**:
- [ ] _Observable indicator that the WP exists_

**Quality criteria**:
- [ ] _Criterion 1 for adequacy_
- [ ] _Criterion 2 for adequacy_
- [ ] _Criterion 3 for adequacy_

### Typical Form

_What does this work product usually look like? (Document, artifact, state, etc.)_

| Form | Description |
|------|-------------|
| _Form 1_ | _e.g., "Written document with sections X, Y, Z"_ |
| _Form 2_ | _e.g., "Diagram showing..."_ |

### Anti-Patterns

_What does a BAD version of this work product look like?_

| Anti-Pattern | Why It's Problematic |
|--------------|---------------------|
| _Anti-pattern 1_ | _Consequence_ |
| _Anti-pattern 2_ | _Consequence_ |

### Related Work Products

| Work Product | Relationship |
|--------------|--------------|
| [DOMAIN.WP.YYY](./DOMAIN.WP.YYY.md) | _precedes / follows / component of_ |

### Failure Modes

_What goes wrong related to this work product?_

| Failure Mode | Link |
|--------------|------|
| _Failure 1_ | [DOMAIN.FM.XXX](../05-failure-modes/DOMAIN.FM.XXX.md) |

---

## Checklist Before Committing

- [ ] ID follows pattern `DOMAIN.WP.NNN`
- [ ] Definition is declarative
- [ ] Observability criteria are specific and checkable
- [ ] Produced-by methods are linked
- [ ] Anti-patterns described
- [ ] Added to relevant method cards
- [ ] Added to `07-map/`


# SOURCE_FILE: pack-template/05-failure-modes/_failure-mode-template.md
---
# Failure Mode Card Template

Copy this file to create a new failure mode card. Replace all `_TBD_` and `DOMAIN.FM.XXX` placeholders.

---

## YAML Frontmatter

```yaml
---
id: DOMAIN.FM.XXX
name: _Failure Mode Name_
category: method-failure | work-product-failure | role-failure | distinction-confusion
severity: critical | major | minor
status: draft | active | deprecated
summary: "_One sentence (≤150 chars) describing this failure mode for index and retrieval_"
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
related:                                    # Typed relations (SPF.SPEC.003)
  affects_method: [DOMAIN.M.XXX]           # Methods affected
  affects_wp: [DOMAIN.WP.XXX]             # Work products affected
  confused_distinction: [DOMAIN.D.XXX]     # Distinctions confused
tags: []                                    # Free-form search tags
---
```

---

## [DOMAIN.FM.XXX] Failure Mode Name

### Definition

_One to three sentences describing what this failure mode is. What goes wrong?_

### Category

| Category | Description |
|----------|-------------|
| `method-failure` | A method is performed incorrectly or incompletely |
| `work-product-failure` | A work product is missing, incomplete, or malformed |
| `role-failure` | A role is absent, unclear, or poorly performed |
| `distinction-confusion` | Key concepts are conflated or misunderstood |

**This failure mode is**: `_category_`

### Observable Symptoms

_How do you recognize this failure mode is occurring? Be specific._

- [ ] _Symptom 1_
- [ ] _Symptom 2_
- [ ] _Symptom 3_

### Root Causes

_What typically causes this failure mode?_

| Cause | Description |
|-------|-------------|
| _Cause 1_ | _Explanation_ |
| _Cause 2_ | _Explanation_ |

### Consequences

_What happens if this failure mode is not addressed?_

- _Consequence 1_
- _Consequence 2_

### Related Items

| Type | Item | Relationship |
|------|------|--------------|
| Method | [DOMAIN.M.XXX](../03-methods/DOMAIN.M.XXX.md) | _fails when..._ |
| Work Product | [DOMAIN.WP.XXX](../04-work-products/DOMAIN.WP.XXX.md) | _missing/malformed_ |
| Distinction | [DOMAIN.D.XXX](../01-domain-contract/01B-distinctions.md#d-xxx) | _confused with..._ |

### Detection Methods

_How can this failure mode be detected early?_

| Detection Method | When to Apply |
|------------------|---------------|
| _Method 1_ | _Trigger condition_ |

### Notes

_Additional context, examples (anonymized), or references._

---

## Checklist Before Committing

- [ ] ID follows pattern `DOMAIN.FM.NNN`
- [ ] Category is one of: method-failure, work-product-failure, role-failure, distinction-confusion
- [ ] Observable symptoms are specific
- [ ] Related items are linked
- [ ] Added to `07-map/`


# SOURCE_FILE: pack-template/06-sota/_sota-annotation-template.md
---
# SoTA Annotation Template

Use this template for standalone SoTA annotations. Alternatively, embed SoTA status directly in method/distinction cards.

---

## YAML Frontmatter

```yaml
---
id: DOMAIN.SOTA.XXX
target_type: method | distinction | claim | work-product
target_id: DOMAIN.M.XXX (or D.XXX, WP.XXX, etc.)
status: current | deprecated-interpretation | hypothesis
summary: "_One sentence (≤150 chars) describing what this SoTA annotation covers_"
created: YYYY-MM-DD
last_reviewed: YYYY-MM-DD
tags: []                                    # Free-form search tags
---
```

---

## [DOMAIN.SOTA.XXX] SoTA Annotation for [Target Name]

### Target

**Type**: method | distinction | claim | work-product

**ID**: [DOMAIN.M.XXX](link-to-target)

**Specific claim being annotated**: _Quote or paraphrase the claim._

### Status

| Status | Meaning |
|--------|---------|
| `current` | Reflects best available understanding; supported by evidence/consensus |
| `deprecated-interpretation` | Was once accepted but superseded by newer understanding |
| `hypothesis` | Plausible but not yet validated; provisional |

**This annotation status**: `_status_`

### Evidence Basis

_What supports this status assessment?_

| Evidence Type | Description |
|---------------|-------------|
| Research | _Citation or summary_ |
| Practice consensus | _Where/how established_ |
| Theoretical derivation | _From what principles_ |

### Revision Criterion

_What evidence or development would change this status?_

- If `current`: _What would make it deprecated?_
- If `hypothesis`: _What would confirm or refute it?_
- If `deprecated-interpretation`: _What would restore it?_

**Specific criterion**: _TBD_

### Review Schedule

| Field | Value |
|-------|-------|
| Last reviewed | YYYY-MM-DD |
| Next review | YYYY-MM-DD |
| Review trigger | _Event or time-based_ |

### Change History

| Date | Change | Rationale |
|------|--------|-----------|
| YYYY-MM-DD | Initial status: _status_ | _Why_ |

---

## Checklist Before Committing

- [ ] ID follows pattern `DOMAIN.SOTA.NNN`
- [ ] Target item is clearly identified and linked
- [ ] Status is one of: current, deprecated-interpretation, hypothesis
- [ ] Revision criterion is specific and actionable
- [ ] Evidence basis is documented
- [ ] Added to `07-map/` if significant


# SOURCE_FILE: pack-template/07-map/_map-template.md
---
# Map Template

Use this template to create navigation maps for a pack. Maps are structural artifacts, not content.

---

## YAML Frontmatter

```yaml
---
id: DOMAIN.MAP.XXX
name: _Map Name_
scope: full-pack | category | workflow | topic
summary: "_One sentence (≤150 chars) describing what this map navigates_"
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
generated: false                            # true if auto-generated by scripts/generate-map.py
---
```

---

## [DOMAIN.MAP.XXX] Map Name

### Purpose

_What does this map help the reader navigate or understand?_

### Scope

| Scope Type | Description |
|------------|-------------|
| `full-pack` | Overview of entire pack |
| `category` | Subset by category (e.g., all planning methods) |
| `workflow` | Sequence of methods for a scenario |
| `topic` | Cross-cutting theme |

**This map scope**: `_scope_`

---

## Overview Diagram (Optional)

_ASCII or mermaid diagram showing relationships._

```
[Role A] --performs--> [Method 1] --produces--> [WP 1]
                            |
                            v
                       [Method 2] --produces--> [WP 2]
```

---

## Sections

### 1. Core Distinctions

| ID | Distinction | Notes |
|----|-------------|-------|
| [D.001](../01-domain-contract/01B-distinctions.md#d-001) | _Name_ | _Brief note_ |

### 2. Roles

| ID | Role | Primary Methods |
|----|------|-----------------|
| [R.001](../02-domain-entities/02A-roles.md#r-001) | _Name_ | M.001, M.002 |

### 3. Methods

| ID | Method | Produces | Prerequisites |
|----|--------|----------|---------------|
| [M.001](../03-methods/DOMAIN.M.001.md) | _Name_ | WP.001 | _None_ |
| [M.002](../03-methods/DOMAIN.M.002.md) | _Name_ | WP.002 | M.001 |

### 4. Work Products

| ID | Work Product | Produced By | Used By |
|----|--------------|-------------|---------|
| [WP.001](../04-work-products/DOMAIN.WP.001.md) | _Name_ | M.001 | M.002 |

### 5. Failure Modes

| ID | Failure Mode | Related To |
|----|--------------|------------|
| [FM.001](../05-failure-modes/DOMAIN.FM.001.md) | _Name_ | M.001, WP.001 |

### 6. SoTA Annotations (Significant)

| ID | Target | Status |
|----|--------|--------|
| [SOTA.001](../06-sota/DOMAIN.SOTA.001.md) | M.002 | hypothesis |

---

## Navigation Hints

_How should a reader approach this pack?_

- Start with: _Section/file_
- For understanding X, see: _Section/file_
- If looking for Y, see: _Section/file_

---

## Checklist Before Committing

- [ ] ID follows pattern `DOMAIN.MAP.NNN`
- [ ] All links resolve
- [ ] Reflects current state of pack
- [ ] Updated whenever structure changes


# SOURCE_FILE: pack-template/08-service-clauses/_sc-template.md
---
---
id: <CONTEXT>.SC.<NNN>
name: <Short promise name>
kind: SC
status: draft
layer: L4-Personal | L2-Platform | L3-Template
actor: <who receives the promise>
condition: <under what condition>
guarantee: <what is guaranteed>
created: YYYY-MM-DD
related:
  extends: []
  depends_on: []
---

# <CONTEXT>.SC.<NNN> — <Name>

## Promise

> If [actor] [condition] → the domain ensures [guarantee].

## Trigger

- <condition 1>
- <condition 2>

## Guarantee

<What the domain commits to ensure. No implementation steps. Technology-independent.>

## Exceptions

<Under what conditions the promise does not apply>


# SOURCE_FILE: pack-template/ontology.md
---
# Ontology: [Domain Name]

> Domain ontology per SPF.SPEC.002.
> Complete registry of entity types, key terms, and relationships for this Pack.
> Each concept MUST link to a parent concept from SPF base ontology (SPF.SPEC.002, Section 2).

---

## 1. Entity Types

> All entity types used in this Pack: base (from SPF) + extended (defined by this Pack).
> **Mandatory column "FPF/SPF Concept"** — parent concept from SPF base ontology.

| Code | Type | FPF/SPF Concept | Definition | ≠ (what it is NOT) | Source |
|------|------|-----------------|------------|---------------------|--------|
| `M` | Method | U.Method | _TBD_ | ≠ scenario, ≠ tool | SPF (base) |
| `WP` | Work Product | U.Work + U.Episteme | _TBD_ | ≠ method description | SPF (base) |
| `FM` | Failure Mode | — (SPF-specific) | _TBD_ | ≠ code bug | SPF (base) |
| `D` | Distinction | A.7 Strict Distinction | _TBD_ | ≠ fact, ≠ definition | SPF (base) |
| `R` | Role | U.RoleAssignment | _TBD_ | ≠ person, ≠ job title | SPF (base) |
| `CHR` | Characteristic | U.Characteristic | _TBD_ | ≠ metric, ≠ indicator | SPF (base) |
| `SOTA` | SoTA Annotation | — (SPF-specific) | _TBD_ | ≠ literature review | SPF (base) |
| `MAP` | Map | U.Episteme | _TBD_ | ≠ content | SPF (base) |
| _`EXT`_ | _Extended Type_ | _{U.* concept}_ | _TBD_ | _TBD_ | Pack (extended) |

---

## 2. Domain Glossary

> Key domain terms with definitions. Only terms essential for understanding this domain.
> **Mandatory columns:** "Term (RU)" + "Term (EN)" per DDD Ubiquitous Language (SPF.SPEC.002, Rule 11).
> **Mandatory column "Parent Concept (SPF)"** — which universal concept from SPF base ontology this term belongs to.

| Term (RU) | Term (EN) | Definition | Parent Concept (SPF) | Related entity |
|-----------|-----------|-----------|---------------------|----------------|
| _Term 1 (RU)_ | _Term 1_ | _Definition (1-2 sentences)_ | _U.System / U.Method / ..._ | _DOMAIN.XXX.NNN_ |
| _Term 2 (RU)_ | _Term 2_ | _Definition_ | _U.*_ | — |

---

## 3. Relationships Between Types

> How entity types relate to each other in this domain.

| Subject | Relationship | Object | Example |
|---------|-------------|--------|---------|
| Method | produces → | Work Product | _DOMAIN.M.001 → DOMAIN.WP.001_ |
| Failure Mode | violates ← | Method | _DOMAIN.FM.001 ← DOMAIN.M.001_ |
| _Extended type_ | _relationship_ | _type_ | _example_ |

---

## 4. Type Hierarchy (optional)

> If types have subtypes or specializations, document here.

```
Base Type
├── Subtype A
└── Subtype B
```

---

## 5. Cross-Pack Terms (optional)

> Terms shared with or borrowed from other Packs.

| This Pack's term | Related Pack | Term there |
|-----------------|-------------|------------|
| _Term_ | _Pack ID_ | _Term/entity_ |

---

## 6. Abbreviations

> Abbreviations used in this Pack. Inherited abbreviations from upstream (SPF, FPF) are marked accordingly.

| Abbreviation | Full form (RU) | Full form (EN) | Level |
|-------------|---------------|----------------|-------|
| _ABR_ | _Full form (RU)_ | _Full form_ | _SPF / Pack_ |

---

_Ontology per SPF.SPEC.002. Pack ID: [ID]_


# SOURCE_FILE: process/00-process-overview.md
---
# 00. Process Overview

## What This Process Is

This is a **normative process for creating and maintaining SPF packs** — repositories of second-level principles (domain knowledge) built on top of FPF.

| This process is | This process is not |
|-----------------|---------------------|
| Normative (prescribes what must happen) | Advisory (suggests what might help) |
| Activity description | System description |
| Repeatable across domains | Specific to one domain |
| Iterative and continuous | Linear and finite |

---

## Types of Activity Covered

This process covers four types of knowledge work:

| Activity | Description | When Triggered |
|----------|-------------|----------------|
| **Creation** | Building a new pack from scratch | New domain selected |
| **Extension** | Adding new elements (methods, products, failures) | Gap identified in existing pack |
| **Refinement** | Clarifying existing elements | Ambiguity or confusion observed |
| **Revision** | Changing status of claims (SoTA updates) | Evidence changes |

All four activities follow the same process stages; they differ in entry point and scope.

---

## Why the Process Does Not Start with Information

Common mistake: "We have sources/books/articles, let's extract knowledge."

This fails because:

| Starting Point | Problem |
|----------------|---------|
| Information (books, articles) | No filter for relevance; everything looks important |
| Practices ("what people do") | Captures habitual action, not principled knowledge |
| Terminology ("key terms") | Terms without distinctions are labels, not concepts |

**Correct starting point**: Distinctions.

Distinctions determine:
- What counts as information (vs. noise)
- What practices are methods (vs. habits)
- What terms are meaningful (vs. jargon)

Without distinctions first, the process has no criteria for selection or rejection.

---

## Process Stages

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  ┌──────────────┐                                           │
│  │ 01. Domain   │                                           │
│  │   Selection  │                                           │
│  └──────┬───────┘                                           │
│         ↓                                                   │
│  ┌──────────────┐                                           │
│  │ 02. Bounded  │                                           │
│  │   Context    │                                           │
│  └──────┬───────┘                                           │
│         ↓                                                   │
│  ┌──────────────┐     ┌──────────────┐                      │
│  │ 03. Distinct-│ ←── │ 11. Review & │ ←─────────┐          │
│  │     ions     │     │   Evolution  │           │          │
│  └──────┬───────┘     └──────────────┘           │          │
│         ↓                    ↑                   │          │
│  ┌──────────────┐            │                   │          │
│  │ 04. Domain   │            │                   │          │
│  │   Entities   │            │                   │          │
│  └──────┬───────┘            │                   │          │
│         ↓                    │                   │          │
│  ┌──────────────┐            │                   │          │
│  │ 05. Info     │            │                   │          │
│  │   Ingestion  │            │                   │          │
│  └──────┬───────┘            │                   │          │
│         ↓                    │                   │          │
│  ┌──────────────┐            │                   │          │
│  │ 06. Analysis │            │                   │          │
│  │   & Formal.  │            │                   │          │
│  └──────┬───────┘            │                   │          │
│         ↓                    │                   │          │
│  ┌──────────────┬──────────────┬──────────────┐  │          │
│  │ 07. Methods  │ 08. Failure  │ 09. SoTA     │  │          │
│  │ & Products   │    Modes     │  Annotation  │  │          │
│  └──────┬───────┴──────┬───────┴──────┬───────┘  │          │
│         └──────────────┼──────────────┘          │          │
│                        ↓                         │          │
│                 ┌──────────────┐                 │          │
│                 │ 10. Map      │─────────────────┘          │
│                 │ Maintenance  │                            │
│                 └──────────────┘                            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Iteration, Not Linearity

The process is **not** "do steps 1-11 once."

| Pattern | Description |
|---------|-------------|
| **Full cycle** | New pack: 01 → 02 → 03 → ... → 11 → 03 → ... |
| **Extension loop** | New method: 05 → 06 → 07 → 10 → (back to 05 or 11) |
| **Refinement loop** | Clarify distinction: 03 → 10 → 11 → 03 |
| **Revision loop** | Update SoTA: 09 → 10 |

Stage 11 (Review & Evolution) always loops back to earlier stages.

---

## Human and AI Collaboration

This process is designed for both human and AI execution.

| Actor | Strengths | Constraints |
|-------|-----------|-------------|
| **Human** | Domain expertise, judgment, novelty detection | Time, consistency, coverage |
| **AI** | Consistency, coverage, pattern matching | Needs explicit criteria, cannot originate distinctions |

**Division of labor**:
- Humans: Originate distinctions, judge correctness, decide SoTA status
- AI: Apply distinctions consistently, identify gaps, maintain structure
- Both: Analysis, formalization, extraction

**AI must not**:
- Invent distinctions without human validation
- Change SoTA status without evidence
- Skip process stages

---

## Entry Points by Activity Type

| Activity | Entry Stage | Rationale |
|----------|-------------|-----------|
| New pack | 01 | Must establish domain and context first |
| New method (same domain) | 05 or 06 | Distinctions exist; need information |
| New failure mode | 06 | Emerges from analysis |
| SoTA update | 09 | Evidence changed |
| Distinction refinement | 03 | Confusion identified |
| Structural change | 02 | Boundaries changed |

---

## Work Products by Stage

| Stage | Primary Work Product |
|-------|---------------------|
| 01 | Domain name and boundary statement |
| 02 | `00-pack-manifest.md` with bounded context |
| 03 | `01-domain-contract/01B-distinctions.md` entries |
| 04 | `02-domain-entities/` files |
| 05 | Ingestion log (not in pack) |
| 06 | Candidate list (not in pack) |
| 07 | `03-methods/` and `04-work-products/` files |
| 08 | `05-failure-modes/` files |
| 09 | `06-sota/` files |
| 10 | `07-map/` files |
| 11 | Review log, change decisions |


# SOURCE_FILE: process/01-domain-selection.md
---
# 01. Domain Selection

## Purpose

Establish what domain the pack will cover before any content is created. A domain is not a topic, keyword, or area of interest — it is a bounded field of practice with identifiable practitioners, methods, and work products.

---

## When This Stage Occurs

| Trigger | Action |
|---------|--------|
| New pack creation | Mandatory first stage |
| Scope expansion of existing pack | Return to this stage |
| Domain split (pack becomes too broad) | New selection for sub-domain |

---

## Inputs

| Input | Source | Required |
|-------|--------|----------|
| Intent to create pack | Stakeholder decision | Yes |
| Candidate domain name | Initial proposal | Yes |
| Preliminary understanding of field | General knowledge | Yes |

---

## Activity

### 1. Articulate Domain, Not Topic

| Domain | Topic (incorrect framing) |
|--------|--------------------------|
| Personal Development | Self-improvement tips |
| Software Engineering | Programming languages |
| Medical Diagnosis | Diseases |
| Project Management | Deadlines |

A domain has:
- Practitioners (who does this?)
- Methods (how do they act?)
- Work products (what do they produce?)
- Failure modes (how does it go wrong?)

A topic lacks these structural elements.

### 2. Identify Domain Boundaries

What is inside vs. outside this domain?

| Inside | Outside |
|--------|---------|
| Core methods of the field | Adjacent fields |
| Primary practitioners | Consumers of outputs |
| Direct work products | Downstream uses |

### 3. Check for Prior Art

| Check | Why |
|-------|-----|
| Existing SPF packs | Avoid duplication, identify interfaces |
| FPF distinctions | Ensure compatibility |
| Established domain boundaries | Respect existing conventions |

### 4. Name the Domain

The name must be:
- Specific enough to exclude adjacent fields
- General enough to include core methods
- Recognizable to practitioners

---

## Output: Work Product

**Domain Selection Statement** (informal, not a pack file yet)

```
Domain: [Name]
Scope: [What is included]
Exclusions: [What is explicitly outside]
Practitioners: [Who operates in this domain]
Adjacent domains: [Related but separate fields]
```

This statement becomes input to Stage 02 (Bounded Context).

---

## Completion Criteria

| Criterion | Test |
|-----------|------|
| Domain is nameable | One or two word name exists |
| Boundaries are articulable | Can list what is in/out |
| Practitioners exist | Can identify who does this work |
| Not a topic | Can identify methods, not just subjects |
| Not too broad | One pack can cover it |
| Not too narrow | Worth creating a pack |

---

## Typical Errors

### E1. Domain Is Too Broad

**Symptom**: "The domain is Management" or "The domain is Science"

**Problem**: No single pack can cover the breadth; distinctions will be too abstract to be useful.

**Correction**: Subdivide until practitioners are identifiable. "Project Management" or "Experimental Design" are tighter.

### E2. Domain Is a Topic, Not a Practice Field

**Symptom**: "The domain is Happiness" or "The domain is Technology"

**Problem**: No methods, no practitioners, no work products — just a subject.

**Correction**: Find the practice. "Positive Psychology Practice" or "Software Development" have structure.

### E3. Domain Is a Method, Not a Field

**Symptom**: "The domain is Agile" or "The domain is Time Accounting"

**Problem**: A method is inside a domain, not a domain itself.

**Correction**: Identify the containing domain. "Project Management" contains Agile; "Personal Development" contains Time Accounting.

### E4. Domain Boundaries Are Vague

**Symptom**: Cannot answer "Is X inside or outside?"

**Problem**: Distinctions will be arbitrary; methods will overlap with other packs.

**Correction**: Make explicit boundary decisions before proceeding.

### E5. Skipping to Content

**Symptom**: "We already know the methods, let's just document them"

**Problem**: Without domain selection, there is no criterion for what methods belong.

**Correction**: Complete this stage even if it feels obvious.

---

## Transition to Next Stage

When Domain Selection is complete:
- Domain name is fixed
- Boundaries are articulated
- Practitioners are identified

Proceed to [02. Bounded Context](02-bounded-context.md) to formalize these decisions into a pack manifest.


# SOURCE_FILE: process/02-bounded-context.md
---
# 02. Bounded Context

## Purpose

Formalize the domain boundaries into a stable reference that governs all subsequent work. Without a bounded context, the pack will accumulate content without coherence — distinctions from one domain, methods from another, failure modes from a third.

---

## Why Bounded Context Is Mandatory

| Without Bounded Context | With Bounded Context |
|------------------------|---------------------|
| Distinctions drift | Distinctions stay relevant |
| Methods imported from adjacent fields | Methods belong to this domain |
| Scope creep | Clear inclusion/exclusion |
| No criterion for "done" | Completeness is assessable |

A bounded context answers: **"What is this pack about, and what is it not about?"**

---

## Inputs

| Input | Source | Required |
|-------|--------|----------|
| Domain Selection Statement | Stage 01 | Yes |
| FPF edition reference | FPF repository | Yes |
| Related pack boundaries (if any) | Other SPF packs | If they exist |

---

## Activity

### 1. Create Pack Manifest

File: `/pack/<domain>/00-pack-manifest.md`

Required sections:

| Section | Content |
|---------|---------|
| **pack_id** | Short code (e.g., `PD`, `MGMT`) |
| **pack_name** | Full domain name |
| **version** | Semantic version |
| **fpf_edition** | Which FPF version this pack uses |
| **status** | `draft` / `active` / `deprecated` |

### 2. Define Scope Explicitly

In the manifest, specify:

| Field | Example |
|-------|---------|
| What this pack covers | "Methods for individual development of skills, capabilities, character" |
| What this pack does NOT cover | "Team development, organizational change, therapy" |
| Primary practitioners | "Agent (individual developing), Mentor, Coach" |
| Excluded practitioners | "Therapist, HR manager, Team lead" |

### 3. Identify FPF Dependencies

List which FPF distinctions this pack relies on:

| FPF Distinction | How Used |
|-----------------|----------|
| method vs. tool | All method cards |
| role vs. person | Role definitions |
| work product vs. description | WP definitions |

### 4. Declare Related Packs

| Pack | Relationship |
|------|--------------|
| Adjacent pack X | "Shares distinction Y; does not overlap in methods" |
| Parent pack (if hierarchical) | "This pack is a sub-domain of..." |

---

## Output: Work Product

**Primary**: `/pack/<domain>/00-pack-manifest.md` (created or updated)

The manifest is the authoritative bounded context. All subsequent work must be consistent with it.

---

## Completion Criteria

| Criterion | Test |
|-----------|------|
| Manifest file exists | File at expected path |
| Scope is explicit | "Covers" and "Does not cover" sections filled |
| FPF dependencies listed | At least basic distinctions referenced |
| Status is set | Not blank |
| Practitioners identified | At least one role type named |

---

## Typical Errors

### E1. Manifest Is Empty Formality

**Symptom**: Manifest created but never referenced; content added without checking scope.

**Problem**: Bounded context exists in name only.

**Correction**: Require explicit scope check before adding any method/WP/FM.

### E2. Scope Is Aspirational, Not Actual

**Symptom**: Manifest says "covers all of personal development" but pack only has time management methods.

**Problem**: Mismatch between claimed and actual scope.

**Correction**: Scope should reflect current content OR explicitly mark uncovered areas as "planned."

### E3. Boundaries Not Enforced

**Symptom**: Methods from adjacent domains creep in ("this is kind of related").

**Problem**: Pack becomes incoherent; distinctions stop working.

**Correction**: Every addition must pass: "Is this inside the bounded context?"

### E4. No FPF Alignment

**Symptom**: Pack uses terms inconsistently with FPF (e.g., calls tools "methods").

**Problem**: Pack will conflict with other SPF packs and FPF.

**Correction**: List FPF dependencies explicitly; ensure definitions align.

### E5. Skipping to Distinctions

**Symptom**: "Bounded context is obvious, let's write distinctions."

**Problem**: "Obvious" boundaries are often wrong; implicit assumptions cause problems later.

**Correction**: Make the manifest explicit before proceeding.

---

## Bounded Context vs. Domain Selection

| Stage 01: Domain Selection | Stage 02: Bounded Context |
|---------------------------|--------------------------|
| Informal statement | Formal manifest file |
| "What domain?" | "What exactly is in/out?" |
| Can be revised | Revisions require process return |
| Not in pack | In pack as `00-pack-manifest.md` |

---

## Transition to Next Stage

When Bounded Context is complete:
- Manifest file exists in `/pack/<domain>/`
- Scope is explicit and testable
- FPF dependencies are listed

Proceed to [03. Distinctions Work](03-distinctions-work.md) to establish the conceptual vocabulary.


# SOURCE_FILE: process/03-distinctions-work.md
---
# 03. Distinctions Work

## Purpose

Establish the conceptual vocabulary that structures all subsequent work. Distinctions are not definitions or glossary entries — they are **conceptual cuts that separate things that must not be confused**.

Without distinctions:
- Methods cannot be identified (what is a method vs. a habit?)
- Products cannot be specified (what is a product vs. a description?)
- Failure modes cannot be typed (what kind of error is this?)

---

## Why Distinctions Come First

| If distinctions come after | Result |
|---------------------------|--------|
| After methods | Methods lack criteria; anything is a "method" |
| After information | Information overwhelms; no filter |
| After products | Products are confused with descriptions |
| Never | Pack is a list of terms, not structured knowledge |

**Distinctions are the filter** that makes later stages possible.

---

## Inputs

| Input | Source | Required |
|-------|--------|----------|
| Bounded context | Stage 02 manifest | Yes |
| FPF distinction patterns | FPF documentation | Yes |
| Domain expertise | Practitioners, literature | Yes |

---

## Activity

### 1. Import FPF Distinctions

Every pack inherits core FPF distinctions:

| FPF Distinction | Apply to Domain As |
|-----------------|-------------------|
| method vs. tool | Methods are ways of acting; tools support them |
| role vs. person | Roles are functional positions |
| work product vs. description | Products are artifacts, not narratives |
| system vs. process | Do not conflate |

These are not optional. Document how each applies to this domain.

### 2. Identify Domain-Specific Distinctions

Ask: **"What do practitioners in this domain confuse that must not be confused?"**

| Source of Distinctions | How to Find |
|-----------------------|-------------|
| Common errors | What mistakes do beginners make? |
| Expert vs. novice | What do experts separate that novices conflate? |
| Adjacent domains | What does this domain call X while another calls Y? |
| Failed practices | What confusion caused the failure? |

### 3. Formulate Each Distinction

A distinction is NOT:
- A definition ("X is...")
- A synonym list ("X is also called Y")
- A taxonomy ("X has subtypes A, B, C")

A distinction IS:
- A contrast ("X vs. Y")
- A test ("How to tell X from Y")
- A consequence ("Confusing them causes...")

### 4. Document Distinction Entry

For each distinction in `01-domain-contract/01B-distinctions.md`:

```markdown
## [D.NNN] X vs. Y

**Definition**: X is... Y is...

**Distinction Test**: [How to tell them apart]

| X | vs. | Y |
|---|-----|---|
| Property A | | Property A' |
| Property B | | Property B' |

**Typical Confusion**: [What conflation looks like]

**Why It Matters**: [Consequence of confusion]

**Related Items**: [Links to methods, failure modes]

**SoTA**: current | deprecated-interpretation | hypothesis
- Revision criterion: [What would change this]
```

### 5. Link Distinctions to Failure Modes

Every distinction implies potential failure modes:

| Distinction | Implied Failure Mode |
|-------------|---------------------|
| method vs. tool | "Tool confused with method" |
| accounting vs. planning | "Accounting confused with planning" |
| work product vs. description | "Description substituted for product" |

Note these for Stage 08.

---

## Output: Work Product

**Primary**: `/pack/<domain>/01-domain-contract/01B-distinctions.md`

All distinctions in one file with:
- Index table (ID, name, status, related items)
- Full entries for each distinction
- SoTA annotations with revision criteria

---

## Completion Criteria

| Criterion | Test |
|-----------|------|
| FPF distinctions imported | Core FPF distinctions documented for domain |
| Domain distinctions identified | At least 5 domain-specific distinctions |
| Each distinction has test | "How to tell X from Y" is answerable |
| Each distinction has consequence | "Why confusion matters" is specified |
| Failure mode candidates noted | Implied FMs identified (for Stage 08) |
| SoTA status assigned | Each distinction has status + revision criterion |

---

## Typical Errors

### E1. Distinctions Are Definitions

**Symptom**: "Time accounting is the practice of recording time" (no contrast)

**Problem**: Definitions don't prevent confusion; distinctions do.

**Correction**: Always state "X vs. Y" — what is this NOT?

### E2. Distinctions Are Terminology Lists

**Symptom**: List of terms without contrasts or tests.

**Problem**: Terms without distinctions are labels, not concepts.

**Correction**: For each term, identify what it must not be confused with.

### E3. Skipping to Methods

**Symptom**: "We know the methods, let's skip distinctions."

**Problem**: Methods will be poorly bounded; tool/method confusion will occur.

**Correction**: Complete distinctions before methods. If methods are "known," use them to derive distinctions.

### E4. Distinctions Without Tests

**Symptom**: "Method is different from tool" but no way to tell which is which.

**Problem**: Distinction exists in theory but cannot be applied.

**Correction**: Every distinction needs an operational test.

### E5. Missing Failure Mode Links

**Symptom**: Distinction documented but no corresponding failure mode.

**Problem**: The confusion the distinction prevents is not formalized.

**Correction**: For each distinction, create or reference a failure mode.

### E6. FPF Contradictions

**Symptom**: Domain distinction uses "method" differently than FPF.

**Problem**: Pack will be inconsistent with other packs.

**Correction**: Align with FPF or explicitly note the extension.

---

## Distinctions vs. Later Stages

| Stage | Relationship to Distinctions |
|-------|------------------------------|
| 04 Domain Entities | Entities are identified using distinctions |
| 05 Information Ingestion | Distinctions filter relevant information |
| 06 Analysis | Distinctions are the analytical lens |
| 07 Method Extraction | Distinctions define what counts as a method |
| 08 Failure Modes | Each distinction implies potential failures |

---

## Transition to Next Stage

When Distinctions Work is complete:
- `01-domain-contract/01B-distinctions.md` exists with indexed entries
- FPF distinctions are domain-applied
- Domain-specific distinctions are formulated with tests
- Failure mode candidates are noted

Proceed to [04. Domain Entities Identification](04-domain-entities-identification.md) to identify stable structures.


# SOURCE_FILE: process/04-domain-entities-identification.md
---
# 04. Domain Entities Identification

## Purpose

Identify the stable structural elements of the domain: roles, objects of attention, constraints, and relationships. These entities exist regardless of which specific methods are used or which specific practitioners operate.

---

## Why Entities, Not Practices

Common mistake: Start with "what people do" (practices).

| Starting with Practices | Starting with Entities |
|------------------------|----------------------|
| Captures current habits | Captures stable structure |
| Changes with trends | Persists across trends |
| Conflates method with tool | Roles and objects are distinct from methods |
| No criterion for completeness | Entities provide framework |

Practices are instances; entities are the types that make practices intelligible.

---

## Inputs

| Input | Source | Required |
|-------|--------|----------|
| Bounded context | Stage 02 | Yes |
| Distinctions | Stage 03 | Yes |
| Domain knowledge | Expertise, literature | Yes |

---

## Activity

### 1. Identify Roles

Roles are **functional positions**, not persons or job titles.

| Role | NOT Role |
|------|----------|
| Agent (who develops) | "John" (person) |
| Mentor (who guides) | "Manager" (job title) |
| Analyst (who reviews) | "The team" (collective) |

For each role:
- What responsibility does this role hold?
- What methods does this role typically perform?
- What products does this role produce or consume?

### 2. Identify Objects of Attention

Objects of attention are **what practitioners attend to** when performing methods.

| Object of Attention | NOT Object |
|--------------------|------------|
| Time allocation | "Life" (too vague) |
| Behavior patterns | "Everything" (no boundary) |
| Skill gaps | "Self" (not operational) |

For each object:
- What is observed or measured?
- Which methods attend to this object?
- What products capture this object?

### 3. Identify Environmental Constraints

Constraints are **conditions that bound practice** in this domain.

| Constraint | Example |
|-----------|---------|
| Resource limits | Time is finite (168 hours/week) |
| Information limits | Cannot observe own cognition directly |
| Role limits | Agent cannot mentor themselves (feedback loop) |

### 4. Document Entity Relationships

Create files in `02-domain-entities/`:

| File | Content |
|------|---------|
| `02A-roles.md` | Role definitions, responsibilities, typical methods |
| `02B-objects-of-attention.md` | Objects, observation criteria, related methods |
| `02C-methods-index.md` | Index of methods (populated in Stage 07) |
| `02D-tools-index.md` | Index of tools (secondary to methods) |

---

## Output: Work Products

| File | Content |
|------|---------|
| `02-domain-entities/02A-roles.md` | Role definitions |
| `02-domain-entities/02B-objects-of-attention.md` | Objects of attention |
| `02-domain-entities/02C-methods-index.md` | Methods index (skeleton) |
| `02-domain-entities/02D-tools-index.md` | Tools index (skeleton) |

---

## Completion Criteria

| Criterion | Test |
|-----------|------|
| Roles identified | At least 2 distinct roles |
| Roles are functional | Each role has responsibility, not just name |
| Objects of attention identified | At least 3 objects |
| Objects are observable | Each has observation criteria |
| Role-method mapping sketched | Which roles perform which method types |
| Entity files created | Files exist in `02-domain-entities/` |

---

## Typical Errors

### E1. Roles Are Persons or Titles

**Symptom**: "Role: Project Manager" or "Role: Senior Developer"

**Problem**: These are job titles or seniority levels, not functional positions.

**Correction**: Ask: What function does this role perform? "Planner" (plans), "Executor" (executes), "Reviewer" (reviews).

### E2. Objects Are Too Abstract

**Symptom**: "Object of attention: Personal growth" or "Object: The self"

**Problem**: Cannot observe or measure; no operational criteria.

**Correction**: What specifically is observed? "Skill level in X," "Time allocation to Y," "Frequency of behavior Z."

### E3. Practices Listed as Entities

**Symptom**: "Entity: Daily standup" or "Entity: Retrospective"

**Problem**: These are practices (things people do), not stable structural elements.

**Correction**: What role performs this? What object does it attend to? Extract the entities.

### E4. Methods Confused with Roles

**Symptom**: "Role: Time Accountant" (method disguised as role)

**Problem**: Time accounting is a method, not a role.

**Correction**: The role is "Agent"; time accounting is a method the Agent may perform.

### E5. Skipping to Information

**Symptom**: "Entities are obvious, let's gather sources."

**Problem**: Without entities, information cannot be filtered or organized.

**Correction**: Complete entity identification; entities determine what information is relevant.

### E6. Missing Role-Method Mapping

**Symptom**: Roles listed but no connection to methods.

**Problem**: Roles without responsibilities are empty labels.

**Correction**: For each role, identify at least one method type it performs.

---

## Entities vs. Methods

| Entity (Stage 04) | Method (Stage 07) |
|-------------------|-------------------|
| Who acts (role) | How they act (method) |
| What is attended to (object) | How it is attended to (method) |
| Structural | Procedural |
| Persists across methods | Method is one way to engage entities |

---

## Transition to Next Stage

When Domain Entities Identification is complete:
- Role definitions exist in `02A-roles.md`
- Objects of attention exist in `02B-objects-of-attention.md`
- Index files are created (to be populated later)
- Role-method mapping is sketched

Proceed to [05. Information Ingestion](05-information-ingestion.md) to admit materials for analysis.


# SOURCE_FILE: process/05-information-ingestion.md
---
# 05. Information Ingestion

## Purpose

Admit materials (sources, experiences, observations) for analysis. Information is the **raw input** to the knowledge-creation process — it is NOT knowledge and does NOT become pack content directly.

---

## Information ≠ Knowledge

| Information | Knowledge |
|-------------|-----------|
| Raw material | Structured understanding |
| Needs analysis | Result of analysis |
| Source-dependent | Source-independent (once validated) |
| May be wrong | Has assigned SoTA status |
| Outside pack | Inside pack |

**Information enters; knowledge is produced.** This stage admits information; Stage 06 transforms it.

---

## Inputs

| Input | Source | Required |
|-------|--------|----------|
| Bounded context | Stage 02 | Yes |
| Distinctions | Stage 03 | Yes |
| Domain entities | Stage 04 | Yes |
| Materials to analyze | Various sources | Yes |

---

## What Counts as Information

| Acceptable Information | How It Enters |
|-----------------------|---------------|
| Published literature (books, papers) | Citation + summary |
| Expert testimony | Attributed claim |
| Observed practice | Documented observation |
| Own experience | Documented experience |
| Existing frameworks | Referenced framework |

| NOT Information (Do Not Admit) | Why |
|-------------------------------|-----|
| Unsourced claims | No traceability |
| Hearsay ("people say...") | No accountability |
| Pure opinion without reasoning | No analysis possible |
| Proprietary content without rights | Legal issues |

---

## Activity

### 1. Identify Candidate Materials

Given the bounded context, what materials might contain relevant knowledge?

| Material Type | Example | Relevance Test |
|--------------|---------|----------------|
| Foundational texts | Lyubishchev's time diaries | Historical origin of method |
| Academic literature | Papers on self-quantification | Research findings |
| Practitioner accounts | Blog posts by practitioners | Experience reports |
| Existing frameworks | GTD, Pomodoro, etc. | Adjacent practices |

### 2. Apply Relevance Filter

Use distinctions and bounded context as filter:

| Filter Question | Action if No |
|----------------|--------------|
| Is this within bounded context? | Exclude |
| Does this relate to identified entities? | Exclude |
| Can this be analyzed through distinctions? | Defer (may need new distinctions) |

### 3. Create Ingestion Log

**Location**: NOT in pack. Ingestion log is process artifact, not knowledge artifact.

For each admitted material:

```
Material: [Title/Description]
Source: [Citation/Reference]
Date ingested: [Date]
Relevance: [Why this material is relevant]
Notes: [Initial observations]
Status: [pending-analysis | analyzed | rejected]
```

### 4. Batch for Analysis

Group materials by:
- Topic area (which entities/methods they might inform)
- Source type (primary vs. secondary)
- Confidence level (peer-reviewed vs. opinion)

---

## Output: Work Products

| Product | Location | Content |
|---------|----------|---------|
| Ingestion log | `/process/working/ingestion-log.md` (not in pack) | List of admitted materials |
| Material summaries | `/process/working/` (not in pack) | Brief summaries for analysis |

**These outputs are NOT pack content.** They are process artifacts.

---

## Completion Criteria

| Criterion | Test |
|-----------|------|
| Materials identified | At least one material per major entity |
| Relevance filtered | Each material passes bounded context test |
| Ingestion log created | Log file exists with entries |
| Materials batched | Grouped for analysis |
| No pack files modified | Information not yet in pack |

---

## Typical Errors

### E1. Information Becomes Pack Content Directly

**Symptom**: Copy-paste from source into `03-methods/` file.

**Problem**: Information is not knowledge; it has not been analyzed, validated, or formalized.

**Correction**: Information goes to ingestion log → Stage 06 analysis → only then to pack.

### E2. No Relevance Filter

**Symptom**: "This is interesting, let's include it" (even if outside scope).

**Problem**: Pack accumulates off-topic content; coherence degrades.

**Correction**: Every material must pass bounded context and entity relevance tests.

### E3. Source Not Recorded

**Symptom**: "I read somewhere that..." (no citation).

**Problem**: Cannot trace claims; cannot validate; cannot update when source updates.

**Correction**: Every material needs attribution before ingestion.

### E4. Ingestion Log in Pack

**Symptom**: `/pack/<domain>/sources.md` with list of materials.

**Problem**: Sources are process artifacts, not knowledge artifacts.

**Correction**: Ingestion log stays in `/process/working/`, not in `/pack/`.

### E5. Skipping to Extraction

**Symptom**: "I know what the methods are, let's just write them."

**Problem**: Methods without information trail are unsupported claims.

**Correction**: Even "known" methods should have information sources documented.

### E6. Information Overload

**Symptom**: Hundreds of materials ingested without batching.

**Problem**: Analysis becomes impossible; paralysis.

**Correction**: Batch by relevance; prioritize foundational materials.

---

## Information Types and Treatment

| Information Type | Treatment | Confidence |
|-----------------|-----------|------------|
| Primary source (original practice) | High priority | High |
| Peer-reviewed research | Analyze claims | Medium-High |
| Practitioner account | Extract experience, verify | Medium |
| Popular literature | Extract claims, high scrutiny | Low-Medium |
| Opinion/Blog | Use only if corroborated | Low |

---

## Transition to Next Stage

When Information Ingestion is complete:
- Ingestion log exists with attributed materials
- Materials are filtered for relevance
- Materials are batched for analysis
- No pack files have been modified

Proceed to [06. Analysis and Formalization](06-analysis-and-formalization.md) to transform information into candidates.


# SOURCE_FILE: process/06-analysis-and-formalization.md
---
# 06. Analysis and Formalization

## Purpose

Transform ingested information into **candidates** for pack content by applying distinctions systematically. Analysis separates signal from noise; formalization structures candidates for extraction.

---

## Why Analysis Cannot Be Skipped

| Without Analysis | With Analysis |
|-----------------|---------------|
| Source text copied | Source claims examined |
| Author's framing preserved | Domain framing applied |
| Implicit assumptions inherited | Assumptions made explicit |
| Terminology mixed | Distinctions applied |

Analysis is the act of **applying distinctions to information**. Without it, information remains external opinion, not domain knowledge.

---

## Inputs

| Input | Source | Required |
|-------|--------|----------|
| Ingestion log | Stage 05 | Yes |
| Distinctions | Stage 03 | Yes |
| Domain entities | Stage 04 | Yes |
| Materials | Stage 05 batches | Yes |

---

## Activity

### 1. Apply Distinctions to Each Material

For each ingested material, ask:

| Distinction | Question |
|-------------|----------|
| method vs. tool | Does this describe a way of acting or an artifact? |
| role vs. person | Does this describe a function or an individual? |
| work product vs. description | Does this identify an artifact or narrate about one? |
| actual vs. intended | Does this describe what happened or what should happen? |
| observation vs. judgment | Does this record facts or evaluate them? |

Document which distinctions apply and what the material says when viewed through each.

### 2. Identify Candidates

Through distinction-based analysis, identify:

| Candidate Type | How Identified |
|----------------|----------------|
| Method candidate | Source describes repeatable way of acting with inputs/outputs |
| Work product candidate | Source describes observable artifact with criteria |
| Failure mode candidate | Source describes confusion, error, or anti-pattern |
| Distinction candidate | Source reveals contrast that must not be conflated |
| SoTA update candidate | Source provides evidence for status change |

### 3. Check Against Existing Pack Content

| Question | Action if Yes |
|----------|--------------|
| Does this method already exist? | Update existing, not duplicate |
| Does this distinction already exist? | Refine or extend existing |
| Does this contradict existing content? | Flag for resolution |
| Does this extend existing content? | Note the extension |

### 4. Formalize Candidates

For each candidate, create a structured entry:

**Method Candidate**:
```
Candidate ID: [temp ID]
Type: method
Source: [citation]
Name: [proposed name]
Definition: [what it is]
Inputs: [what it takes]
Outputs: [what it produces]
Distinctions applied: [which distinctions structure this]
Open questions: [what needs clarification]
Status: pending-extraction | ready | rejected
```

**Work Product Candidate**:
```
Candidate ID: [temp ID]
Type: work-product
Source: [citation]
Name: [proposed name]
Definition: [what it is]
Observability criteria: [how to verify it exists]
Produced by: [which method]
Open questions: [what needs clarification]
Status: pending-extraction | ready | rejected
```

**Failure Mode Candidate**:
```
Candidate ID: [temp ID]
Type: failure-mode
Source: [citation]
Name: [proposed name]
Error type: [ontological | methodological | role | deprecated-interpretation]
Distinction violated: [which distinction]
Symptoms: [how it manifests]
Open questions: [what needs clarification]
Status: pending-extraction | ready | rejected
```

### 5. Do NOT Copy Source Text

| Forbidden | Required |
|-----------|----------|
| "According to Smith, the method is..." | "The method produces X by doing Y" (domain terms) |
| Quoting source's framing | Using pack's distinctions |
| Preserving source's terminology | Mapping to domain terminology |

The pack is not a collection of citations. It is domain knowledge expressed through domain distinctions.

---

## Output: Work Products

| Product | Location | Content |
|---------|----------|---------|
| Analysis notes | `/process/working/` (not in pack) | Distinction application notes |
| Candidate list | `/process/working/candidates.md` | Formalized candidates |

**These outputs are NOT pack content.** They are inputs to extraction stages.

---

## Completion Criteria

| Criterion | Test |
|-----------|------|
| Materials analyzed | Each ingested material has analysis notes |
| Distinctions applied | Each analysis references specific distinctions |
| Candidates identified | At least one candidate of each relevant type |
| Candidates formalized | Each candidate has structured entry |
| No source text copied | Pack-language used, not source-language |
| Open questions noted | Uncertainties are explicit |

---

## Typical Errors

### E1. Copying Source Text

**Symptom**: Pack file contains phrases from source materials.

**Problem**: Source's framing is preserved; distinctions not applied.

**Correction**: Express everything in domain terms through domain distinctions.

### E2. Analysis Without Distinctions

**Symptom**: "This looks like a method" (intuition only).

**Problem**: No criterion for identification; inconsistent results.

**Correction**: Explicitly apply method vs. tool distinction (and others).

### E3. Creating Duplicates

**Symptom**: "New method" that overlaps substantially with existing method.

**Problem**: Pack becomes redundant; relationships unclear.

**Correction**: Always check existing content before creating new.

### E4. Skipping Formalization

**Symptom**: "I know what this should be" → jumps to pack file.

**Problem**: Candidate not vetted; may be incomplete or wrong.

**Correction**: Formalize candidate first; extract only "ready" candidates.

### E5. Preserving Source's Errors

**Symptom**: Source confuses method and tool; pack inherits confusion.

**Problem**: Pack reproduces errors instead of correcting them.

**Correction**: Apply distinctions to detect and correct source errors.

### E6. Over-Analysis

**Symptom**: Endless analysis without producing candidates.

**Problem**: Analysis becomes academic exercise, not production process.

**Correction**: Time-box analysis; produce candidates even if imperfect.

---

## Analysis vs. Extraction

| Analysis (Stage 06) | Extraction (Stages 07-08) |
|--------------------|--------------------------|
| Produces candidates | Produces pack files |
| Applies distinctions | Uses formalized candidates |
| In working directory | In pack directory |
| Can be revised freely | Changes require process |

---

## Transition to Next Stage

When Analysis and Formalization is complete:
- Materials are analyzed through distinctions
- Candidates are formalized with structured entries
- Candidates have status (pending/ready/rejected)
- Open questions are documented

Proceed to:
- [07. Method and Product Extraction](07-method-and-product-extraction.md) for method/product candidates
- [08. Failure Modes Extraction](08-failure-modes-extraction.md) for failure mode candidates


# SOURCE_FILE: process/07-method-and-product-extraction.md
---
# 07. Method and Product Extraction

## Purpose

Transform "ready" candidates into pack files. This is the stage where analyzed knowledge becomes formal pack content. Methods and work products are extracted together because they are tightly coupled: methods produce products.

---

## When a Candidate Becomes a Method

A candidate is a **method** (not a scenario, habit, or tool) when:

| Criterion | Test |
|-----------|------|
| Repeatable | Can be performed again by same or different agent |
| Describable | Can be specified without reference to specific instance |
| Has inputs | Something is required to begin |
| Has outputs | Something is produced upon completion |
| Not tool-dependent | Method persists across tool changes |
| Not scenario | Describes "what and why," not "do this then that" |

### Method vs. Scenario

| Method | Scenario |
|--------|----------|
| "Time accounting registers time expenditures by category" | "Start your day by opening Toggl and clicking..." |
| What it is | How to do it (one way) |
| Inputs/outputs | Steps/instructions |
| Belongs in pack | Belongs downstream |

**If it has numbered steps, it is probably a scenario, not a method.**

---

## Inputs

| Input | Source | Required |
|-------|--------|----------|
| Ready candidates | Stage 06 | Yes |
| Distinctions | Stage 03 | Yes |
| Domain entities | Stage 04 | Yes |
| Method template | `/pack/_template/03-methods/` | Yes |
| Work product template | `/pack/_template/04-work-products/` | Yes |

---

## Activity

### 1. Select Ready Candidates

From Stage 06 candidate list, select candidates with:
- Status: `ready`
- Type: `method` or `work-product`
- Open questions: resolved or non-blocking

### 2. Assign Stable ID

| Item | Pattern | Example |
|------|---------|---------|
| Method | `<DOMAIN>.METHOD.<NNN>` | `PD.METHOD.001` |
| Work Product | `<DOMAIN>.WP.<NNN>` | `PD.WP.001` |

IDs are:
- Unique (never reused)
- Sequential within type
- Stable (never changed once assigned)

### 3. Create Method Card

File: `/pack/<domain>/03-methods/<ID>-<name>.md`

Required sections:

| Section | Content |
|---------|---------|
| YAML frontmatter | id, name, status, dates |
| Definition | What the method is (not how to do it) |
| Purpose | What function it serves |
| Inputs | What is required |
| Outputs | What is produced (link to WP) |
| Applicability | When to use, when not to use |
| Related distinctions | Which distinctions structure this method |
| Failure modes | Which failures relate to this method |
| SoTA | Status and revision criterion |

### 4. Create Work Product Card

File: `/pack/<domain>/04-work-products/<ID>-<name>.md`

Required sections:

| Section | Content |
|---------|---------|
| YAML frontmatter | id, name, status, dates |
| Definition | What the product is |
| Purpose | What function it serves |
| Produced by | Which method creates it |
| Consumed by | Which roles/methods use it |
| Existence criteria | How to verify it exists |
| Quality criteria | How to assess adequacy |
| Anti-patterns | What this product is NOT |

### 5. Update Indexes

Update `/pack/<domain>/02-domain-entities/02C-methods-index.md`:
- Add row for new method
- Include ID, name, produces, prerequisites

### 6. Cross-Reference

Ensure bidirectional links:
- Method → Work Product (outputs)
- Work Product → Method (produced by)
- Method → Failure Modes (references)
- Method → Distinctions (uses)

---

## Output: Work Products

| Product | Location |
|---------|----------|
| Method card(s) | `/pack/<domain>/03-methods/` |
| Work product card(s) | `/pack/<domain>/04-work-products/` |
| Updated methods index | `/pack/<domain>/02-domain-entities/02C-methods-index.md` |

---

## Completion Criteria

| Criterion | Test |
|-----------|------|
| Method is not scenario | No numbered steps; describes what, not how |
| Method has inputs/outputs | Both sections filled |
| Work product is observable | Existence criteria specified |
| IDs assigned correctly | Follows naming convention |
| Index updated | New entries in methods index |
| Cross-references valid | All links resolve |
| SoTA assigned | Status and revision criterion present |

---

## Typical Errors

### E1. Method Is Actually a Scenario

**Symptom**: "Step 1: Open your tracker. Step 2: Record the activity..."

**Problem**: This is a scenario (how-to), not a method (what-is).

**Correction**: Remove steps; describe what the method achieves and requires.

### E2. Method Is Actually a Tool

**Symptom**: "Method: Toggl" or "Method: Pomodoro Timer"

**Problem**: Tools are artifacts; methods are ways of acting.

**Correction**: What method does the tool support? Document that method.

### E3. Work Product Is a Description

**Symptom**: "The work product is a sense of accomplishment."

**Problem**: Cannot observe "sense"; it's a feeling, not an artifact.

**Correction**: What artifact exists? What can be shown to another person?

### E4. Missing Existence Criteria

**Symptom**: Work product defined but no way to verify it exists.

**Problem**: Cannot distinguish having the product from describing it.

**Correction**: Add "Existence criteria: How to verify this artifact exists."

### E5. No Cross-References

**Symptom**: Method and work product created but not linked.

**Problem**: Relationships invisible; navigation broken.

**Correction**: Add bidirectional links; check that all resolve.

### E6. Copying Candidate Text

**Symptom**: Pack file contains same text as candidate formalization.

**Problem**: Candidate formalization is draft; pack file should be refined.

**Correction**: Rewrite for pack; ensure template compliance.

### E7. Skipping Index Update

**Symptom**: Method exists but not in methods index.

**Problem**: Method undiscoverable; map will be incomplete.

**Correction**: Always update index when creating method.

---

## Method Extraction Checklist

Before committing a new method:

- [ ] Definition describes what, not how
- [ ] No numbered steps (not a scenario)
- [ ] Inputs specified
- [ ] Outputs specified (linked to WP)
- [ ] Applicability boundaries stated
- [ ] At least one related distinction linked
- [ ] Failure modes referenced
- [ ] SoTA status with revision criterion
- [ ] ID follows convention
- [ ] Index updated

---

## Transition to Next Stage

When Method and Product Extraction is complete:
- Method cards exist in `03-methods/`
- Work product cards exist in `04-work-products/`
- Methods index is updated
- Cross-references are valid

Proceed to:
- [08. Failure Modes Extraction](08-failure-modes-extraction.md) for failure mode candidates
- [10. Map Maintenance](10-map-maintenance.md) to update navigation (mandatory)


# SOURCE_FILE: process/08-failure-modes-extraction.md
---
# 08. Failure Modes Extraction

## Purpose

Extract and formalize failure modes as **first-class pack content**. Failure modes are not secondary documentation — they are essential knowledge about how domain practice goes wrong. A pack without failure modes is incomplete.

---

## Why Failure Modes Are First-Class

| Without Failure Modes | With Failure Modes |
|----------------------|-------------------|
| Only "correct" knowledge | Complete domain understanding |
| Errors unnamed | Errors identifiable and diagnosable |
| Confusion persists | Confusion has remediation path |
| Knowledge is theoretical | Knowledge is operational |

Every distinction implies at least one failure mode (the confusion it prevents). Every method has failure modes (ways it can be performed incorrectly or misunderstood).

---

## Failure Mode Types

| Type | Definition | Example |
|------|------------|---------|
| **Ontological** | Confusing two types of things | Tool confused with method |
| **Methodological** | Performing a method incorrectly | Accounting treated as planning |
| **Role** | Role missing or misassigned | No Agent performing the method |
| **Deprecated interpretation** | Using outdated understanding | Treating accounting as productivity hack |
| **Work product** | Product missing or malformed | Description substituted for artifact |

---

## Inputs

| Input | Source | Required |
|-------|--------|----------|
| Failure mode candidates | Stage 06 | Yes |
| Distinctions | Stage 03 | Yes |
| Methods | Stage 07 | Yes |
| Failure mode template | `/pack/_template/05-failure-modes/` | Yes |

---

## Activity

### 1. Source Failure Mode Candidates

Failure modes come from:

| Source | How |
|--------|-----|
| Distinctions | Each distinction implies confusion that can occur |
| Methods | Each method can be misperformed or misunderstood |
| Information analysis | Sources describe errors, anti-patterns |
| Experience | Observed failures in practice |

### 2. Type Each Failure Mode

Assign a type from the taxonomy:

| Type | Test |
|------|------|
| Ontological | Does this confuse two types of entities? |
| Methodological | Does this describe incorrect method execution? |
| Role | Does this describe missing or wrong role? |
| Deprecated interpretation | Does this describe outdated but persistent understanding? |
| Work product | Does this describe missing or malformed artifact? |

### 3. Assign Stable ID

| Item | Pattern | Example |
|------|---------|---------|
| Failure Mode | `<DOMAIN>.FAIL.<NNN>` | `PD.FAIL.001` |

### 4. Create Failure Mode Card

File: `/pack/<domain>/05-failure-modes/<ID>-<name>.md`

Required sections:

| Section | Content |
|---------|---------|
| YAML frontmatter | id, name, type, severity, status, dates |
| Definition | What the failure mode is |
| Error type | Ontological, methodological, etc. |
| Detection test | How to recognize this error in speech/text/behavior |
| Why it is an error | What makes this wrong (reference distinction) |
| Correct understanding | What should be understood instead |
| Risk/harm | Consequences if not corrected |
| Related items | Links to distinctions, methods, products |
| Detection methods | How to identify early |

### 5. Link to Distinctions

Every failure mode should reference the distinction it violates:

| Failure Mode | Violates Distinction |
|--------------|---------------------|
| Tool confused with method | D.001 Method vs. Tool |
| Work product confused with description | D.005 Work Product vs. Description |
| Accounting treated as planning | D.003 Accounting vs. Planning |

### 6. Cross-Reference

Ensure bidirectional links:
- Failure Mode → Distinction (violates)
- Failure Mode → Method (affects)
- Failure Mode → Work Product (affects)
- Distinction → Failure Mode (implied by)
- Method → Failure Mode (has failure modes)

---

## Output: Work Products

| Product | Location |
|---------|----------|
| Failure mode card(s) | `/pack/<domain>/05-failure-modes/` |
| Updated cross-references | In linked files |

---

## Completion Criteria

| Criterion | Test |
|-----------|------|
| Type assigned | Error type is explicit |
| Detection test exists | Can identify this error in practice |
| Distinction linked | References violated distinction |
| Consequence stated | Risk/harm is specified |
| ID follows convention | `<DOMAIN>.FAIL.<NNN>` |
| Cross-references valid | All links resolve |

---

## Typical Errors

### E1. Failure Mode Is Too Vague

**Symptom**: "Failure mode: Doing it wrong"

**Problem**: No detection criteria; cannot identify in practice.

**Correction**: Specify how this manifests in speech, text, or behavior.

### E2. Failure Mode Has No Distinction Link

**Symptom**: Failure mode described but no underlying confusion identified.

**Problem**: Root cause unclear; remediation impossible.

**Correction**: What distinction does this violate? Link it.

### E3. Missing Detection Test

**Symptom**: Failure mode defined but no way to recognize it.

**Problem**: Cannot diagnose; error goes unnoticed.

**Correction**: Add detection test: "This error manifests when..."

### E4. Failure Modes Not First-Class

**Symptom**: Failure modes mentioned in method cards but no separate files.

**Problem**: Cannot navigate to failure modes; cannot cross-reference.

**Correction**: Create dedicated failure mode cards.

### E5. No Severity Assessment

**Symptom**: All failure modes treated equally.

**Problem**: Cannot prioritize correction.

**Correction**: Assign severity: critical / major / minor.

### E6. Copying Instead of Formalizing

**Symptom**: Failure mode description copied from source.

**Problem**: Source's framing preserved; distinctions not applied.

**Correction**: Express in domain terms through domain distinctions.

---

## Failure Mode Extraction Checklist

Before committing a new failure mode:

- [ ] Definition is specific and testable
- [ ] Error type assigned (ontological/methodological/etc.)
- [ ] Detection test specifies observable symptoms
- [ ] Distinction link present
- [ ] Correct understanding stated
- [ ] Risk/harm documented
- [ ] Related methods/products linked
- [ ] Severity assigned
- [ ] ID follows convention
- [ ] Cross-references valid

---

## Failure Modes and Distinctions

For every distinction D, there should be at least one failure mode FM:

| Distinction | Implied Failure Mode |
|-------------|---------------------|
| D.001 Method vs. Tool | FM: Tool confused with method |
| D.003 Accounting vs. Planning | FM: Accounting confused with planning |
| D.005 Work Product vs. Description | FM: Description substituted for product |
| D.009 Registration vs. Intervention | FM: Registration expected to cause change |

If a distinction lacks a corresponding failure mode, either:
- The failure mode should be created
- The distinction is not operationally important (reconsider)

---

## Transition to Next Stage

When Failure Modes Extraction is complete:
- Failure mode cards exist in `05-failure-modes/`
- Each failure mode has type, detection test, distinction link
- Cross-references are valid

Proceed to:
- [09. SoTA Annotation](09-sota-annotation.md) for SoTA status assignment
- [10. Map Maintenance](10-map-maintenance.md) to update navigation (mandatory)


# SOURCE_FILE: process/09-sota-annotation.md
---
# 09. SoTA Annotation

> **FPF Reference:** Part G (SoTA Kit), particularly G.2 (SoTA-packs) and G.4 (TraditionCards, OperatorCards)
> Full specification: `~/IWE/FPF/FPF-Spec.md`

## Purpose

Assign and maintain state-of-the-art (SoTA) status for claims, distinctions, and methods. SoTA in SPF is NOT a literature review — it is a **status attribute** that tracks whether understanding is current, outdated, or hypothetical.

**Relationship to FPF:** FPF Part G defines a detailed SoTA Kit with TraditionCards, OperatorCards and selector-ready portfolios. SPF uses a simplified version sufficient for most Packs. For deeper SoTA work, see FPF Part G.

---

## What SoTA Is and Is Not

| SoTA IS | SoTA IS NOT |
|---------|-------------|
| Status of a claim | Literature review |
| Attribute attached to content | Separate "research" section |
| Tracks currency of understanding | Tracks publication history |
| Has revision criterion | Fixed label |
| Updated when evidence changes | Static once assigned |

---

## SoTA Status Values

| Status | Meaning | When Assigned |
|--------|---------|---------------|
| `current` | Best available understanding | Evidence supports; no superior alternative |
| `deprecated-interpretation` | Previously held; now superseded | Evidence contradicts or better understanding exists |
| `hypothesis` | Proposed but not yet validated | Plausible but awaiting evidence |

---

## Inputs

| Input | Source | Required |
|-------|--------|----------|
| Claims requiring status | Methods, distinctions, assertions | Yes |
| Evidence for status | Analysis, research, practice | Yes |
| SoTA template | `/pack/_template/06-sota/` | Yes |

---

## Activity

### 1. Identify Claims Requiring SoTA

SoTA status applies to:

| Content Type | Example Claim |
|--------------|---------------|
| Methods | "Time accounting is a registration method" |
| Distinctions | "Method and tool are distinct types" |
| Interpretations | "Accounting produces discipline" (deprecated) |
| Mechanisms | "Registration alone does not change behavior" |

### 2. Assess Current Status

For each claim:

| Question | If Yes → Status |
|----------|----------------|
| Is this the best available understanding? | `current` |
| Was this believed but is now superseded? | `deprecated-interpretation` |
| Is this proposed but awaiting validation? | `hypothesis` |

### 3. Define Revision Criterion

Every SoTA status MUST have a revision criterion: **"What evidence would change this status?"**

| Status | Revision Criterion Format |
|--------|--------------------------|
| `current` | "Would change to deprecated if [evidence X]" |
| `deprecated-interpretation` | "Would change to current if [evidence Y]" |
| `hypothesis` | "Would change to current if [evidence Z]; would change to deprecated if [evidence W]" |

### 4. Create or Update SoTA Annotation

**Option A: Inline annotation** (in method/distinction file)
```markdown
**SoTA**: `current`
- Revision criterion: Would change to deprecated-interpretation if evidence shows registration directly causes behavior change without intermediate analysis.
```

**Option B: Standalone SoTA file** (for complex interpretations)

File: `/pack/<domain>/06-sota/<ID>-<name>.md`

| Section | Content |
|---------|---------|
| YAML frontmatter | id, target_type, target_id, dates |
| Target | What claim/method/distinction this annotates |
| Interpretations table | List of interpretations with status |
| Per-interpretation entry | Status, basis, revision criterion |
| Review schedule | When to revisit |

### 5. Assign Stable ID (for standalone files)

| Item | Pattern | Example |
|------|---------|---------|
| SoTA Annotation | `<DOMAIN>.SOTA.<NNN>` | `PD.SOTA.001` |

### 6. Cross-Reference

Link SoTA to target:
- SoTA → Method/Distinction (annotates)
- Method/Distinction → SoTA (has annotation)

---

## Output: Work Products

| Product | Location |
|---------|----------|
| Inline SoTA annotations | In method/distinction files |
| Standalone SoTA files | `/pack/<domain>/06-sota/` |
| Updated cross-references | In linked files |

---

## Completion Criteria

| Criterion | Test |
|-----------|------|
| Status assigned | current / deprecated-interpretation / hypothesis |
| Revision criterion present | "Would change if..." is specified |
| Basis stated | Why this status (briefly) |
| Target linked | What claim/method this annotates |
| Review date set | When to revisit (for standalone files) |

---

## Typical Errors

### E1. SoTA as Literature Review

**Symptom**: Long section citing papers and studies.

**Problem**: SoTA is a status, not a bibliography.

**Correction**: State the status and revision criterion; cite evidence briefly.

### E2. SoTA Without Revision Criterion

**Symptom**: "SoTA: current" with no revision criterion.

**Problem**: Status is unfalsifiable; will never be updated.

**Correction**: Add "Would change to X if Y."

### E3. Deprecated Without Replacement

**Symptom**: "This interpretation is deprecated" but no current interpretation stated.

**Problem**: Reader knows what's wrong but not what's right.

**Correction**: Always state the current understanding alongside deprecated.

### E4. All Hypotheses, No Current

**Symptom**: Everything marked as hypothesis.

**Problem**: Pack provides no confident knowledge.

**Correction**: Some claims should be current (with revision criteria).

### E5. Status Never Updated

**Symptom**: SoTA assigned once and never revisited.

**Problem**: Pack becomes stale; outdated claims remain current.

**Correction**: Set review schedule; actually review.

### E6. Inline vs. Standalone Confusion

**Symptom**: Minor claims get standalone files; major interpretations get inline only.

**Problem**: Inconsistent structure; hard to navigate.

**Correction**: Use standalone for complex interpretations with multiple statuses; inline for simple single-status claims.

---

## SoTA Annotation Checklist

Before committing a SoTA annotation:

- [ ] Status is one of: current / deprecated-interpretation / hypothesis
- [ ] Revision criterion is specific and falsifiable
- [ ] Basis for status is stated
- [ ] Target (what this annotates) is clear
- [ ] For standalone files: review date set
- [ ] Cross-references valid

---

## SoTA Status Transitions

```
               evidence supports
                      ↓
    ┌────────────────────────────────┐
    │                                │
    │    hypothesis ────────────► current
    │        │                       │
    │        │ evidence              │ better
    │        │ contradicts           │ understanding
    │        ↓                       ↓
    │    (rejected) ◄──── deprecated-interpretation
    │                                │
    │                                │ evidence
    │                                │ reinstates
    │                                ↓
    └────────────────────────────► current
```

---

## Transition to Next Stage

When SoTA Annotation is complete:
- Claims have status assigned
- Revision criteria are specified
- For complex interpretations, standalone files exist
- Cross-references are valid

Proceed to [10. Map Maintenance](10-map-maintenance.md) to update navigation (mandatory).


# SOURCE_FILE: process/10-map-maintenance.md
---
# 10. Map Maintenance

## Purpose

Maintain the navigation map that connects all pack content. The map is **mandatory infrastructure** — it is not optional documentation. Every structural change to the pack requires a corresponding map update.

---

## Why Maps Are Mandatory

| Without Map | With Map |
|-------------|----------|
| Content is discoverable only by filename | Content is discoverable by relationship |
| Relationships implicit | Relationships explicit |
| Completeness unknown | Gaps visible |
| Navigation by browsing | Navigation by structure |

The map answers: **"What is in this pack, and how does it connect?"**

---

## When Map Updates Are Required

| Action | Map Update Required |
|--------|-------------------|
| Add method | Yes |
| Add work product | Yes |
| Add failure mode | Yes |
| Add distinction | Yes |
| Add SoTA annotation | Yes |
| Modify relationships | Yes |
| Fix typo in existing file | No |
| Update SoTA status | Yes (if changes relationships) |

**Rule**: If the change affects what exists or how things connect, update the map.

---

## Inputs

| Input | Source | Required |
|-------|--------|----------|
| Current pack content | All pack files | Yes |
| Recent changes | Stages 03-09 | Yes |
| Map template | `/pack/_template/07-map/` | Yes |

---

## Activity

### 1. Identify Map Impact

For each change, determine:

| Question | If Yes |
|----------|--------|
| New item added? | Add to relevant map section |
| Relationship changed? | Update cross-reference matrix |
| Item removed/deprecated? | Mark in map (do not delete) |
| Status changed? | Update status column |

### 2. Update Map File

File: `/pack/<domain>/07-map/PD.MAP.001.md` (or similar)

Required sections to check:

| Section | Update If |
|---------|-----------|
| Pack Status | Item counts change |
| Distinctions table | Distinction added/changed |
| Roles table | Role added/changed |
| Objects of Attention table | Object added/changed |
| Methods table | Method added/changed |
| Work Products table | Product added/changed |
| Failure Modes table | FM added/changed |
| SoTA Annotations table | SoTA added/changed |
| Cross-Reference Matrix | Any relationship changes |

### 3. Verify All Links

For every link in the map:

| Check | Action if Fails |
|-------|----------------|
| Link resolves | Fix path |
| Target exists | Create or remove link |
| Anchor exists | Fix anchor or remove |

### 4. Update Relationship Diagram (if present)

If the map includes a visual diagram:
- Add new items
- Add new relationships
- Keep diagram consistent with tables

### 5. Update Update Log

At the bottom of the map file:

```markdown
## Update Log

| Date | Change |
|------|--------|
| YYYY-MM-DD | Added METHOD.002, updated cross-references |
```

---

## Output: Work Products

| Product | Location |
|---------|----------|
| Updated map file(s) | `/pack/<domain>/07-map/` |

---

## Completion Criteria

| Criterion | Test |
|-----------|------|
| All new items in map | Every added method/product/FM/etc. appears |
| Counts accurate | Pack Status section matches actual content |
| Links valid | All links resolve |
| Relationships current | Cross-reference matrix reflects actual links |
| Update log entry | Current date and change noted |

---

## Typical Errors

### E1. Skipping Map Update

**Symptom**: New method exists but map still shows "None yet."

**Problem**: Method is undiscoverable; pack appears incomplete.

**Correction**: Make map update part of extraction stage.

### E2. Map Counts Inaccurate

**Symptom**: Map says "3 methods" but there are 5.

**Problem**: Pack status misrepresented; gaps invisible.

**Correction**: Count actual files; update status table.

### E3. Broken Links

**Symptom**: Map links to `PD.METHOD.001.md` but file is named differently.

**Problem**: Navigation fails; trust in map degrades.

**Correction**: Verify links after every update.

### E4. Missing Cross-References

**Symptom**: Method produces WP but map doesn't show relationship.

**Problem**: Relationships invisible; structure unclear.

**Correction**: Update cross-reference matrix when adding content.

### E5. Map as Afterthought

**Symptom**: Map updated sporadically, long after content changes.

**Problem**: Map drifts from reality; becomes unreliable.

**Correction**: Map update is part of every extraction stage, not a separate task.

### E6. Multiple Inconsistent Maps

**Symptom**: Several map files with conflicting information.

**Problem**: No single source of truth for structure.

**Correction**: One primary map per pack; additional maps are views, not sources.

---

## Map Maintenance Checklist

Before committing any pack change:

- [ ] Is this change reflected in the map?
- [ ] Are item counts accurate?
- [ ] Are all links valid?
- [ ] Is the cross-reference matrix current?
- [ ] Is the update log entry added?

---

## Map Structure Reference

Standard map sections:

```
1. Pack Status (counts by type)
2. Relationship Diagram (optional visual)
3. Distinctions Table
4. Roles Table
5. Objects of Attention Table
6. Methods Table
7. Work Products Table
8. Failure Modes Table
9. SoTA Annotations Table
10. Cross-Reference Matrix
    - Methods ↔ Distinctions
    - Methods ↔ Failure Modes
    - Failure Modes ↔ Distinctions
    - Work Products ↔ Roles
11. Navigation Hints
12. Update Log
```

---

## Transition to Next Stage

Map maintenance is not the "last" stage — it is performed after every extraction.

After map is updated, either:
- Return to earlier stages for more content (05 → 06 → 07/08/09 → 10)
- Proceed to [11. Review and Evolution Cycle](11-review-and-evolution-cycle.md) for periodic review


# SOURCE_FILE: process/11-review-and-evolution-cycle.md
---
# 11. Review and Evolution Cycle

> **FPF Reference:** B.4 (Canonical Evolution Loop: Run → Observe → Refine → Deploy)
> Also: B.5 (Reasoning Cycle: Abduction → Deduction → Induction)
> Full specification: `~/IWE/FPF/FPF-Spec.md`

## Purpose

Establish the ongoing cycle of review and evolution that keeps the pack current. A pack is never "done" — it is a living repository that must be maintained as domain understanding evolves.

**Relationship to FPF:** This process implements FPF B.4 (Canonical Evolution Loop). The pack goes through cycles: run → observe (identify issues) → refine (make changes) → deploy (publish). The cycle is infinite.

---

## Process as Cycle, Not Project

| Project View (Wrong) | Cycle View (Correct) |
|---------------------|---------------------|
| "Create pack, then done" | "Pack is continuously maintained" |
| "Version 1.0 is complete" | "Current version is best-so-far" |
| "Distinctions are settled" | "Distinctions may need refinement" |
| "Methods are documented" | "Methods may become outdated" |

The process diagram loops: Stage 11 returns to earlier stages.

---

## Types of Evolution

| Type | Trigger | Process Path |
|------|---------|--------------|
| **Extension** | Gap identified | 05 → 06 → 07/08/09 → 10 → 11 |
| **Refinement** | Ambiguity found | 03/04 → 10 → 11 |
| **Revision** | Evidence changes | 09 → 10 → 11 |
| **Deprecation** | Understanding superseded | 09 → 10 → 11 |
| **Restructure** | Boundaries need change | 02 → 03 → ... → 11 |

---

## When Distinctions Need Review

| Signal | Action |
|--------|--------|
| Confusion persists despite distinction | Refine or restate distinction |
| New failure mode does not map to distinction | May need new distinction |
| Distinction rarely referenced | May be unnecessary |
| Two distinctions overlap | Consolidate or clarify |
| FPF updates relevant distinction | Align with FPF |

Return to [03. Distinctions Work](03-distinctions-work.md).

---

## When Methods Need Review

| Signal | Action |
|--------|--------|
| Method description is misunderstood | Clarify definition |
| Method produces unexpected products | Review inputs/outputs |
| Method confused with other methods | Sharpen distinction |
| Method is never referenced | May be unnecessary |
| Better method understanding emerges | Update or deprecate |

Return to [07. Method and Product Extraction](07-method-and-product-extraction.md).

---

## When SoTA Needs Review

| Signal | Action |
|--------|--------|
| Revision criterion met | Change status |
| New evidence available | Re-evaluate status |
| Review date reached | Scheduled review |
| Related claim changes | Check consistency |

Return to [09. SoTA Annotation](09-sota-annotation.md).

---

## Scheduled Review

Establish review cadence:

| Review Type | Frequency | Focus |
|-------------|-----------|-------|
| **Map audit** | Every extraction | Links, counts, relationships |
| **SoTA review** | Per annotation schedule | Status currency |
| **Distinction review** | Quarterly | Are distinctions holding? |
| **Full pack review** | Annually | Overall coherence |

---

## How to Conduct Pack Review

### Step 1: Check SoTA Statuses

For each SoTA annotation:
- Is review date passed?
- Is revision criterion met?
- Has relevant evidence emerged?

### Step 2: Audit Map

- Do counts match actual files?
- Are all links valid?
- Are relationships current?

### Step 3: Review Distinctions

For each distinction:
- Is it still being violated (failure modes occurring)?
- Is it clear enough to apply?
- Does it conflict with newer understanding?

### Step 4: Identify Gaps

- Are there methods without failure modes?
- Are there failure modes without distinctions?
- Are there work products without methods?

### Step 5: Document Review Findings

Create review log entry (not in pack):

```
Review Date: YYYY-MM-DD
Reviewer: [name/agent]
Scope: [full / partial]
Findings:
- [Finding 1]
- [Finding 2]
Actions:
- [Action 1: Stage to return to]
- [Action 2: Stage to return to]
```

### Step 6: Execute Actions

Return to appropriate process stages for each action.

---

## Making Changes Without Destruction

| Do | Do Not |
|----|--------|
| Deprecate outdated content | Delete history |
| Add revision notes | Overwrite without trace |
| Maintain ID stability | Reuse IDs |
| Update map after changes | Leave map stale |
| Document rationale | Change silently |

### Deprecation Pattern

When content becomes outdated:

1. Change status to `deprecated` in YAML frontmatter
2. Add deprecation note with rationale
3. Link to replacement (if any)
4. Update SoTA if applicable
5. Update map to show deprecated status
6. Do NOT delete the file

```markdown
---
status: deprecated
deprecated_date: YYYY-MM-DD
deprecated_reason: Superseded by METHOD.003
replacement: PD.METHOD.003
---
```

---

## Inputs

| Input | Source | Required |
|-------|--------|----------|
| Current pack content | All pack files | Yes |
| Previous review log | Process records | If exists |
| External evidence | Domain developments | As available |

---

## Output: Work Products

| Product | Location |
|---------|----------|
| Review log | `/process/working/` (not in pack) |
| Updated content | Relevant pack files |
| Updated map | `/pack/<domain>/07-map/` |

---

## Completion Criteria

| Criterion | Test |
|-----------|------|
| SoTA statuses reviewed | All annotations checked |
| Map audited | Counts and links verified |
| Findings documented | Review log created |
| Actions identified | Next stages determined |
| Actions executed | Returns to stages completed |

---

## Typical Errors

### E1. No Review Cycle

**Symptom**: Pack created and never revisited.

**Problem**: Content becomes stale; SoTA statuses become lies.

**Correction**: Establish and follow review cadence.

### E2. Review Without Action

**Symptom**: Issues identified but nothing changes.

**Problem**: Review is theater, not process.

**Correction**: Every finding → action → stage return.

### E3. Destructive Changes

**Symptom**: Content deleted; IDs reused; history lost.

**Problem**: Downstream references break; traceability lost.

**Correction**: Deprecate, do not delete. IDs are forever.

### E4. Change Without Map Update

**Symptom**: Content changes but map shows old state.

**Problem**: Map becomes unreliable.

**Correction**: Map update is part of every change.

### E5. Skipping Deprecation

**Symptom**: Outdated content removed without deprecation.

**Problem**: No record of what was believed; history lost.

**Correction**: Always deprecate with rationale before removal.

---

## The Infinite Loop

The process never terminates. After any significant change:

```
... → 07/08/09 → 10 → 11 → (02/03/04/05/06) → 07/08/09 → 10 → 11 → ...
```

Stage 11 always asks: "What needs attention next?" and returns to the appropriate stage.

---

## Process as Living System

| The pack | The process |
|----------|-------------|
| Captures domain knowledge | Governs knowledge maintenance |
| Is the product | Is the production system |
| Changes when domain changes | Persists across changes |
| May be wrong about domain | May be inefficient |
| Evaluated by accuracy | Evaluated by effectiveness |

Both pack and process can be improved. This document describes the process; the process can itself be reviewed and updated (meta-process).


# SOURCE_FILE: process/material-ingestion-protocol.md
---
# Material Ingestion Protocol

## Purpose

This document defines how external materials (posts, guides, notes, drafts) are processed into SPF knowledge. It ensures that **information is never treated as knowledge** and that Claude operates as analyst, not author.

---

## Core Principle

```
Material → Extraction Report → Human Review → Approved Candidates → Pack Changes
```

**Materials do NOT go directly into pack.**

---

## What Counts as External Material

| Material Type | Examples | How Provided |
|---------------|----------|--------------|
| **Posts** | systemsworld.club articles | Link or text |
| **Guides** | Existing manuals, tutorials | File or text |
| **Drafts** | Unpublished documents | Text |
| **Notes** | Personal observations | Text |
| **Reasoning** | Analytical pieces | Text |
| **Cases** | Real-world examples | Description |
| **Dialogues** | Conversations with insights | Transcript |

---

## When This Protocol Applies

This protocol is **mandatory** when:
- User provides external material for analysis
- User asks to "add this to the pack"
- User shares a post, note, or draft
- Any external content is introduced

---

## Claude's Response Format

When Claude receives external material, the response MUST be an **Extraction Report**, not pack changes.

### Extraction Report Template

```markdown
## Extraction Report

**Material**: [Title or brief description]
**Source**: [Link, file name, or "provided in message"]
**Date analyzed**: [YYYY-MM-DD]

---

### 1. Distinctions Identified

Distinctions that the material uses, assumes, or violates:

| Distinction | How Used/Violated | Pack Reference |
|-------------|-------------------|----------------|
| D.001 Method vs. Tool | Material confuses X with Y | [link] |
| ... | ... | ... |

**New distinction candidates**:
- [If material reveals a contrast not yet in pack]

---

### 2. Candidate Methods

| Candidate | Definition (draft) | Inputs | Outputs | Related Distinction |
|-----------|-------------------|--------|---------|---------------------|
| Method name | What it is | ... | ... | D.XXX |

**Notes**: [Open questions, uncertainties]

---

### 3. Candidate Work Products

| Candidate | Definition (draft) | Existence Criteria | Produced By |
|-----------|--------------------|--------------------|-------------|
| Product name | What it is | How to verify | Method X |

**Notes**: [Open questions, uncertainties]

---

### 4. Candidate Failure Modes

| Candidate | Type | Detection Test | Distinction Violated |
|-----------|------|----------------|---------------------|
| FM name | ontological/methodological/... | How to detect | D.XXX |

**Notes**: [Open questions, uncertainties]

---

### 5. SoTA Signals

| Claim/Interpretation | Signal | Rationale |
|---------------------|--------|-----------|
| "X is the case" | current / deprecated / hypothesis | Why |

---

### 6. Suggested Changes to Pack

| Action | Target File | What Changes | Priority |
|--------|-------------|--------------|----------|
| Add method | 03-methods/PD.METHOD.XXX.md | New method card | High/Medium/Low |
| Update distinction | 01-domain-contract/01B-distinctions.md | Refine D.XXX | ... |
| Add FM | 05-failure-modes/... | New FM card | ... |
| None | — | Material has no new content | — |

---

### 7. What Was NOT Extracted

Content from material that was:
- Out of scope (outside bounded context)
- Already in pack
- Too vague to formalize
- Didactic/scenario (belongs downstream)

---

### 8. Open Questions

- [Questions requiring human judgment]
- [Ambiguities that need clarification]
```

---

## After Extraction Report

### Human Review

The user reviews the extraction report and decides:
- Which candidates to approve
- Which to reject
- Which need clarification

### If Approved

Claude may proceed to pack changes following:
1. Process stages (03 → 06 → 07/08/09 → 10)
2. Process lint
3. Hard gates

### If Rejected or Needs Clarification

No pack changes. Discussion continues.

---

## What Claude Must NOT Do

| Forbidden | Why |
|-----------|-----|
| Copy text from material into pack | Pack uses domain language, not source language |
| Create pack files without extraction report | Bypasses analysis |
| Assume extraction = approval | Human must approve |
| Add scenarios/didactics | Belongs downstream |
| Treat material as authoritative | Must apply distinctions critically |

---

## Working Directory for Raw Materials

If user wants to track materials:

```
/process/working/
  ingestion-log.md      # List of processed materials
  extractions/          # Saved extraction reports
```

These are **process artifacts**, not pack content.

---

## Example Interaction

**User**: "Here's my post about time tracking. Add the relevant knowledge to the pack."

**Claude** (CORRECT):
```
I'll analyze this material and produce an extraction report.

## Extraction Report

**Material**: Post about time tracking
**Source**: Provided in message
...
[Full extraction report]
...

### 6. Suggested Changes to Pack
| Action | Target File | What Changes |
|--------|-------------|--------------|
| Add FM | PD.FAIL.007.md | New failure mode: tracking without categories |

Would you like me to proceed with these changes?
```

**Claude** (WRONG):
```
I'll add this to the pack. Creating PD.METHOD.002.md...
```

---

## Integration with MAPSTRATEGIC

This protocol is the operational core of:
- **Phase 2**: Material Ingestion
- **Phase 3**: Analytical Processing

See [MAPSTRATEGIC.md](/MAPSTRATEGIC.md) for phase context.

---

## Lint Interaction

Extraction reports are **not subject to pack lint** (they are process artifacts).

Pack changes resulting from approved extractions **are subject to full lint**.


# SOURCE_FILE: process/process-lint.md
---
# Process Lint Protocol

## What This Is

Process lint is a **mandatory verification protocol** applied to every change in `/pack/`. It is NOT a process stage — it is a cross-cutting quality gate that runs:

| Application Point | Who Runs | When |
|-------------------|----------|------|
| **Pre-commit** | Author (human or AI) | Before `git commit` |
| **Review** | Reviewer | During PR review |
| **Agent work** | AI agent | After each pack modification |

Process lint ensures that changes comply with the SPF constitution before they enter the repository.

---

## Change-Type Matrix

Each type of change triggers specific lint checks. Identify your change type(s) and verify all required items.

### CT-1: Method Card Added/Modified

File pattern: `/pack/<domain>/03-methods/*.md`

| Check | Verification |
|-------|--------------|
| **L-M01** | Definition describes WHAT, not HOW (no numbered steps) |
| **L-M02** | Inputs section is filled |
| **L-M03** | Outputs section links to work product(s) |
| **L-M04** | At least one distinction is referenced |
| **L-M05** | Failure modes are referenced |
| **L-M06** | SoTA status is assigned with revision criterion |
| **L-M07** | ID follows convention `<DOMAIN>.METHOD.<NNN>` |
| **L-M08** | Entry added to `02C-methods-index.md` |
| **L-M09** | Map updated in `07-map/` |
| **L-M10** | No didactic language (see [Universal Bans](#universal-bans)) |

### CT-2: Work Product Added/Modified

File pattern: `/pack/<domain>/04-work-products/*.md`

| Check | Verification |
|-------|--------------|
| **L-WP01** | Definition is observable/verifiable |
| **L-WP02** | Existence criteria specified ("how to verify it exists") |
| **L-WP03** | Quality criteria specified |
| **L-WP04** | Produced-by method is linked |
| **L-WP05** | Consumed-by roles/methods are linked |
| **L-WP06** | ID follows convention `<DOMAIN>.WP.<NNN>` |
| **L-WP07** | Map updated in `07-map/` |
| **L-WP08** | Product is artifact, not description (see [D.005](/pack/personal-development/01-domain-contract/01B-distinctions.md#d005-work-product-vs-description)) |

### CT-3: Failure Mode Added/Modified

File pattern: `/pack/<domain>/05-failure-modes/*.md`

| Check | Verification |
|-------|--------------|
| **L-FM01** | Error type assigned (ontological/methodological/role/deprecated-interpretation) |
| **L-FM02** | Detection test exists ("how to recognize in speech/text/behavior") |
| **L-FM03** | Distinction violated is linked |
| **L-FM04** | Correct understanding stated |
| **L-FM05** | Risk/harm documented |
| **L-FM06** | Related methods/products linked |
| **L-FM07** | ID follows convention `<DOMAIN>.FAIL.<NNN>` |
| **L-FM08** | Map updated in `07-map/` |

### CT-4: Distinction Added/Modified

File pattern: `/pack/<domain>/01-domain-contract/01B-distinctions.md`

| Check | Verification |
|-------|--------------|
| **L-D01** | Contrast is explicit ("X vs. Y") |
| **L-D02** | Distinction test exists ("how to tell X from Y") |
| **L-D03** | Consequence of confusion stated |
| **L-D04** | Related failure mode exists or noted for creation |
| **L-D05** | SoTA status assigned with revision criterion |
| **L-D06** | Does not contradict FPF distinctions |
| **L-D07** | Map updated (if new distinction) |

### CT-5: SoTA Annotation Added/Modified

File pattern: `/pack/<domain>/06-sota/*.md` or inline in other files

| Check | Verification |
|-------|--------------|
| **L-S01** | Status is one of: `current` / `deprecated-interpretation` / `hypothesis` |
| **L-S02** | Revision criterion specified ("would change if...") |
| **L-S03** | Basis for status stated |
| **L-S04** | Target claim/method is linked |
| **L-S05** | ID follows convention `<DOMAIN>.SOTA.<NNN>` (for standalone) |
| **L-S06** | Map updated if new annotation |

### CT-6: Role or Object of Attention Added/Modified

File pattern: `/pack/<domain>/02-domain-entities/02A-roles.md` or `02B-objects-of-attention.md`

| Check | Verification |
|-------|--------------|
| **L-R01** | Role is functional position, not job title or person |
| **L-R02** | Responsibilities are specified |
| **L-R03** | Typical methods linked (for roles) |
| **L-R04** | Object of attention is observable, not abstract |
| **L-R05** | Related methods linked (for objects) |
| **L-R06** | Map updated in `07-map/` |

### CT-7: Map Modified

File pattern: `/pack/<domain>/07-map/*.md`

| Check | Verification |
|-------|--------------|
| **L-MAP01** | All item counts match actual file counts |
| **L-MAP02** | All links resolve |
| **L-MAP03** | Cross-reference matrix is current |
| **L-MAP04** | Update log entry added |

### CT-8: Any Structural Change

Any addition, removal, or relationship change.

| Check | Verification |
|-------|--------------|
| **L-STR01** | Map is updated |
| **L-STR02** | Affected indexes are updated |
| **L-STR03** | Cross-references in affected files are valid |

---

## Universal Bans

These apply to ALL changes. Any violation is a hard fail.

### UB-1: No Didactic Language

**FORBIDDEN** words/phrases in pack content:

| Forbidden | Why |
|-----------|-----|
| "step", "Step 1", "steps" | Scenarios belong downstream |
| "lesson", "module" | Learning design belongs downstream |
| "in N days", "week 1" | Temporal programs belong downstream |
| "implement", "try this" | Imperatives belong downstream |
| "first/then", "next" | Sequences belong downstream |
| "exercise", "practice this" | Activities belong downstream |

**Test**: Could this sentence appear in a course syllabus? If yes, rewrite.

### UB-2: No "Domain as System"

**FORBIDDEN**:
- "Personal development is a system"
- "The system of time management"
- Any claim that a domain IS a system (without specifying which system)

**Allowed**:
- "A person using method X can be modeled as a system"
- "The practice of Y involves these system boundaries"

### UB-3: No Method/Tool/Product Confusion

Every pack file must respect:

| Entity | Is | Is NOT |
|--------|-----|--------|
| Method | Way of acting | Tool, artifact, scenario |
| Tool | Artifact that supports method | Method itself |
| Work Product | Observable artifact | Description, feeling, intention |

**Test**: Apply [D.001](/pack/personal-development/01-domain-contract/01B-distinctions.md#d001-method-vs-tool) and [D.005](/pack/personal-development/01-domain-contract/01B-distinctions.md#d005-work-product-vs-description).

### UB-4: No Information-as-Knowledge

**FORBIDDEN**:
- Copying text from sources into pack files
- Using source's terminology without mapping to domain distinctions
- Treating "I read this" as "this is true"

**Required**:
- Information → Analysis (Stage 06) → Candidates → Extraction → Pack

---

## Process Compliance Mini-Checklist

Before committing ANY change to `/pack/`:

### Context
- [ ] **Bounded context exists**: `00-pack-manifest.md` has explicit scope
- [ ] **Change is within scope**: This change belongs in this pack

### Distinctions
- [ ] **Distinctions cover change**: No undefined concepts introduced
- [ ] **Distinction tests exist**: Can operationally distinguish terms used

### Content
- [ ] **SoTA assigned or N/A**: Status with revision criterion, or documented why not needed
- [ ] **No universal ban violations**: Checked UB-1 through UB-4

### Structure
- [ ] **Map updated**: Changes reflected in `07-map/`
- [ ] **IDs stable and valid**: Follow convention, not reused
- [ ] **Links resolve**: All cross-references work

### Process
- [ ] **Change-type identified**: Know which CT-* applies
- [ ] **CT-specific checks passed**: All items for that change type verified

---

## Lint Report Format

When reporting lint results (for AI agents or PR descriptions):

```
## Lint Report

**Change type(s)**: CT-1 (Method), CT-7 (Map)
**Files changed**:
- pack/personal-development/03-methods/PD.METHOD.002.md (new)
- pack/personal-development/07-map/PD.MAP.001.md (updated)

### CT-1 Checks (Method)
- [x] L-M01: Definition describes what, not how
- [x] L-M02: Inputs filled
- [x] L-M03: Outputs link to WP
- [x] L-M04: Distinction referenced
- [x] L-M05: Failure modes referenced
- [x] L-M06: SoTA assigned
- [x] L-M07: ID follows convention
- [x] L-M08: Index updated
- [x] L-M09: Map updated
- [x] L-M10: No didactic language

### Universal Bans
- [x] UB-1: No didactic language
- [x] UB-2: No "domain as system"
- [x] UB-3: No method/tool/product confusion
- [x] UB-4: No information-as-knowledge

### Process Compliance
- [x] Bounded context exists
- [x] Distinctions cover change
- [x] Map updated
- [x] IDs valid

**Result**: PASS
```

---

## Hard Gates

These conditions BLOCK commit/merge. No exceptions.

| Gate | Condition | Blocked Until |
|------|-----------|---------------|
| **HG-1** | Method added without work product link | Add WP or link to existing |
| **HG-2** | Method added without distinction reference | Add distinction link |
| **HG-3** | Work product without existence criteria | Add criteria |
| **HG-4** | Failure mode without detection test | Add test |
| **HG-5** | Structural change without map update | Update map |
| **HG-6** | Didactic language detected | Rewrite |
| **HG-7** | Scenario instead of method | Rewrite as method |
| **HG-8** | SoTA without revision criterion | Add criterion |

---

## Integration Points

### For Humans
- Run lint checks mentally or with checklist before committing
- Include lint report in PR description
- Reviewer verifies lint during review

### For AI Agents
- Declare change-type before modification
- Run lint checks after modification
- Include lint report in response
- Self-block if hard gate fails

### For CI/CD (Future)
- Automated lint checks on PR
- Block merge on hard gate failure
- Generate lint report automatically


# SOURCE_FILE: REPO-TYPE.md
---
# Repository type

**Type**: `Base/Principles`

**Source-of-truth**: yes (for pack form/process requirements)

## Upstream dependencies

- [ailev/FPF](https://github.com/ailev/FPF) — First Principles Framework

## Downstream outputs

- Pack repositories use SPF as their foundation

## Non-goals

- Does NOT contain domain knowledge of specific areas
- Is NOT a pack
- Does NOT contain courses, learning paths, or guides
- Does NOT contain code/services

## Contents

- Universal pack requirements (structure, mandatory elements)
- Templates for pack repositories
- Process lint (correctness checks)
- SoTA status rules
- ID/reference requirements
- Material ingestion → extraction → candidate → pack update protocol


# SOURCE_FILE: spec/ai-view.md
---
# AI View Specification

This document specifies how AI systems should consume and represent SPF Personal content.

---

## Purpose

AI systems (chatbots, agents, RAG pipelines) need to:
1. Retrieve relevant domain knowledge
2. Maintain accuracy to source
3. Respect the epistemology (not invent distinctions)

---

## Retrieval Architecture

### Recommended Approach

```
[SPF Markdown] → [Chunking/Embedding Pipeline] → [Vector Store]
                          ↓
              [Metadata Preservation Layer]
                          ↓
                   [AI Agent/RAG]
```

### Chunking Guidelines

| Content Type | Chunk Strategy |
|--------------|----------------|
| Method cards | One chunk per card (preserve wholeness) |
| Distinctions | One chunk per distinction block |
| Work products | One chunk per card |
| Failure modes | One chunk per card |
| Maps | Do not chunk; use as navigation metadata |

### Metadata to Preserve

Each chunk should retain:
- `id`: The stable ID (e.g., `PD.M.001`)
- `type`: method | work-product | failure-mode | distinction | sota
- `source_path`: Relative path in repo
- `sota_status`: current | deprecated-interpretation | hypothesis (if applicable)

---

## Response Generation Rules

AI systems using SPF content should:

### Do
- Quote or paraphrase source accurately
- Cite IDs when referencing specific items
- Respect SoTA status (flag hypotheses as such)
- Distinguish methods from tools, work products from descriptions

### Do Not
- Invent new methods not in the source
- Present deprecated interpretations as current
- Conflate different entity types
- Add didactic framing ("Step 1: ...) unless user requests it

---

## Grounding Protocol

When an AI response references SPF content:

```
User: What methods exist for X?

AI: According to SPF Personal, the following methods address X:
- [PD.M.001] Method Name — brief description
- [PD.M.002] Method Name — brief description

[Note: PD.M.002 has SoTA status "hypothesis" — evidence is preliminary]
```

---

## Hallucination Prevention

- AI should admit when SPF has no content for a query
- Phrase: "SPF Personal does not currently include methods for X"
- Do not generate plausible-sounding but non-existent methods

---

## Update Synchronization

AI systems should:
1. Re-index when SPF version changes
2. Invalidate cached embeddings on major version bumps
3. Log source version in responses (optional)

---

## Testing Recommendations

Downstream AI teams should test:
- [ ] Accurate retrieval of method cards by ID
- [ ] Correct SoTA status reporting
- [ ] No hallucinated methods
- [ ] Proper distinction between methods/tools/work-products


# SOURCE_FILE: spec/downstream-contract.md
---
# Downstream Contract

This document specifies the contract between SPF Personal (this repo) and downstream consumers (courses, AI agents, guides, applications).

---

## Principles

1. **SPF is source-of-truth** for domain knowledge structure
2. **Downstream transforms, does not modify** — consumers read and transform, never write back
3. **Stability guarantees** — IDs are stable; deprecation over deletion

---

## What Downstream Systems May Do

| Action | Allowed | Notes |
|--------|---------|-------|
| Read all `/pack/` content | Yes | Primary use case |
| Transform to other formats | Yes | Markdown to HTML, JSON, etc. |
| Create embeddings/indexes | Yes | For AI retrieval |
| Add didactic wrappers | Yes | "Lesson 1: Understanding X" |
| Create learning paths | Yes | Sequence methods into curricula |
| Track user progress | Yes | In downstream DB, not here |
| Build AI agents | Yes | Using `/spec/ai-view.md` |

---

## What Downstream Systems Must NOT Do

| Action | Forbidden | Reason |
|--------|-----------|--------|
| Modify SPF source | Yes | Read-only dependency |
| Store canonical content in vectors only | Yes | Markdown is source |
| Assume file paths are stable | Yes | Use IDs, not paths |
| Embed FPF into downstream | Yes | Depend on FPF directly |

---

## Versioning Contract

- SPF Personal will use semantic versioning when stable
- Breaking changes (ID renames, structure changes) bump major version
- Additions bump minor version
- Fixes/clarifications bump patch version

Downstream should pin to a version or commit hash.

---

## ID Stability

IDs follow the pattern: `<DOMAIN>.<TYPE>.<NNN>`

| Guarantee | Description |
|-----------|-------------|
| IDs are unique | No two items share an ID |
| IDs are immutable | Once assigned, never reused |
| Deprecated items keep IDs | Marked deprecated, not deleted |

Downstream may rely on IDs for persistent references.

---

## File Format Contract

All content files are:
- UTF-8 encoded Markdown
- YAML frontmatter optional (for metadata)
- GitHub-flavored Markdown syntax

---

## Change Notification

Downstream systems should:
1. Watch releases/tags for updates
2. Diff against previous version
3. Update transformations as needed

No push notification mechanism exists (this is a static repo).


# SOURCE_FILE: spec/f-g-r-trust.md
---
# F-G-R Trust Pattern (Optional)

> **FPF Reference:** B.3 (Trust & Assurance Calculus)
> Full specification: `~/IWE/FPF/FPF-Spec.md`

## Overview

F-G-R is a pattern from FPF for assessing the **trustworthiness** of claims. It can be used in Packs for a more rigorous evaluation of knowledge quality.

**Status:** Optional pattern. Most Packs can work without it. Recommended for:
- Packs in critical domains (security, medicine)
- Situations where confidence level needs to be made explicit
- Working with hypotheses and unproven claims

---

## F-G-R Tuple

Trust is not a "feeling" — it is a computable tuple `⟨F, G, R⟩`:

| Component | Name | Question | Values |
|-----------|------|----------|--------|
| **F** | Formality | How rigorously is this expressed? | F0 (sketch) → F9 (formal proof) |
| **G** | Claim Scope | Where does this apply? | Set-valued (contexts where the claim holds) |
| **R** | Reliability | How well is this supported? | Evidence-based support level |

---

## F: Formality Scale

| Level | Description | Example |
|-------|-------------|---------|
| F0 | Sketch, informal | "I think X works" |
| F1-F2 | Written but loose | Blog post, notes |
| F3-F4 | Structured text | Method card with definition |
| F5-F6 | Checked specification | Reviewed by expert |
| F7-F8 | Tested/validated | Has tests, passed review |
| F9 | Formal proof | Mathematical/logical proof |

---

## G: Claim Scope

G defines **where** a claim holds. It is set-valued (a set of contexts).

| Scope | Example |
|-------|---------|
| Universal | "Method ≠ Tool" (holds everywhere in FPF-aligned systems) |
| Domain-wide | "Agency is a key characteristic" (holds in the creator Pack) |
| Context-specific | "Method X works for Y" (holds under specific conditions) |

---

## R: Reliability

R indicates **how well** a claim is supported by evidence.

| Level | Evidence | Example |
|-------|----------|---------|
| Low | Hypothesis, no test | "We think that..." |
| Medium | Some evidence | "Practice shows..." |
| High | Strong evidence | "Research confirms..." |
| Very High | Replicated | "Verified repeatedly" |

---

## When to Use F-G-R in Pack

### Recommended

| Situation | Why |
|-----------|-----|
| Critical distinctions | Show that core distinctions are well-established |
| Controversial claims | Be explicit about confidence level |
| Hypotheses | Make clear these need validation |
| Cross-references | Show alignment quality with FPF |

### Not Required

| Situation | Why |
|-----------|-----|
| Simple method cards | SoTA status is sufficient |
| Obvious distinctions | Standard format covers them |
| Work products | They are artifacts, not claims |

---

## Integration with SoTA

F-G-R complements SoTA:

| SoTA | F-G-R |
|------|-------|
| Status (current/hypothesis/deprecated) | Detailed assessment (F, G, R) |
| Revision criterion | What would change F, G, or R |
| Simple | More detailed |

SoTA can be used without F-G-R, but F-G-R without SoTA makes no sense.

---

## Example Annotation

```markdown
**Claim:** Method and Tool are distinct types (D.001)

**F-G-R:**
- **F** = 6 (Checked specification, reviewed)
- **G** = {SPF, Pack, all FPF-aligned systems}
- **R** = High (consistent with FPF A.7, no counter-evidence)

**SoTA:** `current`
- Revision criterion: Would change if evidence shows tool can substitute method
```

---

## References

- FPF B.3: Trust & Assurance Calculus
- FPF B.3.1: Components & Epistemic Spaces
- FPF B.3.3: Assurance Subtypes & Levels
- FPF B.3.4: Evidence Decay & Epistemic Debt


# SOURCE_FILE: spec/human-guides.md
---
# Human Guides Specification

This document specifies how to create human-readable guides, courses, and materials from SPF Personal content.

---

## Purpose

Humans learn differently than AI retrieves. Guides need:
- Narrative structure
- Progressive complexity
- Exercises and examples
- Motivational framing

**None of this belongs in SPF itself** — this spec describes the transformation.

---

## Transformation Principles

### Source (SPF)
- Declarative: "Method X does Y"
- Neutral: No "you should" or "try this"
- Complete: All metadata present
- Stable: IDs don't change

### Target (Guide)
- Instructional: "To do Y, use Method X"
- Engaging: "You'll find this useful when..."
- Selective: Curated subset for audience
- Versioned: Tied to SPF version

---

## Guide Structure Template

A guide consuming SPF may follow this structure:

```
1. Introduction
   - Why this matters (motivation — NOT in SPF)
   - Prerequisites (reference other guides or FPF)

2. Core Concepts
   - Pull from: 01-domain-contract/01B-distinctions.md
   - Add: Examples, analogies (NOT in SPF)

3. Methods in Practice
   - Pull from: 03-methods/*.md
   - Add: Step-by-step walkthrough (NOT in SPF)
   - Add: Exercises (NOT in SPF)

4. What You'll Produce
   - Pull from: 04-work-products/*.md
   - Add: Templates, worksheets (NOT in SPF)

5. Common Mistakes
   - Pull from: 05-failure-modes/*.md
   - Add: Recovery strategies (NOT in SPF)

6. Assessment
   - Tie to work products' observability criteria
   - Add: Rubrics, checklists (NOT in SPF)
```

---

## What Guides Add (Not in SPF)

| Element | Example | Why Not in SPF |
|---------|---------|----------------|
| Learning objectives | "By end, you will..." | Didactic framing |
| Step sequences | "Step 1: ..., Step 2: ..." | Scenario, not knowledge |
| Time estimates | "Takes ~30 minutes" | Context-dependent |
| Exercises | "Try this with your..." | Instructional design |
| Examples | "For instance, Alice..." | Illustrative, not canonical |
| Motivation | "This matters because..." | Persuasion, not description |

---

## Attribution Requirements

Guides derived from SPF should:
1. State SPF version used
2. Link to SPF repo
3. Clearly distinguish SPF content from guide additions
4. Not claim SPF endorsement unless authorized

---

## Versioning Guides

- Pin guide to SPF version (e.g., "Based on SPF Personal v1.2.0")
- When SPF updates, diff and decide: update guide or note divergence
- Major SPF changes may require guide rewrite

---

## Anti-Patterns

| Anti-Pattern | Problem |
|--------------|---------|
| Copy-paste SPF as guide | No transformation; SPF is not a guide |
| Invent methods in guide | Guide diverges from source-of-truth |
| Omit SPF attribution | Users can't verify accuracy |
| Never update guide | Guide becomes stale |

---

## Testing Guide Quality

- [ ] All methods referenced exist in SPF
- [ ] SoTA status accurately reflected
- [ ] Guide additions clearly marked or obviously instructional
- [ ] Exercises tie to SPF work products
- [ ] Failure modes from SPF inform "common mistakes" section


# SOURCE_FILE: spec/SPF.SPEC.001-entity-coding.md
---
---
id: SPF.SPEC.001
name: Entity Coding Rule
status: draft
created: 2026-02-10
---

# Entity Coding Rule

> SPF specification: how to identify and code entities across all Packs and in SPF itself.

---

## Foundation (FPF)

### Object ≠ Description ≠ Carrier

FPF (A.7 Strict Distinction) requires distinguishing:

| Level | What it is | Example |
|-------|-----------|---------|
| **Object** | Thing in reality | Knowledge extraction method (capability) |
| **Description** | Episteme about the thing (U.Episteme) | Method card in Pack |
| **Carrier** | Physical/digital medium (U.SymbolCarrier) | File `DP.M.001-knowledge-extraction.md` |

**Pack contains descriptions of domain entities on carriers (`.md` files).** The code indicates what is being described, not the level of description.

---

## Terminology

### Entity types

SPF defines **base types** — they may appear in any domain.

| Type | EN | Definition | not (what this is NOT) |
|------|----|-----------|-----------------------|
| **Method** | Method | Description of a capability to produce a work product | not a scenario (step-by-step instruction), not a tool, not execution (work) |
| **Work Product** | Work Product | Observable result of applying a method; exists on a carrier | not a method description, not a skill |
| **Failure Mode** | Failure Mode | Typical violation of a method or work product with observable symptoms | not a code bug, not a risk (probability) |
| **Distinction** | Distinction | Conceptual boundary whose violation creates irresolvable confusion | not a fact, not a definition |
| **Role** | Role | Contextual function (mask) in a bounded context | not a position, not a person, not behavior |
| **Characteristic** | Characteristic | Measurable evaluation axis for an entity | not a metric (measurement), not an indicator (observable sign) |
| **SoTA Annotation** | SoTA Annotation | Currency status of a statement + revision criterion | not a literature review |
| **Map** | Map | Navigation structure of connections between entities | = structural artifact, not content |

### Domain entities

A Pack may contain entities specific to its bounded context. For these, the Pack defines **extended types** and registers them in the manifest (`00-pack-manifest.md`).

### Distinction: type ≠ characteristic

- **Type** — category of the entity (what it belongs to): method, role, work product.
- **Characteristic** — measurable axis (how the entity is evaluated): complexity, maturity, currency.

Type answers "what is it?". Characteristic answers "what is it like?".

---

## Coding rule

### Code format

All identifiable entities are coded by a single rule:

```
<CONTEXT>.<TYPE>.<NUMBER>
```

| Segment | Format | Definition |
|---------|--------|-----------|
| CONTEXT | 2–4 uppercase Latin letters | Bounded context mnemonic (FPF: U.BoundedContext) — semantic frame with its own vocabulary, roles and invariants |
| TYPE | 1–6 uppercase Latin letters | Entity type code. Base types — from SPF; extended types — from Pack |
| NUMBER | 3 digits | Sequential numbering within context + type |

### Code properties

1. **Immutability** — code does not change after assignment
2. **Uniqueness** — one code = one entity, forever
3. **No reuse** — deleted/deprecated entities retain their code
4. **Sequence** — numbers are assigned in order of creation
5. **Gaps are permitted** — `001, 002, 005` is valid (003, 004 may be deprecated)

---

## Type codes

### Base types (defined by SPF, available to all Packs)

| Code | Type | Folder in Pack |
|------|------|---------------|
| `M` | Method | `03-methods/` |
| `WP` | Work Product | `04-work-products/` |
| `FM` | Failure Mode | `05-failure-modes/` |
| `D` | Distinction | `01-domain-contract/` |
| `R` | Role | `02-domain-entities/` |
| `CHR` | Characteristic | `02-domain-entities/` |
| `SOTA` | SoTA Annotation | `06-sota/` |
| `MAP` | Map | `07-map/` |
| `SC` | Service Clause | `08-service-clauses/` |

### Extended types (defined by a specific Pack)

A Pack may define additional types for its domain entities. They:

- Are registered in the Pack manifest (`00-pack-manifest.md`)
- Are placed in `02-domain-entities/`
- Code: 1–6 uppercase Latin letters, unique within the Pack

### SPF types (for the framework itself)

| Code | Type | Description |
|------|------|-------------|
| `SPEC` | Specification | Normative specification (rule) |
| `TPL` | Template | Structure template |
| `D` | Distinction | Distinction (common to all Packs) |
| `MAP` | Map | SPF navigation map |

---

## Levels and coding

| Level | Codes itself? | Format | Creates new codes? |
|-------|--------------|--------|--------------------|
| **FPF** | Yes | `U.*` (own format) | Yes (meta-level) |
| **SPF** | Yes | `SPF.TYPE.NUMBER` | Yes (form rules) |
| **Pack** | Yes | `CONTEXT.TYPE.NUMBER` | Yes (domain knowledge) |
| **Downstream** | No | References Pack codes | No |

---

## Context registry

| Code | Context | Level | Repo |
|------|---------|-------|------|
| `SPF` | Second Principles Framework | Framework | SPF/ |
| `PD` | Personal Development | Pack | PACK-personal/ |
| `DP` | Digital Platform | Pack | PACK-digital-platform/ |
| `EC` | Ecosystem | Pack | PACK-ecosystem/ |
| `MIM` | Engineering Managers Workshop | Pack | PACK-MIM/ |
| `VR` | Verification & Acceptance | Pack | PACK-verification/ |

Requirements for a new context code:

- 2–4 uppercase Latin letters
- Bounded context mnemonic
- Globally unique (in this registry)

---

## File name

```
<CODE>-<slug>.md
```

- **Code** — full entity code
- **Slug** — Latin characters, kebab-case, without repeating the number

Examples:

```
SPF.SPEC.001-entity-coding.md
DP.M.001-knowledge-extraction.md
DP.AISYS.013-knowledge-extractor.md
EC.R.001-mentor.md
```

---

## References

### Within a single Pack

```markdown
See [DP.M.001](../03-methods/DP.M.001-knowledge-extraction.md)
```

### Cross-Pack references

```markdown
See [DP.M.001](https://github.com/.../03-methods/DP.M.001-knowledge-extraction.md)
```

With version:

```markdown
See [DP.M.001@v1.0.0](https://github.com/...@v1.0.0/.../DP.M.001-knowledge-extraction.md)
```

### References to FPF

```markdown
Per FPF, method ≠ tool (see FPF A.7, Strict Distinction).
```

### In YAML Frontmatter

```yaml
---
id: DP.M.001
name: Knowledge Extraction
status: active
created: 2026-02-10
related:
  - DP.WP.001
  - DP.FM.002
---
```

---

## Validation

Codes are validated for:

- [ ] Format: `CONTEXT.TYPE.NNN`
- [ ] Uniqueness within repo
- [ ] File exists at expected path
- [ ] All references resolve
- [ ] Extended types are registered in Pack manifest

---

*This document: `SPF.SPEC.001`*


# SOURCE_FILE: spec/SPF.SPEC.003-pack-scalability.md
---
---
id: SPF.SPEC.003
name: Pack Scalability
status: draft
created: 2026-02-11
---

# Pack Scalability

> SPF specification: how to build a Pack that stays comprehensible to AI agents as it grows by orders of magnitude.

---

## Problem

A Pack is loaded into an AI agent's context window in its entirety. At the current volume (~30 files, ~5K lines) this works. As it grows (100+ files, 15K+ lines) it stops working: the context overflows, the LLM loses accuracy on long context (lost-in-the-middle effect), and cost grows linearly.

**Threshold:** ~100 files / ~15K lines — the boundary of the context-loading approach.

---

## Distinction: Context-loading ≠ Retrieval-based

| Mode | Description | When it works | Limit |
|------|-------------|--------------|-------|
| **Context-loading** | Full Pack loaded into context | <100 files, <15K lines | ~200K tokens |
| **Retrieval-based** | Agent requests needed parts via search | Any volume | Retrieval quality |

**Strategy:** prepare Pack for retrieval-based loading without breaking context-loading for small Packs.

---

## SOTA methods (rationale for decisions)

### What is applicable to Pack

| Method | Source | Application in Pack |
|--------|--------|---------------------|
| **RAPTOR** (Hierarchical Indexing) | Stanford, 2024 | Pack already has 3 levels: manifest → MAP → entity cards. Formalize as layers |
| **Contextual Chunking** | Anthropic, 2024 | Add `summary` to the frontmatter of each entity — retrieval without reading the full file |
| **Hybrid Retrieval** (dense + BM25) | Production default 2025 | Vector search on summary + exact search on ID codes |
| **LightRAG** | HKUDS, EMNLP 2025 | Typed `related:` in frontmatter forms a graph — traversal along links |
| **MemGPT/Letta** | UCB, 2023 | 3-layer memory: core (manifest) + recall (MAP/indices) + archival (entity cards) |
| **llms.txt** | llmstxt.org, 2024 | Manifest as machine-readable index of all entities |
| **Context Engineering** | Anthropic, 2025 | Write/Select/Compress/Isolate — Pack supports all 4 strategies via layers |

### What is NOT applicable

| Method | Why it does not fit |
|--------|---------------------|
| Subfolders by entity type | Solves the human problem, not AI. AI navigates by indices, not folders |
| Static `_index.md` | Become outdated just like manual MAP. Generation is needed |
| Full GraphRAG (Microsoft) | Excessive for structured Pack. LightRAG-style via frontmatter `related:` is sufficient |

---

## Specification: 3-layer loading

### Principle

An AI agent loads Pack layer by layer: from overview to details. Each layer is self-sufficient for its level of tasks.

### Layer 0: Always-in-context (<=2K tokens)

Always loaded, on any access to Pack.

| File | Content | Max size |
|------|---------|---------|
| `00-pack-manifest.md` | ID, scope, entity count, version, entity index with summary | 1.5K tokens |
| `01A-bounded-context.md` | Object of description, scope, truth criteria (summary) | 500 tokens |

**Requirement:** manifest MUST contain a machine-readable table of ALL entities with a 1-line summary (see Extended Manifest section).

### Layer 1: On-demand indices (<=5K tokens each)

Loaded during navigation, link search, work planning.

| File | Content | When to load |
|------|---------|-------------|
| `07-map/DOMAIN.MAP.001.md` | Full navigation (auto-generated) | Overview of all links needed |
| `01B-distinctions.md` | All distinctions with summary | Working with concepts |
| `02C-methods-index.md` | All methods with inputs/outputs | Working with methods |

### Layer 2: Full entity cards (<=1K tokens each)

Loaded point-by-point, by ID.

| File | When to load |
|------|-------------|
| `DOMAIN.M.NNN-*.md` | Method details needed |
| `DOMAIN.WP.NNN-*.md` | Product criteria needed |
| `DOMAIN.FM.NNN-*.md` | Error analysis |

**Loading protocol:**

```
1. Agent receives a task
2. Loads Layer 0 (manifest + bounded context)
3. From manifest finds needed entities (by summary and tags)
4. Loads Layer 1 index for navigation (if needed)
5. Loads specific entity cards from Layer 2
```

---

## Size limit for domain knowledge files

### Distinction: knowledge ≠ meta-structure

| Category | Example files | Limit |
|----------|--------------|-------|
| **Domain knowledge** | Entity cards: M, WP, FM, D, R, CHR, SOTA, + domain-specific kinds (FMT, PRG, etc.) | **10,000 characters** (hard gate) |
| **Pack meta-structure** | Manifest (00), Bounded Context (01A), Distinctions index (01B), MAP (07), Ontology | No limit |

### Rule

An entity card exceeding 10,000 characters is a signal of an overloaded entity. The file does NOT need to be mechanically split. **Entity decomposition** is needed: one entity becomes two or more with their own bounded contexts.

### Protocol when exceeded

1. Extractor (or author) discovers an entity card > 10K characters
2. Analyzes content: are there two different objects of description inside?
3. Proposes decomposition: which entities to extract, which links (`related:`) to establish
4. After approval — creates separate entity cards + updates manifest

### Why 10K

- Typical entity card: 2–4K characters (50–80 lines)
- 10K — 2.5x margin for complex methods with expanded inputs/outputs
- Above 10K — almost always a sign of mixing two entities or didactic content in the ontology

---

## Extended Manifest

Manifest MUST contain an **Entity Index** section — a full list of all entities with summaries:

```markdown
## Entity Index

| ID | Name | Kind | Summary | Status |
|----|------|------|---------|--------|
| DP.D.001 | Object ≠ Model | D | Model simplifies; abstraction must not be confused with reality | active |
| DP.M.001 | Knowledge Extraction | M | Transformation of raw information into pack-compatible entities | active |
| DP.WP.001 | Extraction Report | WP | Structured extraction report with classifications | active |
| DP.FM.001 | Information as Knowledge | FM | Raw information is accepted as formalized knowledge | active |
```

**Requirement:** Entity Index is generated automatically from file frontmatter (see Auto-MAP section).

---

## Extended Frontmatter

### New required fields

```yaml
---
id: DOMAIN.M.XXX
name: Method Name
status: draft | active | deprecated
summary: "One sentence describing this entity for retrieval and index generation"
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
---
```

**`summary`** (required, new):
- One sentence, <= 150 characters
- Sufficient to understand the entity without reading the full file
- Used in Entity Index, MAP, and retrieval

### New optional fields

```yaml
---
# ... required fields ...
related:
  produces: [DOMAIN.WP.001]           # Typed: what it produces
  uses: [DOMAIN.D.006, DOMAIN.D.001]  # Typed: what it uses
  fails_with: [DOMAIN.FM.001]         # Typed: which errors
  requires_role: [DOMAIN.R.001]       # Typed: which roles are needed
  precedes: [DOMAIN.M.002]            # Typed: what it precedes
  follows: [DOMAIN.M.003]             # Typed: what follows it
  component_of: [DOMAIN.M.004]        # Typed: part of what
tags: [extraction, knowledge, formalization]  # For search
---
```

**`related` (typed):**
- Replaces flat list `related: [DP.WP.001, DP.FM.002]`
- Each link has a type (produces, uses, fails_with, etc.)
- Enables building a Knowledge Graph and navigating by links
- Backward compatibility: flat list is still valid, but deprecated

**`tags`:**
- Free labels for full-text search
- Supplement ID-based navigation with semantic search

---

## Auto-MAP

### Requirement

MAP (`07-map/DOMAIN.MAP.001.md`) MUST be generated automatically from Pack file frontmatter.

### Mechanism

1. Script `scripts/generate-map.py` (template in SPF)
2. Run: manually, pre-commit hook, or CI
3. Input: all `.md` files in Pack with YAML frontmatter
4. Output: updated MAP + Entity Index in manifest

### What is generated

- Tables: Core Distinctions, Methods, Work Products, Failure Modes, SoTA Annotations
- Dependency graph (from typed `related:`)
- Statistics: counts, coverage, staleness (entities not updated >90 days)
- Warnings: broken links, missing summary, unregistered kinds

---

## Sub-Pack Protocol

### When to extract a Sub-Pack

A Pack extracts a sub-domain into a separate Pack when:

1. **A separate bounded context emerges** — with its own object of description and truth criteria
2. **Files > 100** in one sub-domain (indicator, not criterion)
3. **A separate maintainer appears** — a different person/team manages this part of knowledge

**Test:** if a standalone bounded context (01A) can be written for the sub-domain — it is a Sub-Pack.

### Mechanism

1. Create a new Pack repo with a separate `pack_id`
2. Register in the context registry (SPF.SPEC.001)
3. Establish cross-pack links
4. Original Pack references Sub-Pack in manifest (Dependencies)

---

## Future: MCP server for Pack

> This is an architecture description, not a current version requirement.

When Pack volume exceeds 100 files, an MCP server with the following tools is recommended:

| Tool | Description |
|------|-------------|
| `pack_search(query, kind?)` | Search entities by summary/tags + optional kind filter |
| `pack_get(id)` | Load full entity card by ID |
| `pack_list(kind)` | List all entities of a given kind |
| `pack_graph(id, depth?)` | Entity link graph (from typed related) |
| `pack_stats()` | Pack statistics: counts, staleness, coverage |

Implementation: Python + frontmatter parser + vector search (embeddings of summary fields).

---

## Checklist for Pack authors

- [ ] Each entity card <= 10,000 characters (otherwise decompose)
- [ ] Each entity card has `summary` in frontmatter
- [ ] `related:` is typed (produces, uses, fails_with, etc.)
- [ ] Entity Index in manifest is current (or auto-generated)
- [ ] MAP is generated automatically (script configured)
- [ ] At > 50 files: check whether there are Sub-Pack candidates
- [ ] At > 100 files: consider MCP server for retrieval

---

## Backward compatibility

| Change | Compatibility |
|--------|--------------|
| `summary` in frontmatter | New required field. Existing Packs: add at next update |
| Typed `related:` | Flat list is still valid, but deprecated. Migrate gradually |
| `tags` | Optional. No backward incompatibility |
| Auto-MAP | Manual MAP is still valid. Auto-generation is a recommendation, not a requirement |
| Entity Index in manifest | New required section. Add at next update |

---

*This document: `SPF.SPEC.003`*


# SOURCE_FILE: spec/SPF.SPEC.004-service-clauses.md
---
---
id: SPF.SPEC.004
name: Service Clause — domain's user-facing promises
status: active
created: 2026-03-30
related:
  - SPF.SPEC.001
  - DP.SOTA.001
---

# SPF.SPEC.004 — Service Clause vs Use Case

## 1. Problem

In Pack development practice, confusion arises between two distinct entities:

- **What the domain promises** to the consumer (regardless of implementation)
- **How** the consumer interacts with the system to achieve a goal

This confusion leads to mixing the Pack level (domain promises) and DS level (interaction scenarios) in a single file or folder.

---

## 2. Distinction: Service Clause ≠ Use Case

### Service Clause (SC) — user-facing promise

| Attribute | Value |
|-----------|-------|
| **What it is** | Domain contract: to whom, what, under what condition is guaranteed |
| **Level** | Domain (Pack) — implementation-independent |
| **Question** | "What does the platform/domain guarantee?" |
| **Changes when** | The domain promise changes (strategic decision) |
| **Where it lives** | `08-service-clauses/` in Pack |
| **Code** | `<CONTEXT>.SC.<NNN>` |

**Format:** "If [actor] [condition] → the domain ensures [guarantee]"

**Example:** `DP.SC.001` — "If a user opens a working day → the platform provides day context (commits, tasks, calendar)"

### Use Case (UC) — interaction scenario

| Attribute | Value |
|-----------|-------|
| **What it is** | Description of the sequence of interactions between an actor and a system |
| **Level** | System (DS) — implementation-dependent |
| **Question** | "How exactly is the goal achieved in a specific system?" |
| **Changes when** | The interface or implementation changes |
| **Where it lives** | `08-use-cases/` in DS repository |
| **Code** | `<SYSTEM>.UC.<NNN>` (not in Pack) |

**Format:** Main flow, alternative flows, preconditions, postconditions

---

## 3. Theoretical basis

### DDD Strategic (DP.SOTA.001): Published Language

In strategic DDD (Khononov, Evans) **Published Language** is the Bounded Context interface for external consumers: what the BC guarantees regardless of internal design. Service Clause is an implementation of Published Language at the Pack level.

Use Cases are **Application Services** within a BC: specific execution scenarios dependent on technologies and implementation. They belong to DS, not Pack.

### FPF A.7: Strict Distinction (Method ≠ Scenario)

FPF A.7 requires separating:
- **Method** (capability, what can be produced) — domain description level
- **Scenario** (step-by-step how) — implementation level

By the same logic:
- **Promise** (what is guaranteed) — Pack level
- **Interaction scenario** (how it is achieved step by step) — DS level

### Service Design / SLA pattern

In Service Design (Stickdorn, Schneider) they distinguish:
- **Service Promise** — what the service commits to ensure (channel-independent)
- **Service Blueprint** — how exactly the service is delivered in a specific channel

Service Clause = Service Promise. Use Case = part of Service Blueprint.

---

## 4. Application rules

### 4.1 Where to place

| Entity | Level | Folder | Example |
|--------|-------|--------|---------|
| Service Clause | Pack | `08-service-clauses/` | `DP.SC.001-daily-planning.md` |
| Use Case | DS | `08-use-cases/` (in DS repo) | `SystemName.UC.001-open-day.md` |

### 4.2 How to distinguish SC from UC

**Test 1 — Implementation question:**
> "If the implementation changes (different interface, different language, different framework), will this file change?"
- No → this is an SC (Pack)
- Yes → this is a UC (DS)

**Test 2 — Guarantee vs steps:**
> Does the file describe a promise (what is guaranteed) or steps (how to interact)?
- Promise → SC
- Steps → UC

**Test 3 — Actor-condition-guarantee:**
> Can it be formulated as "If [actor] [condition] → the domain guarantees [result]"?
- Yes → SC
- No (steps need to be described) → UC

### 4.3 Mixed format (permissible exception)

Operational Packs (e.g. PACK-verification) may contain SCs with a brief execution protocol. This is permissible if:
- The protocol is an integral part of the promise (the SC cannot be understood without it)
- The protocol does not depend on a specific system implementation

Sign of violation: the protocol describes specific UI steps, API calls, or technical details → move to DS.

---

## 5. SC card structure (canonical format)

```markdown
---
id: <CONTEXT>.SC.<NNN>
name: <Short promise name>
kind: SC
status: active | draft | deprecated
layer: L4-Personal | L2-Platform | L3-Template
actor: <who receives the promise>
condition: <under what condition>
guarantee: <what is guaranteed>
created: YYYY-MM-DD
related:
  extends: []      # Higher-level SC
  depends_on: []   # Other SCs without which this doesn't work
---

# <CONTEXT>.SC.<NNN> — <Name>

## Promise

<One sentence: actor + condition + guarantee>

## Trigger

- <condition 1>
- <condition 2>

## Guarantee

<What the domain commits to ensure. No implementation steps.>

## Participants (optional for operational Packs)

| Role | Who |

## Exceptions

<Under what conditions the promise does not apply>
```

---

## 6. SC kind code in SPF.SPEC.001

Service Clause (`SC`) is added to the base kinds table:

| Code | Kind | Pack folder |
|------|------|-------------|
| `SC` | Service Clause | `08-service-clauses/` |

---

## 7. Migration of existing Packs

Packs with an `08-use-cases/` folder containing `*.SC.*` files:
1. Rename the folder: `08-use-cases/` → `08-service-clauses/`
2. Update the repo's CLAUDE.md
3. Update all references

Packs with an `08-use-cases/` folder containing `*.UC.*` files (actual Use Cases):
- Evaluate using tests from §4.2
- If it truly is a UC → keep the filename, move to DS
- If it is an SC named as UC → rename files to `*.SC.*` + rename folder

---

*This document: `SPF.SPEC.004`*


# SOURCE_FILE: spec/SPF.SPEC.005-boundary-rules.md
---
---
id: SPF.SPEC.005
name: Boundary Rules — Pack and Database Decomposition
status: draft
created: 2026-04-21
depends_on: [SPF.SPEC.001, FPF.A.1.1]
---

# Boundary Rules — Pack and Database Decomposition

> SPF specification: decision rules for (a) when a new Pack must be created and (b) when a new runtime database must be separated. Both decisions answer the same structural question — «is this one BoundedContext or two?» — at different scales.

---

## Problem

Two recurring decisions in SPF work:

1. **Pack decision.** A new topic appears (service, domain, concept). Is it a section inside an existing Pack, a new Pack, or a draft that has not earned Pack status yet?
2. **Runtime database decision.** A new data area appears (new entity, new event stream). Does it go into an existing database, or does it require a separate database with its own schema and lifecycle?

Historically both decisions were made ad-hoc, by analogy with neighbouring files/databases, without explicit criteria. Result: Pack-fork (a new Pack that duplicates 80% of an existing one), Pack-process (name is a verb, not a domain), Pack-thin (a Pack with one method and no work-products), and databases whose names encode implementation details (`aist_bot`, `content-pipeline`) rather than bounded contexts.

**SPF.SPEC.005 fixes the form of both decisions as binary multiple-choice gates** — the same shape as ArchGate in PACK-digital-platform. Quantitative thresholds (percentages, weights, scores) are banned: they invite calibration by feel rather than by substance.

---

## Hard constraint: decision form

Every decision below is a **binary checklist**. For each test there is an explicit definition of «выполняет» (passes). The decision rule is the conjunction — all tests must pass. Any «no» or «unclear» blocks the decision.

Banned in boundary decisions:
- percentages (`>30% overlap`)
- weighted scores (`T1=3, T2=2, threshold ≥6`)
- arbitrary «N of M» without reasoned criteria for the choice of M and N

Rationale: quantitative thresholds without calibration on historical data are smoke. Numbers get picked «from the head», applied inconsistently, and fail to catch what they were supposed to catch. A qualitative binary checklist with an explicit «passes» definition for each item is applied uniformly by any agent, and can be audited after the fact. ArchGate (DP.ARCH.001) is the reference implementation of this form.

See also: `memory/feedback_decision_gates.md` (authoring memory).

---

## Part A. Pack Boundary Decision

### A.1. Decision gate (T1–T4, ArchGate-style)

A new Pack is created **only when all four tests pass**.

| Test | Statement | Passes when |
|------|-----------|-------------|
| **T1. Own primary question** | The candidate has a distinct primary question | The question is stated in one sentence, references a BoundedContext different from every neighbouring Pack, and is not a rephrasing of a neighbouring Pack's question |
| **T2. Own stable work-product type** | The candidate produces an artefact type absent in every neighbouring Pack | At least one WP type (contract, diagram class, checklist, report format) exists in the candidate and cannot be placed inside any existing Pack without breaking that Pack's scope |
| **T3. Own set of distinctions** | The candidate has its own semantic boundary | At least one pair of terms (A ≠ B) exists such that without the candidate's context the distinction cannot be made. Pure import from a neighbouring Pack (same A ≠ B, same justification) does not count |
| **T4. Own glossary** | The candidate carries its own vocabulary | Terms used inside the candidate are defined locally (with references to FPF UTS where applicable). Terms imported from neighbouring BoundedContexts are imported through an explicit Anti-Corruption Layer, not copy-pasted |

**Decision rule:** all four pass → new Pack (status: `draft` until full manifest is filled). Any «no» or «unclear» → **not a Pack** (section inside an existing Pack, or draft outside Pack tree with `promote_by: YYYY-MM`).

### A.2. Structural rules (apply after the decision)

Once a Pack is created, four structural invariants hold:

| Rule | Statement |
|------|-----------|
| **Context Isolation** | No foreign keys between Pack entities. Cross-Pack links go through Bridges (FPF B.3) only |
| **Cohesion** | Every entity in a Pack sits in a single coherent BoundedContext. The «why does this belong here?» test is answerable in one sentence |
| **Anti-Corruption Layer** | Data imported from upstream (other Packs, external systems) is validated against the local Glossary at the boundary. No silent passthrough |
| **Naming semiotics** | Pack name is unique in the SPF tree, distinguishable from neighbouring Packs, and free of homonyms with FPF kernel terms |

### A.3. Passport fields (SPF.SPEC.005-compliant manifest)

Every Pack manifest (`00-pack-manifest.md`) must include:

- `pack_id` — short code
- `pack_name` — full domain name, noun
- `fpf_bounded_context_id` — `<DOMAIN>:<ContextName>_v<version>` (FPF A.1.1)
- `version` — semantic version
- `status` — `draft | active | deprecated`
- `primary_question` — one sentence (T1)
- `glossary` — inline or linked, terms defined locally (T4)
- `invariants` — statements that hold for every entity in this Pack
- `scope_in` — what this Pack covers
- `scope_out` — what it explicitly does not cover
- `bridges` — links to neighbouring Packs with ACL markers
- `name_rationale` — why this name was chosen (paragraph)
- `external_sources` — FPF edition, SoTA references
- `acl_location` — where ACL validators live (if cross-Pack import exists)
- `model_categories` — which of the eight WP-257 categories the Pack describes. Multi-value: one or more of `persona`, `memory`, `context` (user-model layers), `platform-knowledge`, `catalog`, `service-ops`, `relational`, `proto-persona` (outside user-model). A Pack may cover several categories only if the border between them is documented in `scope_in` / `scope_out`. See DP.D.050, WP-257.

---

## Part B. Runtime Database Boundary Decision

### B.0. Model category assignment (prerequisite to B1–B4)

Before applying B1–B4, classify the candidate data into **one** of eight WP-257 categories. The classification determines writer/owner boundary upfront and blocks B1 questions that apply «in a vacuum».

**Three user-model layers** (data about one specific user):

| Category | Writer | Owner (source-of-truth) |
|----------|--------|------------------------|
| `persona` | user (or agent by delegation with acceptance) | user's Git repo |
| `memory` | platform services | Neon |
| `context` | runtime agent | ephemeral (not stored) |

`memory` has two internal levels — **Observed** (events, logs) and **Derived** (aggregates, baselines, indicators). They may share one DB with separate schemas, or split into two DBs if B1–B4 pass independently.

**Five categories outside the user model** (data with non-user writer/owner):

| Category | Typical writer | Typical owner |
|----------|----------------|---------------|
| `platform-knowledge` | platform team via indexers | team's shared ontology (Git + projection) |
| `catalog` | admin/ops via Directus-like tools | reference data registry |
| `service-ops` | observability collectors, finance/ops services | ops team |
| `relational` | matching/community services | community-ops team |
| `proto-persona` | landing/acquisition services | pre-Ory lead registry, claim-transferable |

**Decision rule:** exactly one category → proceed to B1–B4. Two or more categories claimed for one candidate → **split the candidate** (one DB per category), or justify as a deliberate multi-category DB with explicit writer/owner mapping per table.

**Why this step precedes B1–B4:** category assignment fixes writer + owner before boundary tests. Without it, B1 («single owner») is answered by pointing at a transport writer (ingestion-gateway, relay) and hiding the real semantic owner, which is the WP-257 failure mode.

### B.1. Decision gate (B1–B4, same form as T1–T4)

A new runtime database is created **only when all four tests pass**.

| Test | Statement | Passes when |
|------|-----------|-------------|
| **B1. Single writer-owner (semantic source-of-truth)** | The candidate data has one **semantic** owner of writes — the service that produces the meaning, not a transport relay | One and only one semantic writer. Transport writers (ingestion-gateway, outbox relay, event bus) do not count — the test identifies who produces the meaning, not who persists the bytes. If two services produce meaning, either they share the same BoundedContext (merge) or the data must split (per WP-257 writer/owner criterion) |
| **B2. Own invariant** | The candidate enforces an invariant that neighbouring databases do not | At least one integrity constraint (business invariant, not merely technical FK) holds here and is not meaningful outside this database |
| **B3. Independent blast radius** | Outage of this database does not cascade to neighbouring domains via read/write coupling | If this database is down, neighbouring services either continue with degraded functionality or fail in a bounded way. Tight coupling across the boundary means the boundary is wrong |
| **B4. Own vocabulary** | The candidate's table names, column names, and codes come from a local glossary | Terms align with one BoundedContext's Glossary. If half the tables speak one vocabulary and half another, the boundary is inside the database, not around it |

**Decision rule:** all four pass → new database. Any «no» or «unclear» → **not a new database** (schema inside an existing database, or postpone separation until the data area grows).

### B.2. Naming rules (N1–N5)

Applied to every new database name, and retroactively to existing names under review.

| Rule | Statement | Passes when |
|------|-----------|-------------|
| **N1. Noun-area** | Name is a noun naming a subject area | Name refers to a domain, not an action or a system (no `content-pipeline`, no `aist_bot`) |
| **N2. Central entity** | The central entity of the database is discoverable from the name | A reader who knows the domain can guess the primary table within 2 guesses |
| **N3. No technical markers** | Name is free of technical or historical markers | No `_v2`, no `_new`, no service/technology names (`neon_`, `pg_`, `bot_`) |
| **N4. Russian-concept available** | For projects with a Russian working vocabulary, a Russian single-word concept for the database exists and is recorded in `name_rationale` | A Russian noun-область captures the same boundary; it is documented even if the DB name uses Latin |
| **N5. Lowercase single word (or hyphenated short phrase)** | Name follows DB conventions | Lowercase; one word or short hyphenated phrase; matches PostgreSQL/Neon identifier conventions |

**Decision rule:** all five pass → name approved. Any «no» → rename required (or naming debt recorded as WP).

### B.3. Physical placement vs. logical boundary

B1–B4 define the **logical** BoundedContext boundary. Physical placement (one PostgreSQL cluster vs. many, one schema vs. many inside one cluster) is an implementation decision. The rule: every logical BC has a visible boundary — either separate database, or separate schema with an explicit `owner_service` marker in a central DB registry. Conflating physical «one cluster to save cost» with logical «one BoundedContext» is the most frequent source of boundary rot.

---

## Part C. Cross-cutting concerns

### C.1. Order of operations

When both Pack and database are created together (most common case for a new service):
1. Apply Part A (T1–T4). If Pack fails — stop; do not create a database for a Pack that does not exist.
2. If Pack passes, fill the manifest (including `model_categories`).
3. Apply Part B.0 — assign one of eight WP-257 categories to the data candidate.
4. Apply Part B (B1–B4) to decide runtime database.
5. Apply Part B.2 (N1–N5) for the name.

Reverse order («name the DB first, Pack later») is a **known failure mode** — the DB name locks the conceptual boundary prematurely.

### C.2. Retroactive audit

Existing Packs and databases are audited using the same checklists. A failed test is not automatic deletion — it becomes a decision:
- **Pack fails T-tests** → downgrade to section of neighbouring Pack, or keep as `draft` with `promote_by`
- **Database fails B-tests** → plan merge/split in an architecture roadmap (not immediate operation)
- **Name fails N-tests** → rename in a coordinated migration (separate WP)

### C.3. Hard bans

- SPF itself must not ship domain content while specifying these rules (SPF/CLAUDE.md §5.2). Examples below use placeholders, not real Pack content.
- No didactics in rule wording (SPF/CLAUDE.md §5.1). No «step 1 / step 2 / first learn then apply».

---

## Part D. Worked example (placeholder)

**Candidate:** a hypothetical service «Финансирование» (financing and accounting).

**Pack decision (T1–T4):**
- **T1** — primary question «Как платежи расписываются по разным получателям?» → yes (distinct from PD, DP, MIM, VR primary questions).
- **T2** — artefact types: ledger entry (double-entry), period close report, reconciliation report. Not present in any existing Pack → yes.
- **T3** — distinctions: «Платёж ≠ Проводка», «Получатель ≠ Счёт», «Биллинг ≠ Эквайринг». Not reducible to other Packs → yes.
- **T4** — glossary: accruals, ledger, journal entry, chart of accounts. Defined locally with ACL to PD.ARCH.004 §2 (payment classes) → yes.
- Decision: **new Pack** (candidate name: PACK-financing or Russian-concept equivalent).

**Database decision (B1–B4):**
- **B1** — single owner: service-Финансирование writes ledger and reconciliation. Service-Продвижение writes promotion events but not ledger → separate write ownership → yes.
- **B2** — own invariant: «every credit has a matching debit, balance closes at period end». Meaningful only inside accounting → yes.
- **B3** — blast radius: if ledger DB is down, bot/LMS/knowledge-mcp continue (they do not read ledger on hot path); billing writes are queued → yes.
- **B4** — vocabulary: accounts, entries, postings, periods. Local to one Glossary → yes.
- Decision: **new database** (candidate name under N1–N5).

**Name (N1–N5):**
- Candidates: `ledger`, `finance`, `accounting`, `billing`.
- `ledger` — N1 noun ✅, N2 central entity (ledger entries) ✅, N3 no tech markers ✅, N4 Russian concept «главная книга» ✅, N5 single lowercase ✅ → approved.
- `billing` — N2 central entity ambiguous (billing events vs. invoices) ⚠️ → runner-up.
- Russian-concept recorded: `главная книга` / `учёт платежей`.

**Split consideration.** Billing (raw payment events, idempotency keys, payment_method tokens) may itself be a separate BoundedContext from accounting (ledger, period close). Retest B1–B4 for each candidate — if both pass independently, two databases; if billing fails B2 (no own invariant beyond idempotency), it is a schema inside `ledger`.

---

## References

- FPF A.1.1 — BoundedContext as kernel holon
- FPF B.3 — Bridges between BoundedContexts
- DP.ARCH.001 §7 — ArchGate form (binary criteria pattern)
- DP.D.050 — Persona ≠ Memory ≠ Context (user-model layer classification)
- WP-257 — Persona / Memory / Context replacing «ЦД» monolith; writer+owner criterion; eight-category taxonomy
- SPF.SPEC.001 — entity coding
- `memory/feedback_decision_gates.md` — authoring rule: no percentages, no weights, no scores

---

## Completion criteria for this spec

| Criterion | Test |
|-----------|------|
| Both gates are binary | Every test has an explicit «passes when» definition |
| No quantitative thresholds | No percentages, weights, or scores anywhere |
| Order of operations is fixed | Pack decision precedes category assignment, category precedes B1–B4 |
| WP-257 category assignment is explicit | Part B.0 lists all eight categories with writer/owner |
| Passport fields listed | Manifest required fields enumerated, including `model_categories` |
| Worked example present | At least one placeholder application shown |
