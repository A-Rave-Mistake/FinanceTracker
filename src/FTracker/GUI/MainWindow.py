import customtkinter

from .WalletContainer import WalletContainer
from .WalletDetailedView import WalletDetailedView
from .WidgetSwitcher import WidgetSwitcher
from .SelectionSpinBox import SpinBox
from .PageButton import PageButton
from .EntryAdd import EntryAdd

from ..utils import FT_Time
from ..wallet import Wallet



# Main Window
class MainWindow:
    def __init__(self, darkmode: bool = True, geometry: tuple[int, int] = (1000, 700)):
        """
        Desc:
            This class creates a window that contains all widgets and acts as parent for widget to widget communication.
            It's so called an "app" itself.
        Args:
            darkmode::bool
                Enable/Disable dark mode for the wiidget
                True by default
            geometry::(int, int)
                Window size
                (width, height)
        """


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

            # Wallet List

        self.ContentFrame = customtkinter.CTkFrame(master=self.MainFrame, fg_color="transparent")
        self.ContentFrame.pack(fill="both", expand=True)

        self.WalletFrame = customtkinter.CTkFrame(master=self.ContentFrame, fg_color="transparent")
        self.WalletFrame.pack(fill="both", expand=True)

        self.WalletMaster = WalletContainer(master=self.WalletFrame, parent=self, root=self.root, time=FT_Time.now)

        self.WalletFrame.pack_forget()
        self.Content.add_widget(object_ref=self.WalletFrame, packing="pack", fill="both", expand=True)



        # Recent Entries List
        self.Test = customtkinter.CTkFrame(self.ContentFrame, fg_color="transparent")
        self.Test.pack(fill="both", expand=True)

        self.WalletSelect = SpinBox(self.Test, self.root, callables=[self.on_WalletSelect_change])
        self.WalletSelect.WidgetSwitcher = self.Content

        self.CurrentWalletInfo = WalletDetailedView(master=self.Test, parent=self, root=self.root)

        #self.EntriesMaster = EntryListBox(master=self.Test, parent=self, root=self.root)

        self.Test.pack_forget()
        self.Content.add_widget(self.Test, "pack", expand=True, fill="x")

        # Quick Entry Add
        self.EntryFrame = customtkinter.CTkFrame(self.MainFrame, height=200)
        self.EntryFrame.pack(anchor="s", fill="x")

        self.EntryAdd = EntryAdd(parent=self.EntryFrame,
                                 root=self.root,
                                 MainWindow=self,
                                 wallets=self.WalletMaster.wallets)


        new_wallet = self.add_wallet()
        self.go_to_wallet(new_wallet[0], new_wallet[1])
        #self.EntriesMaster.current_wallet = self.WalletMaster.wallets[0]
        self.WalletSelect.selection_at(0)

        self.Content.switch_to_index(1)

        new_wallet[0].add_category(name="Food", type="Income", color="green")

        self.root.mainloop()


    # ---- Functions ---- #

    def add_wallet(self):
        self.WalletMaster.add_wallet()
        return (self.WalletMaster.wallets[-1], self.WalletMaster.wallets.index(self.WalletMaster.wallets[-1]))

    def update_wallets(self, wallets: list[Wallet]):
        self.EntryAdd.update_wallet_list(wallets)
        self.update_wallet_select()

    def show_wallets(self, *args):
        self.Content.switch_to(self.WalletFrame)

    def show_entries(self, *args):
        self.Content.switch_to(self.Test)

    def update_wallet_select(self):
        self.WalletSelect.selection_values = []
        for x in self.WalletMaster.wallets:
            self.WalletSelect.add_widget(x.wallet_name)
        self.WalletSelect.selection_at(self.WalletSelect.selection_index or 0)

    def go_to_wallet(self, wallet, index: int):
        self.show_entries()
        self.HomeButton.set_selected()
        self.CurrentWalletInfo.set_wallet(wallet)
        self.EntryAdd.set_wallet(index)
        self.WalletSelect.selection_at(index)

    def on_WalletSelect_change(self, index: int):
        self.go_to_wallet(self.WalletMaster.wallets[index], index)

    def update_categories(self):
        self.CurrentWalletInfo.WalletCategories.refresh_categories()
        self.EntryAdd.update_categories()