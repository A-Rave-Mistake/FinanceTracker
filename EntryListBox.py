import customtkinter

from entry import TrackerEntry
from SortButton import SortButton

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

        self.entries: list[TrackerEntry] = []


        # ---- Widget ---- #

        self.MainFrame = customtkinter.CTkFrame(master=self.master)
        self.MainFrame.pack(expand=True, fill="x", side="left")


        self.TopBar = customtkinter.CTkFrame(master=self.MainFrame, fg_color="transparent")
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


    # ---- Functions ---- #

    def add_entry(self, entry: TrackerEntry):
        self.entries.append(entry)