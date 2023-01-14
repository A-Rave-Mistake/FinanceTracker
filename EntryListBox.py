import customtkinter

from entry import TrackerEntry
from SortButton import SortButton


class EntryListElement:
    def __init__(self, master: customtkinter, parent, entry: TrackerEntry):
        self.master: customtkinter = master
        self.parent = parent
        self.entry = entry


        # ---- Widget ---- #

        self.MainFrame = customtkinter.CTkFrame(master=self.master, fg_color="#43444f")
        self.MainFrame.pack(expand=True, fill="x", anchor="n", padx=2, pady=2)

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
                                               text=str(self.entry.value),
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

        self.entries: list[EntryListElement] = []


        # ---- Widget ---- #

        self.MainFrame = customtkinter.CTkFrame(master=self.master)
        self.MainFrame.pack(expand=True, fill="x", side="left", anchor="n")

        self.TopBar = customtkinter.CTkFrame(master=self.MainFrame)
        self.TopBar.pack(expand=True, fill="x")

        self.TopLabel = customtkinter.CTkLabel(master=self.TopBar,
                                               text="Recent Entries",
                                               font=(("Lato"), 20, "bold"))
        self.TopLabel.pack(anchor="w", pady=5, padx=5)

        self.WalletButton = SortButton(master=self.TopBar, parent=self, text="Wallet")
        self.NameButton = SortButton(master=self.TopBar, parent=self, text="Name")
        self.TypeButton = SortButton(master=self.TopBar, parent=self, text="Type")
        self.ValueButton = SortButton(master=self.TopBar, parent=self, text="Value")
        self.CategoryButton = SortButton(master=self.TopBar, parent=self, text="Category")
        self.DateButton = SortButton(master=self.TopBar, parent=self, text="Date")

        self.EntryList = customtkinter.CTkFrame(master=self.MainFrame)
        self.EntryList.pack(expand=True, fill="x", anchor="n")


    # ---- Functions ---- #

    def add_entry(self, entry: TrackerEntry):
        self.entries.append(EntryListElement(master=self.EntryList, parent=self, entry=entry))