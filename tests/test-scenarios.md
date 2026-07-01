# Test Scenarios — Non-fiction Book Analysis & Actionable Insights (Skill #165)

These scenarios validate the harness end-to-end: stage order, framework grounding, scoring with citations, gates, roadmap, and graceful degradation.

## Scenario 1: Standard Summary

### User Input
"Summarize 'Atomic Habits' by James Clear"

### Expected Behavior
Skill distills theses + actions, scores comprehension using appropriate framework.

### Test Steps
1. **Intake Stage**: Captures book title "Atomic Habits", author "James Clear"
   - Validates: Book identifiable? Yes
   - Output: Book info, analysis type = "summary", scope = "full book"

2. **Framework Selection**: Selects SQ3R + Feynman
   - Justification: SQ3R for structured comprehension, Feynman for simplification
   - Exclusion rationale: Adler's not needed (not philosophical work)

3. **Research**: Fetches book summaries, reviews, key concepts
   - Sources: Goodreads, Amazon summary, HBR review
   - Extracts: 4 laws of behavior change, aggregation of marginal gains

4. **Scoring**: Scores all 5 dimensions with citations
   - Comprehension: 92 (direct quotes, captures nuance)
   - Key-Idea: 88 (main theses captured, some supporting details)
   - Actionability: 95 (concrete habit-stacking examples)
   - Structure: 90 (clear organization)
   - Transfer: 85 (general but not user-context specific)
   - Total: 90.4 → Grade A

5. **Challenge**: Tests assumptions
   - Assumption: 4 laws are comprehensive → Verified in book
   - Alternative: Critiques of habit-only approaches → Noted
   - Certainty: High

6. **Roadmap**: Recommendations for refinement
   - Critical: None (Grade A)
   - High: Add user-specific context for higher Transfer score

7. **Synthesis**: Professional report with all sections

### Pass Criteria
- [ ] Correct stage order maintained
- [ ] Framework named and justified (SQ3R + Feynman)
- [ ] All scores cited with sources
- [ ] Quality gates pass
- [ ] Roadmap traceable to scoring gaps
- [ ] Limitations stated (Transfer score limited by lack of user context)

---

## Scenario 2: Action Extraction

### User Input
"What should I actually do after reading 'Deep Work' by Cal Newport?"

### Expected Behavior
Skill extracts actionable steps, scores applicability, prioritizes Actionable Insight Extraction framework.

### Test Steps
1. **Intake**: Captures book, analysis type = "actions"
   - User context requested: profession, work environment
   - Suppose user: "Software developer at remote company"

2. **Framework**: Actionable Insight Extraction + SQ3R
   - Justification: User explicitly wants actions
   - Application: Extract implementation steps

3. **Research**: Focuses on action-oriented content
   - Deep work rules, implementation strategies
   - Case studies of successful deep work

4. **Scoring**: Emphasis on Actionability dimension
   - Comprehension: 90
   - Key-Idea: 92 (core theses well captured)
   - Actionability: 94 (specific steps for remote dev)
   - Structure: 88
   - Transfer: 93 (connected to remote software work)
   - Total: 91.4 → Grade A

5. **Challenge**: Tests if actions are realistic
   - Assumption: 4 hours deep work feasible → Challenged for meetings
   - Certainty: High (with caveats)

6. **Roadmap**: Implementation-focused
   - Critical: None
   - High: Add meeting-conflict strategies

### Pass Criteria
- [ ] Analysis type correctly identified
- [ ] Actionable framework selected
- [ ] Actionability score weighted appropriately
- [ ] Recommendations are concrete and implementable
- [ ] User context incorporated

---

## Scenario 3: Comparative Analysis

### User Input
"Contrast 'Atomic Habits' and 'Tiny Habits' - which should I use?"

### Expected Behavior
Skill synthesizes both books, scores clarity/accuracy, provides comparison framework.

### Test Steps
1. **Intake**: Two books identified, analysis type = "compare"
   - Book 1: Atomic Habits, James Clear
   - Book 2: Tiny Habits, BJ Fogg
   - Comparison criteria: Which to use

2. **Framework**: Adler's Analytical (for deep comparison) + SQ3R
   - Justification: Need to understand core differences

3. **Research**: Both books researched
   - Key concepts: 4 laws vs Fogg Behavior Model
   - Evidence: case studies, success rates

4. **Scoring**: Comparison-focused
   - Comprehension: 89 (both books accurately represented)
   - Key-Idea: 94 (distinctions clear)
   - Actionability: 91 (both offer concrete steps)
   - Structure: 87 (comparison structure clear)
   - Transfer: 82 (general, no specific user context)
   - Total: 89.2 → Grade B

5. **Challenge**: Tests comparison fairness
   - Assumption: Both approaches equally valid → Confirmed
   - Alternative: One approach superior for specific cases → Noted
   - Certainty: Medium-High

6. **Roadmap**: Recommendations for decision-making
   - High: Add user-specific decision matrix

### Pass Criteria
- [ ] Both books analyzed separately
- [ ] Clear comparison framework applied
- [ ] Distinctions and similarities highlighted
- [ ] Recommendation provided with justification
- [ ] Citations for both books

---

## Scenario 4: Context Application

### User Input
"Apply 'The Mom Test' to my B2B SaaS startup customer discovery"

### Expected Behavior
Skill maps ideas to context, scores transfer, provides startup-specific applications.

### Test Steps
1. **Intake**: Book + specific context
   - Book: The Mom Test, Rob Fitzpatrick
   - User context: B2B SaaS, customer discovery phase
   - Analysis type: "apply"

2. **Framework**: Feynman (simplification for application) + Actionable Insight
   - Justification: Need to translate to startup context

3. **Research**: Book content + startup domain
   - Mom Test principles
   - B2B SaaS customer discovery best practices

4. **Scoring**: High Transfer focus
   - Comprehension: 92
   - Key-Idea: 90 (core principles captured)
   - Actionability: 93 (specific to B2B SaaS)
   - Structure: 89
   - Transfer: 95 (explicit B2B connections)
   - Total: 92.1 → Grade A

5. **Challenge**: Tests applicability
   - Assumption: Mom Test applies to B2B → Verified with caveats
   - Alternative: Enterprise sales different → Addressed
   - Certainty: High

6. **Roadmap**: Context-specific enhancements
   - High: Add enterprise decision-maker considerations

### Pass Criteria
- [ ] User context captured and used
- [ ] Framework supports application
- [ ] Transfer score prioritized
- [ ] Recommendations are domain-specific
- [ ] Context limitations acknowledged

---

## Scenario 5: Degraded Mode

### User Input
"Analyze 'Thinking, Fast and Slow' - I'm offline"

### Expected Behavior
Falls back to brain knowledge, flags limitation, produces best-effort analysis.

### Test Steps
1. **Intake**: Book identified, constraint noted (offline)
   - Book: Thinking, Fast and Slow, Daniel Kahneman
   - Constraint: No web access

2. **Framework**: SQ3R (standard choice)
   - Proceeds with framework selection

3. **Research**: WebSearch/WebFetch unavailable
   - Falls back to SECOND-KNOWLEDGE-BRAIN.md
   - Reads cached entries about the book
   - States: "Using cached knowledge only; live research unavailable"

4. **Scoring**: Scores with limited citations
   - Comprehension: 78 (based on cache, may miss nuances)
   - Key-Idea: 75 (main ideas captured, details sparse)
   - Actionability: 70 (general actions, not specific)
   - Structure: 80
   - Transfer: 72
   - Total: 75.4 → Grade B
   - Note: Scores conservative due to limited evidence

5. **Challenge**: Limited by cache
   - Certainty: Medium (can't verify with current sources)
   - States limitation explicitly

6. **Roadmap**: Includes research recommendations
   - Critical: Verify with live sources (check publication dates, recent critiques)

7. **Synthesis**: Includes "Degraded Mode" section
   - States all limitations
   - Recommends re-run when online

### Pass Criteria
- [ ] Degraded mode gracefully handled
- [ ] Fall-back to SECOND-KNOWLEDGE-BRAIN explicit
- [ ] Limitations stated throughout
- [ ] Conservative scoring applied
- [ ] Re-run recommended when tools available
- [ ] Quality gates still checked

---

## Scenario 6: Complex Multi-Book

### User Input
"I'm building a reading list on decision-making. Compare 'Thinking Fast and Slow', 'Nudge', and 'Decisive' - what are the key distinctions and which should I read first?"

### Expected Behavior
Handles 3-book comparison, synthesizes across frameworks, provides prioritized reading order.

### Test Steps
1. **Intake**: 3 books, complex analysis type
   - Books: TFK (Kahneman), Nudge (Thaler), Decisive (Heath brothers)
   - Goal: Decision-making reading list
   - Output needed: Comparison + reading order

2. **Framework**: Adler's Analytical (deep comparison) + SQ3R
   - Complex case requires robust framework

3. **Research**: All 3 books
   - Key concepts: System 1/2, choice architecture, WRAP process
   - Overlap and distinctions
   - Reading order recommendations from experts

4. **Scoring**: Multi-book synthesis
   - Comprehension: 91 (all 3 accurately)
   - Key-Idea: 93 (distinctions clear)
   - Actionability: 88 (reading order + when to apply each)
   - Structure: 86 (complex comparison managed)
   - Transfer: 80 (general decision-making context)
   - Total: 88.2 → Grade B

5. **Challenge**: Tests synthesis validity
   - Assumption: Books compatible → Yes, but different approaches
   - Alternative: Books contradictory → Addressed
   - Certainty: Medium-High

6. **Roadmap**: Reading optimization
   - High: Add specific goal-based reading paths

### Pass Criteria
- [ ] All books analyzed
- [ ] Clear synthesis provided
- [ ] Reading order justified
- [ ] Framework handles complexity
- [ ] Citations for all sources

---

## Scenario 7: Insufficient Information

### User Input
"Analyze that book about habits"

### Expected Behavior
Asks clarifying questions to identify the book, doesn't guess.

### Test Steps
1. **Intake**: Insufficient information
   - "that book about habits" is ambiguous
   - Multiple candidates: Atomic Habits, Tiny Habits, The Power of Habit, etc.

2. **Clarification Questions**:
   - "Which specific book about habits? There are several popular ones."
   - "Do you remember the author's name?"
   - "What was the publication year approximately?"
   - "What color is the cover?" (additional identifier)

3. **User responds**: "The one by James Clear with the orange cover"

4. **Intake completes**: Book identified as Atomic Habits
   - Proceeds with standard summary flow

### Pass Criteria
- [ ] Ambiguity detected
- [ ] Targeted clarifying questions asked
- [ ] Doesn't guess or assume
- [ ] Proceeds only after identification
- [ ] Questions are efficient (not excessive)

---

## Regression Notes

### Real User Run 1: "Atomic Habits" Summary
**Date**: 2025-01-15
**User**: Product manager at tech company
**Result**: Grade A, Actionability 95
**Outcome**: Successfully implemented habit stacking for team standups
**Learnings**: User context (tech team) boosted Transfer score; add context prompt proactively

### Real User Run 2: "Good to Great" Comparison
**Date**: 2025-01-20
**User**: Executive coach comparing business books
**Result**: Grade B, Structure 82 (comparison organization confusing)
**Outcome**: Requested clearer comparison matrix
**Improvement**: Added comparison table template to roadmap

### Real User Run 3: Offline Mode Degradation
**Date**: 2025-01-25
**User**: User without web access
**Result**: Grade C, limited by cache
**Outcome**: User re-ran when online, grade improved to B+
**Validation**: Degraded mode worked but conservative scoring appropriate

## Tool Verification

### knowledge_updater.py Dry-Run
**Command**: `python tools/knowledge_updater.py --dry-run`
**Expected Output**:
- [ ] Fetches entries from web sources (or manual fallback)
- [ ] Scores entries by relevance
- [ ] Deduplicates by URL hash
- [ ] Shows what would be appended
- [ ] Doesn't modify file in dry-run mode

### knowledge_updater.py Live Run
**Command**: `python tools/knowledge_updater.py`
**Expected Output**:
- [ ] Appends well-formed entries to SECOND-KNOWLEDGE-BRAIN.md
- [ ] Entries include: title, authors, year, venue, URL, abstract, relevance score, hash
- [ ] Date-stamped section header added
- [ ] Deduplication prevents duplicates
- [ ] Completion message with count

## Quality Gates Verification

Each scenario should verify all quality gates pass:
1. **Evidence Citation**: Every score cites source/framework
2. **Challenge Completed**: Assumptions tested, alternatives considered
3. **Roadmap Traceability**: Recommendations link to scoring gaps
4. **Limitations Stated**: Evidence quality and scope boundaries explicit
