from pathlib import Path


def init():
    van = Path(".van")

    (van / "objects").mkdir(parents=True, exist_ok=True)
    (van / "index.json").write_text("{}")
    (van / "commits.json").write_text("[]")


    print("initialized van repository")