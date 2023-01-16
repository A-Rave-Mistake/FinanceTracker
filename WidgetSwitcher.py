import customtkinter
from typing import NamedTuple

class WidgetSwitcher:
    def __init__(self, root: customtkinter.CTk, widgets: list):
        """
        Args:
            root::customtkinter.CTk
                Root of the MainWindow
            widgets::list[(object, str, **kwargs)]
                List of (object, str, **) tuple
                Object is a customtkinter.CtkFrame refenrece
                String is a packing method - either "pack" or "grid"
                **kwargs is a list of arguments / parameters for the packing method
        """
        self.root: customtkinter.CTk = root
        self.widgets: list = widgets

        self.current_index: int = 0


    def switch_to(self, item):
        items = [x['object'] for x in self.widgets]
        if item in items:
            i = items.index(item)
            self.hide_widget(self.current_index)
            self.show_widget(i)
        else:
            print("Widget not found")

    def switch_to_index(self, index: int):
        if index < len(self.widgets):
            self.hide_widget(self.current_index)
            self.show_widget(index)

    def next_widget(self):
        if self.current_index < len(self.widgets):
            self.current_index += 1
        else:
            self.current_index = 0
        return self.widgets[self.current_index]

    def show_widget(self, index: int):
        self.current_index = index

        if self.widgets[index]['packing'] == "pack":
            self.widgets[index]['object'].pack(**self.widgets[index]['options'])
        else:
            self.widgets[index]['object'].grid(**self.widgets[index]['options'])

    def hide_widget(self, index: int = 0):
        if self.widgets[index]['packing'] == "pack":
            self.widgets[index]['object'].pack_forget()
        else:
            self.widgets[index]['object'].grid_forget()

    def add_widget(self, object_ref: customtkinter, packing: str, **options):
        self.widgets.append({"object": object_ref, "packing": packing, "options": options})
        
        
class SwitcherSpinBox(WidgetSwitcher):
    def __init__(self, master: customtkinter, root: customtkinter.CTk, widgets: list):
        super().__init__(root, widgets)

        self.master: customtkinter = master

        self.selection_values: list[str] = []


        # ---- Widgets ---- #

        self.MainFrame = customtkinter.CTkFrame(master=self.master, fg_color="transparent", height=100)
        self.MainFrame.pack(anchor="n")

        self.LeftButton = customtkinter.CTkButton(master=self.MainFrame, text="<", width=10, font=(("Lato"), 20))
        self.LeftButton.pack(expand=True,side="left")

        self.SelectionLabel = customtkinter.CTkLabel(master=self.MainFrame, text="Selection", font=(("Lato"), 18))
        self.SelectionLabel.pack(expand=True,side="left", padx=20)

        self.RightButton = customtkinter.CTkButton(master=self.MainFrame, text=">", width=10, font=(("Lato"), 20))
        self.RightButton.pack(expand=True,side="left")
        
        
    def add_widget(self, object_ref: customtkinter, packing: str, **options):
        super(SwitcherSpinBox, self).add_widget(object_ref, packing)
        self.selection_values.append(options.get('selection'))