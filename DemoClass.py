from select import select


class Calculator:

    # Data Member - Variable Initialization
    # Global Variable
    #Class Variable
    result = 0

    # Self ==> The current object
    def Add(self, a, b):
        Calculator.result = a + b
        self.result = a + b
        print("With in the Function", self.result)
        self.result = 100
        print("The sum is {}".format(self.result))

calc = Calculator()
Calculator.result = 20
calc.Add(10,20)
calc.Add(20,30)

