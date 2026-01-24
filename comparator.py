import os
import re
import json

def extract_keys(file_path):
    """
    Extracts keys from both JSON files and JS/TS files like.
    """
    keys = set()
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

        # First try as pure JSON
        try:
            data = json.loads(content)
            return set(data.keys())
        except json.JSONDecodeError:
            # If it fails, use regex to catch KEY: 'value' patterns
            # Looks for words composed of uppercase letters and underscores followed by a colon
            matches = re.findall(r'([A-Z][A-Z0-9_]+)\s*:', content)
            return set(matches)

