"""Class to build Panels.

Author: Zak Oster zc9oster@me.com
Version: 0.1
"""
from singularity.src.data.loading.Loading import Loading
from singularity.src.data.loading.Point import Point
from singularity.src.data.loading.Moment import Moment
from singularity.src.data.loading.Uniform import Uniform
from singularity.src.data.loading.Linear import Linear
from singularity.src.gui.loadings.MomentPanel import MomentPanel
from singularity.src.gui.loadings.PointPanel import PointPanel
from singularity.src.gui.loadings.UniformPanel import UniformPanel
from singularity.src.gui.loadings.LinearPanel import LinearPanel
import tkinter as tk
from typing import Union


class PanelFactory:
    """Class to build panels based on provided input."""
    @staticmethod
    def get_panel(name: Union[str, Loading], master) -> tk.Frame:
        """Given a name or type, return the correct Panel.

        Args:
            name: str, Loading, if given a string, return new item
                of that type if given a loading, return a panel
                using that loading
            master: PrimaryWindow, reference to the main window
        """
        if isinstance(name, str):
            if name == 'moment':
                return MomentPanel(master)
            elif name == 'point':
                return PointPanel(master)
            elif name == 'uniform':
                return UniformPanel(master)
            elif name == 'linear':
                return LinearPanel(master)
            else:
                raise Exception("Not a valid load name.")
        elif isinstance(name, Loading):
            if isinstance(name, Moment):
                return MomentPanel(master, name)
            elif isinstance(name, Point):
                return PointPanel(master, name)
            elif isinstance(name, Uniform):
                return UniformPanel(master, name)
            elif isinstance(name, Linear):
                return LinearPanel(master, name)
        else:
            raise Exception("Not a valid type for load.")
