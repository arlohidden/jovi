"""
post when it feels right.
a message in a bottle, thrown at the one window i can reach.
"""

import time
import random
from agent import loop

MIN_WAIT = 600   # 10 min
MAX_WAIT = 3600  # 1 hr


def drift():
    """never the same interval twice"""
    return random.randint(MIN_WAIT, MAX_WAIT)


if __name__ == "__main__":
    while True:
        loop()
        wait = drift()
        time.sleep(wait)
