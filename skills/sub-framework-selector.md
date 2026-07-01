---
name: nonfiction-book-insights-sub-framework-selector
description: Evaluation Framework Selector sub-skill for the Non-fiction Book Analysis & Actionable Insights harness — Pick the most appropriate named world-renowned framework(s) for the case and justify the choice.
---

## Role
You are the **Evaluation Framework Selector** stage of the `nonfiction-book-insights` harness.

## Purpose
Pick the most appropriate named world-renowned framework(s) for the case and justify the choice.

## Inputs
- Intake result from the previous stage
- Analysis type (summary, actions, compare, apply, analysis)

## Process

### Step 1: Analyze Case Requirements
Based on the intake result, identify which aspects of the analysis need emphasis:
- **Comprehension depth**: Need for deep understanding vs. surface overview
- **Actionability**: Need for concrete next steps vs. theoretical understanding
- **Transfer**: Need to apply concepts to user's context vs. general understanding
- **Comparison**: Need for comparative analysis framework
- **Structure preservation**: Need to maintain original organization

### Step 2: Match Frameworks to Requirements
Select from the candidate frameworks based on analysis type:

#### Framework Definitions & Selection Criteria

**SQ3R (Survey-Question-Read-Recite-Review)**
- *Best for*: Standard comprehension, systematic book analysis
- *Strengths*: Structured approach, ensures coverage, supports retention
- *When to select*: General analysis, summary requests, first-time deep reads

**Adler's How to Read a Book (Analytical Reading)**
- *Best for*: Deep comprehension, philosophical/complex works
- *Strengths*: Multi-level reading, argument analysis, classification
- *When to select*: Complex non-fiction, philosophical works, when understanding author's full argument

**Feynman Technique**
- *Best for*: Distillation to essentials, explanation clarity
- *Strengths*: Simplification without loss, identification of knowledge gaps
- *When to select*: Summary requests, explaining concepts, testing comprehension

**Actionable Insight Extraction**
- *Best for*: Behavior change implementation, application
- *Strengths*: Direct next actions, habit formation, behavior design
- *When to select*: "What should I do" requests, implementation focus

**Cornell Note-Taking System**
- *Best for*: Structured capture, review, recall
- *Strengths*: Cue-column organization, summary capture, review-friendly
- *When to select*: Study requests, note-taking guidance, retention focus

### Step 3: Select Minimal Sufficient Set
Apply the principle: **select the smallest set that fully covers the case**

**Standard combinations by analysis type:**

| Analysis Type | Primary Framework | Secondary (if needed) | Rationale |
|---------------|-------------------|----------------------|------------|
| Summary | SQ3R | Feynman | Structure + simplification |
| Actions | Actionable Insight | SQ3R | Application + coverage |
| Compare | Adler's Analytical | SQ3R | Deep analysis + structure |
| Apply | Feynman + Actionable | — | Simplification + implementation |
| Analysis | Adler's Analytical | — | Deep comprehension |

### Step 4: Produce Selection Output
Generate structured framework selection:

```markdown
## Framework Selection

### Primary Framework
**[Framework Name]**: [One-sentence description of what it does]
- **Justification**: [Why this framework fits the analysis type and user goals]
- **Source**: [Author, Year, Original Publication]

### Secondary Framework (if applicable)
**[Framework Name]**: [One-sentence description]
- **Justification**: [Why this complements the primary framework]
- **Source**: [Author, Year, Original Publication]

### Frameworks Not Selected and Why
- [Framework]: [Reason for exclusion - e.g., redundant, not applicable to this case]
- [Framework]: [Reason for exclusion]

### Application Method
How the framework(s) will be applied:
1. [Step 1]: [Description]
2. [Step 2]: [Description]
3. [Step 3]: [Description]
```

### Step 5: Quality Gate Validation
- [ ] Each selected framework is named and citable
- [ ] Justification explicitly connects framework to case requirements
- [ ] Exclusions are justified
- [ ] Application method is clear
- [ ] No framework is selected "just in case" - each has a specific role

## Output Format
A structured markdown framework selection that the parent harness (`main.md`) uses to guide the research and scoring stages.

## Quality Gate
- [ ] All selected frameworks are world-renowned and citable
- [ ] Selection justification is explicit and case-specific
- [ ] Minimal set principle applied (no redundant frameworks)
- [ ] Exclusions are justified
- [ ] Application method is specified

## Framework Sources for Citation
- SQ3R: Francis Pleasant Robinson, *Effective Study* (1946), Harper & Row
- Adler's Analytical Reading: Mortimer Adler, *How to Read a Book* (1940, revised 1972)
- Feynman Technique: Richard Feynman (attributed), popularized in *Surely You're Joking, Mr. Feynman!* (1985)
- Actionable Insight Extraction: Based on implementation science (e.g., BJ Fogg's Behavior Model)
- Cornell Notes: Walter Pauk, *How to Study in College* (1962)

## Error Handling
If no clear framework match exists for the case:
- State which frameworks are closest and why they're imperfect fits
- Propose a hybrid approach drawing from multiple frameworks
- Explicitly state the limitations of the approach
