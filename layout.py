import tkinter as tk
import tkinter.font as tkFont

class TkBtn(tk.Button):
    def __init__(self, root, text, x, y, width, height, command):
        super().__init__(root)
        self.btn_ft = tkFont.Font(family='Times',size=10)
        self["bg"] = "#f0f0f0"
        self["font"] = self.btn_ft
        self["fg"] = "#000000"
        self["justify"] = "center"
        self["text"] = text
        self.place(x=x, y=y, width=width, height=height)
        self["command"] = command

class TkLabel(tk.Label):
    def __init__(self, root, text, x, y, width, height):
        super().__init__(root)
        self.lbl_ft = tkFont.Font(family='Times',size=10)
        self["font"] = self.lbl_ft
        self["fg"] = "#5fb878"
        self["justify"] = "left"
        self["text"] = text
        self.place(x=x, y=y, width=width, height=height)

class TkLabelFrame(tk.LabelFrame):
    def __init__(self, root, text, x, y, width, height):
        super().__init__(root)
        self["text"] = text
        self.place(x=x, y=y, width=width, height=height)

class TkListbox(tk.Listbox):
    def __init__(self, root, x, y, width, height):
        super().__init__(root)
        self.btn_ft = tkFont.Font(family='Times',size=10)
        self["borderwidth"] = "1px"
        self["font"] = self.btn_ft
        self["fg"] = "#333333"
        self["justify"] = "center"
        self.place(x=x, y=y, width=width, height=height)