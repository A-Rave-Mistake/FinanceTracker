import customtkinter

from EntryListBox import EntryListBox
from WalletInfoBox import WalletInfoBox, WalletTargetBox, WalletCategoryBox


class WalletDetailedView:
    def __init__(self, master: customtkinter, parent, root: customtkinter.CTk, wallet=None):
        self.master: customtkinter = master
        self.parent = parent
        self.root: customtkinter.CTk = root
        self.wallet = wallet


        # ---- Widgets ---- #

        self.MainFrame = customtkinter.CTkFrame(master=self.master, fg_color="transparent")
        self.MainFrame.pack(expand=True, fill="x", anchor="n")

        self.WalletEntries = EntryListBox(master=self.MainFrame, parent=self, root=self.root)

        self.RightBox = customtkinter.CTkFrame(master=self.MainFrame, fg_color="transparent")
        self.RightBox.pack(expand=True, fill="x", side="left")

        self.WalletInfo = WalletInfoBox(master=self.RightBox,
                                        parent=self.parent,
                                        root=self.root)

        self.WalletTargets = WalletTargetBox(master=self.RightBox,
                                             parent=self.parent,
                                             root=self.root)

        self.WalletCategories = WalletCategoryBox(master=self.RightBox,
                                                  parent=self.parent,
                                                  root=self.root)

    def set_wallet(self, wallet):
        self.wallet = wallet
        self.WalletEntries.current_wallet = wallet

        self.WalletEntries.load_entries(wallet.entries.get_all_entries())
        self.WalletCategories.set_wallet_info(self.wallet)
        self.refresh_wallet_info()

    def refresh_wallet_info(self):
        self.WalletInfo.set_wallet_info(wallet_name=self.wallet.wallet_name,
                                        value=self.wallet.current_money,
                                        currency=self.wallet.currency)

        self.WalletTargets.set_wallet_info(expense_target=self.wallet.target_expense,
                                           expense_current=self.wallet.entries.get_total_expenses(),
                                           income_target=self.wallet.target_income,
                                           income_current=self.wallet.entries.get_total_income())