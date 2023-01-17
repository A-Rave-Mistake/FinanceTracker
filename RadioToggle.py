import customtkinter

class RadioToggle:
    def __init__(self, master:customtkinter, root:customtkinter.CTk, parent, values: list[(str, int)], **kwargs):
        """
        Args:
            master::customtkinter
                Parent widget this widget belongs to
            root:customtkinter.CTk
                Root window of the parent
            parent:MainWindow
                MainWindow reference
        """

        self.master = master
        self.root = root
        self.parent = parent

        self.radio_buttons: list[customtkinter.CTkRadioButton] = []
        self.selection = customtkinter.IntVar(self.root)
        self.selection.set(0)


        # ---- Widget ---- #

        self.MainFrame = customtkinter.CTkFrame(master=self.master, fg_color=kwargs.get('fg_color') or "transparent")
        self.MainFrame.grid(padx=10, pady=5)

        for index, item in enumerate(values):
            new_radio_button = customtkinter.CTkRadioButton(master=self.MainFrame,
                                                            text=item[0],
                                                            variable=self.selection,
                                                            value=item[1])
            new_radio_button.grid(row=kwargs.get('row') or 0, column=index)
            self.radio_buttons.append(new_radio_button)

    def get_selection(self) -> int:
        return self.selection.get()