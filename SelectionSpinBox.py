import customtkinter

class SpinBox():
    def __init__(self, master: customtkinter, root: customtkinter.CTk):

        self.master: customtkinter = master
        self.root = root

        self.selection_values: list[str] = []
        self.selection_index = 0

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

    def add_widget(self, value: str):
        self.selection_values.append(value)

    def prev_selection(self):
        if self.selection_index == 0:
            return

        self.selection_index -= 1
        self.SelectionLabel.configure(text=self.selection_values[self.selection_index])

    def next_selection(self):
        if self.selection_index == len(self.selection_values)-1:
            return

        self.selection_index += 1
        self.SelectionLabel.configure(text=self.selection_values[self.selection_index])

    def selection_at(self, index: int):
        if index > len(self.selection_values)-1:
            return

        self.selection_index = index
        self.SelectionLabel.configure(text=self.selection_values[self.selection_index])