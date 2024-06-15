from tkinter import *
import math

class Calculator:

    def __init__(self):
        # Set up the basic UI
        # Window
        self.window = Tk()
        self.window.title("Calculator")
        self.window.resizable(width=False, height=False)
        self.window.config(padx=10, pady=10)

        # Screen
        self.screen = Label(text="0", width=25, height=5, borderwidth=1, relief="solid", padx=25)
        self.screen.grid(row=0, column=0, columnspan=7, pady=10)

        # Buttons (30 buttons)
        self.calc_button_names = [
            "off", "sin", "cos", "tan", "del",
            "C", "x^y", "sqrt", "1/x", "+",
            "n!", "7", "8", "9", "-",
            "log", "4", "5", "6", "x",
            "π", "1", "2", "3", "/",
            "e", ".", "0", "ans", "="
        ]

        self.buttons = []

        self.op = ""
        self.input = ""
        self.answer = 0

        # Buttons
        # First row
        Button(text="off", width=5, command=lambda: self.button_function("off")).grid(row=1, column=0)
        Button(text="sin", width=5, command=lambda: self.button_function("sin")).grid(row=1, column=1)
        Button(text="cos", width=5, command=lambda: self.button_function("cos")).grid(row=1, column=2)
        Button(text="tan", width=5, command=lambda: self.button_function("tan")).grid(row=1, column=3)
        Button(text="del", width=5, command=lambda: self.button_function("del")).grid(row=1, column=4)

        # Second row
        Button(text="C", width=5, command=lambda: self.button_function("C")).grid(row=2, column=0)
        Button(text="x^y", width=5, command=lambda: self.button_function("x^y")).grid(row=2, column=1)
        Button(text="√", width=5, command=lambda: self.button_function("sqrt")).grid(row=2, column=2)
        Button(text="1/x", width=5, command=lambda: self.button_function("1/x")).grid(row=2, column=3)
        Button(text="+", width=5, command=lambda: self.button_function("+")).grid(row=2, column=4)

        # Third row
        Button(text="n!", width=5, command=lambda: self.button_function("n!")).grid(row=3, column=0)
        Button(text="7", width=5, command=lambda: self.button_function("7")).grid(row=3, column=1)
        Button(text="8", width=5, command=lambda: self.button_function("8")).grid(row=3, column=2)
        Button(text="9", width=5, command=lambda: self.button_function("9")).grid(row=3, column=3)
        Button(text="-", width=5, command=lambda: self.button_function("-")).grid(row=3, column=4)

        # Fourth row
        Button(text="log", width=5, command=lambda: self.button_function("log")).grid(row=4, column=0)
        Button(text="4", width=5, command=lambda: self.button_function("4")).grid(row=4, column=1)
        Button(text="5", width=5, command=lambda: self.button_function("5")).grid(row=4, column=2)
        Button(text="6", width=5, command=lambda: self.button_function("6")).grid(row=4, column=3)
        Button(text="x", width=5, command=lambda: self.button_function("x")).grid(row=4, column=4)

        # Fifth row
        Button(text="π", width=5, command=lambda: self.button_function("π")).grid(row=5, column=0)
        Button(text="1", width=5, command=lambda: self.button_function("1")).grid(row=5, column=1)
        Button(text="2", width=5, command=lambda: self.button_function("2")).grid(row=5, column=2)
        Button(text="3", width=5, command=lambda: self.button_function("3")).grid(row=5, column=3)
        Button(text="/", width=5, command=lambda: self.button_function("/")).grid(row=5, column=4)

        # Sixth row
        Button(text="e", width=5, command=lambda: self.button_function("e")).grid(row=6, column=0)
        Button(text=".", width=5, command=lambda: self.button_function(".")).grid(row=6, column=1)
        Button(text="0", width=5, command=lambda: self.button_function("0")).grid(row=6, column=2)
        Button(text="ans", width=5, command=lambda: self.button_function("ans")).grid(row=6, column=3)
        Button(text="=", width=5, command=lambda: self.button_function("=")).grid(row=6, column=4)

        self.window.mainloop()

    def button_function(self, button: str):
        if button.isdigit():
            self.input += button
            self.screen.config(text=self.input)
        elif button == "off":
            exit()
        elif button == "del":
            if self.input != "" and len(self.input) != 1:
                self.input = self.input[:-1]
                self.screen.config(text=self.input)
            else:
                self.input = ""
                self.screen.config(text="0")
        elif button == "C":
            self.input = ""
            self.op = ""
            self.answer = 0
            self.screen.config(text="0")
        elif button == ".":
            self.input += button
            self.screen.config(text=self.input)
        elif button == "ans":
            self.input = ""
            self.screen.config(text=self.answer)
        elif button == "e":
            self.input = math.e
            self.screen.config(text=self.input)
        elif button == "π":
            self.input = math.pi
            self.screen.config(text=self.input)
        elif button != "=":
            self.op = button
            if "." in self.input:
                self.answer = float(self.input)
            elif self.input != "":
                self.answer = int(self.input)
            self.input = ""
        else:
            self.calculate()

    def calculate(self):
        pass