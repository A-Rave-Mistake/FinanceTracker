import customtkinter

import FT_Time

from WalletContainer import WalletContainer
from wallet import Wallet
from EntryListBox import EntryListBox
from WidgetSwitcher import WidgetSwitcher
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

        # Content Frame
        self.Content = WidgetSwitcher(self.root, [])

        self.WalletFrame = customtkinter.CTkFrame(master=self.MainFrame)
        self.WalletFrame.pack(fill="both", expand=True)

        self.WalletMaster = WalletContainer(master=self.WalletFrame, parent=self, root=self.root, time=FT_Time.now)

        self.WalletMaster.WalletFrame.pack_forget()
        self.Content.add_widget(object_ref=self.WalletMaster.WalletFrame, packing="pack", expand=True, anchor="nw")

        self.EntriesMaster = EntryListBox(master=self.WalletFrame, parent=self, root=self.root)

        self.EntriesMaster.MainFrame.pack_forget()
        self.Content.add_widget(self.EntriesMaster.MainFrame, "pack", expand=True, fill="x", side="left", anchor="n")

        self.EntryAdd = EntryAdd(parent=self.MainFrame,
                                 root=self.root,
                                 MainWindow=self,
                                 wallets=self.WalletMaster.wallets)


        self.add_wallet()

        self.Content.switch_to_index(1)

        self.root.mainloop()


    # ---- Functions ---- #

    def add_wallet(self):
        self.WalletMaster.add_wallet()

    def update_wallets(self, wallets: list[Wallet]):
        self.EntryAdd.update_wallet_list(wallets)

    def show_wallets(self, *args):
        self.Content.switch_to(self.WalletMaster.WalletFrame)

    def show_entries(self, *args):
        self.Content.switch_to(self.EntriesMaster.MainFrame)