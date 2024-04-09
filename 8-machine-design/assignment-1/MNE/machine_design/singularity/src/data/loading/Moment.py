"""Moment Loading Class.

This class represents moment loads on a beam.

Author: Zak Oster zc9oster@me.com
Version: 0.1
"""
from sympy import symbols, Symbol, Piecewise
from singularity.src.data.loading.Loading import Loading


class Moment(Loading):
    """Moment Loading Class."""
    def __init__(self, val: float, loc: float) -> None:
        """Constructor for moment class.

        Args:
            val: float, the value of the loading
            loc: float, the location of the loading

        Returns:
            None
        """
        super().__init__(val, loc)

    @property
    def distribution(self) -> Piecewise:
        """Distributing function for the loading.

        Args:
            None

        Returns:
            q: Piecewise, distribution equation
        """
        x: Symbol = symbols('x')
        q: Piecewise = Piecewise(
            (0, x <= self._loc),
            (self._val * (x - self._loc)**(-2), x > self._loc)
        )
        return q

    @property
    def shear(self) -> Piecewise:
        """Shear function for the loading.

        Args:
            None

        Returns:
            V: Piecewise, shear equation
        """
        x: Symbol = symbols('x')
        v: Piecewise = Piecewise(
            (0, x <= self._loc),
            (self._val * (x - self._loc)**(-1), x > self._loc)
        )
        return v

    @property
    def moment(self) -> Piecewise:
        """Moment function for the loading.

        Args:
            None

        Returns:
            M: Piecewise, moment equation
        """
        x: Symbol = symbols('x')
        m: Piecewise = Piecewise(
            (0, x <= self._loc),
            (self._val * (x - self._loc)**(0), x > self._loc)
        )
        return m

    @property
    def slope(self) -> Piecewise:
        """Slope function for the loading.

        Args:
            None

        Returns:
            theta: Piecewise, slope equation
        """
        x: Symbol = symbols('x')
        theta: Piecewise = Piecewise(
            (0, x <= self._loc),
            (self._val * (x - self._loc)**(1), x > self._loc)
        )
        return theta

    @property
    def deflection(self) -> Piecewise:
        """Deflection function for the loading.

        Args:
            None

        Returns:
            v: Piecewise, deflection equation
        """
        x: Symbol = symbols('x')
        v: Piecewise = Piecewise(
            (0, x <= self._loc),
            ((self._val / 2) * (x - self._loc)**(2), x > self._loc)
        )
        return v

    def __eq__(self, obj: object) -> bool:
        """Change the default equal operator.

        This makes loadings equal if they have the same
        type, value, and location.

        Args:
            obj: object, the object to compare to

        Returns:
            val: bool, true if loadings are the same, else false
        """
        if isinstance(obj, Moment):
            return (self._val == obj.val and
                    self._loc == obj.loc)
        else:
            return False

    def __str__(self) -> str:
        """Change the default string.

        Args:
            None

        Returns:
            val: str, the string representation of the load
        """
        return ('Moment = {} @x = {}'.format(
            self._val, self._loc))
