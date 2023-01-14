import customtkinter

class SortButton:
    def __init__(self, master: customtkinter, parent, text: str, **kwargs):

        self.master:customtkinter = master
        self.parent = parent

        self.MainFrame = customtkinter.CTkFrame(master=self.master, fg_color="transparent")
        self.MainFrame.pack(side="left", expand=True, fill="x", padx=2)

        self.DateButton = customtkinter.CTkButton(master=self.MainFrame,
                                                  text=text,
                                                  corner_radius=0,
                                                  font=(("Lato"), 15))
        self.DateButton.pack(side="left", expand=True, fill="x")