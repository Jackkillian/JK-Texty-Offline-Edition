"""
Name:    (add-on name, e.g. MyAddOn)
Version: (version e.g. Prerelease: 1.0.0-beta)
Author:  (author e.g. your username on GitHub)
License: MIT License
Website: (website, e.g. myaddon.com)
O.S.:    (the o.s. that this add-on can run on, e.g. Any O.S./mac OS/Windows)
"""

import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText as scrolledtext

class MyAddOnName():
    """Run MyAddOnName"""
    def __init__(self):
        """Run MyAddOnName"""
        self.setup()
        self.def_gui()
        self.grid_gui()
        self.root.mainloop()

    def setup(self):
        """Setup MyAddOnName"""
        self.root = tk.Tk()
        self.root.title('MyAddOnName')
        self.root_theme = ttk.Style(self.root)
        self.root_theme.theme_use('clam')

    def def_gui(self):
        """Define the GUI"""
        self.main_text = scrolledtext(self.root)
        self.quit_button = ttk.Button(self.root, text='Quit MyAddOnName', command=lambda: self._quit())
        self.save_button = ttk.Button(self.root, text='Save', command=lambda: self._save())

    def grid_gui(self):
        self.main_text.grid(row=2, column=0, columnspan=10)
        self.quit_button.grid(row=1, column=0)
        self.save_button.grid(row=1, column=1)

def main():
    MyAddOnName()

if __name__ == '__main__':
    main()
