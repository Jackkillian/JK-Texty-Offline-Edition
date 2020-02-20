"""
Name:    JK Texty
Version: 1.0.0 Offline (for John)
Author:  Jackkillian a.k.a. Jack Freund
License: MIT License
Website: https://github.com/Jackkillian/JK-Texty
O.S.:    UNIX-path operating systems
"""

"""
Whew! This was fun to code.
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mbox
from tkinter import filedialog as fd
from tkinter import font
from tkinter.scrolledtext import ScrolledText as scrolledtext
from webbrowser import open as open_url
from urllib.request import urlretrieve as download
from random import randint
import urllib
from os.path import dirname
import os
import sys
import smtplib as smtp
import socket
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

__texty_version__ = '1.0.0'

class About_Texty():

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('About Texty')
        self.credits = open('Add_Ons/credits.txt').read()
        self.license = open('Add_Ons/license.txt').read()

class Texty():
    """Run Texty"""

    def __init__(self):
        """Run Texty"""
        self.setup()
        self.def_gui('all')
        self.grid_gui()
        self.root.mainloop()

    ############################
    # Definitions for __init__ #
    ############################
    
    def setup(self):
        """Setup Texty"""
        # Setup the main window
        self.root = tk.Tk()
        self.root.title('Texty | New File')
        # Setup the theme for the main window
        self.root_theme = ttk.Style(self.root)
        self.root_theme.theme_use('clam')
        Texty.root_theme = 'clam'
        # Setup menubar
        self.menubar = tk.Menu(self.root)
        ### Texty menu
        self.Texty_menu = tk.Menu(self.menubar)
        self.Texty_menu.add_command(label="About", command=lambda:About_Texty())
        self.Texty_menu.add_command(label="Settings", command=lambda:self._Texty_settings())
        self.Texty_menu.add_command(label="Check for updates", command=lambda:self._check_for_updates())
        self.Texty_menu.add_command(label="Quit", command=lambda:self._quit())
        ### File menu
        self.file_menu = tk.Menu(self.menubar)
        self.file_menu.add_command(label="New", command=lambda:Texty())
        self.file_menu.add_command(label="Save", command=lambda:self._save())
        self.file_menu.add_command(label="Open", command=lambda:self._open())
        ### Edit menu
        self.edit_menu = tk.Menu(self.menubar)
        ### Mode menu
        self.mode_menu = tk.Menu(self.menubar)
        ### Help menu
        self.help_menu = tk.Menu(self.menubar)
        self.help_menu.add_command(label="What's new in 1.0.0", command=lambda:open_url("https://github.com/Jackkillian/JK-Texty/blob/master/Newest-Version/What's%20New.md"))
        self.help_menu.add_command(label="Texty Help", command=lambda:open_url('https://github.com/Jackkillian/JK-Texty/wiki'))
        ### Rest of menubar
        self.menubar.add_cascade(label='Texty', menu=self.Texty_menu)
        self.menubar.add_cascade(label="File", menu=self.file_menu)
        self.menubar.add_cascade(label="Edit", menu=self.edit_menu)
        self.menubar.add_cascade(label="Mode", menu=self.mode_menu)
        self.menubar.add_cascade(label="Help", menu=self.help_menu)
        self.root.config(menu=self.menubar)
        # Define needed variables
        self.Texty_version = '1.0.0'
        self.Texty_author = 'Jackkillian, a.k.a. Jack Freund'
        self.Texty_license = 'MIT License'
        self.Texty_website = 'https://sites.google.com/view/jk-texty-website/home'
        self.Texty_os = 'Source Code'
        self.toolbar_status = 'same'
        self.open_filetypes=(('All Files', '.*'),
                             ('AppleScript', '.scpt'),
                             ('C', '.c'),
                             ('C++', '.cc'),
                             ('HTML', '.html'),
                             ('JK Dashboard Extension', '.jkbdext'),
                             ('JK PyApp', '.py'),
                             ('JavaScript', '.js'),
                             ('Markdown', '.md'),
                             ('Python', '.py'),
                             ('Python GUI App', '.py'),
                             ('Plain Text', '.txt'),
                             ('Rich Text', '.rtf'),
                             ('Ruby', '.rb'))
        self.save_filetypes=(('AppleScript', '.scpt'),
                             ('C', '.c'),
                             ('C++', '.cc'),
                             ('HTML', '.html'),
                             ('JK Dashboard Extension', '.jkbdext'),
                             ('JK PyApp', '.py'),
                             ('JavaScript', '.js'),
                             ('Markdown', '.md'),
                             ('Python', '.py'),
                             ('Python GUI App', '.py'),
                             ('Plain Text', '.txt'),
                             ('Rich Text', '.rtf'),
                             ('Ruby', '.rb'))

        self.mode_list=['AppleScript',
                        'C',
                        'C++',
                        'HTML',
                        'JavaScript',
                        'JK Dashboard Extension',
                        'JK PyApp',
                        'Markdown',
                        'Python',
                        'Python GUI App',
                        'Plain Text',
                        'Rich Text',
                        'Ruby']
        
    def def_gui(self, mode):
        """Define the GUI"""
        if mode == 'all':
            self.main_text_input = scrolledtext(self.root)
            self.main_text_input.insert(1.0, self._Texty_info())
            self.save_button = ttk.Button(self.root, text='Save', command=lambda: self._save())
            self.open_button = ttk.Button(self.root, text='Open', command=lambda: self._open())
            self.quit_button = ttk.Button(self.root, text='Quit', command=lambda: self._quit())
            self.toggle_toolbar_button = ttk.Button(self.root, text='Toggle Toolbar', command=lambda: self._toggle_toolbar())
            self.mode_label = ttk.Label(self.root, text='Mode:')
            self.mode_combo = ttk.Combobox(self.root, values=self.mode_list)
            self.change_mode_button = ttk.Button(self.root, text='Launch Mode', command=lambda: self._change_mode())
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
        elif mode == 'toolbar':
            self.save_button = ttk.Button(self.root, text='Save', command=lambda: self._save())
            self.open_button = ttk.Button(self.root, text='Open', command=lambda: self._open())
            self.quit_button = ttk.Button(self.root, text='Quit', command=lambda: self._quit())
            self.toggle_toolbar_button = ttk.Button(self.root, text='Toggle Toolbar', command=lambda: self._toggle_toolbar())
            self.mode_label = ttk.Label(self.root, text='Mode:')
            self.mode_combo = ttk.Combobox(self.root, values=self.mode_list)
            self.change_mode_button = ttk.Button(self.root, text='Launch Mode', command=lambda: self._change_mode())
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
        self._words=open( "Add_Ons/wordlist.txt").read().split("\n")
        self.main_text_input.bind("<space>", self.Spellcheck)
        self.main_text_input.tag_configure("misspelled", foreground="red", underline=True)

    def grid_gui(self):
        """Grid the GUI"""
        self.save_button.grid(row=1, column=0)
        self.open_button.grid(row=1, column=1)
        self.quit_button.grid(row=1, column=2)
        self.toggle_toolbar_button.grid(row=1, column=3)
        self.main_text_input.grid(row=2, column=0, columnspan=6, rowspan=10)
        self.mode_label.grid(row=1, column=5)
        self.mode_combo.grid(row=1, column=7, columnspan=2)
        self.change_mode_button.grid(row=2, column=7)
        self.settings_button.grid(row=5, column=7)
        self.font_frame.grid(row=6, column=7)
        self.font_combo.grid(row=1, column=0)
        self.font_button.grid(row=4, column=0)
        self.font_size.grid(row=2, column=0)
        self.font_opt.grid(row=3, column=0)
        
    ###########################
    # Definitions for def_gui #
    ###########################

    def Spellcheck(self, event):
        '''Spellcheck the word preceeding the insertion point'''
        index = self.main_text_input.search(r'\s', "insert", backwards=True, regexp=True)
        if index == "":
            index ="1.0"
        else:
            index = self.main_text_input.index("%s+1c" % index)
        word = self.main_text_input.get(index, "insert")
        if word.islower() and word.isalpha():
            if word in self._words:
                self.main_text_input.tag_remove("misspelled", index, "%s+%dc" % (index, len(word)))
            else:
                self.main_text_input.tag_add("misspelled", index, "%s+%dc" % (index, len(word)))

    def _change_font(self):
        """Change the font"""
        size = self.font_size.get()
        if self.font_size.get() == '':
            size = 12
        self.main_text_input.config(font=(self.font_combo.get(), size, self.font_opt.get()))
        
    def _Texty_info(self):
        """Return Texty info"""
        info="JK Texty\nVersion: 1.0.0\nAuthor:  Jackkillian\nLicense: MIT License\nHave fun!\n(you can type in this box)"
        
        return info

    def _change_mode(self):
        """Change the Texty mode"""
        mode = self.mode_combo.get()
        # DO NOT CHANGE THE FOLLOWING LINES,
        # AS THEN YOUR ADD-ONS WILL NOT WORK.
        #-# ADD-ONS #-#
        import Add_Ons.AppleScript as AppleScript
        import Add_Ons.C as C
        import Add_Ons.CC as CC
        import Add_Ons.HTML as HTML
        import Add_Ons.JavaScript as JavaScript
        import Add_Ons.JK_Dashboard_Extension as JK_Dashboard_Extension
        import Add_Ons.JK_PyApp as JK_PyApp
        import Add_Ons.Markdown as Markdown
        import Add_Ons.Python as Python
        import Add_Ons.Python_GUI_App as Python_GUI_App
        import Add_Ons.Plain_Text as Plain_Text
        import Add_Ons.Rich_Text as Rich_Text
        import Add_Ons.Ruby as Ruby
        #-# RUN ADD-ONS #-#
        if mode == 'AppleScript':
            AppleScript.main()
        elif mode == 'C':
            C.main()
        elif mode == 'C++':
            CC.main()
        elif mode == 'HTML':
            HTML.main()
        elif mode == 'JavaScript':
            JavaScript.main()
        elif mode == 'JK Dashboard Extension':
            JK_Dashboard_Extension.main()
        elif mode == 'JK PyApp':
            JK_PyApp.main()
        elif mode == 'Markdown':
            Markdown.main()
        elif mode == 'Python':
            Python.main()
        elif mode == 'Python GUI App':
            Python_GUI_App.main()
        elif mode == 'Plain Text':
            Plain_Text.main()
        elif mode == 'Rich Text':
            Rich_Text.main()
        elif mode == 'Ruby':
            Ruby.main()
        else:
            mbox.showerror('Add-On not found', 'Please make sure the add-on you selected is intalled.', parent=self.root)
    def _toggle_toolbar(self):
        """Toggle the toolbar"""
        # I KNOW 'seperate' is mispelled
        if self.toolbar_status == 'same':
            self.ungrid_gui()
            self.redef_gui()
            self.regrid_gui()
            self.toolbar_status = 'seperate'
        elif self.toolbar_status == 'seperate':
            self.reungrid_gui()
            self.def_gui('toolbar')
            self.grid_gui()
            self.toolbar_root.destroy()
            self.toolbar_status = 'same'
            
    def _settings(self):
        """Launch Texty Settings"""
        self._Texty_settings()
    
    def _save(self):
        """Save a file"""
        path = fd.asksaveasfilename(title='Save as', parent=self.root, filetypes=self.save_filetypes)
        
        try:
            file = open(path, mode='w')
            file.write(self.main_text_input.get(1.0, tk.END))
            file.close()
            self.root.title('Texty | ' + path)
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
            self.root.title('Texty | '+ path)
        except:
            mbox.showerror('Error Opening File', 'There was an error opening your file. Please make sure you selected a file, not a folder.', parent=self.root)
        
    def _quit(self):
        """Quit Texty"""
        self.root.quit()
        self.root.destroy()
        try:
            self.toolbar_root.destroy()
            self.set_root.destroy()
        except:
            pass

    def save_changes(self):
            """Save Texty Settings Changes"""
            self.root_theme.theme_use(self.tc.get())
            Texty.root_theme = self.tc.get()
            self.set_root.quit()
            self.set_root.destroy()

    def _Texty_settings(self):
        """Texty Settings"""
        self.set_root = tk.Tk()
        self.set_root.title('Texty | Settings')
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
        self.c_l = ttk.Label(self.set_root, text='———Credits———')
        self.c_l.pack()
        self.v_l = ttk.Label(self.set_root, text='JK Texty Version: ' + self.Texty_version)
        self.v_l.pack()
        self.a_l = ttk.Label(self.set_root, text='JK Texty Author: ' + self.Texty_author)
        self.a_l.pack()
        self.l_l = ttk.Label(self.set_root, text='JK Texty License: ' + self.Texty_license)
        self.l_l.pack()
        self.w_l = ttk.Label(self.set_root, text='JK Texty Website: ')
        self.w_l.pack()
        self.w_b = ttk.Button(self.set_root, text='JK Texty Website', command=lambda: open_url(self.Texty_website))
        self.w_b.pack()
        self.o_l = ttk.Label(self.set_root, text='JK Texty O.S. version: ' + self.Texty_os)
        self.o_l.pack()
        self.s_b = ttk.Button(self.set_root, text='Save Changes', command=lambda: self.save_changes())
        self.s_b.pack()
            
    ###################################
    # Definitions for _toggle_toolbar #
    ###################################

    def redef_gui(self):
        self.toolbar_root = tk.Tk()
        self.toolbar_root.title('Texty Toolbar')
        self.toolbar_theme = ttk.Style(self.toolbar_root)
        self.toolbar_theme.theme_use('clam')
        self.save_button = ttk.Button(self.toolbar_root, text='Save', command=lambda: self._save())
        self.open_button = ttk.Button(self.toolbar_root, text='Open', command=lambda: self._open())
        self.quit_button = ttk.Button(self.toolbar_root, text='Quit', command=lambda: self._quit())
        self.toggle_toolbar_button = ttk.Button(self.toolbar_root, text='Toggle Toolbar', command=lambda: self._toggle_toolbar())
        self.mode_label = ttk.Label(self.toolbar_root, text='Mode:')
        self.mode_combo = ttk.Combobox(self.toolbar_root, values=self.mode_list)
        self.change_mode_button = ttk.Button(self.toolbar_root, text='Launch Mode', command=lambda: self._change_mode())
        self.settings_button = ttk.Button(self.toolbar_root, text='Settings', command=lambda: self._settings())
        self.font_frame = ttk.Labelframe(self.toolbar_root, text='Font Options')
        self.font_combo = ttk.Combobox(self.font_frame, values=font.families())
        self.font_button = ttk.Button(self.font_frame, text='Change Font', command=lambda: self._change_font())
        try:
            self.font_size = ttk.Spinbox(self.font_frame, from_=1, to=100)
        except:
            # Older tkinter version
            self.font_size = tk.Spinbox(self.font_frame, from_=1, to=100)
            mbox.showwarning('Warning', 'You are using an older version of Tkinter. It is suggested that you update Tkinter, but if you don\'t feel like it, you can continue using Texty, just some of the features may not work right.', parent=self.root)
        self.font_opt = ttk.Combobox(self.font_frame, values=('normal', 'bold', 'italic', 'bold italic'))

    def regrid_gui(self):
        self.save_button.grid(row=1, column=0)
        self.open_button.grid(row=2, column=0)
        self.toggle_toolbar_button.grid(row=3, column=0)
        self.quit_button.grid(row=5, column=0)
        self.mode_label.grid(row=6, column=0)
        self.mode_combo.grid(row=7, column=0)
        self.change_mode_button.grid(row=8, column=0)
        self.settings_button.grid(row=11, column=0)
        self.font_frame.grid(row=12, column=0)
    
    def reungrid_gui(self):
        self.save_button.grid_forget()
        self.open_button.grid_forget()
        self.toggle_toolbar_button.grid_forget()
        self.quit_button.grid_forget()
        self.mode_label.grid_forget()
        self.mode_combo.grid_forget()
        self.change_mode_button.grid_forget()
        self.settings_button.grid_forget()
        self.font_frame.grid_forget()

    def ungrid_gui(self):
        self.save_button.grid_forget()
        self.open_button.grid_forget()
        self.toggle_toolbar_button.grid_forget()
        self.quit_button.grid_forget()
        self.mode_label.grid_forget()
        self.mode_combo.grid_forget()
        self.change_mode_button.grid_forget()
        self.settings_button.grid_forget()
        self.font_frame.grid_forget()
                
if __name__ == '__main__':
    Texty()
