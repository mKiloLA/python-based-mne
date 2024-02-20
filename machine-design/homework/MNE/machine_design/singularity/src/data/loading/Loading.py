"""Loading Parent Class.

This is the base class for the different loading types.
It is an abstract class and should not be instantiated.

Author: Zak Oster zc9oster@me.com
Version: 0.1
"""


class Loading:
    """Loading Parent Class."""
    def __init__(self, val: float, loc: float) -> None:
        """Constructor for Loading class.

        Args:
            val: float, the value of the loading
            loc: float, the location of the loading

        Returns:
            None
        """
        if loc < 0:
            raise ValueError
        self._val: float = val
        self._loc: float = loc

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
    def loc(self) -> float:
        """Returns the location of the loading.

        Args:
            None

        Returns:
            loc: float, the location of the loading.
        """
        return self._loc

    @loc.setter
    def loc(self, loc: float) -> None:
        """Changes the location of the loading.

        Args:
            val: float, the location of the loading.

        Returns:
            None
        """
        if loc < 0:
            raise ValueError
        self._loc = loc

    @property
    def distribution(self) -> None:
        """Distributing function for the loading.

        Implement in child class.

        Args:
            None

        Returns:
            None
        """
        raise NotImplementedError

    @property
    def shear(self) -> None:
        """Shear function for the loading.

        Implement in child class.

        Args:
            None

        Returns:
            None
        """
        raise NotImplementedError

    @property
    def moment(self) -> None:
        """Moment function for the loading.

        Implement in child class.

        Args:
            None

        Returns:
            None
        """
        raise NotImplementedError

    @property
    def slope(self) -> None:
        """Slope function for the loading.

        Implement in child class.

        Args:
            None

        Returns:
            None
        """
        raise NotImplementedError

    @property
    def deflection(self) -> None:
        """Deflection function for the loading.

        Implement in child class.

        Args:
            None

        Returns:
            None
        """
        raise NotImplementedError

    def __eq__(self, obj: object) -> bool:
        """Default equal operator.

        Args:
            obj: Object, object to compare against

        Returns:
            None
        """
        raise NotImplementedError
