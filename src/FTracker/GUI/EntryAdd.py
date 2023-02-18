import customtkinter


# Button for quickly adding income / expense entry into the log
class EntryAdd:
    def __init__(self,
                 parent: customtkinter,
                 root: customtkinter.CTk,
                 MainWindow,
                 wallets: list):

        self.parent: customtkinter = parent
        self.root: customtkinter.CTk = root
        self.wallets: list = [wallet.wallet_name for wallet in wallets]
        self.walletsO: list = wallets

        self.current_wallet = None


        # ---- Widget ---- #

        self.MainFrame = customtkinter.CTkFrame(master=self.parent, fg_color="transparent")
        self.MainFrame.pack(side="left", pady=5, padx=5, anchor="s")

        # Wallet Select
        self.WalletFrame = customtkinter.CTkFrame(master=self.MainFrame, fg_color="transparent", height=25)
        self.WalletFrame.grid(row=0, column=0, padx=5)

        self.WalletLabel = customtkinter.CTkLabel(master=self.WalletFrame,
                                                text="Wallet",
                                                font=(("Lato"), 15))
        self.WalletLabel.grid(row=0, sticky="w")

        self.WalletDropdown = customtkinter.CTkOptionMenu(master=self.WalletFrame,
                                                        values=self.wallets,
                                                        font=(("Lato"), 17),
                                                        bg_color="transparent",
                                                        width=125,
                                                        corner_radius=5,
                                                        dynamic_resizing=False,
                                                        command=self.set_current_wallet)

        self.WalletDropdown.grid(row=1)

        # Name Entry
        self.NameFrame = customtkinter.CTkFrame(master=self.MainFrame, fg_color="transparent", height=25)
        self.NameFrame.grid(row=0, column=1, padx=5)

        self.NameLabel = customtkinter.CTkLabel(master=self.NameFrame,
                                                text="Name",
                                                font=(("Lato"), 15))
        self.NameLabel.grid(row=0, sticky="w")

        self.NameEntry = customtkinter.CTkEntry(master=self.NameFrame,
                                                width=250,
                                                font=(("Lato"), 17))
        self.NameEntry.grid(row=1)

        # Amount
        self.AmountFrame = customtkinter.CTkFrame(master=self.MainFrame, fg_color="transparent", height=25)
        self.AmountFrame.grid(row=0, column=2, padx=5)

        self.AmountLabel = customtkinter.CTkLabel(master=self.AmountFrame, text="Amount", font=(("Lato"), 15))
        self.AmountLabel.grid(row=0, sticky="w")

        self.AmountEntry = customtkinter.CTkEntry(master=self.AmountFrame, width=125, font=(("Lato"), 17))
        self.AmountEntry.grid(row=1)

        self.CurrencyLabel = customtkinter.CTkLabel(master=self.AmountFrame, text="USD$", font=(("Lato"), 15))
        self.CurrencyLabel.grid(row=1, column=1, padx=10)

        # Type
        self.TypeFrame = customtkinter.CTkFrame(master=self.MainFrame, fg_color="transparent", height=25)
        self.TypeFrame.grid(row=0, column=3, padx=5)

        self.TypeLabel = customtkinter.CTkLabel(master=self.TypeFrame,
                                                text="Type",
                                                font=(("Lato"), 15))
        self.TypeLabel.grid(row=0, sticky="w")

        self.TypeDropdown = customtkinter.CTkOptionMenu(master=self.TypeFrame,
                                                        values=["Income", "Expense"],
                                                        font=(("Lato"), 17),
                                                        bg_color="transparent",
                                                        width=35,
                                                        corner_radius=5,
                                                        command=self.update_categories)

        self.TypeDropdown.grid(row=1)

        # Category
        self.CategoryFrame = customtkinter.CTkFrame(master=self.MainFrame, fg_color="transparent", height=25)
        self.CategoryFrame.grid(row=0, column=4, padx=5)

        self.CategoryLabel = customtkinter.CTkLabel(master=self.CategoryFrame,
                                                    text="Category",
                                                    font=(("Lato"), 15))
        self.CategoryLabel.grid(row=0, sticky="w")

        self.CategoryDropdown = customtkinter.CTkOptionMenu(master=self.CategoryFrame,
                                                    values=['Category'],
                                                    font=(("Lato"), 17),
                                                    bg_color="transparent",
                                                    width=35,
                                                    corner_radius=5)

        self.CategoryDropdown.grid(row=1)

        # AddButton
        self.AddFrame = customtkinter.CTkFrame(master=self.MainFrame, fg_color="transparent", height=25)
        self.AddFrame.grid(row=0, column=5, padx=5)

        self.AddLabel = customtkinter.CTkLabel(master=self.AddFrame,
                                                text="",
                                                font=(("Lato"), 15))
        self.AddLabel.grid(row=0)

        self.AddButton = customtkinter.CTkButton(master=self.AddFrame,
                                                 text="+ Add",
                                                 font=(("Lato"), 20, "bold"),
                                                 fg_color="#32a852",
                                                 hover_color="#42bd63",
                                                 bg_color="transparent",
                                                 width=25,
                                                 corner_radius=5,
                                                 command=self.add_entry)

        self.AddButton.grid(row=1)


    # ---- Functions ---- #

    # Add income/expense entry to the currently selected wallet
    def add_entry(self, *args):
        if self.is_entry_valid(self.NameEntry.get(), self.AmountEntry.get()):
            print(self.current_wallet.wallet_name)
            self.current_wallet.add_entry(self.get_entry_values())
            self.reset_input()
        else:
            print("Failed to add new entry")
            return

    # Get all values inserted by the user and return them as a dictionary
    def get_entry_values(self) -> dict:
        d = {}
        d['name'] = self.NameEntry.get()
        d['type'] = self.TypeDropdown.get()
        d['category'] = self.CategoryDropdown.get()
        d['value'] = float(self.AmountEntry.get())
        d['currency'] = self.CurrencyLabel.cget("text")
        d['wallet'] = self.current_wallet.wallet_name
        return d

    def is_entry_valid(self, name: str, amount: int|float) -> bool:
        self.NameEntry.configure(border_color="gray")
        self.AmountEntry.configure(border_color="gray")

        if name == "":
            self.NameEntry.configure(border_color="red")
            return False

        if amount == "":
            self.AmountEntry.configure(border_color="red")
            return False

        if not type(amount) in [float, int]:
            self.AmountEntry.configure(border_color="red")
            return False

        return True

    def reset_input(self):
        self.NameEntry.delete(0, len(self.NameEntry.get()))
        self.AmountEntry.delete(0, len(self.AmountEntry.get()))

    def set_current_wallet(self, *args):
        self.current_wallet = self.find_wallet(self.WalletDropdown.get())[1]
        self.update_currency()
        self.update_categories()

    def find_wallet(self, wallet_name: str) -> tuple[int, object]:
        for wallet in self.walletsO:
            if wallet.wallet_name == wallet_name:
                return (self.walletsO.index(wallet), wallet)

    def set_wallet(self, index: int):
        if index < 0 or index > len(self.wallets)-1:
            return -1

        wallet = self.walletsO[index]

        self.current_wallet = wallet
        self.update_currency()
        self.update_categories()
        self.WalletDropdown.set(self.wallets[index])

    def update_wallet_list(self, wallets):
        self.wallets  = [wallet.wallet_name for wallet in wallets]
        self.WalletDropdown.configure(values=self.wallets)
        self.WalletDropdown.set(self.wallets[0])
        self.current_wallet = None if len(self.walletsO) == 0 else self.walletsO[0]

    def update_currency(self):
        self.CurrencyLabel.configure(text=self.current_wallet.currency)

    def update_categories(self, *args):
        if self.TypeDropdown.get().lower() == 'income':
            incomeCategories = [vars(item)['name'] for item in self.current_wallet.entries.incomeList.categories]
            self.CategoryDropdown.configure(values=incomeCategories)
            if len(incomeCategories) > 0:
                self.CategoryDropdown.set(incomeCategories[0])
            else:
                self.CategoryDropdown.set("Default")

        if self.TypeDropdown.get().lower() == 'expense':
            expenseCategories = [vars(item)['name'] for item in self.current_wallet.entries.expenseList.categories]
            self.CategoryDropdown.configure(values=expenseCategories)
            if len(expenseCategories) > 0:
                self.CategoryDropdown.set(expenseCategories[0])
            else:
                self.CategoryDropdown.set("Default")