class Employee:

    def __init__(self,first_name, last_name,annual_salary,myraise = ''):
        self.fn = first_name
        self.ln = last_name
        self.sal = annual_salary
        self.myraise = myraise

    def give_raise(self):

        if self.myraise:
            self.sal += self.myraise
        else:
            self.myraise = 5_000
            self.sal += self.myraise
        #print(self.sal)
        return (f"The employee: '{self.fn} {self.ln}' had an annual salary of {self.sal - self.myraise} and a recent raise of {self.myraise}")


#e = Employee('Marc','Mail',70_000,myraise=10_000).give_raise()
#print(e)