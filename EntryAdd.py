import customtkinter


# Button for quickly adding income / expense entry into the log
class EntryAdd:
    def __init__(self,
                 parent: customtkinter,
                 root: customtkinter.CTk,
                 wallets: list):

        self.parent = parent
        self.root = root
        self.wallets = [wallet.wallet_name for wallet in wallets]


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
                                                          dynamic_resizing=False)

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
                                                 corner_radius=5)

        self.AddButton.grid(row=1)


    def update_wallet_list(self, wallets):
        self.wallets  = [wallet.wallet_name for wallet in wallets]
        self.WalletDropdown.configure(values=self.wallets)
        self.WalletDropdown.set(self.wallets[0])