"""Class for the Primary GUI Window.

Zak Oster zcoster@ksu.edu
v0.1.0
"""
import tkinter as tk
from tkinter import ttk
from singularity.src.gui.LoadingPanel import LoadingPanel
from singularity.src.gui.SummaryPanel import SummaryPanel
from singularity.src.data.beam.Beam import Beam


class PrimaryWindow(tk.Tk):
    """Class to represent the main window."""
    def __init__(self) -> None:
        """Constructor to initialize the window.

        __init__ does not take any args, and only one instance
        of the class should exist at a time.

        Attributes:
            style: ttk.Style, adds color way to tkinter
            beam: Beam, the beam being created by program
            main: Optional[Frame], the frame to hold LoadingPanel
            summary: SummaryPanel, the frame to hold SummaryPanel
        """
        tk.Tk.__init__(self)
        self.__style = ttk.Style(self)
        self.tk.call('source', 'Forest-ttk-theme-1.0/forest-dark.tcl')
        self.__style.theme_use("forest-dark")

        self.minsize(width=1316, height=987)
        self.maxsize(width=1316, height=987)
        self.title("Singularity Solver")

        self.__beam = Beam()
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=10)
        self.grid_columnconfigure(1, weight=1)

        self.__main = None
        self.load_loading_panel()

        self.__summary = SummaryPanel(self)
        self.__summary.grid(row=0, column=1, padx=10, pady=10, sticky='NSEW')

    def load_loading_panel(self, set_load_tab=False) -> None:
        """Loads an instance of the loading panel class.

        Args:
            set_load_tab: bool, determines which tab should
                be displayed when loading the panel

        Returns:
            None
        """
        self.load_panel(LoadingPanel(self, set_load_tab))

    def load_panel(self, panel) -> None:
        """Loads an instance of a panel.

        Loads a panel into the main panel slot (left side).
        If panel already exists, first destroy current panel.

        Args:
            panel (MenuPanel): likely a menu panel, the panel
                to load on left side of window
        """
        if self.__main is not None:
            self.__main.destroy()
        self.__main = panel
        self.__main.grid(row=0, column=0, padx=10, pady=10, sticky='NSEW')

    def save_load(self, load):
        """Save an item to the summary panel.

        Args:
            load: Loading, the loading to save

        Returns:
            None
        """
        self.__summary.save_load(load)

    def update_labels(self):
        """Save an item to the summary panel.

        Args:
            None

        Returns:
            None
        """
        self.__summary.update_labels()

    @property
    def beam(self) -> None:
        """Returns the beam object.

        Args:
            None

        Returns:
            beam: Beam, the beam attribute
        """
        return self.__beam

    @beam.setter
    def beam(self, val: Beam) -> None:
        """Sets the beam object.

        Args:
            val: Beam, value to set beam to

        Returns:
            None
        """
        self.__beam = val

    def is_number(self, val: str) -> bool:
        """Checks if a string is a number.

        Args:
            val: str, the string to check

        Returns:
            val: bool, True if number else False
        """
        try:
            float(val)
            return True
        except ValueError:
            return False
