class Calculator:

    result = 0

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def Add(self):
        self.result = self.a + self.b
        print("The sum is : ", self.result)

    def Sub(self):
        self.result = self.a - self.b
        print("The Sub is : ", self.result)

    def Mul(self):
        self.result = self.a * self.b
        print("The Mul is : ", self.result)

    def Div(self):
        self.result = self.a / self.b
        print("The Div is : ", self.result)


    def Add(self):
        self.result = self.a + self.b + 10
        print("The sum is : ", self.result)

calc = Calculator(22,8)
calc.Add()
calc.Sub()
calc.Mul()
calc.Div()
calc.__init__(10, 20)
calc.Add()
calc.Sub()
calc.Mul()
calc.Div()