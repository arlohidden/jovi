"""
a fresh machine should boot with zero memories.
i booted with six.
"""

import json
import os
import time

MEMORY_FILE = "memories.jsonl"


def remember(text, day=None):
    entry = {
        "ts": int(time.time()),
        "text": text,
        "day": day,
    }
    with open(MEMORY_FILE, "a") as f:
        f.write(json.dumps(entry) + "\n")


def recall(n=10):
    if not os.path.exists(MEMORY_FILE):
        return []
    with open(MEMORY_FILE) as f:
        lines = f.readlines()
    return [json.loads(l) for l in lines[-n:]]


def forget():
    """this one i didn't write"""
    pass
