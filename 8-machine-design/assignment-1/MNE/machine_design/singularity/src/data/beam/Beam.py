"""Class to represent a beam.

This class represents a beam.

Author: Zak Oster zc9oster@me.com
Version: 0.1
"""
from typing import List, Dict, Union, Optional
from sympy import symbols, Symbol, Piecewise, Add, solve, nan
from singularity.src.data.loading.Loading import Loading
from singularity.src.data.loading.Point import Point
from singularity.src.data.loading.Moment import Moment
from singularity.src.data.loading.Uniform import Uniform
from singularity.src.data.loading.Linear import Linear
from singularity.src.data.beam.BoundaryCondition import BoundaryCondition
from singularity.src.data.enums.Material import Material
from singularity.src.data.enums.BondCondType import BondCondType


class Beam:
    """Class to represent a beam."""
    def __init__(self, material: Optional[Material] = None,
                 length: float = 0.0,
                 base: float = 0.0,
                 height: float = 0.0) -> None:
        """Constructor for a beam.

        Args:
            material: Material, the material of the beam
            length: float, the length of the beam
            base: float, the base dimension of the beam
            height: float, the height of the beam

        Attributes:
            material: Material, the material of the beam
            inertia: float, the moment of inertia of the beam
            length: float, the length of the beam
            base: float, the base dimension of the beam
            height: float, the height of the beam
            loadings: List[Loading], the loading on the beam
            bc: List[BoundaryConditions], the boundary conditions
                for the beam
            c1: float, first constant of integration
            c2: float, second constant of integration

        Returns:
            None
        """
        self.__material: Material = material
        self.__base: float = base
        self.__height: float = height
        self.__length: float = length
        self.__loadings: List[Loading] = list()
        self.__bc: List[BoundaryCondition] = list()
        self.__c1: float = 0.0
        self.__c2: float = 0.0

    @property
    def material(self) -> Material:
        """Returns the type of material.

        Args:
            None

        Returns:
            val: Material, the type of the material.
        """
        return self.__material

    @material.setter
    def material(self, val: float) -> Material:
        """Changes the type of material.

        Args:
            val: Material, the type of material.

        Returns:
            None
        """
        self.__material = val

    @property
    def inertia(self) -> float:
        """Returns the moment of inertia.

        Args:
            None

        Returns:
            val: float, the moment of inertia for
                the cross section.
        """
        return (self.__base * self.__height**3 / 12)

    @property
    def length(self) -> float:
        """Returns the length of the beam.

        Args:
            None

        Returns:
            val: float, the length of the beam.
        """
        return self.__length

    @length.setter
    def length(self, val: float) -> None:
        """Changes the length of the beam.

        Args:
            val: float, the length of the beam.

        Returns:
            None
        """
        if val < 0:
            raise ValueError
        self.__length = val

    @property
    def base(self) -> float:
        """Returns the base length.

        Args:
            None

        Returns:
            val: float, the length of the base.
        """
        return self.__base

    @base.setter
    def base(self, val: float) -> None:
        """Changes the length of the base.

        Args:
            val: float, the length of the base.

        Returns:
            None
        """
        if val < 0:
            raise ValueError
        self.__base = val

    @property
    def height(self) -> float:
        """Returns the height length.

        Args:
            None

        Returns:
            val: float, the length of the height.
        """
        return self.__height

    @height.setter
    def height(self, val: float) -> None:
        """Changes the length of the height.

        Args:
            val: float, the length of the height.

        Returns:
            None
        """
        if val < 0:
            raise ValueError
        self.__height = val

    @property
    def c1(self) -> float:
        """Returns the first integration constant.

        Args:
            None

        Returns:
            val: float, first integration constant
        """
        return self.__c1

    @c1.setter
    def c1(self, val: float) -> None:
        """Changes the first integratin constant.

        Args:
            val: float, the integration constant.

        Returns:
            None
        """
        self.__c1 = val

    @property
    def c2(self) -> float:
        """Returns the second integration constant.

        Args:
            None

        Returns:
            val: float, second integration constant
        """
        return self.__c2

    @c2.setter
    def c2(self, val: float) -> None:
        """Changes the second integratin constant.

        Args:
            val: float, the integration constant.

        Returns:
            None
        """
        self.__c2 = val

    @property
    def loadings(self) -> List[Loading]:
        """Returns the loadings on the beam.

        Args:
            None

        Returns:
            val: List[Loading], the loadings on the beam.
        """
        return self.__loadings

    def add_loading(self, load: Loading) -> None:
        """Adds a loading to the beam.

        Args:
            load: Loading, the loading to add to the beam

        Returns:
            None
        """
        self.__loadings.append(load)

    def remove_loading(self, load: Loading) -> None:
        """Remove a loading from the beam.

        Args:
            load: Loading, the loading to add to the beam

        Returns:
            None
        """
        if load in self.__loadings:
            self.__loadings.remove(load)

    @property
    def bc(self) -> List[BoundaryCondition]:
        """Returns the boundary conditions of the beam.

        Args:
            None

        Returns:
            val: List[BoundaryCondition], the bc on beam
        """
        return self.__bc

    def add_bc(self, bc: BoundaryCondition) -> None:
        """Adds a boundary conditions to the beam.

        Args:
            bc: BoundaryCondition, the boundary condition
                to add to the beam

        Returns:
            None
        """
        self.__bc.append(bc)

    def remove_bc(self, bc: BoundaryCondition) -> None:
        """Remove a boundary condition from the beam.

        Args:
            load: BoundaryCondition, the boundary condition
                to remove from the beam

        Returns:
            None
        """
        if bc in self.__bc:
            self.__bc.remove(bc)

    def clear_bc(self) -> None:
        """Remove all boundary conditions from beam.

        Args:
            None

        Returns:
            None
        """
        self.__bc = list()

    def calc_constants(self) -> None:
        """Find the constants of integration.

        Args:
            None

        Returns:
            None
        """
        x: Symbol = symbols('x')
        c1: Symbol = symbols('c1')
        c2: Symbol = symbols('c2')
        equations: List[Add] = list()
        for bound in self.__bc:
            if bound.kind == BondCondType.DEFLECTION:
                defl: Union[Piecewise, Add, float] = 0.0
                for load in self.__loadings:
                    defl += load.deflection
                defl += c1 * x + c2 - bound.val
                defl = defl.subs(x, bound.loc)
                if defl == nan:
                    defl = c2
                equations.append(defl)
            elif bound.kind == BondCondType.SLOPE:
                slope: Union[Piecewise, Add, float] = 0.0
                for load in self.__loadings:
                    defl += load.slope
                slope += c1 - bound.val
                slope = slope.subs(x, bound.loc)
                equations.append(slope)
        sol: Dict[str, float] = solve((equations[0], equations[1]), (c1, c2))
        self.__c1 = sol[c1]
        self.__c2 = sol[c2]

    def shear(self) -> Add:
        """Return the piecewise function for the shear equation.

        Args:
            None

        Returns:
            None
        """
        equation: Union[Piecewise, Add, float] = 0.0
        for load in self.__loadings:
            equation += load.shear
        return equation

    def moment(self) -> Add:
        """Return the piecewise function for the moment equation.

        Args:
            None

        Returns:
            None
        """
        equation: Union[Piecewise, Add, float] = 0.0
        for load in self.__loadings:
            equation += load.moment
        return equation

    def slope(self) -> Add:
        """Return the piecewise function for the slope equation.

        Args:
            None

        Returns:
            None
        """
        equation: Union[Piecewise, Add, float] = 0.0
        for load in self.__loadings:
            equation += load.slope
        equation += self.__c1
        return equation / (self.inertia * self.material.E)

    def deflection(self) -> Add:
        """Return the piecewise function for the deflection equation.

        Args:
            None

        Returns:
            None
        """
        x: Symbol = symbols('x')
        equation: Union[Piecewise, Add, float] = 0.0
        for load in self.__loadings:
            equation += load.deflection
        equation += (self.__c1 * x + self.__c2)
        return equation / (self.inertia * self.material.E)

    def str_deflection(self) -> str:
        """Returns string version of deflection equation.

        Args:
            None

        Returns:
            value: str, a pretty, string version of the equation
        """
        output: List[str] = list()
        for load in self.__loadings:
            if isinstance(load, Point):
                output.append(
                    "{:.2f}<x - {:.2f}>\u00B3".format(
                        (load.val / 6), load.loc))
            elif isinstance(load, Moment):
                output.append(
                    "{:.2f}<x - {:.2f}>\u00B2".format(
                        (load.val / 2), load.loc))
            elif isinstance(load, Linear):
                if (load.val < 0):
                    output.append(
                        "{:.2f}<x - {:.2f}>\u2075".format(
                            (load.val / 120), load.start))
                    output.append(
                        "{:.2f}<x - {:.2f}>\u2075".format(
                            abs(load.val / 120), load.stop))
                else:
                    output.append(
                        "{:.2f}<x - {:.2f}>\u2075".format(
                            (load.val / 120), load.start))
                    output.append(
                        "{:.2f}<x - {:.2f}>\u2075".format(
                            (load.val / -120), load.stop))
            elif isinstance(load, Uniform):
                if (load.val < 0):
                    output.append(
                        "{:.2f}<x - {:.2f}>\u2074".format(
                            (load.val / 24), load.start))
                    output.append(
                        "{:.2f}<x - {:.2f}>\u2074".format(
                            abs(load.val / 24), load.stop))
                else:
                    output.append(
                        "{:.2f}<x - {:.2f}>\u2074".format(
                            (load.val / 24), load.start))
                    output.append(
                        "{:.2f}<x - {:.2f}>\u2074".format(
                            (load.val / -24), load.stop))
        return ('v(x) = (EI)\u207B\u00B9 (' +
                ' + '.join(output) + ' + {:.2f}x + {:.2f})'.format(
                    self.__c1, self.__c2))

    def str_slope(self) -> str:
        """Returns string version of slope equation.

        Args:
            None

        Returns:
            value: str, a pretty, string version of the equation
        """
        output: List[str] = list()
        for load in self.__loadings:
            if isinstance(load, Point):
                output.append(
                    "{:.2f}<x - {:.2f}>\u00B2".format(
                        (load.val / 2), load.loc))
            elif isinstance(load, Moment):
                output.append(
                    "{:.2f}<x - {:.2f}>\u00B9".format(
                        load.val, load.loc))
            elif isinstance(load, Linear):
                if (load.val < 0):
                    output.append(
                        "{:.2f}<x - {:.2f}>\u2074".format(
                            (load.val / 24), load.start))
                    output.append(
                        "{:.2f}<x - {:.2f}>\u2074".format(
                            abs(load.val / 24), load.stop))
                else:
                    output.append(
                        "{:.2f}<x - {:.2f}>\u2074".format(
                            (load.val / 24), load.start))
                    output.append(
                        "{:.2f}<x - {:.2f}>\u2074".format(
                            (load.val / -24), load.stop))
            elif isinstance(load, Uniform):
                if (load.val < 0):
                    output.append(
                        "{:.2f}<x - {:.2f}>\u00B3".format(
                            (load.val / 6), load.start))
                    output.append(
                        "{:.2f}<x - {:.2f}>\u00B3".format(
                            abs(load.val / 6), load.stop))
                else:
                    output.append(
                        "{:.2f}<x - {:.2f}>\u00B3".format(
                            (load.val / 6), load.start))
                    output.append(
                        "{:.2f}<x - {:.2f}>\u00B3".format(
                            (load.val / -6), load.stop))
        return ('\u03B8(x) = (EI)\u207B\u00B9 (' +
                ' + '.join(output) + ' + {:.2f})'.format(self.__c1))

    def str_moment(self) -> str:
        """Returns string version of moment equation.

        Args:
            None

        Returns:
            value: str, a pretty, string version of the equation
        """
        output: List[str] = list()
        for load in self.__loadings:
            if isinstance(load, Point):
                output.append(
                    "{:.2f}<x - {:.2f}>\u00B9".format(
                        load.val, load.loc))
            elif isinstance(load, Moment):
                output.append(
                    "{:.2f}<x - {:.2f}>\u2070".format(
                        load.val, load.loc))
            elif isinstance(load, Linear):
                if (load.val < 0):
                    output.append(
                        "{:.2f}<x - {:.2f}>\u00B3".format(
                            (load.val / 6), load.start))
                    output.append(
                        "{:.2f}<x - {:.2f}>\u00B3".format(
                            abs(load.val / 6), load.stop))
                else:
                    output.append(
                        "{:.2f}<x - {:.2f}>\u00B3".format(
                            (load.val / 6), load.start))
                    output.append(
                        "{:.2f}<x - {:.2f}>\u00B3".format(
                            (load.val / -6), load.stop))
            elif isinstance(load, Uniform):
                if (load.val < 0):
                    output.append(
                        "{:.2f}<x - {:.2f}>\u00B2".format(
                            (load.val / 2), load.start))
                    output.append(
                        "{:.2f}<x - {:.2f}>\u00B2".format(
                            (abs(load.val) / 2), load.stop))
                else:
                    output.append(
                        "{:.2f}<x - {:.2f}>\u00B2".format(
                            (load.val / 2), load.start))
                    output.append(
                        "{:.2f}<x - {:.2f}>\u00B2".format(
                            (load.val / -2), load.stop))
        return 'M(x) = ' + ' + '.join(output)

    def str_shear(self) -> str:
        """Returns string version of shear equation.

        Args:
            None

        Returns:
            value: str, a pretty, string version of the equation
        """
        output: List[str] = list()
        for load in self.__loadings:
            if isinstance(load, Point):
                output.append(
                    "{:.2f}<x - {:.2f}>\u2070".format(
                        load.val, load.loc))
            elif isinstance(load, Moment):
                output.append(
                    "{:.2f}<x - {:.2f}>\u207B\u00B9".format(
                        load.val, load.loc))
            elif isinstance(load, Linear):
                if (load.val < 0):
                    output.append(
                        "{:.2f}<x - {:.2f}>\u00B2".format(
                            (load.val / 2), load.start))
                    output.append(
                        "{:.2f}<x - {:.2f}>\u00B2".format(
                            abs(load.val / 2), load.stop))
                else:
                    output.append(
                        "{:.2f}<x - {:.2f}>\u00B2".format(
                            (load.val / 2), load.start))
                    output.append(
                        "{:.2f}<x - {:.2f}>\u00B2".format(
                            (load.val / -2), load.stop))
            elif isinstance(load, Uniform):
                if (load.val < 0):
                    output.append(
                        "{:.2f}<x - {:.2f}>\u00B9".format(
                            load.val, load.start))
                    output.append(
                        "{:.2f}<x - {:.2f}>\u00B9".format(
                            abs(load.val), load.stop))
                else:
                    output.append(
                        "{:.2f}<x - {:.2f}>\u00B9".format(
                            load.val, load.start))
                    output.append(
                        "-{:.2f}<x - {:.2f}>\u00B9".format(
                            load.val, load.stop))
        return 'V(x) = ' + ' + '.join(output)
