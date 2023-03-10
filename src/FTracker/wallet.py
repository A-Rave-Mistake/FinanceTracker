import customtkinter

from .utils import FT_Time
from .entry import DateEntry
from .entry import DATE
from .utils.linkedlist import LinkedList_Element
from .GUI.LabeledProgressBar import LabeledProgressBar_Target


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
                 parent,
                 year: int,
                 name: str,
                 currency: str,
                 index: int,
                 row: int = 0,
                 column: int = 0,
                 **kwargs):
        '''
        Args:
            master::customtkinter
                The container this Wallet belongs to (typically customtkinter.CTkFrame)
            root::customtkinter.CTk
                CTk root of the main GUI window (MainWindow class)
            parent::MainWindow
                MainWindow reference
            year::int
                Current real-time year
            name::str
                Name of the wallet, by default it's indexed ("Wallet #1", "Wallet #2", etc.)
            currency::str
                Currency this wallet uses
            row::int & column::int
                Widget component's placement in master widget
            kwargs::dict
                Additional parameters for the widget elements
        '''

        super().__init__()
        self.master: customtkinter = master
        self.root: customtkinter.CTk = root
        self.parent = parent
        self.row: int = row
        self.column: int = column

        # Wallet Info
        self.wallet_name: str = name
        self.currency: str = currency
        self.current_year: int = year
        self.index: int = index

        self.time = FT_Time.now
        self.months = [FT_Time.months[month] for month in range(1, self.time.tm_mon + 1)]

        self.categories: list[dict] = [] # List of Category.__dict__ elements

        # Current year, contains months as children according to real time
        self.entries: DateEntry = DateEntry(DATE(("year", self.current_year)))

        # Create a month DateEntry for every month that has already occured in this year
        self.entries.create_months(self.months)

        # Create a day DateEntry for every day elapsed in current month
        for child in self.entries.children:
            month = child.date[1]
            if month != FT_Time.months[self.time.tm_mon]:
                child.create_days(FT_Time.get_days_bystr(month))
            else:
                child.create_days(self.time.tm_mday)

        # Money
        self.current_money: float = 0.0
        self.target_expense: float = 1000.0
        self.target_income: float = 1000.0


        # ---- Widget ---- #

        self.MainFrame = customtkinter.CTkFrame(master=self.master, fg_color="transparent")
        self.MainFrame.grid(row=self.row, column=self.column, padx=5, pady=5, sticky="wn")

        self.WalletButton = customtkinter.CTkButton(master=self.MainFrame,
                                                    fg_color=kwargs.get("wallet_color") or wallet_colors[0][0],
                                                    text=f"{self.wallet_name}\n{self.current_money} {self.currency}",
                                                    font=(("Lato"), 22),
                                                    width=310,
                                                    height=125,
                                                    corner_radius=15,
                                                    border_color=kwargs.get("border_color") or wallet_colors[0][1],
                                                    border_width=4,
                                                    hover_color=kwargs.get("border_color") or wallet_colors[0][1],
                                                    anchor="sw",
                                                    command=self.go_to_wallet)
        self.WalletButton.grid()


        self.IncomeBar = LabeledProgressBar_Target(master=self.MainFrame,
                                                   root=self.root,
                                                   text="Income",
                                                   progress_color="#48c746",
                                                   fg_color="#7fab7e",
                                                   currency=self.currency)

        self.update_IncomeBar()

        self.ExpensesBar = LabeledProgressBar_Target(master=self.MainFrame,
                                                     root=self.root,
                                                     text="Expenses",
                                                     progress_color="#cf413e",
                                                     fg_color="#874646",
                                                     currency=self.currency)

        self.update_ExpensesBar()


    # ---- Functions ---- #

    def update_ExpensesBar(self):
        self.ExpensesBar.update_progressbar(self.entries.get_total_expenses(), self.target_expense)
        self.ExpensesBar.format_progress_text(self.entries.get_total_expenses(), self.target_expense, self.currency)

    def update_IncomeBar(self):
        self.IncomeBar.update_progressbar(self.entries.get_total_income(), self.target_income)
        self.IncomeBar.format_progress_text(self.entries.get_total_income(), self.target_income, self.currency)

    def add_entry(self, entry):
        result = self.entries.add_entry(entry)

        if result[0]:
            print("Added New Entry")
            self.update_widgets()
            if self.parent.WalletSelect.selection_index == self.index:
                self.parent.CurrentWalletInfo.WalletEntries.add_entry(result[1])

    def add_category(self, **kwargs) -> bool:
        if self.category_exists(kwargs.get('name')):
            print("The category already exists!")
            return False

        if kwargs.get('type').lower() == "income":
            new_cat = self.entries.incomeList.add_category(kwargs)
        elif kwargs.get('type').lower() == "expense":
            new_cat = self.entries.expenseList.add_category(kwargs)
        elif kwargs.get('type').lower() == "both":
            new_cat = self.entries.incomeList.add_category(kwargs)
            new_cat = self.entries.expenseList.add_category(kwargs)
        else:
            print("Invalid Type")
            return False

        self.categories.append(new_cat)
        self.parent.update_categories()
        return True

    def category_exists(self, name: str) -> bool:
        if name in [cat['name'] for cat in self.categories]:
            return True
        else:
            return False

    def update_widgets(self):
        self.current_money = self.entries.get_total_income()
        self.WalletButton.configure(text=f"{self.wallet_name}\n{self.current_money} {self.currency}")
        self.update_IncomeBar()
        self.update_ExpensesBar()

    def go_to_wallet(self):
        self.parent.go_to_wallet(self, self.index)



# Functions as a button to create a new Wallet
# Unusable on it's own
class DullWallet(BaseWallet):
    def __init__(self, master: customtkinter, parent, row: int = 0, column: int = 0):

        '''
        Args:
            master::customtkinter
                The container this Wallet belongs to (typically customtkinter.CTkFrame)
            parent::WalletContainer
                WalletContainer object reference
            row::int & column::int
                Widget component's placement in master widget
            kwargs::dict
                Additional parameters for the widget elements
        '''

        super().__init__()
        self.master: customtkinter = master
        self.parent = parent
        self.row: int = row
        self.column: int = column


        # ---- Widget ---- #

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