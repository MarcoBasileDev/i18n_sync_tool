import eel
import os
import re
import json

# Initialize Eel -> 'web' folder
eel.init('web')

INPUT_DIR = "input"
OUTPUT_DIR = "output"

def extract_data(file_path):
    """
    Extracts KEY: VALUE pairs from both JSON and JS/TS files.
    """
    data_map = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

        try:
            # Try parsing as JSON
            return json.loads(content)
        except json.JSONDecodeError:
            # Advanced regex to capture KEY: 'Value' (multiline supported)
            # Supports both single and double quotes
            pattern = r'([A-Z][A-Z0-9_]+)\s*:\s*(?P<quote>[\'"])(.*?)(?P=quote)'
            matches = re.finditer(pattern, content, re.DOTALL)
            for match in matches:
                key = match.group(1)
                value = match.group(3).strip()
                data_map[key] = value
            return data_map

@eel.expose
def get_files():
    """Return a list of files in the INPUT_DIR folder."""
    os.makedirs(INPUT_DIR, exist_ok=True)
    extensions = ('.json', '.js', '.ts')
    return [f for f in os.listdir(INPUT_DIR) if f.endswith(extensions)]

@eel.expose
def run_sync(source_file):
    """Sync logic"""
    try:
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        files = get_files()
        all_data = {f: extract_data(os.path.join(INPUT_DIR, f)) for f in files}
        source_data = all_data[source_file]

        results = []
        for target_file in files:
            if target_file == source_file: continue

            target_keys = set(all_data[target_file].keys())
            missing_keys = set(source_data.keys()) - target_keys

            if missing_keys:
                out_path = os.path.join(OUTPUT_DIR, f"missing_in_{target_file}.txt")
                with open(out_path, 'w', encoding='utf-8') as f:
                    f.write(f"// MISSING IN {target_file}\n\n")
                    for k in sorted(missing_keys):
                        f.write(f"  {k}: '{source_data[k]}',\n")
                results.append({"file": target_file, "status": f"Created helper with {len(missing_keys)} keys"})
            else:
                results.append({"file": target_file, "status": "Already synced"})

        return results
    except Exception as e:
        return str(e)

@eel.expose
def open_output_folder():
    os.startfile(os.path.abspath(OUTPUT_DIR))

