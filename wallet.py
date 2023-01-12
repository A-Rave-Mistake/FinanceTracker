import customtkinter

from entry import DateEntry
from entry import DATE

from linkedlist import LinkedList_Element

from LabeledProgressBar import LabeledProgressBar


wallet_colors: list[tuple[str, str]] = [("#32a852","#42bd63"),
                            ("#eb4034", "#ed544a"),
                           ("#4b8bde", "#609ae6"),
                            ("#e05cd3", "#e368d7"),
                            ("#e05c7b", "#e8748f"),
                            ("#d1be4f", "#e0ce60"),
                            ("#4ec0c2", "#69d4d6"),
                            ("#c4895e", "#d19971")]



class BaseWallet(LinkedList_Element):
    def __init__(self, row: int = 0, column: int = 0):
        super().__init__()
        self.MainFrame = None

    def remove(self):
        self.MainFrame.destroy()
        del self


# Depicts a single account that contains expenses, income, savings and targets
class Wallet(BaseWallet):
    def __init__(self,
                 master: customtkinter,
                 root: customtkinter.CTk,
                 year: int,
                 name: str,
                 currency: str,
                 row: int = 0,
                 column: int = 0,
                 **kwargs):

        '''
        :param master: the container this Wallet belongs to
        :param root: CTk root of the main gui window
        :param year: current real-time year
        :param name: name of the wallet, by default it's indexed ("Wallet #1", "Wallet #2", etc.)
        :param kwargs: additional parameters for the widget elements
        '''

        super().__init__()
        self.master = master
        self.root = root
        self.row = row
        self.column = column

        # Wallet Info
        self.wallet_name = name
        self.currency = currency
        self.current_year = year

        self.entries: DateEntry = DateEntry(DATE("year"))

        # Targets
        self.target_expense = 0.0
        self.target_income = 0.0


        # ---- Widget ---- #

        self.MainFrame = customtkinter.CTkFrame(master=self.master, fg_color="transparent")
        self.MainFrame.grid(row=self.row, column=self.column, padx=5, pady=5, sticky="wn")

        self.WalletButton = customtkinter.CTkButton(master=self.MainFrame,
                                                    fg_color=kwargs.get("wallet_color") or wallet_colors[0][0],
                                                    text=f"{self.wallet_name}\n$4345",
                                                    font=(("Lato"), 22),
                                                    width=310,
                                                    height=125,
                                                    corner_radius=15,
                                                    border_color=kwargs.get("border_color") or wallet_colors[0][1],
                                                    border_width=4,
                                                    hover_color=kwargs.get("border_color") or wallet_colors[0][1],
                                                    anchor="sw")
        self.WalletButton.grid()


        self.IncomeBar = LabeledProgressBar(master=self.MainFrame,
                                            root=self.root,
                                            text="Income",
                                            progress_color="#48c746",
                                            fg_color="#7fab7e")

        self.ExpensesBar = LabeledProgressBar(master=self.MainFrame,
                                            root=self.root,
                                            text="Expenses",
                                            progress_color="#cf413e",
                                            fg_color="#874646")



# This functions as a button to create new Wallet object
class DullWallet(BaseWallet):
    def __init__(self, master: customtkinter, parent, row: int = 0, column: int = 0):

        super().__init__()
        self.master = master
        self.parent = parent
        self.row = row
        self.column = column

        self.MainFrame = customtkinter.CTkFrame(master=self.master, fg_color="transparent")
        self.MainFrame.grid(row=self.row, column=self.column, sticky="wn", padx=5, pady=5)

        self.WalletButton = customtkinter.CTkButton(master=self.MainFrame,
                                                    fg_color="transparent",
                                                    text_color="#326ed9",
                                                    text=f"+",
                                                    font=(("Lato"), 50),
                                                    width=200,
                                                    height=125,
                                                    corner_radius=15,
                                                    border_color="#326ed9",
                                                    border_width=4,
                                                    hover_color="#4f5154",
                                                    anchor="center",
                                                    command=self.add_wallet)
        self.WalletButton.grid()


    def add_wallet(self):
        self.parent.add_wallet()