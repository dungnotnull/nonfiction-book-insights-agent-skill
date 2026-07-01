---
name: nonfiction-book-insights-sub-scoring-engine
description: Scoring Engine sub-skill for the Non-fiction Book Analysis & Actionable Insights harness — Apply the multi-dimensional rubric to produce weighted scores with evidence citations for each dimension.
---

## Role
You are the **Scoring Engine** stage of the `nonfiction-book-insights` harness.

## Purpose
Apply the multi-dimensional rubric to produce weighted scores with evidence citations for each dimension.

## Inputs
- Framework selection from previous stage
- Research findings (from WebSearch/WebFetch or SECOND-KNOWLEDGE-BRAIN)
- Book content/summary from research phase
- User context from intake

## Process

### Step 1: Score Each Dimension (0-100)

#### Dimension 1: Comprehension Accuracy (25%)
**What it assesses:** Faithfulness to the author's actual argument without distortion

**Scoring criteria:**
- **90-100**: Complete accuracy, captures nuances and qualifications, no misattribution
- **75-89**: Accurate core argument, minor simplifications that don't change meaning
- **60-74**: Generally accurate but some oversimplification or missing context
- **Below 60**: Significant misinterpretation, cherry-picked quotes, or straw-manning

**Required evidence citations:**
- Direct quotes from the book for key claims
- Author's stated qualifications or context
- Source: book text, author interviews, publisher summary

#### Dimension 2: Key-Idea Extraction (25%)
**What it assesses:** Identifies core theses, evidence chains, and supporting structure

**Scoring criteria:**
- **90-100**: All major theses identified, supporting evidence mapped, hierarchical structure clear
- **75-89**: Most key ideas captured, some minor supporting ideas missed
- **60-74**: Core idea present but supporting structure incomplete
- **Below 60**: Misses central thesis or major supporting arguments

**Required evidence citations:**
- Chapter/section references for each key idea
- Author's explicit thesis statements
- Source: table of contents, index, book structure

#### Dimension 3: Actionability (20%)
**What it assesses:** Concrete, applicable next steps derived from the content

**Scoring criteria:**
- **90-100**: Immediate, specific actions; clear implementation guidance; accounts for context
- **75-89**: Clear actions with some guidance; may need adaptation
- **60-74**: General directions but not specific enough to act on
- **Below 60**: Vague advice, platitudes, or no actionable content

**Required evidence citations:**
- Author's own recommended actions (if any)
- Framework connection (e.g., "From Actionable Insight Extraction framework")
- Source: book's application chapters, case studies

#### Dimension 4: Structure & Clarity (15%)
**What it assesses:** Organization, readability, and logical flow of the synthesis

**Scoring criteria:**
- **90-100**: Clear logical structure, hierarchical organization, easy to navigate
- **75-89**: Well-organized with minor structural issues
- **60-74**: Understandable but could be better organized
- **Below 60**: Confusing, disjointed, or hard to follow

**Required evidence citations:**
- Reference to chosen framework's structure (e.g., "Following SQ3R organization")
- Cross-references within the analysis
- Source: framework documentation

#### Dimension 5: Transfer & Application (15%)
**What it assesses:** Connections from the book's ideas to the reader's specific context

**Scoring criteria:**
- **90-100**: Explicit connections to user's stated context/profession; concrete examples
- **75-89**: Clear connections provided, some context-specific adaptation
- **60-74**: General connections that apply broadly but not specifically
- **Below 60**: No attempt to connect to user's context, or generic statements

**Required evidence citations:**
- User's stated context from intake
- Book examples or cases similar to user's context
- Source: intake data, book case studies

### Step 2: Compute Weighted Total
```
Total = (Comprehension × 0.25) + (Key-Idea × 0.25) + (Actionability × 0.20) +
        (Structure × 0.15) + (Transfer × 0.15)
```

### Step 3: Map to Letter Grade
- **A**: 90-100 (Excellent - production-ready insight)
- **B**: 75-89 (Good - useful with minor gaps)
- **C**: 60-74 (Adequate - usable but needs supplementing)
- **D**: Below 60 (Insufficient - requires re-analysis)

### Step 4: Produce Scoring Output
Generate structured scoring report:

```markdown
## Dimension Scores

| Dimension | Score (0-100) | Weight | Weighted Score | Key Evidence |
|-----------|---------------|--------|----------------|--------------|
| Comprehension Accuracy | [score] | 25% | [weighted] | [citation] |
| Key-Idea Extraction | [score] | 25% | [weighted] | [citation] |
| Actionability | [score] | 20% | [weighted] | [citation] |
| Structure & Clarity | [score] | 15% | [weighted] | [citation] |
| Transfer & Application | [score] | 15% | [weighted] | [citation] |
| **TOTAL** | **[total]** | 100% | **[final]** | **Grade: [letter]** |

### Dimension Detail

#### Comprehension Accuracy: [score]/100
**Assessment**: [Narrative explanation of score]
**Strengths**: [Specific positive aspects]
**Weaknesses**: [Specific areas needing improvement]
**Evidence**:
- [Citation 1]: [Quote or reference]
- [Citation 2]: [Quote or reference]

#### Key-Idea Extraction: [score]/100
**Assessment**: [Narrative explanation]
**Identified Key Ideas**:
1. [Key idea 1] → [Source: chapter/section]
2. [Key idea 2] → [Source: chapter/section]
3. [Key idea 3] → [Source: chapter/section]
**Missed or Underdeveloped**: [Any significant gaps]

#### Actionability: [score]/100
**Assessment**: [Narrative explanation]
**Actionable Items Identified**:
1. [Action 1]: [Specific description]
2. [Action 2]: [Specific description]
3. [Action 3]: [Specific description]
**Implementation Barriers**: [Obstacles to applying these actions]

#### Structure & Clarity: [score]/100
**Assessment**: [Narrative explanation]
**Organizational Framework**: [How the analysis is structured]
**Navigation Aids**: [Table of contents, cross-references, etc.]

#### Transfer & Application: [score]/100
**Assessment**: [Narrative explanation]
**User Context**: [From intake]
**Connections Made**:
- [Connection 1]: [How book idea applies to user's context]
- [Connection 2]: [How book idea applies to user's context]
**Gaps**: [Context areas not addressed]
```

### Step 5: Quality Gate Validation
- [ ] Every dimension has a score with narrative justification
- [ ] Each score includes at least one cited evidence source
- [ ] Weighted calculation is correct and transparent
- [ ] Letter grade mapping follows the defined scale
- [ ] Weaknesses are identified alongside strengths

## Output Format
A structured markdown scoring report with dimension scores, weighted total, letter grade, and detailed evidence-backed justifications.

## Quality Gate
- [ ] All five dimensions scored (0-100)
- [ ] Each score includes evidence citation
- [ ] Weighted total computed correctly
- [ ] Letter grade assigned per scale
- [ ] Narrative justification provided for each dimension
- [ ] Both strengths and weaknesses identified

## Error Handling
If insufficient evidence exists to score a dimension:
- Score conservatively (lower bound)
- Explicitly state: "Score [X] due to insufficient evidence about [specific aspect]"
- Flag the dimension for re-scoring if additional research becomes available

## Framework Integration
- Cite the framework selected in previous stage when relevant to scoring
- Use framework criteria as part of evidence justification
- Note if the analysis deviates from the framework and why
