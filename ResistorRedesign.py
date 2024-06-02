import customtkinter as ctk
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.minsize(310, 175)
        CheckBoxFrame(self)
        self.mainloop()
class CheckBoxFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.grid(row=0, column=0, sticky='w', padx=160, pady=10)
        CheckBox(self, '3 bands', ThreeBandFrame(parent), 0)
        CheckBox(self, '4 bands', FourBandFrame(parent), 1)
        CheckBox(self, '5 bands', FiveBandFrame(parent), 2)
class ThreeBandFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.vars = [
            ctk.StringVar(value='black'),
            ctk.StringVar(value='black'),
            ctk.StringVar(value='black')
        ]

        Label(self, '1st Band').grid(row=0, column=0, padx=20)
        OptionMenu(self, options.keys(), self.vars[0]).grid(row=1, column=0)

        Label(self, '2nd Band').grid(row=0, column=1, padx=20)
        OptionMenu(self, options.keys(), self.vars[1]).grid(row=1, column=1)

        Label(self, 'Multiplier').grid(row=0, column=2, padx=20)
        OptionMenu(self, multipliers.keys(), self.vars[2]).grid(row=1, column=2)

        Button(self, self.calculate).grid(row=2, column=1, pady=20)

        self.res_label = Label(self, '')

    '''takes the value of 'band' dropdown options,
    and concatenates them. the result is then multiplied
    with 'multiplier' dropdown value'''
    def calculate(self):
        first = ''
        second = ''
        for key, value in options.items():
            if self.vars[0].get() == key:
                first = value
            if self.vars[1].get() == key:
                second = value
        result = float(first + second)

        for multi_key, multi_val in multipliers.items():
            if self.vars[2].get() == multi_key:
                result *= multi_val

        self.res_label.configure(text=f'{result:.2f} ohms (Ω)')
        self.res_label.grid(row=3, column=0, columnspan=3)
class FourBandFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.vars = [
            ctk.StringVar(value='black'),
            ctk.StringVar(value='black'),
            ctk.StringVar(value='black'),
            ctk.StringVar(value='brown'),
        ]

        Label(self, '1st Band').grid(row=0, column=0, padx=20)
        OptionMenu(self, options.keys(), self.vars[0]).grid(row=1, column=0)

        Label(self, '2nd Band').grid(row=0, column=1, padx=20)
        OptionMenu(self, options.keys(), self.vars[1]).grid(row=1, column=1)

        Label(self, 'Multiplier').grid(row=0, column=2, padx=20)
        OptionMenu(self, multipliers.keys(), self.vars[2]).grid(row=1, column=2)

        Label(self, 'Tolerance').grid(row=0, column=3, padx=20)
        OptionMenu(self, tolerances.keys(), self.vars[3]).grid(row=1, column=3)

        Button(self, self.calculate).grid(row=2, column=1, columnspan=2, pady=20)

        self.res_label = Label(self, '')

    def calculate(self):
        first = ''
        second = ''
        tol = 0
        for k_op, v_op in options.items():
            if self.vars[0].get() == k_op:
                first = v_op
            if self.vars[1].get() == k_op:
                second = v_op
        result = float(first + second)

        for k_multi, v_multi in multipliers.items():
            if self.vars[2].get() == k_multi:
                result = result * v_multi

        for k_tol, v_tol in tolerances.items():
            if self.vars[3].get() == k_tol:
                tol = v_tol

        self.res_label.configure(text=f'{result:.2f} ohms (Ω) ±{tol}')
        self.res_label.grid(row=3, column=0, columnspan=4)
class FiveBandFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.vars = [
            ctk.StringVar(value='black'),
            ctk.StringVar(value='black'),
            ctk.StringVar(value='black'),
            ctk.StringVar(value='black'),
            ctk.StringVar(value='brown'),
        ]
        Label(self, '1st Band').grid(row=0, column=0, padx=20)
        OptionMenu(self, options.keys(), self.vars[0]).grid(row=1, column=0)

        Label(self, '2nd Band').grid(row=0, column=1, padx=20)
        OptionMenu(self, options.keys(), self.vars[1]).grid(row=1, column=1)

        Label(self, '3rd Band').grid(row=0, column=2, padx=20)
        OptionMenu(self, options.keys(), self.vars[2]).grid(row=1, column=2)

        Label(self, 'Multiplier').grid(row=0, column=3, padx=20)
        OptionMenu(self, multipliers.keys(), self.vars[3]).grid(row=1, column=3)

        Label(self, 'Tolerance').grid(row=0, column=4, padx=20)
        OptionMenu(self, tolerances.keys(), self.vars[4]).grid(row=1, column=4)

        self.button = Button(self, self.calculate).grid(row=2, column=2, pady=20)

        self.res_label = Label(self, '')

    def calculate(self):
        first = ''
        second = ''
        third = ''
        tol = 0
        for k_op, v_op in options.items():
            if self.vars[0].get() == k_op:
                first = v_op
            if self.vars[1].get() == k_op:
                second = v_op
            if self.vars[2].get() == k_op:
                third = v_op
        result = float(first + second + third)

        for k_multi, v_multi in multipliers.items():
            if self.vars[3].get() == k_multi:
                result = result * v_multi
        for k_tol, v_tol in tolerances.items():
            if self.vars[4].get() == k_tol:
                tol = v_tol

        self.res_label.configure(text=f'{result:.2f} ohms (Ω) ±{tol}')
        self.res_label.grid(row=3, column=0, columnspan=5)
class CheckBox(ctk.CTkCheckBox):
    def __init__(self, parent, text, frame, c):
        super().__init__(parent)
        self.parent = parent
        self.int_var = ctk.IntVar()
        self.frame = frame
        self._onvalue = 1
        self._offvalue = 0
        self.configure(text=text, variable=self.int_var, command=self.checked, font=('Sans Script', 20))
        self.grid(row=1, column=c, padx=5)

    ''' this function checks if a checkbox is ticked.
    if yes, then the other checkboxes set to disabled, 
    else, all checkboxes are set to normal '''
    def checked(self):
        if self.int_var.get() == 1:
            for i in self.parent.winfo_children():
                if i != self:
                    i._state = 'disabled'
            self.frame.grid(row=1, column=0)
        elif self.int_var.get() == 0:
            for i in self.parent.winfo_children():
                i._state = 'normal'
            self.frame.grid_forget()
class OptionMenu(ctk.CTkOptionMenu):
    def __init__(self, parent, li, var):
        super().__init__(parent)
        self.var = var
        self.configure(width=80, values=list(li), variable=self.var, font=('Sans Script', 20),
                       dropdown_font=('Sans Script', 20))
class Button(ctk.CTkButton):
    def __init__(self, parent, cmd):
        super().__init__(parent)
        self.configure(text='calculate', width=80, command=cmd, font=('Sans Script', 20))
class Label(ctk.CTkLabel):
    def __init__(self, parent, text):
        super().__init__(parent)
        self.configure(text=text, font=('Sans Script', 20))
if __name__ == '__main__':
    options = {
        'black': '0',
        'brown': '1',
        'red': '2',
        'orange': '3',
        'yellow': '4',
        'green': '5',
        'blue': '6',
        'violet': '7',
        'grey': '8',
        'white': '9',
        'gold': '',
        'silver': '',
    }

    multipliers = {
        'black': 1,
        'brown': 10,
        'red': 100,
        'orange': 1000,
        'yellow': 10000,
        'green': 100000,
        'blue': 1000000,
        'violet': 10000000,
        'grey': 100000000,
        'white': 1000000000,
        'gold': 0.1,
        'silver': 0.01,
    }

    tolerances = {
        'brown': 1,
        'gold': 5,
        'silver': 10
    }

    App()
