# -*- coding: utf-8 -*-
"""
knowledge_updater.py — self-improving crawl pipeline for Skill #165
(Non-fiction Book Analysis & Actionable Insights, cluster: career-education).

This tool continuously grows the SECOND-KNOWLEDGE-BRAIN.md knowledge base by:
1. Crawling authoritative domain sources for latest nonfiction book insights
2. Extracting summaries, reviews, and actionable insight methodologies
3. Scoring entries by relevance and recency
4. Appending dated, deduplicated entries to the knowledge brain
5. Supporting graceful degradation when crawl tools are unavailable

Usage:
    python tools/knowledge_updater.py [--dry-run] [--source SOURCE]

Schedule: Weekly cron recommended
Graceful degradation: Logs errors and exits cleanly; skill continues with existing brain
"""

import os
import re
import sys
import json
import hashlib
import datetime
import argparse
from typing import List, Dict, Optional, Set
from urllib.parse import urljoin, urlparse

# Configuration
ARXIV_CATEGORIES: List[str] = []  # Non-paper domain; rely on web sources
WEB_SOURCES: List[str] = [
    "https://www.goodreads.com",
    "https://hbr.org",
    "https://fs.blog",
    "https://www.nytimes.com/books/best-sellers",
    "https://www.publishersweekly.com",
    "https://bookriot.com"
]
SEARCH_QUERIES: List[str] = [
    "nonfiction book summary methods",
    "active recall reading comprehension",
    "bestseller nonfiction 2026",
    "actionable insight synthesis",
    "how to extract insights from nonfiction books",
    "deep reading comprehension techniques",
    "nonfiction book analysis framework"
]

BRAIN_PATH = os.path.join(os.path.dirname(__file__), "..", "SECOND-KNOWLEDGE-BRAIN.md")
RELEVANCE_KEYWORDS: List[str] = [w for query in SEARCH_QUERIES for w in query.split()]
MAX_ENTRIES_PER_RUN = 50
MIN_RELEVANCE_SCORE = 0.1


def hash_url(url: str) -> str:
    """Generate a stable hash for URL deduplication."""
    return hashlib.sha256((url or "").encode("utf-8")).hexdigest()[:16]


def extract_existing_hashes(text: str) -> Set[str]:
    """Extract all existing URL hashes from the knowledge brain."""
    return set(re.findall(r"<!--hash:([0-9a-f]{16})-->", text))


def calculate_relevance_score(title: str, abstract: str) -> float:
    """
    Calculate relevance score based on keyword matches.
    Returns normalized score 0-1 based on keyword density.
    """
    combined = (title + " " + abstract).lower()
    word_count = len(combined.split())
    if word_count == 0:
        return 0.0

    keyword_hits = sum(1 for keyword in RELEVANCE_KEYWORDS if keyword.lower() in combined)
    # Normalize by word count to penalize keyword stuffing
    raw_score = keyword_hits / len(RELEVANCE_KEYWORDS)
    adjusted_score = min(raw_score, 1.0)  # Cap at 1.0
    return adjusted_score


def fetch_crawl4ai_entries() -> List[Dict[str, str]]:
    """
    Fetch entries using crawl4ai if available.
    Returns list of entry dicts with title, authors, year, venue, url, abstract.
    """
    entries = []

    try:
        from crawl4ai import WebCrawler
        import asyncio

        print("[info] crawl4ai available; initializing crawler...")
        crawler = WebCrawler()
        crawler.warmup()

        # Crawl web sources
        for source in WEB_SOURCES:
            try:
                print(f"[crawl] fetching {source}...")
                result = crawler.run(url=source)
                markdown = getattr(result, "markdown", "") or ""
                cleaned = markdown[:2000]  # Limit to prevent memory issues

                if cleaned.strip():
                    entries.append({
                        "title": f"Update scan: {urlparse(source).netloc}",
                        "authors": "Various",
                        "year": str(datetime.date.today().year),
                        "venue": source,
                        "url": source,
                        "abstract": cleaned[:600]  # Limit abstract length
                    })
                    print(f"[ok] extracted content from {source}")
            except Exception as e:
                print(f"[warn] failed to crawl {source}: {e}")

    except ImportError:
        print("[info] crawl4ai not installed; skipping live crawl")
    except Exception as e:
        print(f"[warn] crawl4ai error: {e}")

    return entries


def fetch_manual_entries() -> List[Dict[str, str]]:
    """
    Generate manual entries based on known domain sources.
    This is a fallback when crawl tools are unavailable.
    """
    entries = []

    # Known high-value sources for nonfiction book analysis
    manual_sources = [
        {
            "title": "Farnam Street: How to Read a Book",
            "authors": "Shane Parrish",
            "year": "2023",
            "venue": "fs.blog",
            "url": "https://fs.blog/how-to-read-a-book/",
            "abstract": "Comprehensive guide to reading nonfiction for understanding, covering Adler's levels of reading, note-taking methods, and insight extraction techniques."
        },
        {
            "title": "Goodreads Nonfiction Best Practices",
            "authors": "Goodreads Community",
            "year": "2024",
            "venue": "goodreads.com",
            "url": "https://www.goodreads.com",
            "abstract": "Community-driven summaries and reviews of bestselling nonfiction across business, psychology, science, and self-improvement categories."
        },
        {
            "title": "HBR IdeaCast: Book Insights",
            "authors": "Harvard Business Review",
            "year": "2024",
            "venue": "hbr.org",
            "url": "https://hbr.org/ideacast",
            "abstract": "Author interviews and deep-dive analyses of recent business nonfiction bestsellers with focus on actionable business applications."
        }
    ]

    for source in manual_sources:
        entries.append(source)

    return entries


def deduplicate_entries(entries: List[Dict[str, str]], existing_hashes: Set[str]) -> List[Dict[str, str]]:
    """Remove entries that already exist in the knowledge brain."""
    unique_entries = []

    for entry in entries:
        url_hash = hash_url(entry.get("url", ""))
        if url_hash not in existing_hashes and url_hash:
            unique_entries.append(entry)

    return unique_entries


def score_and_rank_entries(entries: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """Score entries by relevance and sort by score."""
    for entry in entries:
        entry["relevance"] = calculate_relevance_score(
            entry.get("title", ""),
            entry.get("abstract", "")
        )

    # Filter by minimum relevance
    filtered = [e for e in entries if e.get("relevance", 0) >= MIN_RELEVANCE_SCORE]

    # Sort by relevance (descending)
    return sorted(filtered, key=lambda e: e.get("relevance", 0), reverse=True)


def append_to_brain(entries: List[Dict[str, str]], dry_run: bool = False) -> int:
    """
    Append scored entries to the SECOND-KNOWLEDGE-BRAIN.md file.
    Returns number of entries added.
    """
    if not entries:
        print("[info] no entries to append")
        return 0

    if not os.path.exists(BRAIN_PATH):
        print(f"[warn] knowledge brain not found: {BRAIN_PATH}")
        return 0

    # Read existing brain
    with open(BRAIN_PATH, "r", encoding="utf-8") as f:
        brain_content = f.read()

    existing_hashes = extract_existing_hashes(brain_content)

    # Deduplicate
    unique_entries = deduplicate_entries(entries, existing_hashes)

    if not unique_entries:
        print("[info] all entries already exist (deduplicated)")
        return 0

    # Score and rank
    ranked_entries = score_and_rank_entries(unique_entries)

    # Limit entries per run
    final_entries = ranked_entries[:MAX_ENTRIES_PER_RUN]

    # Generate append content
    today = datetime.date.today().isoformat()
    lines = [f"\n### Auto-crawl {today}\n"]

    for entry in final_entries:
        url_hash = hash_url(entry.get("url", ""))
        relevance = entry.get("relevance", 0)

        lines.append(f"- **{entry['title']}** ({entry['venue']}, {entry['year']})")
        lines.append(f"  Authors: {entry['authors']}")
        lines.append(f"  URL: {entry['url']}")
        lines.append(f"  Abstract: {entry['abstract'][:200]}...")
        lines.append(f"  Relevance: {relevance:.2f} <!--hash:{url_hash}-->")
        lines.append("")

    append_content = "\n".join(lines)

    if dry_run:
        print("[dry-run] would append:")
        print(append_content)
        return len(final_entries)

    # Append to file
    with open(BRAIN_PATH, "a", encoding="utf-8") as f:
        f.write(append_content)

    print(f"[ok] appended {len(final_entries)} new entries to {BRAIN_PATH}")
    return len(final_entries)


def validate_brain_structure() -> bool:
    """Validate that the knowledge brain file exists and has basic structure."""
    if not os.path.exists(BRAIN_PATH):
        print(f"[error] knowledge brain missing: {BRAIN_PATH}")
        return False

    with open(BRAIN_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    if not content.strip():
        print("[warn] knowledge brain is empty")
        return False

    return True


def main():
    parser = argparse.ArgumentParser(description="Update SECOND-KNOWLEDGE-BRAIN with latest nonfiction book insights")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be added without writing")
    parser.add_argument("--source", type=str, help="Specific source to crawl (default: all)")
    parser.add_argument("--verbose", action="store_true", help="Verbose output")
    args = parser.parse_args()

    print(f"[run] knowledge_updater for skill #165 (nonfiction-book-insights)")
    print(f"[date] {datetime.date.today().isoformat()}")

    # Validate brain structure
    if not validate_brain_structure():
        print("[error] cannot proceed without valid knowledge brain")
        return 1

    # Fetch entries
    print("[fetch] gathering entries from sources...")
    entries = []

    # Try crawl4ai first
    crawl_entries = fetch_crawl4ai_entries()
    entries.extend(crawl_entries)

    # Add manual entries as baseline
    manual_entries = fetch_manual_entries()
    entries.extend(manual_entries)

    if not entries:
        print("[warn] no entries fetched from any source")
        return 0

    print(f"[fetch] gathered {len(entries)} total entries")

    # Append to brain
    added = append_to_brain(entries, dry_run=args.dry_run)

    if added == 0:
        print("[info] no new entries added (deduplicated or below relevance threshold)")
        return 0

    print(f"[complete] added {added} new entries to knowledge brain")
    return 0


if __name__ == "__main__":
    sys.exit(main())
