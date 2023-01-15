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

        self.items = [item[0] for item in self.widgets]

        self.current_index: int = 0


    def switch_to(self, item):
        if item in self.items:
            i = self.items.index(item)
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

        if self.widgets[index][1] == "pack":
            self.items[index].pack(**self.widgets[index][2])
        else:
            self.items[index].grid(**self.widgets[index][2])

    def hide_widget(self, index: int = 0):
        if self.widgets[index][1] == "pack":
            self.items[index].pack_forget()
        else:
            self.items[index].grid_forget()

    def add_widget(self, object_ref: customtkinter, packing: str, **options):
        self.widgets.append((object_ref, packing, options))
        self.items.append(object_ref)