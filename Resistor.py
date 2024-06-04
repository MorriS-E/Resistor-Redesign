from tkinter import *
from tkinter import ttk
def main(tab):
    var_1 = IntVar()
    var_2 = IntVar()
    var_3 = IntVar()

    checkbox_frame = Frame(tab)
    checkbox_frame.grid(row=-0, column=0, sticky=W)

    def checked(var, check, frame, check_list):
        if var.get() == 1:
            if str(check['state']) == 'normal':
                check['state'] = ACTIVE
                for c in check_list:
                    c['state'] = DISABLED
                frame.grid(row=1, column=0)
        elif var.get() == 0:
            if str(check['state']) == 'active':
                check['state'] = NORMAL
                for c in check_list:
                    c['state'] = NORMAL
                frame.grid_forget()

    def create_stringVar(color='black'):
        string_var = StringVar()
        string_var.set(color)
        return string_var

    frame1 = Frame(tab)
    frame2 = Frame(tab)
    frame3 = Frame(tab)

    check_buttons = [
        ttk.Checkbutton(checkbox_frame, text='3 Bands', onvalue=1, offvalue=0, variable=var_1,
                        command=lambda: checked(var_1, check1, frame1, [check2, check3])),
        ttk.Checkbutton(checkbox_frame, text='4 Bands', onvalue=1, offvalue=0, variable=var_2,
                        command=lambda: checked(var_2, check2, frame2, [check1, check3])),
        ttk.Checkbutton(checkbox_frame, text='5 Bands', onvalue=1, offvalue=0, variable=var_3,
                        command=lambda: checked(var_3, check3, frame3, [check1, check2]))]
    [check1, check2, check3] = check_buttons

    check1.grid(row=0, column=0)
    check2.grid(row=0, column=1)
    check3.grid(row=0, column=2)

    style = ttk.Style(tab)
    style.configure('TCheckbutton', font=('MS Serif', 15))

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

    stringVar_set1 = [
        create_stringVar(),
        create_stringVar(),
        create_stringVar()
    ]
    [band3_1, band3_2, band3_multi] = stringVar_set1

    stringVar_set2 = [
        create_stringVar(),
        create_stringVar(),
        create_stringVar(),
        create_stringVar('brown')
    ]
    [band4_1, band4_2, band4_multi, band4_tolerance] = stringVar_set2

    stringVar_set3 = [
        create_stringVar(),
        create_stringVar(),
        create_stringVar(),
        create_stringVar(),
        create_stringVar('brown')
    ]
    [band5_1, band5_2, band5_3, band5_multi, band5_tolerance] = stringVar_set3

    def menu_set(frame, click, c, menu):
        drop = ttk.Combobox(frame, textvariable=click, width=10, height=15)
        drop.bind('<<ComboboxSelected>>', lambda e: frame.focus())
        drop['values'] = list(menu.keys())
        drop.grid(row=0, column=c, sticky=W)
        return drop

    three_bands = [menu_set(frame1, band3_1, 0, options),
                   menu_set(frame1, band3_2, 1, options),
                   menu_set(frame1, band3_multi, 2, multipliers)]
    [drop1_1, drop2_1, drop3_1] = three_bands

    four_bands = [menu_set(frame2, band4_1, 0, options),
                  menu_set(frame2, band4_2, 1, options),
                  menu_set(frame2, band4_multi, 2, multipliers),
                  menu_set(frame2, band4_tolerance, 3, tolerances)]
    [drop1_2, drop2_2, drop3_2, drop4_2] = four_bands

    five_bands = [menu_set(frame3, band5_1, 0, options),
                  menu_set(frame3, band5_2, 1, options),
                  menu_set(frame3, band5_3, 2, options),
                  menu_set(frame3, band5_multi, 3, multipliers),
                  menu_set(frame3, band5_tolerance, 4, tolerances)]
    [drop1_3, drop2_3, drop3_3, drop4_3, drop5_3] = five_bands

    frame1_result_label = Label(frame1)
    frame2_result_label = Label(frame2)
    frame3_result_label = Label(frame3)

    def threeBands_calc():
        first = ''
        second = ''
        for k_op, v_op in options.items():
            if band3_1.get() == k_op:
                first = v_op
            if band3_2.get() == k_op:
                second = v_op
        result = float(first + second)

        for k_multi, v_multi in multipliers.items():
            if band3_multi.get() == k_multi:
                result = result * v_multi
        frame1_result_label.config(text=f'{result:.2f} ohms (Ω)', font=('MS Sans', 12))
        frame1_result_label.grid(row=3, column=0, columnspan=3)

    def fourBands_calc():
        first = ''
        second = ''
        tol = 0
        for k_op, v_op in options.items():
            if band4_1.get() == k_op:
                first = v_op
            if band4_2.get() == k_op:
                second = v_op
        result = float(first + second)

        for k_multi, v_multi in multipliers.items():
            if band4_multi.get() == k_multi:
                result = result * v_multi

        for k_tol, v_tol in tolerances.items():
            if band4_tolerance.get() == k_tol:
                tol = v_tol
        frame2_result_label.config(text=f'{result:.2f} ohms (Ω) ±{tol}', font=('MS Sans', 12))
        frame2_result_label.grid(row=3, column=0, columnspan=4)

    def fiveBands_calc():
        first = ''
        second = ''
        third = ''
        tol = 0
        for k_op, v_op in options.items():
            if band5_1.get() == k_op:
                first = v_op
            if band5_2.get() == k_op:
                second = v_op
            if band5_3.get() == k_op:
                third = v_op
        result = float(first + second + third)
        for k_multi, v_multi in multipliers.items():
            if band5_multi.get() == k_multi:
                result = result * v_multi
        for k_tol, v_tol in tolerances.items():
            if band5_tolerance.get() == k_tol:
                tol = v_tol
        frame3_result_label.config(text=f'{result:.2f} ohms (Ω) ±{tol}', font=('MS Sans', 12))
        frame3_result_label.grid(row=3, column=0, columnspan=5)

    def create_calcButtons(frame, func):
        return Button(frame, text='Calculate', font=('MS Sans', 12),
                      bg='light grey', activebackground='light grey', command=func)

    create_calcButtons(frame1, threeBands_calc).grid(row=2, column=1, pady=10)
    create_calcButtons(frame2, fourBands_calc).grid(row=2, column=1, columnspan=2, pady=10)
    create_calcButtons(frame3, fiveBands_calc).grid(row=2, column=2, pady=10)

