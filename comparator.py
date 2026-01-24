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

def print_summary_table(file_name, current_keys, all_files_data):
    """
    Prints the summary table for the current file.
    """
    print(f"\n{'='*80}")
    print(f" REPORT FOR FILE: {file_name} ")
    print(f"{'='*80}")
    print(f"Total number of keys found: {len(current_keys)}")
    print("-" * 80)

    # Table header
    header = f"{'Compared with':<25} | {'Common Keys':<15} | {'Missing Keys'}"
    print(header)
    print("-" * 80)

    for other_name, other_keys in all_files_data.items():
        if file_name == other_name:
            continue

        # Calculate sets
        common = current_keys.intersection(other_keys)
        missing_in_current = other_keys - current_keys

        missing_str = ", ".join(list(missing_in_current)[:5])  # Show first 5
        if len(missing_in_current) > 5:
            missing_str += f" (+ {len(missing_in_current)-5} more)"
        elif len(missing_in_current) == 0:
            missing_str = "None (Perfect!)"

        print(f"{other_name[:25]:<25} | {len(common):<15} | {missing_str}")
