import customtkinter

class SortButton:
    def __init__(self, master: customtkinter, parent, text: str, **kwargs):
        '''
        Args:
             master::customtkinter
                Parent widget element
            parent::Any Object
                The parent object this widget
            text::str
                Text displayed by button
            kwargs::dict
                Additional widget attributes
        '''

        self.master:customtkinter = master
        self.parent = parent
        self.text: str = text

        self.sort_type: str = "none"

        self.MainFrame = customtkinter.CTkFrame(master=self.master, fg_color="transparent")
        self.MainFrame.pack(side="left", expand=True, fill="x", padx=2)

        self.Button = customtkinter.CTkButton(master=self.MainFrame,
                                                  text=self.text,
                                                  corner_radius=0,
                                                  font=(("Lato"), 15),
                                                  command=self.change_sort)
        self.Button.pack(side="left", expand=True, fill="x")

        self.change_button_direction()


    # ---- Functions ---- #

    def reset_focus(self):
        if self.parent.current_button:
            self.parent.current_button.reset_sort()
        self.parent.current_button = self

    def change_sort(self):
        self.reset_focus()

        if self.sort_type == "none":
            self.sort_type = "descending"
        elif self.sort_type == "descending":
            self.sort_type = "ascending"
        else:
            self.sort_type = "none"

        self.change_button_direction()

    def reset_sort(self):
        self.sort_type = "none"
        self.change_button_direction()

    def change_button_direction(self):
        if self.sort_type == "descending":
            self.Button.configure(text=f"{self.text} ^")
        elif self.sort_type == "ascending":
            self.Button.configure(text=f"{self.text} v")
        else:
            self.Button.configure(text=f"{self.text}")