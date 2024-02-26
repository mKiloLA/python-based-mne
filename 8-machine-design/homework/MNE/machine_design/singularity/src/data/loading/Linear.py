"""Linear Loading Class.

This class represents linear loadings.

Author: Zak Oster zc9oster@me.com
Version: 0.1
"""
from sympy import symbols, Symbol, Piecewise
from singularity.src.data.loading.Uniform import Uniform


class Linear(Uniform):
    """Linear Loading Class."""
    def __init__(self, val: float, start: float, stop: float) -> None:
        """Constructor for linear loading class.

        Args:
            val: float, the value of the loading
            start: float, starting point of the loading
            stop: float, stopping point of the loading

        Returns:
            None
        """
        super().__init__(val, start, stop)

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
            (0, x <= self._start),
            ((self._val * (x - self._start)**(1) -
              self._val * (x - self._stop)**(1)), x >= self._stop),
            (self._val * (x - self._start)**(1), True)
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
            (0, x <= self._start),
            (((self._val / 2) * (x - self._start)**(2) -
              (self._val / 2) * (x - self._stop)**(2)), x >= self._stop),
            ((self._val / 2) * (x - self._start)**(2), True)
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
            (0, x <= self._start),
            (((self._val / 6) * (x - self._start)**(3) -
              (self._val / 6) * (x - self._stop)**(3)), x >= self._stop),
            ((self._val / 6) * (x - self._start)**(3), True)
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
            (0, x <= self._start),
            (((self._val / 24) * (x - self._start)**(4) -
              (self._val / 24) * (x - self._stop)**(4)), x >= self._stop),
            ((self._val / 24) * (x - self._start)**(4), True)
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
            (0, x <= self._start),
            (((self._val / 120) * (x - self._start)**(5) -
              (self._val / 120) * (x - self._stop)**(5)), x >= self._stop),
            ((self._val / 120) * (x - self._start)**(5), True)
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
        if isinstance(obj, Uniform):
            return (self._val == obj.val and
                    self._start == obj.start and
                    self._stop == obj.stop)
        else:
            return False

    def __str__(self) -> str:
        """Change the default string.

        Args:
            None

        Returns:
            val: str, the string representation of the load
        """
        return ('Linear = {} from x = {} to {}'.format(
            self._val, self._start, self._stop))
