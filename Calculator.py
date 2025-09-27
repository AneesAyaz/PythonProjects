'''def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def calculator():
    print("Select operation:")
    print("Add")
    print("Subtract")
    print("Multiply")
    print("Divide")

    while True:
        choice = input("Enter choice(+,-,*,/): ")

        if choice in ['+', '-', '*', '/']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '+':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '-':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '*':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '/':
                print(f"{num1} / {num2} = {divide(num1, num2)}")

            next_calculation = input("Do you want to perform another calculation? (yes/no): ")
            if next_calculation.lower() != 'yes':
                break
        else:
            print("Invalid Input")

if __name__ == "__main__":
    calculator()'''

import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.expression = ""

        # Create a text entry widget to display the expression
        self.display = tk.Entry(root, font=("Arial", 20), borderwidth=5, relief="sunken", justify='right')
        self.display.grid(row=0, column=0, columnspan=4)

        # Define buttons
        buttons = [
            '7', '8', '9', '/', 
            '4', '5', '6', '*', 
            '1', '2', '3', '-', 
            '0', '.', '=', '+', 
            'C'
        ]

        # Create and position the buttons
        row = 1
        col = 0
        for button in buttons:
            tk.Button(root, text=button, font=("Arial", 20), width=5, height=2, command=lambda b=button: self.click(b)).grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def click(self, button):
        if button == "=":
            try:
                self.expression = str(eval(self.expression))
            except:
                self.expression = "Error"
        elif button == "C":
            self.expression = ""
        else:
            self.expression += str(button)
        
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
