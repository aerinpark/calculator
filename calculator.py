from tkinter import *


class Calculator:
	
	def __init__(self):
		# Set up the basic UI
		# Window
		self.window = Tk()
		self.window.title("Calculator")
		self.window.resizable(width=False, height=False)
		self.window.config(padx=10, pady=10)
		
		# Screen
		self.screen = Label(text="Screen", width=25, height=5, borderwidth=1, relief="solid", padx=25)
		self.screen.grid(row=0, column=0, columnspan=7, pady=10)
		
		# Buttons (30 buttons)
		self.calc_buttons = [
			"off", "sin", "cos", "tan", "del",
			"C", "x^y", "sqrt(x)", "1/x", "+",
			"n!", "7", "8", "9", "-",
			"log", "4", "5", "6", "x",
			"pi", "1", "2", "3", "/",
			"e", ".", "0", "Ans", "="
		]
		
		index = 0
		for new_button in self.calc_buttons:
			button = Button(text=new_button, width=5)
			button.grid(row=int(index / 5)+1, column=int(index % 5)+1)
			index += 1
		
		self.window.mainloop()
