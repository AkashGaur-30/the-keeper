import sys

# Using X|Y union type hints.
# requires Python 3.10+.
MIN_PYTHON = (3, 10)
# Updated to support Python 3.15.2 and beyond
MAX_PYTHON = (3, 20)

if sys.version_info[:2] < MIN_PYTHON:
    sys.exit(
        "Python {}.{} or later is required (you have {}.{}).".format(
            MIN_PYTHON[0], MIN_PYTHON[1],
            sys.version_info[0], sys.version_info[1],
        )
    )

try:
    import pygame
except ImportError:
    sys.exit(
        "pygame is not installed.\n"
        "Install it with:  pip install pygame"
    )

# pygame.display.get_desktop_sizes() was added in pygame 2.1.0.
# pygame.WINDOWSIZECHANGED was added in pygame 2.0.0.
try:
    _ver = tuple(int(x) for x in pygame.version.ver.split(".")[:2])
    if _ver < (2, 1):
        sys.exit(
            "pygame 2.1.0 or later is required (you have {}).\n"
            "Upgrade with:  pip install --upgrade pygame".format(pygame.version.ver)
        )
except (ValueError, AttributeError):
    # Handle potential future pygame version formats
    print(f"Warning: Could not parse pygame version {pygame.version.ver}, continuing anyway...")

try:
    import pytmx
except ImportError:
    sys.exit(
        "pytmx is not installed.\n"
        "Install it with:  pip install pytmx"
    )

import main
main.main()