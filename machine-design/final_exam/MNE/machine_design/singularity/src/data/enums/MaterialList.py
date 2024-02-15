"""Class to represent a list of materials.

Author: Zak Oster zcoster@ksu.edu
Version: 0.1
"""
from typing import List, Dict, Optional, Iterable, Iterator
from singularity.src.data.enums.Material import Material
import json


class MaterialList(Iterable[Material]):
    """Class to represent a list of materials.

    Only one of this class should exist at a time. __new__
    has been highjacked to ensure this is the case.

    Class Attributes:
        instance: MaterialList, the single instance of MaterialList
    """

    _instance: Optional['MaterialList'] = None

    def __new__(cls, path: Optional[str] = None) -> 'MaterialList':
        """Highjacked new method to return single instance.

        Args:
            None

        Attributes:
            mat_list: List[Material], list containing every
                material option

        Returns:
            instance: MaterialList, the single instance of the
                MaterialList class
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.__mat_list: List[Material] = list()
            if path is None:
                cls._instance.__path: str = 'materials.json'
            else:
                cls._instance.__path: str = path
            cls._instance.load()
        return cls._instance

    def save(self) -> None:
        """Saves the materials to the JSON file.

        Args:
            None

        Returns:
            None
        """
        dict_list: List[Dict[str, float]] = list()
        for mat in self.__mat_list:
            mat_dict: Dict[str, float] = dict()
            mat_dict['Name'] = mat.name
            mat_dict['E'] = mat.E
            dict_list.append(mat_dict)

        with open(self.__path, "w") as file:
            json.dump(dict_list, file, indent=3)

    def load(self) -> None:
        """Loads the materials from a json file.

        Args:
            None

        Returns:
            None
        """
        with open(self.__path) as file:
            mat_dict: Dict[str, int] = json.load(file)
            for mat in mat_dict:
                new_mat: Material = Material()
                new_mat.name = mat['Name']
                try:
                    new_mat.E = float(mat['E'])
                except Exception:
                    new_mat.E = 0
                self.__mat_list.append(new_mat)

    def append(self, value: Material) -> None:
        """Add a material to the end of the list.

        Args:
            value: Material, material to be added

        Returns:
            None
        """
        self.__mat_list.append(value)

    def get(self, name: str) -> Optional[Material]:
        """Given a material name, return material.

        Args:
            name: str, the name of the material

        Returns:
            value: Material, the matching material name
        """
        for mat in self.__mat_list:
            if name == mat.name:
                return mat
        return None

    def __iter__(self) -> Iterator[Material]:
        """Iterates through the material list.

        Args:
            None

        Returns:
            value: Iterator[Material], next material in list
        """
        return iter(self.__mat_list)

    def __len__(self) -> int:
        """Returns the length of material list.

        Args:
            None

        Returns:
            value: int, length of the material list
        """
        return len(self.__mat_list)

    def __getitem__(self, position: int) -> Material:
        """Allows indexing by position.

        Args:
            position: int, the index to be accessed.

        Returns:
            value: Material, material at given index
        """
        return self.__mat_list[position]

    def __setitem__(self, position: int, value: Material) -> None:
        """Allows changing value at given index.

        Args:
            position: int, the index to be accessed
            value: Material, item to place at index

        Returns:
            None
        """
        self.__mat_list[position] = value

    def __delitem__(self, position: int) -> None:
        """Delete a list value at given index.

        Args:
            position: int, the index to be accessed.

        Returns:
            None
        """
        del self.__mat_list[position]

    def __contains__(self, mat: Material) -> bool:
        """Check to see if an item is in the material list.

        Args:
            mat: Material, the material to look for

        Returns:
            value: bool, true if contained, else false
        """
        if isinstance(mat, Material):
            for val in self.__mat_list:
                if (val.name == mat.name and
                        val.E == mat.E):
                    return True
        return False
