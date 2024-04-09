"""Class to graph singularity functions.

Author: Zak Oster zcoster@ksu.edu
Version: 0.1
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt  # noqa: E402
from sympy import symbols, lambdify, Add, Symbol  # noqa: E402
import numpy as np  # noqa: E402
from singularity.src.data.beam.Beam import Beam  # noqa: E402


class Grapher:
    """Class to graph singularity functions."""
    @staticmethod
    def graph(rod: Beam, units: bool = True):
        """Graphs a given beam.

        Args:
            rod: Beam, the beam object to analyze
            units: bool, SI units if True, English if False

        Returns:
            fig: matplotlib.fig, the plot created for the beam
        """
        x: Symbol = symbols('x')
        rod.calc_constants()

        shear: Add = rod.shear()
        moment: Add = rod.moment()
        slope: Add = rod.slope()
        defl: Add = rod.deflection()

        if not units:
            slope = (12**2*6.895e6) * slope
            defl = (12**3*6.895e6) * defl

        a: np.ndarray = np.linspace(0, rod.length, 500)
        shear = lambdify(x, shear, 'numpy')
        moment = lambdify(x, moment, 'numpy')
        slope = lambdify(x, slope, 'numpy')
        defl = lambdify(x, defl, 'numpy')
        
        plt.style.use("dark_background")
        fig, axs = plt.subplots(2, 2, figsize=(11, 7), dpi=90)  
        axs[0, 0].plot(a, shear(a), label=rod.str_shear())
        axs[0, 1].plot(a, moment(a), 'tab:orange', label=rod.str_moment())
        axs[1, 0].plot(a, slope(a), 'tab:green', label=rod.str_slope())
        axs[1, 1].plot(a, defl(a), 'tab:red', label=rod.str_deflection())
        axs[0, 1].yaxis.set_label_position('right')
        axs[0, 1].yaxis.tick_right()
        axs[1, 1].yaxis.set_label_position('right')
        axs[1, 1].yaxis.tick_right()

        if units:
            axs[0, 0].set_title('Shear Diagram')
            axs[0, 0].set(ylabel='Shear (N)')
            axs[0, 1].set_title('Moment Diagram')
            axs[0, 1].set(ylabel='Moment (N-m)')
            axs[1, 0].set_title('Slope Diagram')
            axs[1, 0].set(
                xlabel="Location on Beam (m)",
                ylabel='Slope (rad)')
            axs[1, 1].set_title('Deflection Diagram')
            axs[1, 1].set(
                xlabel="Location on Beam (m)",
                ylabel='Deflection (m)')
        else:
            axs[0, 0].set_title('Shear Diagram')
            axs[0, 0].set(ylabel='Shear (kip)')
            axs[0, 1].set_title('Moment Diagram')
            axs[0, 1].set(ylabel='Moment (kip-ft)')
            axs[1, 0].set_title('Slope Diagram')
            axs[1, 0].set(
                xlabel="Location on Beam (ft)",
                ylabel='Slope (rad)')
            axs[1, 1].set_title('Deflection Diagram')
            axs[1, 1].set(
                xlabel="Location on Beam (ft)",
                ylabel='Deflection (in)')
        return fig
