import customtkinter

import FT_Time

from WalletContainer import WalletContainer
from wallet import Wallet
from EntryListBox import EntryListBox
from WidgetSwitcher import WidgetSwitcher
from SelectionSpinBox import SpinBox
from PageButton import PageButton
from EntryAdd import EntryAdd




# Main Window
class MainWindow:
    def __init__(self, darkmode: bool = True, geometry: tuple[int, int] = (1000, 700)):


        # ---- Widget ---- #

        # Root
        self.root = customtkinter.CTk()
        self.root.geometry(f"{geometry[0]}x{geometry[1]}")
        self.root.title("Finance Tracker")
        self.darkmode = darkmode

        customtkinter.set_appearance_mode("dark" if self.darkmode else "light")
        customtkinter.set_default_color_theme("dark-blue")

        self.selectedButton: PageButton = None

        # Main Frame
        self.MainFrame = customtkinter.CTkFrame(master=self.root)
        self.MainFrame.pack(pady=20, padx=20, fill="both", expand=True)

        self.TopFrame = customtkinter.CTkFrame(master=self.MainFrame, width=10, height=10)
        self.TopFrame.pack(pady=20, padx=20, fill="x", anchor="n")

        # Top Buttons
        self.HomeButton = PageButton(self, self.TopFrame, "HOME", selected=True,
                                        command=self.show_entries)

        self.WalletsButton = PageButton(self, self.TopFrame,
                                        "WALLETS",
                                        selected=False,
                                        SelectLabel_width=100,
                                        command=self.show_wallets)

        self.selectedButton = self.HomeButton

        self.WalletSelect = SpinBox(self.MainFrame, self.root, None)

        # Content Frame
        self.Content = WidgetSwitcher(self.root, [])

            # Wallet List
        self.WalletFrame = customtkinter.CTkFrame(master=self.MainFrame, fg_color="transparent")
        self.WalletFrame.pack(fill="both", expand=True)

        self.WalletMaster = WalletContainer(master=self.WalletFrame, parent=self, root=self.root, time=FT_Time.now)

        self.WalletMaster.WalletFrame.pack_forget()
        self.Content.add_widget(object_ref=self.WalletMaster.WalletFrame, packing="pack", expand=True, anchor="nw")

        self.WalletSelect.WidgetSwitcher = self.Content

        # Recent Entries List
        self.EntriesMaster = EntryListBox(master=self.WalletFrame, parent=self, root=self.root)

        self.EntriesMaster.MainFrame.pack_forget()
        self.Content.add_widget(self.EntriesMaster.MainFrame, "pack", expand=True, fill="x", side="left", anchor="n")

        # Quick Entry Add
        self.EntryFrame = customtkinter.CTkFrame(self.MainFrame, height=200)
        self.EntryFrame.pack(anchor="s", fill="x")

        self.EntryAdd = EntryAdd(parent=self.EntryFrame,
                                 root=self.root,
                                 MainWindow=self,
                                 wallets=self.WalletMaster.wallets)


        self.add_wallet()
        self.WalletSelect.selection_at(0)

        self.Content.switch_to_index(1)

        self.root.mainloop()


    # ---- Functions ---- #

    def add_wallet(self):
        new_wallet = self.WalletMaster.add_wallet()

    def update_wallets(self, wallets: list[Wallet]):
        self.EntryAdd.update_wallet_list(wallets)
        self.update_wallet_select()

    def show_wallets(self, *args):
        self.Content.switch_to(self.WalletMaster.WalletFrame)

    def show_entries(self, *args):
        self.Content.switch_to(self.EntriesMaster.MainFrame)

    def update_wallet_select(self):
        self.WalletSelect.selection_values = []
        for x in self.WalletMaster.wallets:
            self.WalletSelect.add_widget(x.wallet_name)
        self.WalletSelect.selection_at(0)