"""Class to begin the gui from.

Author: Zak Oster
Version: 0.1
"""
from singularity.src.gui.PrimaryWindow import PrimaryWindow


class GUI:
    """Main Class.

    Class to start GUI from.
    """
    @staticmethod
    def start_gui() -> None:
        """Static method to begin the gui.

        Args:
            None

        Returns:
            None
        """
        PrimaryWindow().mainloop()
