import customtkinter
import FT_Time

from WalletContainer import WalletContainer
from wallet import Wallet, DullWallet, wallet_colors

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

        self.HomeButton = PageButton(self, self.TopFrame, "HOME", selected=True)
        self.WalletsButton = PageButton(self, self.TopFrame, "WALLETS", selected=False, SelectLabel_width=100)

        self.selectedButton = self.HomeButton

        # Content Frame
        self.WalletFrame = customtkinter.CTkFrame(master=self.MainFrame)
        self.WalletFrame.pack(fill="both", expand=True)

        self.WalletMaster = WalletContainer(master=self.WalletFrame, parent=self, root=self.root, time=FT_Time.now)

        self.EntryAdd = EntryAdd(parent=self.MainFrame,
                                 root=self.root,
                                 MainWindow=self,
                                 wallets=self.WalletMaster.wallets)


        self.add_wallet()

        self.root.mainloop()


    # ---- Functions ---- #

    def add_wallet(self):
        self.WalletMaster.add_wallet()

    def update_wallets(self, wallets: list[Wallet]):
        self.EntryAdd.update_wallet_list(wallets)