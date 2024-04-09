"""Enumeration for Boundary Conditions.

Each enum is a different boundary condition for a beam.

Author: Zak Oster zcoster@ksu.edu
Version: 0.1
"""
from enum import Enum


class BondCondType(Enum):
    """Enumeration of boundary condition name."""
    DISTRIBUTION = 'Distribution'
    SHEAR = 'Shear'
    MOMENT = 'Moment'
    SLOPE = 'Slope'
    DEFLECTION = 'Deflection'

    def __str__(self) -> str:
        """String name of the boundary condition.

        Returns:
            value: str, the name of the enum
        """
        return str(self.value)

    def __repr__(self) -> str:
        """Representation name of the boundary condition.

        Returns:
            value: str, the name of the enum
        """
        return str(self)
