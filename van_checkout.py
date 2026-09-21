import hashlib
import json
from pathlib import Path




def checkout():

    commits_path = Path(".van/commits.json")
    
    if not commits_path.exists():
        print("No commits found")
        return

    commits = json.loads(commits_path.read_text())

    if not commits:
        print("No commits found")
        return
    latest_commit = commits[-1]

    print(f"Checking out latest commit: {latest_commit['id']}")

    # Here you would add the logic to actually checkout the files from the latest commit
    # For example, you might iterate over the files in the commit and restore their contents
    # This is a placeholder for the actual checkout implementation
    for filename, file_hash in latest_commit["files"].items():
        object_path = Path(".van/objects") / file_hash
        content = object_path.read_bytes()
        Path(filename).write_bytes(content)

    print("Checkout complete.")