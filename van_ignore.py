from pathlib import Path


def is_ignored(filename):
    ignore_path = Path(".vanignore")
    ignored = []
    if ignore_path.exists():
        ignored = ignore_path.read_text().splitlines()
    return filename in ignored
