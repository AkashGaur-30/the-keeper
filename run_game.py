"""
THE KEEPER - launcher

Desktop:  python run_game.py
Web:      Pygbag runs main.py directly in the browser (WebAssembly).
          This launcher also works in the browser, where it skips the
          desktop-only version checks.
"""
import sys

# True when running inside the browser (Pygbag / Emscripten).
IS_WEB = sys.platform == "emscripten"

# Using X|Y union type hints, requires Python 3.10+.
MIN_PYTHON = (3, 10)
# Desktop supports Python 3.15.2 and beyond. The web build runs on Python 3.12.
MAX_PYTHON = (3, 20)

if not IS_WEB:
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
            "Install it with:  pip install pygame-ce"
        )

    # pygame.display.get_desktop_sizes() was added in pygame 2.1.0.
    # pygame.WINDOWSIZECHANGED was added in pygame 2.0.0.
    # Works for both pygame and pygame-ce (the web build uses pygame-ce).
    try:
        _ver = tuple(int(x) for x in pygame.version.ver.split(".")[:2])
        if _ver < (2, 1):
            sys.exit(
                "pygame 2.1.0 or later is required (you have {}).\n"
                "Upgrade with:  pip install --upgrade pygame-ce".format(pygame.version.ver)
            )
    except (ValueError, AttributeError):
        # Handle potential future pygame version formats
        print(f"Warning: Could not parse pygame version {pygame.version.ver}, continuing anyway...")

    try:
        import pytmx  # noqa: F401
    except ImportError:
        sys.exit(
            "pytmx is not installed.\n"
            "Install it with:  pip install pytmx"
        )

import asyncio
import main


def run():
    if IS_WEB:
        # The browser needs an async game loop.
        if hasattr(main, "browser_main"):
            asyncio.run(main.browser_main())
        else:
            main.main()
    else:
        main.main()


if __name__ == "__main__":
    run()
