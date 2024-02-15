"""Class to display material properties.

Author: Zak Oster zc9oster@me.com
Version: 0.1
"""
import tkinter as tk
from singularity.src.data.enums.Material import Material
from singularity.src.data.enums.MaterialList import MaterialList


class MaterialPanel(tk.Frame):
    """Class to display moment loadings."""
    def __init__(self, master, material=None) -> None:
        """Constructor to initialize material Panel.

        Attributes:
            master: PrimaryWindow, frame the panel belongs to
            material: Material, material to be edited
            name: StringVar, the name of the material
            young_mod: StringVar, the youngs modulus of material
            info_label: StringVar, information to tell user
        """
        self.__master = master
        if material is None:
            self._material = Material()
        else:
            self._material = MaterialList().get(material)

        tk.Frame.__init__(
            self,
            master=self.__master,
            highlightbackground="gray",
            highlightthickness=1)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)

        top_label = tk.Label(
            master=self,
            text='New/Edit Material List',
            font=(25))
        top_label.grid(
            row=0, column=0, columnspan=2, padx=2, pady=2, sticky='NSEW')

        top_label = tk.Label(
            master=self,
            text='Material:',
            font=12)
        top_label.grid(
            row=1, column=0, padx=2, pady=2, sticky='NE')

        self._name_var = tk.StringVar(value=str(self._material.name))
        name_entry = tk.Entry(master=self,
                              textvariable=self._name_var,
                              font=12)
        name_entry.grid(row=1, column=1, padx=2, pady=2, sticky='NW')

        e_label = tk.Label(
            master=self,
            text='Young\'s Modulus:',
            font=12)
        e_label.grid(
            row=2, column=0, padx=2, pady=2, sticky='NE')

        self._young_mod = tk.StringVar(value=str(self._material.E))
        e_entry = tk.Entry(master=self,
                           textvariable=self._young_mod,
                           font=12)
        e_entry.grid(row=2, column=1, padx=2, pady=2, sticky='NW')

        button1 = tk.Button(master=self, text='Save',
                            command=lambda x='save':
                            self.action_performed(x))
        button1.grid(row=3, column=0, padx=2, pady=2, sticky='NEW')

        button2 = tk.Button(master=self, text='Cancel',
                            command=lambda x='cancel':
                            self.action_performed(x))
        button2.grid(row=3, column=1, padx=2, pady=2, sticky='NEW')

        self.__info_label = tk.Label(
            master=self,
            text='',
            font=12)
        self.__info_label.grid(
            row=4, column=0, columnspan=2, padx=2, pady=2, sticky='NEW')

    def action_performed(self, text: str) -> None:
        """Performs an action given a string.

        Args:
            text: str, string indicator of which action to perform

        Returns:
            None
        """
        if text == 'save':
            if not self.__master.is_number(self._young_mod.get()):
                self.__info_label.config(
                    text='Length must be a number!')
                return
            mat_list: MaterialList = MaterialList()
            self._material.name = self._name_var.get()
            self._material.E = float(self._young_mod.get())
            for material in mat_list:
                if material.name == self._material.name:
                    material.E = float(self._young_mod.get())
                    mat_list.save()
                    self.__master.load_loading_panel(False)
                    return
            mat_list.append(self._material)
            mat_list.save()
            self.__master.load_loading_panel(False)
            return
        elif text == 'cancel':
            self.__master.load_loading_panel(False)
