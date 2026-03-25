#!/usr/bin/env python3
"""
ArXiv Technical Digest (v3.1)
Part of Dasafo Factory Research Department.

Fetches and digests technical papers from ArXiv to provide 
the Architect with actionable math and logic.
"""

import os
import sys
import argparse
import urllib.request
import re
from datetime import datetime

def fetch_arxiv_metadata(arxiv_id):
    """Fetches paper metadata using the ArXiv API."""
    url = f"http://export.arxiv.org/api/query?id_list={arxiv_id}"
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            content = response.read().decode()
            title = re.search(r"<title>(.*?)</title>", content, re.DOTALL).group(1).strip()
            summary = re.search(r"<summary>(.*?)</summary>", content, re.DOTALL).group(1).strip()
            return {"title": title, "summary": summary}
    except Exception as e:
        return None, f"Failed to fetch metadata: {str(e)}"

def generate_digest(paper_info, arxiv_id):
    """Produces the industrial Paper Summary report."""
    now = datetime.now().isoformat()
    
    digest = f"""# 🧠 PAPER SUMMARY: {paper_info['title']} 
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
**ID:** {arxiv_id}
**Source:** https://arxiv.org/abs/{arxiv_id}
**Generated At:** {now}

## 📊 Technical Core (Abstract)
{paper_info['summary']}

## 📐 Formulas & Algorithms (Extracted)
- [PENDING: Deep Semantic Trace Required]

## 🚧 Implementation Constraints
- [ ] Hardware/Memory overhead: 
- [ ] Computational complexity: 

## 🎯 Architecture Impact
- How does this change our current stack?
- Scaling potential:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
*Industrial Research Digest v3.1*
"""
    return digest

def main():
    parser = argparse.ArgumentParser(description="Dasafo Research Digest Tool")
    parser.add_argument("--id", required=True, help="ArXiv ID (e.g., 2301.00001)")
    parser.add_argument("--output", help="Output path for the summary")

    args = parser.parse_args()

    # 1. Fetch Metadata
    info = fetch_arxiv_metadata(args.id)
    if isinstance(info, tuple): # Error case
        print(f"❌ RESEARCH FAILURE: {info[1]}")
        sys.exit(1)
    
    # 2. Generate Digest
    digest = generate_digest(info, args.id)

    if args.output:
        with open(args.output, 'w') as f:
            f.write(digest)
        print(f"✅ Technical Digest saved to {args.output}")
    else:
        print(digest)

if __name__ == "__main__":
    main()
