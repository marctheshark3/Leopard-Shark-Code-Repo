class FindNumbers:

    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        try:
            val1 = int(self.num1)
            val2 = int(self.num2)
        except ValueError:
            print("Both inputs must be numbers, Try again!")

        else:
            total = val1 + val2
            print(f"{self.num1} and {self.num2} added together is: {total} \n")

#FindNumbers(98,89).addition()

flag = True
while flag:

    print("Hello, choose two numbers to add together!")
    print("choose q if you would like to quit")
    first = input("What is the first number?")
    second = input("what will the second number be? \n ")

    if first == 'q' or second == 'q':
        flag = False
    else: FindNumbers(first,second).addition()


