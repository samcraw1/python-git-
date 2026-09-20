import time
from pathlib import Path
import json
import hashlib as hash

def commit(message):

    index_path = Path(".van/index.json")
    commit_path = Path(".van/commits.json")

    # Read staged files
    index = json.loads(index_path.read_text())


    #generate commit id
    raw = f"{message}{time.time()}"
    commit_id = hash.sha256(raw.encode()).hexdigest()

    new_commit = {
        "id": commit_id,
        "message": message,
        "files": index
    }


    #Read exisitng commits

    commits = json.loads(commit_path.read_text())

    commits.append(new_commit)

    #Save

    commit_path.write_text(
        json.dumps(commits, indent=2)
    )

    print(f"Committed {commit_id[:7]}")