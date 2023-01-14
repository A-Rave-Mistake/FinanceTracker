import customtkinter
from typing import Optional

class LabeledProgressBar:
    def __init__(self,
                 master: customtkinter,
                 root: customtkinter.CTk,
                 text: str,
                 current_progress: float = 0.1,
                 max_progress: float = 1.0,
                 **kwargs: Optional):

        self.root = root
        self.master = master

        self.text = text
        self.current_progress = current_progress
        self.max_progress = max_progress


        # ---- Widget ----#

        self.MainFrame = customtkinter.CTkFrame(master=self.master, fg_color="transparent")
        self.MainFrame.grid(sticky="w", padx=15)

        self.Label = customtkinter.CTkLabel(master=self.MainFrame, text=self.text, font=(("Lato"), 15))
        self.Label.grid(row=0, stick="w")

        self.Progress = customtkinter.CTkProgressBar(master=self.MainFrame,
                                                     progress_color=kwargs.get("progress_color") or "green",
                                                     fg_color=kwargs.get("fg_color") or "green",
                                                     width=165)
        self.Progress.grid(row=1,stick="w")

        self.Target = customtkinter.CTkLabel(master=self.MainFrame, text="None", font=(("Lato"), 16))
        self.Target.grid(row=1, column=1, columnspan=2, stick="e", padx=15)


    def update_progressbar(self, value: float, target: float):
        try:
            if not self.current_progress >= 100.0:
                self.current_progress = float(f"{value / target:.1f}")
                self.Progress.set(self.current_progress)
                self.root.update_idletasks()
        except ZeroDivisionError:
            self.current_progress = 0.0
            self.Progress.set(self.current_progress)
            self.root.update_idletasks()

    def format_progress_text(self, current: float, target: float, currency: str):
        self.Target.configure(text=f"{current} {currency}")