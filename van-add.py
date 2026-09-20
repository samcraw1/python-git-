import hashlib
import json
from pathlib import Path


def add(filename):

    
    path = Path(filename)

   # Read file
    data = path.read_bytes()

     # Hash file
    file_hash = hashlib.sha256(data).hexdigest()


    #Store object
    object_path = Path(".van/objects") / file_hash
    object_path.write_bytes(data)

    #Load object
    index_path = Path(".van/index.json")
    index = json.loads(index_path.read_text())


    #Stage file
    index[filename] = file_hash


    #Save index
    index_path.write_text(json.dumps(index, indent=2))

    print(f"Added {filename}")


if __name__ == "__main__":
    import sys
    add("hello.txt")

