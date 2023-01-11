import customtkinter
from typing import Optional

class LabeledProgressBar:
    def __init__(self,
                 master: customtkinter,
                 root: customtkinter.CTk,
                 text: str,
                 current_progress: float = 0.5,
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
                                                     fg_color=kwargs.get("fg_color") or "green")
        self.Progress.grid(row=1)

        self.Target = customtkinter.CTkLabel(master=self.MainFrame, text="0/100", font=(("Lato"), 16))
        self.Target.grid(row=1, column=1, stick="e", padx=15)


        self.update_progressbar()


    def update_progressbar(self):
        self.Progress.set(self.current_progress)
        self.root.update_idletasks()