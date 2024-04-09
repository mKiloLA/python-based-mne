"""Class to display point loadings.

Author: Zak Oster zc9oster@me.com
Version: 0.1
"""
import tkinter as tk
from singularity.src.data.loading.Point import Point


class PointPanel(tk.Frame):
    """Class to display moment loadings."""
    def __init__(self, master, load=None) -> None:
        """Constructor to initialize Point Panel.

        Args:
            master: PrimaryWindow, the parent window
                that this window fits into

        Attributes:
            pass
        """
        self.__master = master
        if load is None:
            self._load = Point(0, 0)
        else:
            self._load = load

        tk.Frame.__init__(
            self,
            master=self.__master,
            highlightbackground="gray",
            highlightthickness=1)

        self.__beam = self.__master.beam

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)

        # Add title
        title = tk.Label(
            master=self,
            text='Point Load',
            font=12)
        title.grid(
            row=0, column=0, columnspan=2,
            padx=2, pady=2, sticky='NSEW')

        # Add value
        val_label = tk.Label(
            master=self,
            text='Value (N or kip):',
            font=8)
        val_label.grid(row=1, column=0, padx=2, pady=2, sticky='NE')

        self._value = tk.StringVar(value=str(self._load.val))
        value_entry = tk.Entry(master=self,
                               textvariable=self._value,
                               font=8)
        value_entry.grid(row=1, column=1, padx=2, pady=2, sticky='NW')

        # Add location
        loc_label = tk.Label(
            master=self,
            text='Location (m or ft):',
            font=8)
        loc_label.grid(row=2, column=0, padx=2, pady=2, sticky='NE')

        self._loc = tk.StringVar(value=str(self._load.loc))
        loc_entry = tk.Entry(master=self,
                             textvariable=self._loc,
                             font=8)
        loc_entry.grid(row=2, column=1, padx=2, pady=2, sticky='NW')

        # Add save button
        save = tk.Button(
            master=self, text='Save',
            command=lambda: self.action_performed('save'))
        save.grid(row=3, column=0, sticky='NEW')

        # Add cancel button
        cancel = tk.Button(
            master=self, text='Cancel',
            command=lambda: self.action_performed('cancel'))
        cancel.grid(row=3, column=1, sticky='NEW')

        self.__info_label = tk.Label(
            master=self,
            text='',
            font=8)
        self.__info_label.grid(
            row=4, column=0, columnspan=2,
            padx=2, pady=2, sticky='NEW')

    def action_performed(self, text: str) -> None:
        """Performs an action given a string.

        Args:
            text: str, string indicator of which action to perform

        Returns:
            None
        """
        if text == 'save':
            # Check value
            if not self.__master.is_number(self._value.get()):
                self.__info_label.config(
                        text='Value must be a number!')
                return
            # Check location
            if self.__master.is_number(self._loc.get()):
                if (float(self._loc.get()) < 0 or
                        float(self._loc.get()) > self.__beam.length):
                    self.__info_label.config(
                        text='Location must be on the bar!')
                    return
            else:
                self.__info_label.config(
                    text='Location must be a number!')
                return
            self._load.val = float(self._value.get())
            self._load.loc = float(self._loc.get())
            self.__master.save_load(self._load)
            self.__master.load_loading_panel(True)
        elif text == 'cancel':
            self.__master.load_loading_panel(True)
