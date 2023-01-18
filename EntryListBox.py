import customtkinter
from tkinter import *

from entry import TrackerEntry
from SortButton import SortButton
from RadioToggle import RadioToggle


class EntryListElement:
    def __init__(self, master: customtkinter, parent, entry: TrackerEntry):
        self.master: customtkinter = master
        self.parent = parent
        self.entry = entry


        # ---- Widget ---- #

        self.MainFrame = customtkinter.CTkFrame(master=self.master, fg_color="#43444f")
        self.MainFrame.pack(expand=True, fill="x", anchor="n")

        self.WalletLabel = customtkinter.CTkLabel(master=self.MainFrame,
                                                text=self.entry.wallet,
                                                corner_radius=0,
                                                font=(("Lato"), 15))
        self.WalletLabel.pack(expand=True, fill="x", side="left")

        self.NameLabel = customtkinter.CTkLabel(master=self.MainFrame,
                                              text=self.entry.name,
                                              corner_radius=0,
                                              font=(("Lato"), 15))
        self.NameLabel.pack(expand=True, fill="x", side="left")

        self.TypeLabel = customtkinter.CTkLabel(master=self.MainFrame,
                                             text=self.entry.type,
                                             corner_radius=0,
                                             font=(("Lato"), 15))
        self.TypeLabel.pack(expand=True, fill="x", side="left")

        self.ValueLabel = customtkinter.CTkLabel(master=self.MainFrame,
                                               text=f"{self.entry.value} {self.entry.currency}",
                                               corner_radius=0,
                                               font=(("Lato"), 15))
        self.ValueLabel.pack(expand=True, fill="x", side="left")

        self.CategoryLabel = customtkinter.CTkLabel(master=self.MainFrame,
                                             text=self.entry.category,
                                             corner_radius=0,
                                             font=(("Lato"), 15))
        self.CategoryLabel.pack(expand=True, fill="x", side="left")

        self.DateLabel = customtkinter.CTkLabel(master=self.MainFrame,
                                                    text=f"{self.entry.date.tm_mday}.{self.entry.date.tm_mon}.{self.entry.date.tm_year}",
                                                    corner_radius=0,
                                                    font=(("Lato"), 15))
        self.DateLabel.pack(expand=True, fill="x", side="left")


class EntryListBox:
    def __init__(self, master: customtkinter, parent, root: customtkinter.CTk, row: int = 0, column: int = 0):
        '''
        Args:
             master::customtkinter
                Parent widget element
            parent::Any Object
                The parent object this list belongs to
            row::int & column::int
                Position of widget component in parent widget
        '''

        self.master: customtkinter = master
        self.parent = parent
        self.root: customtkinter.CTk = root
        self.row: int = row
        self.column: int = column

        self.current_button: SortButton = None

        self.current_wallet = None

        self.entries: list[EntryListElement] = []


        # ---- Widget ---- #

        self.MainFrame = customtkinter.CTkFrame(master=self.master, fg_color="transparent", height=750)
        self.MainFrame.pack(fill="both", expand=True)
        self.MainFrame.columnconfigure(0, weight=2)
        self.MainFrame.rowconfigure(0, weight=2)

        # Top Bar
        self.TopBar1 = customtkinter.CTkFrame(master=self.MainFrame)
        self.TopBar1.grid(sticky="we", row=0)

        self.TopLabel = customtkinter.CTkLabel(master=self.TopBar1,
                                               text="Recent Entries",
                                               font=(("Lato"), 20, "bold"),
                                               padx=5)
        self.TopLabel.grid(row=0, sticky="w")

        # Entry Filter
        self.FilterToggle = RadioToggle(master=self.TopBar1,
                                        root=self.parent.root,
                                        parent=self.parent,
                                        values=[("All", 0), ("Expense", 1), ("Income", 2)],
                                        callables=[self.filter_entries],
                                        row=1)

        # Top Sort Bar
        self.TopBar = customtkinter.CTkFrame(master=self.MainFrame, fg_color="transparent")
        self.TopBar.grid(sticky="we", row=1)

            # Sorting Buttons
        self.WalletButton = SortButton(master=self.TopBar, parent=self, text="Wallet", sortby="wallet", column=0)
        self.NameButton = SortButton(master=self.TopBar, parent=self, text="Name", sortby="name", column=1)
        self.TypeButton = SortButton(master=self.TopBar, parent=self, text="Type", sortby="type", column=2)
        self.ValueButton = SortButton(master=self.TopBar, parent=self, text="Value", sortby="value", column=3)
        self.CategoryButton = SortButton(master=self.TopBar, parent=self, text="Category", sortby="category", column=4)
        self.DateButton = SortButton(master=self.TopBar, parent=self, text="Date", sortby="date", column=5)

        # Entry Container
        self.Canvas = customtkinter.CTkCanvas(self.MainFrame, bg="#212024", bd=0, highlightthickness=0, height=700)
        self.Canvas.grid(sticky="news", row=2)

        self.Scrollbar = customtkinter.CTkScrollbar(self.MainFrame, orientation="vertical", command=self.Canvas.yview)

        self.Canvas.config(yscrollcommand=self.Scrollbar.set)
        self.Canvas.bind('<Configure>', lambda e: self.Canvas.configure(scrollregion=self.Canvas.bbox("all")))

        self.EntryList = Frame(self.Canvas, bg="#212024", bd=0)
        self.Canvas.create_window((0, 0), window=self.EntryList, anchor="nw", width=1900)

        self.Scrollbar.grid(row=0, column=1, rowspan=7, sticky="NS")


    # ---- Functions ---- #

    def add_entry(self, entry: TrackerEntry):
        self.entries.append(EntryListElement(master=self.EntryList, parent=self, entry=entry))
        self.update()

    def update(self):
        self.root.update_idletasks()
        self.Canvas.configure(scrollregion=self.Canvas.bbox('all'))

    def load_entries(self, entries: list[TrackerEntry], **kwargs):
        self.clear_entries()

        type_filter = kwargs.get('filter')
        sort = kwargs.get('sort')

        if type_filter != "All":
            #entries = [entry for entry in entries if entry.type == filter]
            a = self.entry_type_matches(type_filter)
            entries = list(filter(a, entries))

        if sort:
            entries.sort()

        for entry in entries:
            self.add_entry(entry)
        self.update()

    def clear_entries(self):
        for child in self.entries:
            child.MainFrame.destroy()
            del child
        self.entries.clear()
        self.update()

    def filter_entries(self, value: int):
        self.clear_entries()
        FILTERS = {0:"All", 1:"Expense", 2:"Income"}
        self.load_entries(self.current_wallet.entries.get_all_entries(), filter=FILTERS[value])

    def entry_type_matches(self, type: str):
        def match(entry: TrackerEntry):
            return entry.type == type
        return match

    def sort_entries(self, sorting: tuple):
        self.clear_entries()
        self.load_entries(self.current_wallet.entries.get_all_entries, sort=sorting)