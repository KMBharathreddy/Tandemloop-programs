class calculator:
    def __init__(self,a,b,operation):
        self.a=a
        self.b=b
        self.operation=operation

    def calculate(self):
        if self.operation == "addition":
            return self.a + self.b
        elif self.operation == "substraction":
            return self.a + self.b    
        elif self.operation == "multiplication":
            return self.a + self.b    
        elif self.operation == "division":
            if self.b!=0:
                return self.a/self.b
            else:
                return "error:division by zero"
        else:
            return "error: invalid operation"

    a = float(input("enter a first number a"))
    b = float(input("enter a second number"))   
    operation =  input("enter the type of operation(addition,substraction,multiplication,division):")
    calculator = calculator(a,b,operation)
    result = calculator.calculate()
    print(f"the result of {operation} is:{result}")

    print("error :invalid input.please enter valid numbers")             

