class Employee:
    def __init__(self,name,salary,age):
        self.__name = name
        self.__salary = salary
        self.__age = age
    def information(self):
        print(f'Name: {self.__name.title()}')
        print(f'Salary: {self.__salary} dollars')
        print(f'Age: {self.__age} years old')
user = Employee('ivan', 500, 17)
user.information()
