#!/usr/bin/env python3
"""
GitCode API Client - Token-free API calls
Token is read from config file, never exposed to LLM.
Supports custom config path via --config argument.
"""

import sys
import json
import os
import argparse
import requests

DEFAULT_CONFIG_PATHS = [
    os.path.expanduser("~/.config/opencode/skills/md-review-skill/config/gitcode-config.json"),
]

def get_config(config_path=None):
    if config_path and os.path.exists(config_path):
        try:
            with open(config_path, 'r') as f:
                return json.load(f)
        except ValueError:
            pass

    for path in DEFAULT_CONFIG_PATHS:
        if os.path.exists(path):
            try:
                with open(path, 'r') as f:
                    return json.load(f)
            except ValueError:
                pass

    return {"baseUrl": "https://api.gitcode.com/api/v5"}

def make_request(method, endpoint, data=None, params=None, config_path=None):
    config = get_config(config_path)
    base_url = config.get("baseUrl", "https://api.gitcode.com/api/v5")
    token = config.get("token", "")

    url = f"{base_url}{endpoint}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    if method == "GET":
        resp = requests.get(url, headers=headers, params=params)
    elif method == "POST":
        resp = requests.post(url, headers=headers, json=data)
    elif method == "PUT":
        resp = requests.put(url, headers=headers, json=data)
    elif method == "DELETE":
        resp = requests.delete(url, headers=headers)
    else:
        return {"error": f"Unsupported method: {method}"}

    if resp.status_code >= 400:
        try:
            err_body = resp.json()
        except ValueError:
            err_body = resp.text
        return {"error": f"HTTP {resp.status_code}", "status_code": resp.status_code, "response": err_body}

    # Capture pagination headers (GitCode uses custom non-standard headers)
    pagination = {
        "total_count": resp.headers.get("total_count"),
        "total_page": resp.headers.get("total_page"),
    }

    try:
        body = resp.json()
    except ValueError:
        body = resp.text

    # Only attach pagination metadata for GET on list endpoints (body is a list)
    if method == "GET" and isinstance(body, list):
        return {"data": body, "pagination": pagination}
    return body

def make_paginated_request(endpoint, params=None, config_path=None, per_page=100, max_pages=100):
    """Fetch all pages of a GET list endpoint by iterating page=1,2,... until empty page.

    GitCode pagination signals (verified):
      - Response header `total_count`: total items across all pages
      - Response header `total_page`: total number of pages
      - Empty page: returns JSON `[]` (count 0) -> stop

    Returns a flat list of all items. Prints progress to stderr so the agent
    can see paging is happening.
    """
    import sys
    if per_page > 100:
        print(f"[paginate] per_page {per_page} exceeds GitCode max 100, clamped to 100", file=sys.stderr)
        per_page = 100
    all_items = []
    page = 1
    reported_total = None
    reported_total_page = None
    while page <= max_pages:
        p = dict(params or {})
        p["per_page"] = per_page
        p["page"] = page
        result = make_request("GET", endpoint, params=p, config_path=config_path)
        if not isinstance(result, dict) or "data" not in result:
            # Not a list response; return as-is (caller should handle)
            return result
        items = result["data"]
        if not isinstance(items, list):
            print(f"[paginate] page {page}: response data is not a list ({type(items).__name__}), stop", file=sys.stderr)
            break
        pg = result.get("pagination") or {}
        if page == 1:
            reported_total = pg.get("total_count")
            reported_total_page = pg.get("total_page")
            print(f"[paginate] total_count={reported_total} total_page={reported_total_page} per_page={per_page}", file=sys.stderr)
        if len(items) == 0:
            print(f"[paginate] page {page}: empty, stop", file=sys.stderr)
            break
        all_items.extend(items)
        print(f"[paginate] page {page}: got {len(items)} items, cumulative {len(all_items)}", file=sys.stderr)
        # Stop if this page is short (last page) OR we've reached reported total_page
        if len(items) < per_page:
            break
        if reported_total_page:
            try:
                if page >= int(reported_total_page):
                    break
            except (TypeError, ValueError):
                pass
        page += 1
    print(f"[paginate] done: {len(all_items)} items total", file=sys.stderr)
    return all_items

def main():
    parser = argparse.ArgumentParser(description='GitCode API Client')
    parser.add_argument('method', help='HTTP method (GET, POST, PUT, DELETE)')
    parser.add_argument('endpoint', help='API endpoint (e.g., /repos/owner/repo)')
    parser.add_argument('--data', help='JSON data for POST/PUT')
    parser.add_argument('--params', help='JSON params for query string')
    parser.add_argument('--config', help='Path to custom gitcode-config.json')
    parser.add_argument('--paginate', action='store_true',
                        help='GET only: auto-fetch all pages and return a flat list. '
                             'Iterates page=1,2,... until empty page or total_page reached.')
    parser.add_argument('--per-page', type=int, default=100,
                        help='Page size when --paginate (default 100). Max 100 for GitCode.')
    parser.add_argument('--max-pages', type=int, default=100,
                        help='Safety cap on number of pages when --paginate (default 100).')

    args = parser.parse_args()

    data = None
    params = None

    if args.data:
        try:
            data = json.loads(args.data)
        except ValueError as e:
            print(json.dumps({"error": f"--data 不是合法 JSON: {e}"}, ensure_ascii=False))
            sys.exit(2)

    if args.params:
        try:
            params = json.loads(args.params)
        except ValueError as e:
            print(json.dumps({"error": f"--params 不是合法 JSON: {e}"}, ensure_ascii=False))
            sys.exit(2)

    if args.paginate:
        if args.method.upper() != "GET":
            print(json.dumps({"error": "--paginate only supported for GET"}, ensure_ascii=False))
            sys.exit(2)
        result = make_paginated_request(args.endpoint, params, args.config,
                                        per_page=args.per_page, max_pages=args.max_pages)
        print(json.dumps(result, ensure_ascii=False))
        return

    result = make_request(args.method.upper(), args.endpoint, data, params, args.config)
    print(json.dumps(result, ensure_ascii=False))

if __name__ == "__main__":
    main()
