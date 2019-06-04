class Calculator:

    result = 0

    def Add(self, a, b):
        self.result = a + b
        print("The sum is : ", self.result)

    def Sub(self, a, b):
        self.result = a - b
        print("The Sub is : ", self.result)

    def Mul(self, a, b):
        self.result = a * b
        print("The Mul is : ", self.result)

    def Div(self, a, b):
        self.result = a / b
        print("The Div is : ", self.result)

# calc = Calculator()
# calc.Add(20,10)
# print(calc.result)
# calc.Sub(20,10)

# Calculator.Add(Calculator(),10, 20)

calc = Calculator()
calc.Add(22,8)
calc.Sub(22,8)
calc.Mul(22,8)
calc.Div(22,8)