import customtkinter

from RadioToggle import RadioToggle
from wallet import Wallet
from category import Category



class CategoryElement:
    def __init__(self, master: customtkinter, parent, category: Category):
        self.master: customtkinter = master
        self.parent = parent

        self.category: Category = category
        self.value: float = 0.0


        # ---- Widget ---- #

        self.MainFrame = customtkinter.CTkFrame(master=self.master, fg_color="#43444f")
        self.MainFrame.pack(fill="x")

        self.TypeLabel = customtkinter.CTkLabel(master=self.MainFrame,
                                             text=f"[{self.category.type}]",
                                             corner_radius=0,
                                             font=(("Lato"), 15))
        self.TypeLabel.pack(fill="x", padx=10, side="left")

        self.NameLabel = customtkinter.CTkLabel(master=self.MainFrame,
                                              text=self.category.name,
                                              corner_radius=0,
                                              font=(("Lato"), 15))
        self.NameLabel.pack(fill="x", side="left", padx=10)

        self.ValueLabel = customtkinter.CTkLabel(master=self.MainFrame,
                                              text=self.value,
                                              corner_radius=0,
                                              font=(("Lato"), 15))
        self.ValueLabel.pack(fill="x", side="left", padx=10)



class CategoryList:
    def __init__(self, master: customtkinter, parent, root: customtkinter.CTk, wallet: Wallet):
        self.master = master
        self.parent = parent
        self.root = root

        self.wallet: Wallet = wallet
        self.categories: list[Category] = []
        self.cat_widgets: list[CategoryElement] = []


        # ---- Widget ---- #

        self.MainFrame = customtkinter.CTkFrame(master=self.master, fg_color="transparent")
        self.MainFrame.pack(fill="x", expand=True, side="left")

        # Top Bar
        self.TopBar = customtkinter.CTkFrame(master=self.MainFrame)
        self.TopBar.grid(sticky="we", row=0)

        # Entry Filter
        self.FilterToggle = RadioToggle(master=self.TopBar,
                                        root=self.root,
                                        parent=self.parent,
                                        values=[("All", 0), ("Expense", 1), ("Income", 2)],
                                        callables=[],
                                        row=1)

        # Entry Container
        self.Canvas = customtkinter.CTkCanvas(self.MainFrame, bg="#212024", bd=0, highlightthickness=0, height=400)
        self.Canvas.grid(sticky="news", row=2)

        self.Scrollbar = customtkinter.CTkScrollbar(self.MainFrame, orientation="vertical", command=self.Canvas.yview)

        self.Canvas.config(yscrollcommand=self.Scrollbar.set)
        self.Canvas.bind('<Configure>', lambda e: self.Canvas.configure(scrollregion=self.Canvas.bbox("all")))

        self.CategoryMaster = customtkinter.CTkFrame(master=self.Canvas, fg_color="#212024")
        self.Canvas.create_window((0, 0), window=self.CategoryMaster, anchor="nw", width=600, height=400)

        self.Scrollbar.grid(row=0, column=1, rowspan=7, sticky="NS")

        # ---- Functions ---- #

    def add_category(self, category: Category):
        self.categories.append(category)
        new_cat = CategoryElement(master=self.CategoryMaster, parent=self.parent, category=category)
        self.cat_widgets.append(new_cat)
        self.update()

    def update(self):
        self.root.update_idletasks()
        self.Canvas.configure(scrollregion=self.Canvas.bbox('all'))

    def refresh_categories(self, categories: list[Category]):
        self.clear_categories()

        for cat in categories:
            self.add_category(cat)

    def clear_categories(self):
        for child in self.cat_widgets:
            child.MainFrame.destroy()
            del child

        self.categories.clear()
        self.cat_widgets.clear()