"""
Name:    Markdown
Version: 1.0.0-alpha
License: MIT License
Author:  Jack Freund a.k.a. R.D. Junkface
"""

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import font
from tkinter import filedialog as fd
from tkinter import messagebox as mbox
import sys

class JKTextyExtraText(scrolledtext.ScrolledText):
    '''A customized version of tkinter.scrolledtext.ScrolledText'''
    def __init__(self, *args, **kwargs):
        tk.Text.__init__(self, *args, **kwargs)

    def highlight_pattern(self, pattern, tag, start="1.0", end="end",
                          regexp=False):
        '''Apply the given tag to all text that matches the given pattern

        If 'regexp' is set to True, pattern will be treated as a regular
        expression according to Tcl's regular expression syntax.
        '''

        start = self.index(start)
        end = self.index(end)
        self.mark_set("matchStart", start)
        self.mark_set("matchEnd", start)
        self.mark_set("searchLimit", end)

        count = tk.IntVar()
        while True:
            index = self.search(pattern, "matchEnd","searchLimit",
                                count=count, regexp=regexp)
            if index == "": break
            if count.get() == 0: break # degenerate pattern which matches zero-length strings
            self.mark_set("matchStart", index)
            self.mark_set("matchEnd", "%s+%sc" % (index, count.get()))
            self.tag_add(tag, "matchStart", "matchEnd")
            
class Markdown():
    """Run Markdown"""

    def __init__(self):
        """Run Markdown"""
        self.setup()
        self.def_gui()
        self.grid_gui()
        self.root.mainloop()

    ############################
    # Definitions for __init__ #
    ############################
    
    def setup(self):
        """Setup Markdown"""
        # Setup the main window
        self.root = tk.Tk()
        self.root.title('Markdown | New File')
        # Setup the theme for the main window
        self.root_theme = ttk.Style(self.root)
        self.root_theme.theme_use('clam')
        self.open_filetypes=(('All Files', '.*'), ('Markdown', '.scpt'))
        self.save_filetypes=(('Markdown text', '.scpt'),
                             ('text', '.Markdown'))
                                     
    def def_gui(self):
        """Define the GUI"""
        self.main_text_input = JKTextyExtraText(self.root)
        self.main_text_input.config(font=("Helvetica", 12, "normal"))
        self.main_text_input.insert(1.0, self._ASAO_info())
        self.save_button = ttk.Button(self.root, text='Save', command=lambda: self._save())
        self.open_button = ttk.Button(self.root, text='Open', command=lambda: self._open())
        self.quit_button = ttk.Button(self.root, text='Quit', command=lambda: self._quit())
        self.settings_button = ttk.Button(self.root, text='Settings', command=lambda: self._settings())
        self.settings_button = ttk.Button(self.root, text='Settings', command=lambda: self._settings())
        self.font_frame = ttk.Labelframe(self.root, text='Font Options')
        self.font_combo = ttk.Combobox(self.font_frame, values=font.families())
        self.font_button = ttk.Button(self.font_frame, text='Change Font', command=lambda: self._change_font())
        try:
            self.font_size = ttk.Spinbox(self.font_frame, from_=1, to=100)
        except:
            # Older tkinter version
            self.font_size = tk.Spinbox(self.font_frame, from_=1, to=100)
            mbox.showwarning('Warning', 'You are using an older version of Tkinter. It is suggested that you update Tkinter, but if you don\'t feel like it, you can continue using Texty, just some of the features may not work right.', parent=self.root)
        self.font_opt = ttk.Combobox(self.font_frame, values=('normal', 'bold', 'italic', 'bold italic'))
        self.previewer_button = ttk.Button(self.root, text='Markdown Previewer - Alpha', command=lambda: self.preview())
        
    def grid_gui(self):
        """Grid the GUI"""
        self.save_button.grid(row=1, column=0)
        self.open_button.grid(row=1, column=1)
        self.quit_button.grid(row=1, column=2)
        self.main_text_input.grid(row=2, column=0, columnspan=6, rowspan=10)
        self.settings_button.grid(row=1, column=3)
        self.font_frame.grid(row=1, column=7, rowspan=3)
        self.font_combo.grid(row=1, column=0)
        self.font_button.grid(row=4, column=0)
        self.font_size.grid(row=2, column=0)
        self.font_opt.grid(row=3, column=0)
        self.previewer_button.grid(row=4, column=7)
        
    ###########################
    # Definitions for def_gui #
    ###########################

    def _ASAO_info(self):
        """Return Markdown info"""
        info="JK Texty Markdown Add-On\nVersion: 1.0.0-alpha\nAuthor:  Jackkillian\nLicense: MIT License\nHave fun!\n(you can type in this box)"
        
        return info
            
    def _settings(self):
        """Launch Markdown Settings"""
        self._Markdown_settings()
    
    def _save(self):
        """Save a file"""
        path = fd.asksaveasfilename(title='Save as', parent=self.root, filetypes=self.save_filetypes)
        
        try:
            file = open(path, mode='w')
            file.write(self.main_text_input.get(1.0, tk.END))
            file.close()
            self.root.title('Markdown | ' + path)
        except:
            mbox.showerror('Error Saving File', 'There was an error saving your file. Please try a different directory.', parent=self.root)

    def _open(self):
        """Open a file"""
        path = fd.askopenfilename(title='Please select a file to open', parent=self.root, filetypes=self.open_filetypes)

        try:
            file = open(path, mode='r')
            self.main_text_input.delete(1.0, tk.END)
            self.main_text_input.insert(1.0, file.read())
            file.close()
            self.root.title('Markdown | '+ path)
        except:
            mbox.showerror('Error Opening File', 'There was an error opening your file. Please make sure you selected a file, not a folder.', parent=self.root)
        
    def _quit(self):
        """Quit Markdown"""
        self.root.quit()
        self.root.destroy()

    def save_changes(self):
        """Save Markdown Settings Changes"""
        self.root_theme.theme_use(self.tc.get())
        self.set_root.quit()
        self.set_root.destroy()

    def _Markdown_settings(self):
        """Markdown Settings"""
        self.set_root = tk.Tk()
        self.set_root.title('Markdown | Settings')
        self.sr_theme = ttk.Style(self.set_root)
        self.sr_theme.theme_use(self.root_theme.theme_use())
        os_values = ['clam', 'classic', 'default', 'alt']
        os_values.sort()
        win_values = ['clam', 'classic', 'default', 'alt', 'xpnative', 'winnative']
        win_values.sort()
        linux_values = ['clam', 'classic', 'default', 'alt']
        linux_values.sort()
        mac_values = ['clam', 'classic', 'default', 'alt', 'aqua']
        mac_values.sort()
            
        # Do some O.S. checking here
        if sys.platform == 'darwin':
            # mac OS
            self.tc = ttk.Combobox(self.set_root, values=mac_values)
        elif sys.platform == 'linux':
            # Linux
            self.tc = ttk.Combobox(self.set_root, values=linux_values)
        elif sys.platform == 'win32':
            # Windows
            self.tc = ttk.Combobox(self.set_root, values=win_values.sort())
        else:
            # O.S. not recognized
            self.tc = ttk.Combobox(self.set_root, values=os_values)

        self.tc_l = ttk.Label(self.set_root, text='App Theme: ')
        self.tc_l.pack()
        self.tc.pack()
        self.s_b = ttk.Button(self.set_root, text='Save Changes', command=lambda: self.save_changes())
        self.s_b.pack()

    def _highlight_keywords(self, event):
        """Highlight keywords"""
        # There is no highlighting or changing. It is to hard. After all, there is a Markdown preveiwer.
        pass

    def _change_font(self):
        """Change the font"""
        if self.font_size.get() == '':
            self.font_size.set(12)
        self.main_text_input.config(font=(self.font_combo.get(), self.font_size.get(), self.font_opt.get()))

    def preview(self):
        data = self.main_text_input.get(1.0, 'end')
        Markdown_previewer(data, self.font_combo.get(), self.font_size.get())

class Markdown_previewer():
    """Preview the Markdown code (data)"""
    """Made by Jack Freund"""
    """Version: 1.0.0-alpha"""
    
    def __init__(self, data, font, font_size):
        """Preview the Markdown code (data)"""
        if font_size == '':
            font_size = 12
        ###
        self.root = tk.Tk()
        self.root.title('Markdown | Previewer')
        self.root_theme = ttk.Style(self.root)
        self.root_theme.theme_use('clam')
        ###
        lines = data.split('\n')
        for line in lines:
            if line.startswith('# '):
                text = line[2:]
                ttk.Label(self.root, text=text, font=(font, int(font_size)+10, 'normal')).pack()
            elif line.startswith('## '):
                text = line[3:]
                ttk.Label(self.root, text=text, font=(font, int(font_size)+8, 'normal')).pack()
            elif line.startswith('### '):
                text = line[4:]
                ttk.Label(self.root, text=text, font=(font, int(font_size)+6, 'normal')).pack()
            elif line.startswith('#### '):
                text = line[5:]
                ttk.Label(self.root, text=text, font=(font, int(font_size)+4, 'normal')).pack()
            elif line.startswith('##### '):
                text = line[6:]
                ttk.Label(self.root, text=text, font=(font, int(font_size)+2, 'normal')).pack()
            elif line.startswith('###### '):
                text = line[7:]
                ttk.Label(self.root, text=text, font=(font, int(font_size)+0, 'normal')).pack()
            elif line.startswith('_') or line.startswith('*'):
                text = line
                ttk.Label(self.root, text=text, font=(font, int(font_size)+0, 'italic')).pack()
            elif line.startswith('__') or line.startswith('**'):
                text = line
                ttk.Label(self.root, text=text, font=(font, int(font_size)+0, 'bold')).pack()
            else:
                text = line
                ttk.Label(self.root, text=text, font=(font, int(font_size), 'normal')).pack()
                
        ###
        self.root.mainloop()
        
def main():
    Markdown()
