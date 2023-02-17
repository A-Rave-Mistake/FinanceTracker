import customtkinter
from typing import Optional

class PageButton:
    def __init__(self,
                 parent,
                 master: customtkinter.CTkFrame,
                 text: str,
                 selected: bool = False,
                 **kwargs: Optional):
        """
        Args:
            parent::Any Object
                Parent object
            master::customtkinter.CTkFrame
               Parent widget this object belongs to
            text::str
                Button text
            selected::bool (Optional)
                Whether create this button as selected (with highlight) or not
            kwargs::dict
                Additional button widget settings and parameters
        """

        self.parent = parent
        self.master = master
        self.text = text
        self.selected = customtkinter.BooleanVar()
        self.selected.set(selected)

        self.command = kwargs.get('command')


        # ---- Widget ---- #

        self.MainFrame = customtkinter.CTkFrame(master=self.master, fg_color="transparent")
        self.MainFrame.pack(side="left")

        self.PageButton = customtkinter.CTkButton(master=self.MainFrame,
                                                  text=text,
                                                  font=(("Calibri"), 22),
                                                  fg_color="transparent",
                                                  height=6,
                                                  width=4,
                                                  command=self.on_clicked)
        self.PageButton.pack()

        self.SelectLabel = customtkinter.CTkLabel(master=self.MainFrame,
                                                  fg_color=self.set_SelectLabel_color(),
                                                  text="",
                                                  font=(("Arial"), 2),
                                                  width=kwargs.get("SelectLabel_width") or 65,
                                                  height=1)
        self.SelectLabel.pack()


    def is_selected(self) -> bool:
        return self.selected.get()

    def set_SelectLabel_color(self) -> str:
        return "#1656c9" if self.is_selected() else "transparent"

    def deselect(self):
        self.selected.set(False)
        self.SelectLabel.configure(fg_color=self.set_SelectLabel_color())
        self.parent.selectedButton = None

    def set_selected(self):
        if self.parent.selectedButton != self:
            self.parent.selectedButton.deselect()
            self.selected.set(True)
            self.SelectLabel.configure(fg_color=self.set_SelectLabel_color())
            self.parent.selectedButton = self

    # Activated when
    def on_clicked(self):
        self.set_selected()
        self.command()