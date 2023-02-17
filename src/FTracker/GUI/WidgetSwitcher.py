import customtkinter

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