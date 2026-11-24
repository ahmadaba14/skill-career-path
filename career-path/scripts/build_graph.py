#!/usr/bin/env python3
"""Build a self-contained career-path graph page.

Usage: python build_graph.py <data.json> <output.html>

Reads the career data, checks it for common mistakes, and injects it into
assets/graph-template.html. Prints warnings for problems that would make the
graph hard to read, and exits with an error for problems that would break it.
"""
import json
import sys
from pathlib import Path

PLACEHOLDER = '"__CAREER_DATA__"'
ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "assets" / "graph-template.html"
from urllib.parse import urlparse

NODE_TYPES = {"role", "cert", "education"}
OUTLOOKS = {"growing", "stable", "evolving", "declining", "emerging"}


def check_url(url, where, errors, warnings):
    parsed = urlparse(str(url))
    if parsed.scheme not in ("http", "https") or not parsed.netloc:
        errors.append(f"{where}: '{url}' is not a valid http(s) link")
    elif parsed.scheme == "http":
        warnings.append(f"{where}: link uses http, prefer the https version")
    if parsed.netloc and parsed.path.strip("/") == "" and not parsed.fragment and not parsed.query:
        warnings.append(f"{where}: '{url}' is a home page; link the exact page or section instead")


def validate(data):
    errors, warnings = [], []
    paths = data.get("paths")
    if not isinstance(paths, list) or not paths:
        errors.append("'paths' must be a non-empty list")
        return errors, warnings
    horizon = data.get("horizonYears", 10)
    ids = {p.get("id") for p in paths}
    if data.get("recommendedPathId") not in ids:
        errors.append("recommendedPathId does not match any path id")
    if not data.get("rationale"):
        warnings.append("rationale is empty; the recommendation needs a reason")
    if not 3 <= len(paths) <= 5:
        warnings.append(f"{len(paths)} paths; 3 to 5 reads best")
    all_nodes = {}
    for p in paths:
        for n in p.get("nodes", []):
            all_nodes[n.get("id")] = n
    for p in paths:
        pid = p.get("id")
        nodes = p.get("nodes", [])
        if not nodes:
            errors.append(f"path '{pid}' has no nodes")
            continue
        last_year, last_role_year = -1, None
        for n in nodes:
            nid = n.get("id")
            if n.get("type") not in NODE_TYPES:
                errors.append(f"node '{nid}' has unknown type '{n.get('type')}'")
            y = n.get("year")
            if not isinstance(y, (int, float)) or not 0 <= y <= horizon:
                errors.append(f"node '{nid}' needs a year between 0 and {horizon}")
                continue
            if y < last_year:
                warnings.append(f"path '{pid}': nodes are not in year order at '{nid}'")
            last_year = y
            if len(n.get("title", "")) > 30:
                warnings.append(f"node '{nid}' title is long; labels may wrap badly")
            if n.get("type") == "role":
                outlook = n.get("outlook")
                if outlook not in OUTLOOKS:
                    warnings.append(f"role '{nid}' needs an outlook: one of {sorted(OUTLOOKS)}")
                elif outlook == "declining":
                    note = " (recommended path)" if pid == data.get("recommendedPathId") else ""
                    warnings.append(f"role '{nid}' is declining{note}; check the path routes through its successor")
                    if not n.get("outlookNote"):
                        warnings.append(f"role '{nid}' is declining but has no outlookNote naming its successor")
                if last_role_year is not None and y - last_role_year < 1.5:
                    warnings.append(f"path '{pid}': role '{nid}' is under 1.5 years after the previous role")
                last_role_year = y
        for src in p.get("sources", []):
            check_url(src.get("url", ""), f"path '{pid}' source", errors, warnings)
        if not p.get("sources"):
            warnings.append(f"path '{pid}' has no sources; add links that back its claims")
        for n in nodes:
            nid = n.get("id")
            for src in n.get("sources", []):
                check_url(src.get("url", ""), f"node '{nid}' source", errors, warnings)
                if not src.get("where"):
                    warnings.append(f"node '{nid}' source '{src.get('title')}' has no 'where' (the section or page to look at)")
            if n.get("url"):
                check_url(n["url"], f"node '{nid}' url", errors, warnings)
            elif n.get("type") in ("cert", "education"):
                warnings.append(f"node '{nid}' ({n.get('type')}) has no official url")
            for c in n.get("certs", []):
                if c.get("url"):
                    check_url(c["url"], f"cert '{c.get('name')}' on '{nid}'", errors, warnings)
                else:
                    warnings.append(f"cert '{c.get('name')}' on '{nid}' has no official url")
            if n.get("type") == "role":
                jp = n.get("jobPosts")
                early = n.get("year", 0) <= 5
                if early and not jp:
                    warnings.append(f"role '{nid}' (year {n.get('year')}) has no jobPosts; research current postings in the person's market")
                elif jp and jp.get("reviewed", 0) < 5 and not jp.get("note"):
                    warnings.append(f"role '{nid}': only {jp.get('reviewed', 0)} postings reviewed; say so in jobPosts.note")
                if early and not any(x.get("kind") == "job post" for x in n.get("sources", [])):
                    warnings.append(f"role '{nid}' cites no job post in its sources")
            if n.get("type") == "role" and not n.get("sources"):
                warnings.append(f"role '{nid}' has no sources for its outlook or requirements")
        fork = p.get("forksFrom")
        if fork and fork.get("nodeId") not in all_nodes:
            errors.append(f"path '{pid}' forks from unknown node '{fork.get('nodeId')}'")
    return errors, warnings


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    data_path, out_path = Path(sys.argv[1]), Path(sys.argv[2])
    data = json.loads(data_path.read_text(encoding="utf-8"))
    errors, warnings = validate(data)
    for w in warnings:
        print(f"warning: {w}")
    if errors:
        for e in errors:
            print(f"error: {e}")
        sys.exit(1)
    template = TEMPLATE.read_text(encoding="utf-8")
    if PLACEHOLDER not in template:
        sys.exit("error: template is missing the data placeholder")
    # Escape "</" so the data cannot close the script tag early.
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    title = f"Career path: {data.get('person', {}).get('name', '')}".strip()
    html = template.replace(PLACEHOLDER, payload).replace("__PAGE_TITLE__", title)
    out_path.write_text(html, encoding="utf-8")
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
