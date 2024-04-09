"""Class to represent a material.

Young's Modulus is in Pascals.

Author: Zak Oster zcoster@ksu.edu
Version: 0.1
"""
from typing import Optional


class Material:
    """Class to represent a material."""

    def __init__(self) -> None:
        """Constructor for a material type.

        Args:
            None

        Attributes:
            name: str, name of the material
            E: int, modulus of elasticity for the material

        Returns:
            None
        """
        self.__name: Optional[str] = None
        self.__E: Optional[float] = None

    @property
    def name(self) -> Optional[str]:
        """Returns the name of the material.

        Args:
            None

        Returns:
            name: Optional[str], name of the material
        """
        return self.__name

    @name.setter
    def name(self, val: str) -> None:
        """Changes the name of the material.

        Args:
            val: str, the new name of material

        Returns:
            None
        """
        self.__name = val

    @property
    def E(self) -> Optional[float]:  # noqa: E802
        """Returns the young's modulus of the material.

        Args:
            None

        Returns:
            E: Optional[float], young's modulus
        """
        return self.__E

    @E.setter
    def E(self, val: float) -> None:  # noqa: E802
        """Changes the young modulus of the material.

        Args:
            val: float, young's modulus

        Returns:
            None
        """
        self.__E = val
