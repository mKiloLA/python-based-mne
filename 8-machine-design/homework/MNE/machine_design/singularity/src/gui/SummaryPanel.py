"""Class for the Menu Panels.

Zak Oster zcoster@ksu.edu
v0.1.0
"""
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Scrollbar, Treeview
from singularity.src.gui.loadings.PanelFactory import PanelFactory
from singularity.src.gui.ResultPanel import ResultPanel
from singularity.src.data.loading.Moment import Moment
from singularity.src.data.loading.Point import Point
from singularity.src.data.loading.Uniform import Uniform
from singularity.src.data.loading.Linear import Linear
from singularity.src.data.enums.BondCondType import BondCondType
from singularity.src.data.beam.Beam import Beam


class SummaryPanel(tk.Frame):
    """Class for the Order Panel.

    Attributes:
        No public attributes.
    """
    def __init__(self, master) -> None:
        """Constructor to initialize the order panel.

        Args:
            master (PrimaryWindow): the parent window that the
                menu panel fits into

        Attributes:
            master: PrimaryWindow, frame the panel fits in
            items: Dict[Loading], dictionary of loadings for
                treeview
            summary_list: Treeview, tree of loadings
            unit: StringVar, the unit system to use
            material_label: StringVar, material of the beam
            length_label: StringVar, length of the beam
            width_label: StringVar, width of the beam
            height_label: StringVar, height of the beam
            bc1_label: StringVar, first boundary condition
                for the beam
            bc2_label: StringVar, second boundary condition
                for the beam
        """
        # Construct Panel inside PrimaryWindow
        self.__master = master
        tk.Frame.__init__(self, master=self.__master)

        # Assign row and column weights
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        order_label: tk.Label = tk.Label(
            master=self, text="Loading Summary", font=10)
        order_label.grid(row=0, column=0, padx=2, pady=2, sticky='EW')

        # Declare dictionary of items
        self.__items = dict()

        # Create a new Panel inside of SummaryPanel, assign weights
        list_frame = tk.Frame(master=self)
        list_frame.grid_columnconfigure(0, weight=1)
        list_frame.grid_rowconfigure(0, weight=1)

        # Create a Treeview inside of list_frame panel
        self.__summary_list = Treeview(master=list_frame, show="tree",
                                       selectmode="browse")

        # Add a scrollbar to the Treeview, assign weights
        order_list_scrollbar = Scrollbar(master=list_frame, orient="vertical",
                                         command=self.__summary_list.yview)
        self.__summary_list.configure(yscrollcommand=order_list_scrollbar.set)
        self.__summary_list.grid(row=0, column=0, sticky="NSEW")
        order_list_scrollbar.grid(row=0, column=1, sticky="NSE")
        list_frame.grid(row=1, column=0, columnspan=2, sticky="NSEW")

        # Create a new Panel inside of SummaryPanel, assign weights
        beam_frame = tk.Frame(
            master=self,
            highlightbackground="gray",
            highlightthickness=1)
        beam_frame.grid_columnconfigure(0, weight=1)
        beam_frame.grid_columnconfigure(1, weight=1)
        beam_frame.grid_rowconfigure(0, weight=1)
        beam_frame.grid_rowconfigure(1, weight=1)
        beam_frame.grid_rowconfigure(2, weight=1)
        beam_frame.grid_rowconfigure(3, weight=1)
        beam_frame.grid_rowconfigure(4, weight=1)
        beam_frame.grid_rowconfigure(5, weight=1)
        beam_frame.grid_rowconfigure(6, weight=1)
        beam_frame.grid(row=2, column=0, columnspan=2, sticky="NSEW")

        # Indicate the units
        self._unit = tk.StringVar(value=str('S.I.'))
        self._unit.trace_add('write', self.update_labels)
        material_combo = ttk.Combobox(master=self,
                                      textvariable=self._unit,
                                      font=10,
                                      state="readonly")
        material_combo['values'] = ['S.I.', 'English (IPS)']
        material_combo.grid(row=3, column=0, padx=2, pady=2, sticky='NEW')

        # If units are SI, then use the following labels
        if self.__master.beam.material is None:
            mat_name = 'None'
        else:
            mat_name = self.__master.beam.material.name

        if self._unit.get() == 'S.I.':
            beam_title = tk.Label(
                master=beam_frame,
                text='Beam Summary',
                font=6)
            beam_title.grid(
                row=0, column=0, columnspan=2,
                padx=2, pady=2, sticky='NSEW')

            self.__material_label = tk.Label(
                master=beam_frame,
                text='Material: {}'.format(mat_name),
                font=6)
            self.__material_label.grid(
                row=1, column=0, padx=2,
                pady=2, sticky='NSW')

            self.__length_label = tk.Label(
                master=beam_frame,
                text='Length: {}m'.format(
                    self.__master.beam.length),
                font=6)
            self.__length_label.grid(
                row=2, column=0, padx=2,
                pady=2, sticky='NSW')

            self.__height_label = tk.Label(
                master=beam_frame,
                text='Height: {}m'.format(
                    self.__master.beam.height),
                font=6)
            self.__height_label.grid(
                row=3, column=0, padx=2,
                pady=2, sticky='NSW')

            self.__width_label = tk.Label(
                master=beam_frame,
                text='Width: {}m'.format(
                    self.__master.beam.base),
                font=6)
            self.__width_label.grid(
                row=4, column=0, padx=2,
                pady=2, sticky='NSW')

            bc_list = self.__master.beam.bc
            if len(bc_list) == 2:
                bc1 = self.__master.beam.bc[0].kind
                val1 = self.__master.beam.bc[0].val
                loc1 = self.__master.beam.bc[0].loc
                bc2 = self.__master.beam.bc[1].kind
                val2 = self.__master.beam.bc[1].val
                loc2 = self.__master.beam.bc[1].loc
            elif len(bc_list) == 1:
                bc1 = self.__master.beam.bc[0].kind
                val1 = self.__master.beam.bc[0].val
                loc1 = self.__master.beam.bc[0].loc
                bc2 = 'NA'
                val2 = '--'
                loc2 = '--'
            else:
                bc1 = 'NA'
                val1 = '--'
                loc1 = '--'
                bc2 = 'NA'
                val2 = '--'
                loc2 = '--'

            self.__bc1_label = tk.Label(
                master=beam_frame,
                text='BC1: {}({}m) = {}'.format(bc1, loc1, val1),
                font=6)
            self.__bc1_label.grid(
                row=5, column=0, padx=2,
                pady=2, sticky='NSW')

            self.__bc2_label = tk.Label(
                master=beam_frame,
                text='BC2: {}({}m) = {}'.format(bc2, loc2, val2),
                font=6)
            self.__bc2_label.grid(
                row=6, column=0, padx=2,
                pady=2, sticky='NSW')
        else:
            beam_title = tk.Label(
                master=beam_frame,
                text='Beam Summary',
                font=6)
            beam_title.grid(
                row=0, column=0, columnspan=2,
                padx=2, pady=2, sticky='NSEW')

            self.__material_label = tk.Label(
                master=beam_frame,
                text='Material: {}'.format(mat_name),
                font=6)
            self.__material_label.grid(
                row=1, column=0, padx=2,
                pady=2, sticky='NSW')

            self.__length_label = tk.Label(
                master=beam_frame,
                text='Length: {}ft'.format(
                    self.__master.beam.length),
                font=6)
            self.__length_label.grid(
                row=2, column=0, padx=2,
                pady=2, sticky='NSW')

            self.__height_label = tk.Label(
                master=beam_frame,
                text='Height: {}in'.format(
                    self.__master.beam.height),
                font=6)
            self.__height_label.grid(
                row=3, column=0, padx=2,
                pady=2, sticky='NSW')

            self.__width_label = tk.Label(
                master=beam_frame,
                text='Width: {}in'.format(
                    self.__master.beam.base),
                font=6)
            self.__width_label.grid(
                row=4, column=0, padx=2,
                pady=2, sticky='NSW')

            bc_list = self.__master.beam.bc
            if len(bc_list) == 2:
                bc1 = self.__master.beam.bc[0].kind
                val1 = self.__master.beam.bc[0].val
                loc1 = self.__master.beam.bc[0].loc
                bc2 = self.__master.beam.bc[1].kind
                val2 = self.__master.beam.bc[1].val
                loc2 = self.__master.beam.bc[1].loc
            elif len(bc_list) == 1:
                bc1 = self.__master.beam.bc[0].kind
                val1 = self.__master.beam.bc[0].val
                loc1 = self.__master.beam.bc[0].loc
                bc2 = 'NA'
                val2 = '--'
                loc2 = '--'
            else:
                bc1 = 'NA'
                val1 = '--'
                loc1 = '--'
                bc2 = 'NA'
                val2 = '--'
                loc2 = '--'

            self.__bc1_label = tk.Label(
                master=beam_frame,
                text='BC1: {}({}ft) = {}'.format(bc1, loc1, val1),
                font=6)
            self.__bc1_label.grid(
                row=5, column=0, padx=2,
                pady=2, sticky='NSW')

            self.__bc2_label = tk.Label(
                master=beam_frame,
                text='BC2: {}({}ft) = {}'.format(bc2, loc2, val2),
                font=6)
            self.__bc2_label.grid(
                row=6, column=0, padx=2,
                pady=2, sticky='NSW')

        # Edit button
        edit: tk.Button = tk.Button(master=self, text='Edit',
                                    command=lambda:
                                    self.action_performed('edit'))
        edit.grid(row=4, column=0, sticky='NSEW')

        # Delete Button
        delete_button = tk.Button(master=self, text="Delete",
                                  command=lambda:
                                  self.action_performed("delete"))
        delete_button.grid(row=5, column=0, sticky="NSEW")

        # Checkout button
        reset = tk.Button(master=self, text="Reset",
                          command=lambda:
                          self.action_performed("reset"))
        reset.grid(row=6, column=0, sticky="NSEW")

        # New Order button
        solve: tk.Button = tk.Button(master=self, text='Solve',
                                     command=lambda:
                                     self.action_performed('solve'))
        solve.grid(row=7, column=0, sticky='NSEW')

    def action_performed(self, text: str) -> None:
        """Performs an action given a string.

        Args:
            text: str, string indicator of which action to perform

        Returns:
            None
        """
        if text == 'edit':
            # Get the currently selected item's index number
            node = self.__summary_list.focus()
            if node:
                # Traverse the tree until the parent item is found
                while node not in self.__items:
                    node = self.__summary_list.parent(node)
                # Load this panel into menu panel slot
                item = self.__items[node]
                self.__master.load_panel(PanelFactory.get_panel(
                                         item, self.__master))
        elif text == 'delete':
            # Get the currently selected item's index number
            node = self.__summary_list.focus()
            if node:
                # Traverse the tree until the parent item is found
                while node not in self.__items:
                    node = self.__summary_list.parent(node)
                # Remove the item from the order
                self.__master.beam.remove_loading(self.__items[node])
                # Delete the item from the item dictionary
                del self.__items[node]
                # Delete the item from the Treeview
                self.__summary_list.delete(node)
        elif text == 'solve':
            if self.validate_data():
                if self._unit.get() == 'S.I.':
                    self.__master.load_panel(
                        ResultPanel(self.__master, True))
                elif self._unit.get() == 'English (IPS)':
                    self.__master.load_panel(
                        ResultPanel(self.__master, False))
        elif text == 'reset':
            self.__master.beam = Beam()
            self.update_labels()
            # Delete every value in the Treeview
            for val in self.__summary_list.get_children():
                self.__summary_list.delete(val)
            self.__master.load_loading_panel()

    def save_load(self, load) -> None:
        """Save a load to summary.

        Args:
            load: Loading, the load to save to
                summary table

        Returns:
            None
        """
        # Iterate through items dictionary with key and value
        for item_id, value in self.__items.items():
            # Check if item is in the dictionary values
            if load is value:
                # Call update tree to add to Treeview
                self.__update_tree(load, item_id)
                return
        # If the item is not in the dictionary, add item to end
        self.__items[self.__update_tree(load)] = load
        # Add the item to the order
        self.__master.beam.add_loading(load)

    def __update_tree(self, load, index='end'):
        """Update the items on the tree.

        Args:
            load: Loading, the load to update
            index: str, the index in summary_list

        Returns:
            None
        """
        # Add item to the end of the Treeview if index == "end"
        if index == "end":
            # No parent, added to Treeview
            index = self.__summary_list.insert(
                parent="", index="end", text=str(load))
        else:
            # Finds the item in Treeview by index and changes text
            self.__summary_list.item(index, text=str(load))
            # Loops through the children of the index and deletes them
            for child in self.__summary_list.get_children(index):
                self.__summary_list.delete(child)
    # Return the index of the item
        return index

    def update_labels(self, var=None, index=None, mode=None):
        """Update the beam property labels.

        Args:
            None

        Returns:
            None
        """
        if self.__master.beam.material is None:
            mat_name = 'None'
        else:
            mat_name = self.__master.beam.material.name

        if self._unit.get() == 'S.I.':
            self.__material_label.config(
                text='Material: {}'.format(mat_name))

            self.__length_label.config(
                text='Length: {}m'.format(
                    self.__master.beam.length))

            self.__height_label.config(
                text='Height: {}m'.format(
                    self.__master.beam.height))

            self.__width_label.config(
                text='Width: {}m'.format(
                    self.__master.beam.base))

            bc_list = self.__master.beam.bc
            if len(bc_list) == 2:
                bc1 = self.__master.beam.bc[0].kind
                val1 = self.__master.beam.bc[0].val
                loc1 = self.__master.beam.bc[0].loc
                bc2 = self.__master.beam.bc[1].kind
                val2 = self.__master.beam.bc[1].val
                loc2 = self.__master.beam.bc[1].loc
            elif len(bc_list) == 1:
                bc1 = self.__master.beam.bc[0].kind
                val1 = self.__master.beam.bc[0].val
                loc1 = self.__master.beam.bc[0].loc
                bc2 = 'NA'
                val2 = '--'
                loc2 = '--'
            else:
                bc1 = 'NA'
                val1 = '--'
                loc1 = '--'
                bc2 = 'NA'
                val2 = '--'
                loc2 = '--'

            self.__bc1_label.config(
                text='BC1: {}({}m) = {}'.format(bc1, loc1, val1))

            self.__bc2_label.config(
                text='BC2: {}({}m) = {}'.format(bc2, loc2, val2))
        else:
            self.__material_label.config(
                text='Material: {}'.format(mat_name))

            self.__length_label.config(
                text='Length: {}ft'.format(
                    self.__master.beam.length))

            self.__height_label.config(
                text='Height: {}in'.format(
                    self.__master.beam.height))

            self.__width_label.config(
                text='Width: {}in'.format(
                    self.__master.beam.base))

            bc_list = self.__master.beam.bc
            if len(bc_list) == 2:
                bc1 = self.__master.beam.bc[0].kind
                val1 = self.__master.beam.bc[0].val
                loc1 = self.__master.beam.bc[0].loc
                bc2 = self.__master.beam.bc[1].kind
                val2 = self.__master.beam.bc[1].val
                loc2 = self.__master.beam.bc[1].loc
            elif len(bc_list) == 1:
                bc1 = self.__master.beam.bc[0].kind
                val1 = self.__master.beam.bc[0].val
                loc1 = self.__master.beam.bc[0].loc
                bc2 = 'NA'
                val2 = '--'
                loc2 = '--'
            else:
                bc1 = 'NA'
                val1 = '--'
                loc1 = '--'
                bc2 = 'NA'
                val2 = '--'
                loc2 = '--'

            self.__bc1_label.config(
                text='BC1: {}({}ft) = {}'.format(
                    bc1, loc1, val1))

            self.__bc2_label.config(
                text='BC2: {}({}ft) = {}'.format(
                    bc2, loc2, val2))

    def validate_data(self) -> bool:
        """Ensures all loading is on the beam.

        Args:
            None

        Returns:
            value: bool, True if data is good
        """
        if self.__master.beam.material is None:
            tk.messagebox.showerror(
                'Material Error',
                'Please select a material.')
            return False
        if self.__master.beam.length <= 0:
            tk.messagebox.showerror(
                'Length Error',
                'The beam length must be greater than 0.')
            return False
        if self.__master.beam.height <= 0:
            tk.messagebox.showerror(
                'Height Error',
                'The beam height must be greater than 0.')
            return False
        if self.__master.beam.base <= 0:
            tk.messagebox.showerror(
                'Width Error',
                'The beam width/base must be greater than 0.')
            return False
        if len(self.__master.beam.bc) != 2:
            tk.messagebox.showerror(
                'Boundary Condition Error',
                'Please make sure there are two boundary conditions.')
            return False
        for bound in self.__master.beam.bc:
            if (bound.kind == BondCondType.DISTRIBUTION or
                bound.kind == BondCondType.MOMENT or
                    bound.kind == BondCondType.SHEAR):
                tk.messagebox.showerror(
                    'Boundary Condition Error',
                    'Equation must be for deflection or slope.')
                return False
        if self.__master.beam.bc[0] == self.__master.beam.bc[1]:
            tk.messagebox.showerror(
                'Boundary Condition Error',
                'Boundary conditions cannot be the same.')
            return False
        if len(self.__master.beam.loadings) <= 0:
            tk.messagebox.showerror(
                'Loading Error',
                'Please add at least one loading.')
            return False
        for load in self.__master.beam.loadings:
            if (isinstance(load, Point) or isinstance(load, Moment)):
                if load.loc > self.__master.beam.length:
                    tk.messagebox.showerror(
                        'Loading Error',
                        ('Invalid data.' +
                         'Please ensure all loads are on the beam.'))
                    return False
            elif (isinstance(load, Uniform) or isinstance(load, Linear)):
                if (load.start < 0 or
                        load.start > self.__master.beam.length or
                        load.stop < 0 or
                        load.stop > self.__master.beam.length):
                    tk.messagebox.showerror(
                        'Loading Error',
                        ('Invalid data. Please ensure loads ' +
                         'start and stop on the beam.'))
                    return False
        return True
