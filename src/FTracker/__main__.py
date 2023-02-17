#!/usr/bin/env python3

from .GUI.MainWindow import MainWindow
from .utils import FT_Time

if __name__ == "__main__":
    time = FT_Time.now
    app = MainWindow()