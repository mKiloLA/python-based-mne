"""Sample Main Project File.

This file is executed when the entire src directory is run using Python
and serves as the main entry point for the application.

Usage:
    python -m singularity - execute this program (when run from project root).

Author: Zak Oster zcoster@ksu.edu
Version: 0.1
"""
from singularity.src.GUI import GUI


def main() -> None:
    """Main Function.

    Main routine that is called when program begins.

    Args:
        None

    Returns:
        None
    """
    GUI.start_gui()


if __name__ == "__main__":
    main()
