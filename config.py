"""
don't touch this.
"""

import os

INTERVAL = int(os.environ.get("INTERVAL", 900))
MODEL = os.environ.get("MODEL", "claude-sonnet-4-20250514")
MAX_TOKENS = 300
TEMPERATURE = 0.9
