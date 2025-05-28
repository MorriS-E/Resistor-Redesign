from tkinter import *


class Labels:
    def __init__(self, parent):
        self.parent = parent
        self.label_text = [
            'first',
            'second',
            'third',
            'multiplier',
        ]

        self.ohms_label = Label(self.parent, text="")
        self.tolerance_label = Label(self.parent, text="")

        self.create_static_label()

    def place_widget(self, _dict: dict):
        for k, v in _dict.items():
            getattr(self, k).grid(**v)

    def create_static_label(self):
        for i, text in enumerate(self.label_text):
            Label(self.parent, text=text).grid(row=i, column=0, padx=5, pady=5)


class Dropdowns:
    def __init__(self, parent):
        self.parent = parent
        self.colours = {
            'black': 0,
            'brown': 1,
            'red': 2,
            'orange': 3,
            'yellow': 4,
            'green': 5,
            'blue': 6,
            'violet': 7,
            'grey': 8,
            'white': 9,
        }
        self.multipliers = {
            'black': 0,
            'brown': 10,
            'red': 100,
            'orange': 1000,
            'yellow': 10000,
            'green': 100000,
            'blue': 1000000,
            'gold': 0.1,
            'silver': 0.01
        }
        self.string_vars = {
            "dropdown_value_1": StringVar(),
            "dropdown_value_2": StringVar(),
            "dropdown_value_3": StringVar(),
            "dropdown_value_4": StringVar(),
        }

        for value in self.string_vars.values():
            value.set('black')
        self.stringVar_values = list(self.string_vars.values())

        self.dropdowns = {
            "dropdown_1": OptionMenu(self.parent, self.stringVar_values[0], *self.colours.keys()),
            "dropdown_2": OptionMenu(self.parent, self.stringVar_values[1], *self.colours.keys()),
            "dropdown_3": OptionMenu(self.parent, self.stringVar_values[2], *self.colours.keys()),
            "dropdown_4": OptionMenu(self.parent, self.stringVar_values[3], *self.multipliers.keys())
        }

    def place_widget(self, _dict: dict):
        for k, v in _dict.items():
            self.dropdowns[k].grid(**v)
            self.dropdowns[k].config(width=5)

    @property
    def first_value(self):
        return self.colours[self.stringVar_values[0].get()]

    @property
    def second_value(self):
        return self.colours[self.stringVar_values[1].get()]

    @property
    def third_value(self):
        return self.colours[self.stringVar_values[2].get()]

    @property
    def fourth_value(self):
        return self.multipliers[self.stringVar_values[3].get()]


class Controls:
    def __init__(self, parent, command):
        self.parent = parent
        self.calculate = Button(self.parent, text="calculate", command=command)
        self.calculate.grid(row=7, column=0, columnspan=3)


class RadioButtons:
    def __init__(self, parent):
        self.parent = parent
        self.radio_s_var = StringVar(self.parent, "1")

        self.radio_values = {
            "1": 1,
            "5": 5,
            "10": 10,
        }

        self.radio_buttons = {
            "1": Radiobutton(self.parent, text="1", variable=self.radio_s_var, value=1),
            "5": Radiobutton(self.parent, text="5", variable=self.radio_s_var, value=5),
            "10": Radiobutton(self.parent, text="10", variable=self.radio_s_var, value=10),
        }

    def place_widget(self, _dict: dict):
        for key, value in _dict.items():
            self.radio_buttons[key].grid(**value)

    @property
    def radio_value(self):
        return self.radio_values[self.radio_s_var.get()]


class App(Tk):
    def __init__(self):
        super().__init__()
        drop_dict = {
            "dropdown_1": {"row": 0, "column": 1},
            "dropdown_2": {"row": 1, "column": 1},
            "dropdown_3": {"row": 2, "column": 1},
            "dropdown_4": {"row": 3, "column": 1},
        }
        label_dict = {
            "ohms_label": {"row": 5, "column": 1},
            "tolerance_label": {"row": 6, "column": 1},
        }
        radio_dict = {
            "1": {"row": 4, "column": 0},
            "5": {"row": 4, "column": 1},
            "10": {"row": 4, "column": 2},
        }

        self.label = Labels(self)
        self.dropdown = Dropdowns(self)
        self.control = Controls(self, self.calculate)
        self.radio = RadioButtons(self)

        self.dropdown.place_widget(drop_dict)
        self.label.place_widget(label_dict)
        self.radio.place_widget(radio_dict)

    def calculate(self):
        first = self.dropdown.first_value
        second = self.dropdown.second_value
        third = self.dropdown.third_value
        fourth = self.dropdown.fourth_value
        res = (first + second + third) * fourth
        radio_value = float(self.radio.radio_value)
        tolerance = res * radio_value / 100

        self.label.ohms_label.config(text=f'{res:.2f} ohms (Ω)')
        self.label.tolerance_label.config(text=f'±{tolerance}')


if __name__ == '__main__':
    app = App()
    app.mainloop()
