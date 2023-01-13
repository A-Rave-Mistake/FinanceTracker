import customtkinter


# Button for quickly adding income / expense entry into the log
class EntryAdd:
    def __init__(self,
                 parent: customtkinter,
                 root: customtkinter.CTk,
                 MainWindow,
                 wallets: list):

        self.parent = parent
        self.root = root
        self.wallets = [wallet.wallet_name for wallet in wallets]
        self.walletsO = wallets

        self.current_wallet = None


        # ---- Widget ---- #

        self.MainFrame = customtkinter.CTkFrame(master=self.parent, fg_color="transparent")
        self.MainFrame.pack(side="left", pady=5, padx=5)

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
                                                        corner_radius=5)

        self.TypeDropdown.grid(row=1)

        # Category
        self.CategoryFrame = customtkinter.CTkFrame(master=self.MainFrame, fg_color="transparent", height=25)
        self.CategoryFrame.grid(row=0, column=4, padx=5)

        self.CategoryLabel = customtkinter.CTkLabel(master=self.CategoryFrame,
                                                    text="Category",
                                                    font=(("Lato"), 15))
        self.CategoryLabel.grid(row=0, sticky="w")

        self.CategoryDropdown = customtkinter.CTkOptionMenu(master=self.CategoryFrame,
                                                    values=["Food", "Rent", "Car", "Bills", "Gifts"],
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


    # Add income/expense entry to the currently selected wallet
    def add_entry(self, *args):
        if self.is_entry_valid():
            self.current_wallet.add_entry(self.get_entry_values())
            self.reset_entries()
        else:
            print("Failed to add new entry")
            return

    def get_entry_values(self) -> dict:
        d = {}
        d['name'] = self.NameEntry.get()
        d['type'] = self.TypeDropdown.get()
        d['category'] = self.CategoryDropdown.get()
        d['value'] = float(self.AmountEntry.get())
        d['currency'] = self.CurrencyLabel.cget("text")
        return d

    def is_entry_valid(self) -> bool:
        if self.NameEntry.get() == "":
            self.NameEntry.configure(border_color="red")
            return False

        if self.AmountEntry.get() == "":
            self.AmountEntry.configure(border_color="red")
            return False

        if not self.AmountEntry.get().isdigit():
            self.AmountEntry.configure(border_color="red")
            return False

        self.reset_error_colors()
        return True

    def reset_error_colors(self):
        self.NameEntry.configure(border_color="gray")
        self.AmountEntry.configure(border_color="gray")

    def reset_entries(self):
        self.NameEntry.delete(0, len(self.NameEntry.get()))
        self.AmountEntry.delete(0, len(self.AmountEntry.get()))

    def set_current_wallet(self, *args):
        self.current_wallet = self.find_wallet()[1]
        self.update_currency()

    def find_wallet(self) -> tuple[int, object]:
        for wallet in self.walletsO:
            if wallet.wallet_name == self.WalletDropdown.get():
                return (self.walletsO.index(wallet), wallet)

    def update_wallet_list(self, wallets):
        self.wallets  = [wallet.wallet_name for wallet in wallets]
        self.WalletDropdown.configure(values=self.wallets)
        self.WalletDropdown.set(self.wallets[0])
        self.current_wallet = None if len(self.walletsO) == 0 else self.walletsO[0]

    def update_currency(self):
        self.CurrencyLabel.configure(text=self.current_wallet.currency)