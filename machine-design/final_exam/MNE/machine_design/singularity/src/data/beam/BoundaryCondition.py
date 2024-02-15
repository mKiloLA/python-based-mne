"""Class to represent a Boundary Condition.

Each instance of this class is one boundary equation.

Author: Zak Oster zc9oster@me.com
Version: 0.1
"""
from singularity.src.data.enums.BondCondType import BondCondType


class BoundaryCondition:
    """Class to represent a Boundary Condition."""
    def __init__(self, kind: BondCondType,
                 val: float, loc: float) -> None:
        """Constructor for a boundary condition.

        Args:
            kind: BondCondType, the equation to apply
                conditions to
            val: float, the value of the equation
            loc: float, the location of the condition

        Returns:
            None
        """
        if loc < 0:
            raise ValueError
        self.__kind: BondCondType = kind
        self.__val: float = val
        self.__loc: float = loc

    @property
    def kind(self) -> BondCondType:
        """Returns the kind of the equation.

        Args:
            None

        Returns:
            val: float, the kind of the equation.
        """
        return self.__kind

    @kind.setter
    def kind(self, kind: BondCondType) -> None:
        """Changes the kind of the equation.

        Args:
            val: float, the kind of the equation.

        Returns:
            None
        """
        self.__kind = kind

    @property
    def val(self) -> float:
        """Returns the value of the equation.

        Args:
            None

        Returns:
            val: float, the value of the equation.
        """
        return self.__val

    @val.setter
    def val(self, val: float) -> None:
        """Changes the value of the equation.

        Args:
            val: float, the value of the equation.

        Returns:
            None
        """
        self.__val = val

    @property
    def loc(self) -> float:
        """Returns the location of the equation.

        Args:
            None

        Returns:
            loc: float, the location of the equation.
        """
        return self.__loc

    @loc.setter
    def loc(self, loc: float) -> None:
        """Changes the location of the equation.

        Args:
            val: float, the location of the equation.

        Returns:
            None
        """
        if loc < 0:
            raise ValueError
        self.__loc = loc

    def __str__(self) -> str:
        """Change the default string representation.

        Args:
            None

        Returns:
            output: str, the string representation
        """
        return ("{} equation is {:.2f} at x = {:.2f}".format(
            self.__kind, self.__val, self.__loc))

    def __eq__(self, obj: object) -> bool:
        """Change the default equal operator.

        This makes boundary conditions equal if they have the same
        type, value, and location.

        Args:
            obj: object, the object to compare to

        Returns:
            val: bool, true if bc's are the same, else false
        """
        if isinstance(obj, BoundaryCondition):
            return (self.__kind == obj.kind and
                    self.__val == obj.val and
                    self.__loc == obj.loc)
        else:
            return False
