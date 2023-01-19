import customtkinter

class WalletBox:
    def __init__(self, master: customtkinter, parent, root: customtkinter.CTk):
        self.master: customtkinter = master
        self.parent = parent
        self.root: customtkinter.CTk = root


        # ---- Widget ---- #

        self.MainFrame = customtkinter.CTkFrame(master=self.master, border_width=3)
        self.MainFrame.pack(fill="x", expand=True, pady=5, padx=5)

        self.ContentFrame = customtkinter.CTkFrame(self.MainFrame, fg_color="transparent")
        self.ContentFrame.grid(sticky="news", padx=10, pady=5, row=0)



class WalletInfoBox(WalletBox):
    def __init__(self, master: customtkinter, parent, root: customtkinter.CTk, **wallet_info):
        super().__init__(master, parent, root)
        self.master: customtkinter = master
        self.parent = parent
        self.root: customtkinter.CTk = root

        self.wallet_name: str = wallet_info.get('wallet_name')
        self.value: float = wallet_info.get('value')
        self.currency: str = wallet_info.get('currency')


        # ---- Widget ---- #

        self.WalletNameLabel = customtkinter.CTkLabel(self.ContentFrame, text="", font=(("Lato"), 25))
        self.WalletNameLabel.grid(row=0, column=0, pady=5, sticky="w")

        self.WalletValueLabel = customtkinter.CTkLabel(self.ContentFrame, text="", font=(("Lato"), 25))
        self.WalletValueLabel.grid(row=1, column=0, pady=5, sticky="w")


    def set_wallet_info(self, wallet_name: str, value: float, currency: str):
        self.wallet_name = wallet_name
        self.value = value
        self.currency = currency
        self.WalletNameLabel.configure(text=self.wallet_name)
        self.WalletValueLabel.configure(text=f"{self.value} {self.currency}")



class WalletTargetBox(WalletBox):
    def __init__(self, master: customtkinter, parent, root: customtkinter.CTk, **wallet_info):
        super().__init__(master, parent, root)
        self.master: customtkinter = master
        self.parent = parent
        self.root: customtkinter.CTk = root

        self.expense_current: float = wallet_info.get('expense_current')
        self.expense_target: float = wallet_info.get('expense_target')
        self.income_current: float = wallet_info.get('income_current')
        self.income_target: float = wallet_info.get('income_target')


        # ---- Widget ---- #

        self.IncomeLabel = customtkinter.CTkLabel(self.ContentFrame, text="Income", font=(("Lato"), 24, "bold"))
        self.IncomeLabel.grid(row=0, column=0, pady=5, sticky="w")

        self.Income = customtkinter.CTkLabel(self.ContentFrame, text="", font=(("Lato"), 20))
        self.Income.grid(row=1, column=0, pady=5, sticky="w")

        self.ExpenseLabel = customtkinter.CTkLabel(self.ContentFrame, text="Expense", font=(("Lato"), 24, "bold"))
        self.ExpenseLabel.grid(row=2, column=0, pady=5, sticky="w")

        self.Expense = customtkinter.CTkLabel(self.ContentFrame, text="", font=(("Lato"), 20))
        self.Expense.grid(row=3, column=0, pady=5, sticky="w")


    def set_wallet_info(self, expense_current: float, expense_target: float, income_current: float, income_target: float):
        self.expense_current =  expense_current
        self.expense_target = expense_target
        self.income_current = income_current
        self.income_target = income_target

        try:
            expense_progress = (expense_current / expense_target) * 100
        except ZeroDivisionError:
            expense_progress = 0

        try:
            income_progress = (income_current / income_target) * 100
        except ZeroDivisionError:
            income_progress = 0

        self.Expense.configure(text=f"{expense_current} / {expense_target}   ({expense_progress:.1f})%")
        self.Income.configure(text=f"{income_current} / {income_target}   ({income_progress:.1f})%")