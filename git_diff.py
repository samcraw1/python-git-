import hashlib
import json
import difflib  

from pathlib import Path

def diff(filename):

    index_path = Path(".van/index.json")
    current_path = Path(filename)

    # Check if the file exists and calculate its SHA-256 hash
    
    if current_path.is_file():
        with open(current_path, "rb") as f:
            content = f.read()
            file_hash = hashlib.sha256(content).hexdigest()
    else: 
        print(f"File not found: {filename}")
        return None

    stored_hash = json.loads(index_path.read_text())
    stored_hash = stored_hash.get(filename)

    if stored_hash is None:
        print(f"No stored hash for file: {filename}")
        return None

    if file_hash == stored_hash:
        print(f"No changes detected for file: {filename}")
        return False
    else:
        print(f"Changes detected for file: {filename}")
        print(f"Previous hash: {stored_hash}")
        print(f"Current hash: {file_hash}")


        old_path = Path(".van/objects") / stored_hash
        old_content = old_path.read_text()

        old_lines = old_content.encode().decode().splitlines(keepends=True)
        current_lines = content.decode().splitlines(keepends=True)

        diff_output = difflib.unified_diff(old_lines, current_lines, fromfile=f"old/{filename}", tofile=f"current/{filename}")
        print("".join(diff_output))
        return True
    
    
        
       