#!/usr/bin/env python3
"""
GitCode Code Review - Token retrieval for this skill only
"""

import os
import json

def get_token():
    token_file = os.path.expanduser("~/.config/opencode/skills/md-review-skill/config/gitcode-config.json")

    if os.path.exists(token_file):
        try:
            with open(token_file, 'r') as f:
                config = json.load(f)
                if config.get('token'):
                    return config.get('token')
        except ValueError:
            pass

    return None

def get_base_url():
    token_file = os.path.expanduser("~/.config/opencode/skills/md-review-skill/config/gitcode-config.json")

    if os.path.exists(token_file):
        try:
            with open(token_file, 'r') as f:
                config = json.load(f)
                if config.get('baseUrl'):
                    return config.get('baseUrl')
        except ValueError:
            pass

    return "https://api.gitcode.com/api/v5"

if __name__ == "__main__":
    token = get_token()
    if token:
        print("Token configured for md-review-skill")
    else:
        print("No token configured for md-review-skill")
