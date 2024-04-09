"""Class to display loading options.

Author: Zak Oster zcoster@ksu.edu
Version: 0.1
"""
import tkinter as tk
from tkinter import ttk, font
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk)
from singularity.src.data.solver.Grapher import Grapher


class ResultPanel(tk.Frame):
    """Class to display loading options."""
    def __init__(self, master, units) -> None:
        """Constructor to initialize the menu panel.

        Attributes:
            master: PrimaryWindow, frame this panel fits in
            eq_font: font.Font, font to change size of text
        """
        self.__master = master
        ttk.Frame.__init__(self, master=self.__master)
        self.eq_font = font.Font(self, size=10)

        title_label = tk.Label(
            master=self,
            text='Singularity Solver Results',
            font=12)
        title_label.grid(row=0, column=0, padx=2, pady=2, sticky='NSEW')

        graph_panel = tk.Frame(
            master=self,
            highlightbackground="gray",
            highlightthickness=1)
        graph_panel.grid(row=1, column=0, padx=2, pady=2, sticky="NSEW")

        # the figure that will contain the plot
        fig = Grapher.graph(self.__master.beam, units)

        # creating the Tkinter canvas
        # containing the Matplotlib figure
        canvas = FigureCanvasTkAgg(fig, master=graph_panel)
        canvas.draw()

        # placing the canvas on the Tkinter window
        canvas.get_tk_widget().pack()

        # creating the Matplotlib toolbar
        toolbar = NavigationToolbar2Tk(canvas, graph_panel)
        toolbar.update()

        # placing the toolbar on the Tkinter window
        canvas.get_tk_widget().pack()

        eq_label = tk.Label(
            master=self,
            text='Singularity Equations',
            font=12)
        eq_label.grid(row=2, column=0, padx=2, pady=2, sticky='NSEW')

        defl_label = tk.Label(
            master=self,
            text=self.__master.beam.str_deflection(),
            font=self.eq_font)
        defl_label.grid(row=3, column=0, padx=2, pady=2, sticky='NSEW')

        slope_label = tk.Label(
            master=self,
            text=self.__master.beam.str_slope(),
            font=self.eq_font)
        slope_label.grid(row=4, column=0, padx=2, pady=2, sticky='NSEW')

        moment_label = tk.Label(
            master=self,
            text=self.__master.beam.str_moment(),
            font=self.eq_font)
        moment_label.grid(row=5, column=0, padx=2, pady=2, sticky='NSEW')

        shear_label = tk.Label(
            master=self,
            text=self.__master.beam.str_shear(),
            font=self.eq_font)
        shear_label.grid(row=6, column=0, padx=2, pady=2, sticky='NSEW')

        if units:
            ei_label = tk.Label(
                master=self,
                text='Where EI = {:.0f}N-m\u00B2'.format(
                    self.__master.beam.material.E *
                    self.__master.beam.inertia),
                font=self.eq_font)
            ei_label.grid(row=7, column=0, padx=2, pady=2, sticky='NSEW')
        else:
            ei_label = tk.Label(
                master=self,
                text='Where EI = {:.0f}ksi-in\u2074'.format(
                    (self.__master.beam.material.E *
                     self.__master.beam.inertia / 6.895e6)),
                font=self.eq_font)
            ei_label.grid(row=7, column=0, padx=2, pady=2, sticky='NSEW')

        # Add cancel button
        back = tk.Button(
            master=self, text='Back',
            command=lambda: self.action_performed('back'))
        back.grid(row=8, column=0, sticky='SEW')

    def action_performed(self, text: str) -> None:
        """Performs an action given a string.

        Args:
            text: str, string indicator of which action to perform

        Returns:
            None
        """
        if text == 'back':
            self.__master.load_loading_panel(True)
