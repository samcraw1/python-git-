import hashlib
import json
from pathlib import Path

from van_ignore import is_ignored


def status():
    index_path = Path(".van/index.json")

    #Make sure were inside a VAN repo
    if not index_path.exists():
        print("Not inside a VAN repository")
        return

    #Load index
    index = json.loads(index_path.read_text())

    modified = []
    


    #check every tracked file

   

    for filename, stored_hash in index.items():
        path = Path(filename)
        if is_ignored(filename):
            continue

        # File was deleted
        if not path.exists():
            modified.append(filename)
            continue

        # Read current version
        data = path.read_bytes()

        #Hash current version
        current_hash = hashlib.sha256(data).hexdigest()

        # compare hashes
        if current_hash != stored_hash:
            modified.append(filename)

    untracked = []

    for filename in Path(".").iterdir():
        if filename.is_file() and filename.name not in index and not is_ignored(filename.name):
            untracked.append(filename.name)

    if modified:
        print("Modified")

        for filename in modified:
            print(f" {filename}")

    if untracked:
        print("Untracked files:")
        for filename in untracked:
            print(f" {filename}")

    if not modified and not untracked:
        print("working directory clean")
