"""Uniform Loading Class.

This class represents uniform loadings.

Author: Zak Oster zc9oster@me.com
Version: 0.1
"""
from sympy import symbols, Symbol, Piecewise
from singularity.src.data.loading.Loading import Loading


class Uniform(Loading):
    """Uniform Loading Class."""
    def __init__(self, val: float, start: float, stop: float) -> None:
        """Constructor for uniform loading class.

        Args:
            val: float, the value of the loading
            start: float, starting point of the loading
            stop: float, stopping point of the loading

        Returns:
            None
        """
        if (start < 0 or stop < 0):
            raise ValueError
        if stop < start:
            raise ValueError
        self._val: float = val
        self._start: float = start
        self._stop: float = stop

    @property
    def val(self) -> float:
        """Returns the value of the loading.

        Args:
            None

        Returns:
            val: float, the value of the loading.
        """
        return self._val

    @val.setter
    def val(self, val: float) -> None:
        """Changes the value of the loading.

        Args:
            val: float, the value of the loading.

        Returns:
            None
        """
        self._val = val

    @property
    def start(self) -> float:
        """Returns the starting point of the loading.

        Args:
            None

        Returns:
            loc: float, starting point of the loading.
        """
        return self._start

    @start.setter
    def start(self, start: float) -> None:
        """Changes the starting point of the loading.

        Args:
            val: float, starting point of the loading.

        Returns:
            None
        """
        if start < 0:
            raise ValueError
        if self._stop <= start:
            raise ValueError
        self._start = start

    @property
    def stop(self) -> float:
        """Returns the stopping point of the loading.

        Args:
            None

        Returns:
            loc: float, stopping point of the loading.
        """
        return self._stop

    @stop.setter
    def stop(self, stop: float) -> None:
        """Changes the stopping point of the loading.

        Args:
            val: float, stopping point of the loading.

        Returns:
            None
        """
        if stop < 0:
            raise ValueError
        if stop <= self._start:
            raise ValueError
        self._stop = stop

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
            ((self._val * (x - self._start)**(0) -
              self._val * (x - self._stop)**(0)), x >= self._stop),
            (self._val * (x - self._start)**(0), True)
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
            ((self._val * (x - self._start)**(1) -
              self._val * (x - self._stop)**(1)), x >= self._stop),
            (self._val * (x - self._start)**(1), True)
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
            (((self._val / 2) * (x - self._start)**(2) -
              (self._val / 2) * (x - self._stop)**(2)), x >= self._stop),
            ((self._val / 2) * (x - self._start)**(2), True)
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
            (((self._val / 6) * (x - self._start)**(3) -
              (self._val / 6) * (x - self._stop)**(3)), x >= self._stop),
            ((self._val / 6) * (x - self._start)**(3), True)
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
            (((self._val / 24) * (x - self._start)**(4) -
              (self._val / 24) * (x - self._stop)**(4)), x >= self._stop),
            ((self._val / 24) * (x - self._start)**(4), True)
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
        return ('Uniform = {} from x = {} to {}'.format(
            self._val, self._start, self._stop))
