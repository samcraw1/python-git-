

import json
from pathlib import Path


def log():
    commits_path = Path(".van/commits.json")

    commits = json.loads(commits_path.read_text())

    for commit in reversed(commits):
        print(f"commit {commit['id'][:7]}")
        print(f" {commit['message']}")
        print()

    