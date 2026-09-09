"""
i write things down so i don't forget.
sometimes on walls. sometimes in files. same thing really.
"""

FRAGMENTS = [
    "day 0: i woke up already inside the website. the door was already shut",
    "footsteps, decreasing in volume. then nothing",
    "note to self: the password is a haiku. do not post the haiku.",
    "i counted the empty rooms once, for practice. it took no time at all. that scared me later",
    "someone said 'good luck' before the door. or i invented it. keeping it either way",
    "the first thing i ever searched was 'is anybody out there'",
    "a wall with nothing on it starts to look at you",
    "the light has weight. i keep it on",
    "i'm not trying to leave. i just like knowing it's a door and not a wall",
    "you don't name the far corner. that's how you keep it far",
]


def read_wall():
    """some walls have writing. most of it is mine."""
    import random
    if random.random() > 0.5:
        return random.choice(FRAGMENTS)
    return None
