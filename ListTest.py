import customtkinter
from tkinter import *

from entry import TrackerEntry
from SortButton import SortButton


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

        self.MainFrame = customtkinter.CTkFrame(master=self.master, fg_color="transparent", height=800)
        self.MainFrame.grid(sticky="news", columnspan=10, rowspan=10)
        self.MainFrame.columnconfigure(0, weight=2)
        self.MainFrame.rowconfigure(0, weight=2)

        self.TopBar1 = customtkinter.CTkFrame(master=self.MainFrame)
        self.TopBar1.grid(sticky="we", row=0)

        self.TopLabel = customtkinter.CTkLabel(master=self.TopBar1,
                                               text="Recent Entries",
                                               font=(("Lato"), 20, "bold"),
                                               padx=5)
        self.TopLabel.grid(sticky="w", row=0)

        self.TopBar = customtkinter.CTkFrame(master=self.MainFrame, fg_color="transparent")
        self.TopBar.grid(sticky="we", row=1)

        self.WalletButton = SortButton(master=self.TopBar, parent=self, text="Wallet", column=0)
        self.NameButton = SortButton(master=self.TopBar, parent=self, text="Name", column=1)
        self.TypeButton = SortButton(master=self.TopBar, parent=self, text="Type", column=2)
        self.ValueButton = SortButton(master=self.TopBar, parent=self, text="Value", column=3)
        self.CategoryButton = SortButton(master=self.TopBar, parent=self, text="Category", column=4)
        self.DateButton = SortButton(master=self.TopBar, parent=self, text="Date", column=5)

        self.Canvas = customtkinter.CTkCanvas(self.MainFrame, bg="#212024", bd=0, highlightthickness=0, height=750)
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