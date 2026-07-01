# Non-fiction Book Analysis & Actionable Insights

> A Claude Code skill that analyzes non-fiction books using world-renowned comprehension frameworks, extracting actionable insights with evidence-based scoring.

[![Skill Status](https://img.shields.io/badge/status-production--ready-green)](https://github.com/dungnotnull/nonfiction-book-insights-agent-skill)
[![Cluster](https://img.shields.io/badge/cluster-career--education-blue)](https://github.com/dungnotull/nonfiction-book-insights-agent-skill)
[![Version](https://img.shields.io/badge/version-1.0.0-brightgreen)](https://github.com/dungnotull/nonfiction-book-insights-agent-skill)

## Overview

This skill transforms how you read and apply non-fiction books. It uses proven methodologies like SQ3R, Adler's Analytical Reading, and the Feynman Technique to distill books into accurate summaries and concrete, actionable insights—scored for comprehension and applicability.

### What It Does

- **Summarize** complex non-fiction with faithful, citation-backed accuracy
- **Extract** concrete next actions you can implement immediately
- **Compare** multiple books to find the best fit for your goals
- **Apply** book concepts to your specific context (startup, career, life)
- **Score** analysis quality across 5 dimensions with evidence citations
- **Prioritize** recommendations by effort and impact

## Problem It Solves

Readers consume non-fiction without retaining or applying it because they lack a structured extraction method. This skill analyzes a book, distills key ideas, and produces actionable insights scored for comprehension and applicability.

## How It Works

The skill runs a 7-stage research-first workflow:

```
1. Intake           → Gather book info, scope, and user context
2. Framework        → Select world-renowned framework(s) for the case
3. Research         → Fetch highest-tier evidence with graceful degradation
4. Scoring          → Apply 5-dimensional rubric with citations
5. Challenge        → Test assumptions and alternative interpretations
6. Roadmap          → Generate prioritized, traceable recommendations
7. Synthesis        → Assemble professional report with quality gates
```

## Features

### Evidence-Based Scoring

Each analysis is scored across 5 dimensions with explicit evidence citations:

| Dimension | Weight | What It Assesses |
|-----------|--------|------------------|
| Comprehension Accuracy | 25% | Faithful to author's argument |
| Key-Idea Extraction | 25% | Identifies core theses and evidence |
| Actionability | 20% | Concrete, applicable next steps |
| Structure & Clarity | 15% | Organized, readable synthesis |
| Transfer & Application | 15% | Connects ideas to your context |

**Grade Mapping:** A (90+) — Excellent | B (75-89) — Good | C (60-74) — Adequate | D (<60) — Insufficient

### World-Renowned Frameworks

The skill selects and justifies frameworks from these citable sources:

- **SQ3R** (Francis Robinson, 1946) — Structured comprehension method
- **Adler's Analytical Reading** (Mortimer Adler, 1940/1972) — Deep understanding levels
- **Feynman Technique** (Richard Feynman) — Explain-to-understand distillation
- **Actionable Insight Extraction** (Implementation science) — Behavior change framework
- **Cornell Note-Taking** (Walter Pauk, 1962) — Structured capture for recall

### Graceful Degradation

When research tools are unavailable, the skill falls back to its cached knowledge base and explicitly states limitations—so you always know the confidence level of every insight.

### Self-Improving Knowledge Base

Weekly knowledge crawls continuously update the skill's understanding of:
- Latest nonfiction bestsellers and trends
- New reading comprehension research
- Actionable insight synthesis methods
- Author interviews and expert analysis

## Use Cases

### Example 1: Summary
```
User: "Summarize 'Atomic Habits' by James Clear"
Skill: Full analysis with SQ3R + Feynman framework
Output: Comprehensive summary with key ideas, evidence citations, grade A
```

### Example 2: Action Extraction
```
User: "What should I actually do after reading 'Deep Work'?"
Skill: Actionable Insight Extraction framework applied
Output: Specific implementation steps for your context, scored for applicability
```

### Example 3: Comparison
```
User: "Compare 'Atomic Habits' and 'Tiny Habits' — which should I use?"
Skill: Comparative analysis with clear recommendations
Output: Distinctions, similarities, and when to use each approach
```

### Example 4: Context Application
```
User: "Apply 'The Mom Test' to my B2B SaaS startup customer discovery"
Skill: Framework selection for application + transfer scoring
Output: Startup-specific applications with concrete examples
```

## Installation

### For Claude Code Users

This skill is part of the career-education cluster. Add it to your Claude skills directory:

```bash
# Clone to your skills directory
git clone https://github.com/dungnotnull/nonfiction-book-insights-agent-skill ~/.claude/skills/nonfiction-book-insights
```

### For Knowledge Updates

Set up the weekly knowledge crawl:

```bash
# Add cron job (weekly at midnight Sundays)
0 0 * * 0 cd /path/to/skill && python tools/knowledge_updater.py

# Or run manually
python tools/knowledge_updater.py --dry-run  # Test without modifying
python tools/knowledge_updater.py            # Live run to append entries
```

## Project Structure

```
nonfiction-book-insights/
├── skills/
│   ├── main.md                      # Main harness (7-stage workflow)
│   ├── sub-intake.md                # Intake & context gathering
│   ├── sub-framework-selector.md    # Framework selection
│   ├── sub-scoring-engine.md        # Scoring with rubric
│   └── sub-improvement-roadmap.md   # Prioritized recommendations
├── tools/
│   └── knowledge_updater.py         # Self-improving crawl pipeline
├── tests/
│   └── test-scenarios.md            # 7 comprehensive test scenarios
├── SECOND-KNOWLEDGE-BRAIN.md        # Cached knowledge base
├── PROJECT-detail.md                # Technical specification
├── CLAUDE.md                        # Skill documentation
└── README.md                        # This file
```

## Development Status

| Phase | Status | Description |
|-------|--------|-------------|
| Phase 0 — Research & Architecture | ✅ Complete | Frameworks defined, sources mapped |
| Phase 1 — Core Sub-Skills | ✅ Complete | 4 sub-skills with production-grade content |
| Phase 2 — Main Harness | ✅ Complete | 7-stage workflow with quality gates |
| Phase 3 — Knowledge Pipeline | ✅ Complete | Python tool with crawl4ai integration |
| Phase 4 — Testing | ✅ Complete | 7 test scenarios covering all paths |
| Phase 5 — Integration | ✅ Complete | Cluster integration documented |

**Overall Status: Production Ready (v1.0)**

## Testing

The skill includes 7 comprehensive test scenarios:

1. **Standard Summary** — Atomic Habits analysis
2. **Action Extraction** — Deep Work implementation steps
3. **Comparative Analysis** — Atomic Habits vs Tiny Habits
4. **Context Application** — The Mom Test to startup context
5. **Degraded Mode** — Offline analysis with graceful fallback
6. **Complex Multi-Book** — 3-book comparison with reading order
7. **Insufficient Information** — Clarification flow validation

Run tests with the test scenarios documented in `tests/test-scenarios.md`.

## Quality Gates

Every analysis passes these quality gates before delivery:

- **Evidence Citation** — Every score cites a source or framework
- **Challenge Completed** — Assumptions tested, alternatives considered
- **Roadmap Traceability** — Recommendations link to scoring gaps
- **Limitations Stated** — Evidence quality and scope boundaries explicit

## Authoritative Sources

The skill prioritizes evidence from:

- **Primary Sources**: Book text, author interviews, publisher materials
- **Secondary Analysis**: Reputable reviews, academic analyses
- **Aggregated Sources**: Goodreads, HBR, Farnam Street, NYT Best Sellers
- **Cached Knowledge**: SECOND-KNOWLEDGE-BRAIN.md (fallback)

Key URLs:
- https://www.goodreads.com
- https://hbr.org
- https://fs.blog
- https://www.nytimes.com/books/best-sellers

## Contributing

Contributions are welcome! Areas for enhancement:

- Additional comprehension frameworks
- New book analysis patterns
- Improved relevance scoring
- Additional test scenarios
- Multi-language support

## License

MIT License — See LICENSE file for details

## Acknowledgments

Built on the shoulders of giants:

- **Francis Robinson** — SQ3R method
- **Mortimer Adler** — How to Read a Book
- **Richard Feynman** — Feynman Technique
- **BJ Fogg** — Behavior Model
- **Walter Pauk** — Cornell Notes

## Author

Created by Claude Code with human guidance

## Version History

- **v1.0.0** (2026-07-01) — Production-ready release
  - All 5 phases complete
  - 7 test scenarios validated
  - Self-improving knowledge pipeline
  - Open-source ready

## Support

For issues, questions, or contributions:
- Open an issue on GitHub
- Check test scenarios for usage examples
- Review PROJECT-detail.md for technical details

---

**Made with Claude Code — Transforming how we read and apply non-fiction**
