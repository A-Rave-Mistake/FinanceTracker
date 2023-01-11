import customtkinter

from wallet import Wallet, DullWallet, BaseWallet, wallet_colors
from linkedlist import LinkedList



class WalletContainer(LinkedList):
    def __init__(self, master: customtkinter, parent, root: customtkinter.CTk, time):
        super().__init__()

        self.master = master
        self.parent = parent
        self.root = root
        self.time = time

        self.wallets: list[BaseWallet] = []

        self.WalletFrame = customtkinter.CTkFrame(master=self.master, fg_color="transparent")
        self.WalletFrame.grid()


    def add_wallet(self):
        if self.head and self.head.next:
            self.remove_dull_wallet()

        from random import choice
        wcolor = choice(wallet_colors)

        self.append(Wallet(master=self.WalletFrame,
                                   root=self.root,
                                   name=self.wallet_default_name(),
                                   year=self.time.tm_year,
                                   currency="USD",
                                   wallet_color=wcolor[0],
                                   border_color=wcolor[1],
                                   row=self.get_row(),
                                   column=self.get_column()))

        self.add_dull_wallet()

    def add_dull_wallet(self):
        self.append(DullWallet(master=self.WalletFrame,
                               parent=self,
                               row=self.get_row(),
                               column=self.get_column()))

    def remove_dull_wallet(self):
        dull = self.remove_tail()
        dull.remove()

    def get_row(self) -> int:
        return int(max(self.count / 5, 0))

    def get_column(self) -> int:
        return self.count % 5

    def get_wallet_pos(self) -> tuple[int, int]:
        return (self.get_row(), self.get_column())

    # If wallet name is not specified by the user it will automatically be indexed
    def wallet_default_name(self) -> str:
        return f"Wallet #{len(self.wallets)+1}"