"""Class to display loading options.

Author: Zak Oster zcoster@ksu.edu
Version: 0.1
"""
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from singularity.src.data.enums.BondCondType import BondCondType
from singularity.src.data.enums.MaterialList import MaterialList
from singularity.src.data.beam.BoundaryCondition import BoundaryCondition
from singularity.src.gui.loadings.PanelFactory import PanelFactory
from singularity.src.gui.material.MaterialPanel import MaterialPanel


class LoadingPanel(tk.Frame):
    """Class to display loading options."""
    def __init__(self, master, set_load_tab=False) -> None:
        """Constructor to initialize the menu panel.

        Attributes:
            master: PrimaryWindow, master window
            beam: Beam, beam being edited
            loading_tabs: ttk.Notebook, tabs for GUI
            length: StringVar, length of the beam
            height: StringVar, height of the beam
            base: StringVar, width of the beam
            bc1_type: StringVar, te type of the first
                boundary condition
            val1: StringVar, value of the first bc
            loc1: StringVar, location of the first bc
            bc2_type: StringVar, the type of the second
                boundary condition
            val2: StringVar, value of the second bc
            loc2: StringVar, location of the second bc
            info_label: StringVar, instructions for user
            material_edit: StringVar, the material to change
        """
        self.__master = master
        ttk.Frame.__init__(self, master=self.__master)
        self.__beam = master.beam
        self.__loading_tabs = ttk.Notebook(master=self)
        instructions_tab = ttk.Frame(self.__loading_tabs)
        beam_tab = ttk.Frame(self.__loading_tabs)
        load_tab = ttk.Frame(self.__loading_tabs)
        material_tab = ttk.Frame(self.__loading_tabs)

        self.__loading_tabs.add(instructions_tab, text='Instructions')
        self.__loading_tabs.add(beam_tab, text='Beam Configuration')
        self.__loading_tabs.add(load_tab, text='Loadings')
        self.__loading_tabs.add(material_tab, text='Material List')
        self.__loading_tabs.pack(expand=1, fill="both")

        instructions_tab.grid_columnconfigure(0, weight=1)
        beam_tab.grid_columnconfigure(0, weight=1)
        load_tab.grid_columnconfigure(0, weight=1)

        if set_load_tab:
            self.__loading_tabs.select(load_tab)

        # ----- Create the Instructions Tab -----

        instructions_tab.grid_rowconfigure(0, weight=1)
        instructions_tab.grid_rowconfigure(1, weight=1)
        instructions_tab.grid_rowconfigure(2, weight=1)
        instructions_tab.grid_rowconfigure(3, weight=1)

        instruction_p1 = ("Welcome to the Singularity Equation Solver! "
                          "This program is capable of solving bending "
                          "beam problems with known boundary conditions "
                          "and reaction forces. Simple problems like the one "
                          "shown below are perfect for this application.\n")
        text1 = tk.Label(
            master=instructions_tab,
            text=instruction_p1,
            font=8,
            wraplength=1000,
            justify='left')
        text1.grid(row=0, column=0, padx=2, pady=2, sticky='NW')

        image1 = Image.open('singularity/src/static/sample-problem.png')
        width, height = image1.size
        image1 = image1.resize(
            (width//3, height//3),
            Image.LANCZOS)
        sample_problem_image = ImageTk.PhotoImage(image1)
        sample_problem = tk.Label(
            master=instructions_tab,
            image=sample_problem_image)
        sample_problem.image = sample_problem_image
        sample_problem.grid(row=1, column=0, padx=2, pady=2, sticky='NSEW')

        instruction_p2 = ("\nBegin by going to the 'Beam Configuration' tab "
                          "and inputting the parameters of the beam and "
                          "boundary conditions. Hit 'Save' and proceed to "
                          "the Loadings section. Select the type of loading "
                          "and insert that necessary values. Hit 'Save' to "
                          "add the loading to the beam. Once you have added "
                          "all the forces, select the 'Solve' button on the "
                          "'Summary' side bar. The program will "
                          "solve for the shear, moment, slope, and "
                          "deflection equations. These will be returned "
                          "as equations and as a graph. a sample output "
                          "is shown below.\n")
        text2 = tk.Label(
            master=instructions_tab,
            text=instruction_p2,
            font=8,
            wraplength=1000,
            justify='left')
        text2.grid(row=2, column=0, padx=2, pady=2, sticky='NW')

        image2 = Image.open('singularity/src/static/sample-output.png')
        width, height = image2.size
        image2 = image2.resize(
            (width//2, height//2),
            Image.LANCZOS)
        sample_output_image = ImageTk.PhotoImage(image2)
        sample_output = tk.Label(
            master=instructions_tab, image=sample_output_image)
        sample_output.image = sample_output_image
        sample_output.grid(row=3, column=0, padx=2, pady=2, sticky='NSEW')

        instruction_p3 = ("The program shows units using the SI "
                          "standard. You can change the untis to "
                          "English units with the drop down under "
                          "the summary table. This does not change "
                          "the labels in the program but will change "
                          "the results.")
        text3 = tk.Label(
            master=instructions_tab,
            text=instruction_p3,
            font=8,
            wraplength=1000,
            justify='left')
        text3.grid(row=4, column=0, padx=2, pady=2, sticky='NW')

        # ----- Create the Beam Tab -----

        beam_tab.grid_rowconfigure(0, weight=1)
        beam_tab.grid_rowconfigure(1, weight=1)
        beam_tab.grid_columnconfigure(0, weight=1)
        beam_tab.grid_columnconfigure(1, weight=1)

        top_panel = tk.Frame(
            master=beam_tab,
            highlightbackground="gray",
            highlightthickness=1)
        top_panel.grid(
            row=0, column=0, columnspan=2, padx=2, pady=2, sticky="NSEW")
        top_panel.grid_columnconfigure(0, weight=1)
        top_panel.grid_columnconfigure(1, weight=1)
        top_panel.grid_rowconfigure(0, weight=1)
        top_panel.grid_rowconfigure(1, weight=1)
        top_panel.grid_rowconfigure(2, weight=1)
        top_panel.grid_rowconfigure(3, weight=1)

        top_label = tk.Label(
            master=top_panel,
            text='Beam Parameters',
            font=12)
        top_label.grid(
            row=0, column=0, columnspan=2, padx=2, pady=2, sticky='NSEW')

        mat_text = tk.Label(
            master=top_panel,
            text='Beam Material:',
            font=10)
        mat_text.grid(row=1, column=0, padx=2, pady=2, sticky='NE')

        mat_list = MaterialList()
        if self.__beam.material is None:
            material = '-- Select a material --'
        else:
            material = self.__beam.material.name
        self._material = tk.StringVar(value=str(material))
        material_combo = ttk.Combobox(master=top_panel,
                                      textvariable=self._material,
                                      font=10,
                                      state="readonly")
        material_combo['values'] = [str(x.name) for x in mat_list]
        material_combo.grid(row=1, column=1, padx=2, pady=2, sticky='NW')

        length_text = tk.Label(
            master=top_panel,
            text='Beam Length (m or ft):',
            font=10)
        length_text.grid(row=2, column=0, padx=2, pady=2, sticky='NE')

        self._length = tk.StringVar(value=str(self.__beam.length))
        length_entry = tk.Entry(master=top_panel,
                                textvariable=self._length,
                                font=10)
        length_entry.grid(row=2, column=1, padx=2, pady=2, sticky='NW')

        height_text = tk.Label(
            master=top_panel,
            text='Beam Height (m or in):',
            font=10)
        height_text.grid(row=3, column=0, padx=2, pady=2, sticky='NE')

        self._height = tk.StringVar(value=str(self.__beam.height))
        height_entry = tk.Entry(master=top_panel,
                                textvariable=self._height,
                                font=10)
        height_entry.grid(row=3, column=1, padx=2, pady=2, sticky='NW')

        base_text = tk.Label(
            master=top_panel,
            text='Beam Width (m or in):',
            font=10)
        base_text.grid(row=4, column=0, padx=2, pady=2, sticky='NE')

        self._base = tk.StringVar(value=str(self.__beam.base))
        base_entry = tk.Entry(master=top_panel,
                              textvariable=self._base,
                              font=10)
        base_entry.grid(row=4, column=1, padx=2, pady=2, sticky='NW')

        bot_panel = tk.Frame(
            master=beam_tab,
            highlightbackground="gray",
            highlightthickness=1)
        bot_panel.grid(
            row=1, column=0, columnspan=2, padx=2, pady=2, sticky="NSEW")
        bot_panel.grid_columnconfigure(0, weight=1)
        bot_panel.grid_columnconfigure(1, weight=1)
        bot_panel.grid_columnconfigure(2, weight=1)
        bot_panel.grid_columnconfigure(3, weight=1)
        bot_panel.grid_rowconfigure(0, weight=1)
        bot_panel.grid_rowconfigure(1, weight=1)
        bot_panel.grid_rowconfigure(2, weight=1)
        bot_panel.grid_rowconfigure(3, weight=1)
        bot_panel.grid_rowconfigure(4, weight=1)

        bot_label_text = tk.Label(
            master=bot_panel,
            text='Boundary Conditions',
            font=10)
        bot_label_text.grid(
            row=0, column=0, columnspan=4, padx=2, pady=2, sticky='NSEW')

        bc1_label = tk.Label(
            master=bot_panel,
            text='Boundary Condition #1',
            font=8)
        bc1_label.grid(
            row=1, column=0, columnspan=2, padx=2, pady=2, sticky='NSEW')

        eq1_label = tk.Label(
            master=bot_panel,
            text='Equation:',
            font=8)
        eq1_label.grid(
            row=2, column=0, padx=2, pady=2, sticky='NE')

        bc_list = self.__beam.bc
        if len(bc_list) == 2:
            bc1 = self.__beam.bc[0].kind
            val1 = self.__beam.bc[0].val
            loc1 = self.__beam.bc[0].loc
            bc2 = self.__beam.bc[1].kind
            val2 = self.__beam.bc[1].val
            loc2 = self.__beam.bc[1].loc
        elif len(bc_list) == 1:
            bc1 = self.__beam.bc[0].kind
            val1 = self.__beam.bc[0].val
            loc1 = self.__beam.bc[0].loc
            bc2 = '-- Select an equation --'
            val2 = 0
            loc2 = 0
        else:
            bc1 = '-- Select an equation --'
            val1 = 0
            loc1 = 0
            bc2 = '-- Select an equation --'
            val2 = 0
            loc2 = 0
        self._bc1_type = tk.StringVar(value=str(bc1))
        bc1_combo = ttk.Combobox(master=bot_panel,
                                 textvariable=self._bc1_type,
                                 font=10,
                                 state="readonly")
        bc1_combo['values'] = [str(x.value) for x in BondCondType]
        bc1_combo.grid(row=2, column=1, padx=2, pady=2, sticky='NW')

        val1_label = tk.Label(
            master=bot_panel,
            text='Value:',
            font=8)
        val1_label.grid(row=3, column=0, padx=2, pady=2, sticky='NE')

        self._val1 = tk.StringVar(value=str(val1))
        val1_entry = tk.Entry(master=bot_panel,
                              textvariable=self._val1,
                              font=10)
        val1_entry.grid(row=3, column=1, padx=2, pady=2, sticky='NW')

        loc1_label = tk.Label(
            master=bot_panel,
            text='Location (m or ft):',
            font=8)
        loc1_label.grid(row=4, column=0, padx=2, pady=2, sticky='NE')

        self._loc1 = tk.StringVar(value=str(loc1))
        loc1_entry = tk.Entry(master=bot_panel,
                              textvariable=self._loc1,
                              font=10)
        loc1_entry.grid(row=4, column=1, padx=2, pady=2, sticky='NW')

        bc2_label = tk.Label(
            master=bot_panel,
            text='Boundary Condition #2',
            font=8)
        bc2_label.grid(
            row=1, column=2, columnspan=2, padx=2, pady=2, sticky='NSEW')

        eq2_label = tk.Label(
            master=bot_panel,
            text='Equation:',
            font=8)
        eq2_label.grid(row=2, column=2, padx=2, pady=2, sticky='NE')

        self._bc2_type = tk.StringVar(value=str(bc2))
        bc2_combo = ttk.Combobox(master=bot_panel,
                                 textvariable=self._bc2_type,
                                 font=10,
                                 state="readonly")
        bc2_combo['values'] = [str(x.value) for x in BondCondType]
        bc2_combo.grid(row=2, column=3, padx=2, pady=2, sticky='NW')

        val2_label = tk.Label(
            master=bot_panel,
            text='Value:',
            font=8)
        val2_label.grid(row=3, column=2, padx=2, pady=2, sticky='NE')

        self._val2 = tk.StringVar(value=str(val2))
        val2_entry = tk.Entry(master=bot_panel,
                              textvariable=self._val2,
                              font=10)
        val2_entry.grid(row=3, column=3, padx=2, pady=2, sticky='NW')

        loc2_label = tk.Label(
            master=bot_panel,
            text='Location (m or ft):',
            font=8)
        loc2_label.grid(row=4, column=2, padx=2, pady=2, sticky='NE')

        self._loc2 = tk.StringVar(value=str(loc2))
        loc2_entry = tk.Entry(master=bot_panel,
                              textvariable=self._loc2,
                              font=10)
        loc2_entry.grid(row=4, column=3, padx=2, pady=2, sticky='NW')

        save = tk.Button(
            master=beam_tab, text='Save',
            command=lambda: self.action_performed('save'))
        save.grid(row=2, column=0, sticky='NEW')

        self.__info_label = tk.Label(
            master=beam_tab,
            text='Remember to save!',
            font=8)
        self.__info_label.grid(row=2, column=1, padx=2, pady=2, sticky='NEW')

        # ----- Create Loading Tab -----

        load_tab.grid_rowconfigure(0, weight=1)
        load_tab.grid_rowconfigure(1, weight=1)
        load_tab.grid_rowconfigure(2, weight=1)
        load_tab.grid_rowconfigure(3, weight=1)
        button1 = tk.Button(master=load_tab, text='Moment', font=10,
                            command=lambda x='moment':
                            self.action_performed(x))
        button1.grid(row=0, column=0, padx=2, pady=2, sticky='NSEW')
        button2 = tk.Button(master=load_tab, text='Point',  font=10,
                            command=lambda x='point':
                            self.action_performed(x))
        button2.grid(row=1, column=0, padx=2, pady=2, sticky='NSEW')
        button3 = tk.Button(master=load_tab, text='Uniform', font=10,
                            command=lambda x='uniform':
                            self.action_performed(x))
        button3.grid(row=2, column=0, padx=2, pady=2, sticky='NSEW')
        button4 = tk.Button(master=load_tab, text='Linear', font=10,
                            command=lambda x='linear':
                            self.action_performed(x))
        button4.grid(row=3, column=0, padx=2, pady=2, sticky='NSEW')

        # ----- Create Material Tab -----
        material_tab.grid_columnconfigure(0, weight=1)
        material_tab.grid_columnconfigure(1, weight=1)
        material_tab.grid_columnconfigure(2, weight=1)
        material_tab.grid_rowconfigure(0, weight=1)
        material_tab.grid_rowconfigure(1, weight=1)
        material_tab.grid_rowconfigure(2, weight=1)

        top_label = tk.Label(
            master=material_tab,
            text='Material List',
            font=15)
        top_label.grid(
            row=0, column=1, padx=2, pady=2, sticky='NSEW')

        self._material_edit = tk.StringVar(value='-- Select a material --')
        material_combo_edit = ttk.Combobox(
            master=material_tab,
            textvariable=self._material_edit,
            font=10,
            state="readonly")
        material_combo_edit['values'] = [str(x.name) for x in mat_list]
        material_combo_edit.grid(row=1, column=1, padx=2, pady=2, sticky='NEW')

        button5 = tk.Button(master=material_tab, text='New', font=10,
                            command=lambda x='new':
                            self.action_performed(x))
        button5.grid(row=2, column=0, padx=2, pady=2, sticky='NEW')
        button6 = tk.Button(
            master=material_tab, text='Edit', font=10,
            command=lambda x='material_edit':
            self.action_performed(x))
        button6.grid(row=2, column=1, padx=2, pady=2, sticky='NEW')
        button7 = tk.Button(
            master=material_tab, text='Delete', font=10,
            command=lambda x='material_delete':
            self.action_performed(x))
        button7.grid(row=2, column=2, padx=2, pady=2, sticky='NEW')

    def action_performed(self, text: str) -> None:
        """Performs an action given a string.

        Args:
            text: str, string indicator of which action to perform

        Returns:
            None
        """
        if text == 'save':
            self.save_beam()
        elif text == 'new':
            self.__master.load_panel(
                MaterialPanel(self.__master))
        elif text == 'material_edit':
            self.__master.load_panel(
                MaterialPanel(
                    self.__master,
                    self._material_edit.get()))
        elif text == 'material_delete':
            for i, material in enumerate(MaterialList()):
                if material.name == self._material_edit.get():
                    del MaterialList()[i]
                self.__master.load_loading_panel(False)
        else:
            self.__master.load_panel(
                PanelFactory.get_panel(text, self.__master))

    def save_beam(self) -> None:
        """Validates and saves beam data.

        Args:
            None

        Returns:
            None
        """
        # Check material
        if self._material.get() == '-- Select a material --':
            self.__info_label.config(text='Please select a material!')
            return
        self.__beam.material = MaterialList().get(self._material.get())

        # Check length
        if self.__master.is_number(self._length.get()):
            if float(self._length.get()) <= 0:
                self.__info_label.config(
                    text='Length must be greater than 0!')
                return
            self.__beam.length = float(self._length.get())
        else:
            self.__info_label.config(
                    text='Length must be a number!')
            return

        # Check Height
        if self.__master.is_number(self._height.get()):
            if float(self._height.get()) <= 0:
                self.__info_label.config(
                    text='Height must be greater than 0!')
                return
            self.__beam.height = float(self._height.get())
        else:
            self.__info_label.config(
                    text='Height must be a number!')
            return

        # Check Base
        if self.__master.is_number(self._base.get()):
            if float(self._base.get()) <= 0:
                self.__info_label.config(
                    text='Width must be greater than 0!')
                return
            self.__beam.base = float(self._base.get())
        else:
            self.__info_label.config(
                    text='Width must be a number!')
            return

        # Check bc1 equation
        if self._bc1_type.get() == '-- Select an equation --':
            self.__info_label.config(
                text='Please select the first equation type!')
            return

        # Check bc1 value
        if not self.__master.is_number(self._val1.get()):
            self.__info_label.config(
                    text='BC1 value must be a number!')
            return

        # Check bc1 location
        if self.__master.is_number(self._loc1.get()):
            if float(self._loc1.get()) < 0:
                self.__info_label.config(
                    text='BC1 location must be greater than 0!')
                return
            if float(self._loc1.get()) > self.__beam.length:
                self.__info_label.config(
                    text='BC1 location must be less than length!')
                return
        else:
            self.__info_label.config(
                    text='BC1 location must be a number!')

        # Check bc2 equation
        if self._bc2_type.get() == '-- Select an equation --':
            self.__info_label.config(
                text='Please select the second equation type!')
            return

        # Check bc2 value
        if not self.__master.is_number(self._val2.get()):
            self.__info_label.config(
                    text='BC2 value must be a number!')
            return

        # Check bc1 location
        if self.__master.is_number(self._loc2.get()):
            if float(self._loc2.get()) < 0:
                self.__info_label.config(
                    text='BC2 location must be non-negative!')
                return
            if float(self._loc2.get()) > self.__beam.length:
                self.__info_label.config(
                    text='BC2 location must be non-negative!')
                return
        else:
            self.__info_label.config(
                    text='BC2 location must be a number!')

        self.__beam.clear_bc()
        self.__beam.add_bc(
            BoundaryCondition(
                BondCondType(self._bc1_type.get()),
                float(self._val1.get()),
                float(self._loc1.get())
            )
        )

        self.__beam.add_bc(
            BoundaryCondition(
                BondCondType(self._bc2_type.get()),
                float(self._val2.get()),
                float(self._loc2.get())
            )
        )

        self.__info_label.config(
                    text='Saved!')
        self.__master.beam = self.__beam
        self.__master.update_labels()
