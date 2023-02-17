import customtkinter

class SpinBox():
    def __init__(self, master: customtkinter, root: customtkinter.CTk, callables: list[callable]=None):
        """
        Args:
            msater::customtkinter
                Parent widget
            root::customtkinter.CTk
                Root window reference
            callables::list[callable]
                List of functions that will execute when self.on_selection_change is triggered
        """

        self.master: customtkinter = master
        self.root = root

        self.selection_values: list[str] = []
        self.selection_index = 0

        self.callables: list[callable] = callables or []

        # ---- Widgets ---- #

        self.MainFrame = customtkinter.CTkFrame(master=self.master, fg_color="transparent", height=100)
        self.MainFrame.pack(anchor="n")

        self.LeftButton = customtkinter.CTkButton(master=self.MainFrame,
                                                  text="<",
                                                  width=10,
                                                  font=(("Lato"), 20),
                                                  command=self.prev_selection)
        self.LeftButton.pack(expand=True, side="left")

        self.SelectionLabel = customtkinter.CTkLabel(master=self.MainFrame,
                                                     text="Selection",
                                                     font=(("Lato"), 18))
        self.SelectionLabel.pack(expand=True, side="left", padx=20)

        self.RightButton = customtkinter.CTkButton(master=self.MainFrame,
                                                   text=">",
                                                   width=10,
                                                   font=(("Lato"), 20),
                                                   command=self.next_selection)
        self.RightButton.pack(expand=True, side="left")


    # ---- Functions ---- #

    def add_widget(self, value: str):
        self.selection_values.append(value)

    def prev_selection(self):
        if self.selection_index == 0:
            return

        self.selection_index -= 1
        self.SelectionLabel.configure(text=self.selection_values[self.selection_index])

        self.on_selection_change()

    def next_selection(self):
        if self.selection_index == len(self.selection_values)-1:
            return

        self.selection_index += 1
        self.SelectionLabel.configure(text=self.selection_values[self.selection_index])

        self.on_selection_change()

    def selection_at(self, index: int):
        if index > len(self.selection_values)-1:
            return

        self.selection_index = index
        self.SelectionLabel.configure(text=self.selection_values[self.selection_index])

    def on_selection_change(self):
        for item in self.callables:
            item(self.selection_index)