from person import Person

class Customer(Person):
    """ Defines information for a customer using the Person class """

    def __init__(self, name, address, phone, credit_score: int):
        self.name = name
        self.address = address
        self.phone = phone
        self.credit_score = credit_score

    def get_credit_score(self):
        return self.credit_score

    def set_credit_score(self, credit_score):
        self.credit_score = credit_score

    def __str__(self):
        """Returns a string representation of the customer"""
        return "Name: " + self.name + \
               "\nAddress: " + self.address + \
               "\nPhone: " + self.phone + \
               "\nCredit Score: " + str(self.credit_score)

class Employee(Person):
    """ Defines information for a employee using the Person class """

    def __init__(self, name, address, phone, badge: int, salary: int):
        self.name = name
        self.address = address
        self.phone = phone
        self.badge = badge
        self.salary = salary

    def get_badge(self):
        return self.badge

    def set_badge(self, badge):
        self.badge = badge

    def get_salary(self):
        return self.salary

    def set_salary(self, salary):
        self.salary = salary

    def __str__(self):
        """Returns a string representation of the employee"""
        return "Name: " + self.name + \
            "\nAddress: " + self.address + \
            "\nPhone: " + self.phone + \
            "\nBadge: " + str(self.badge) + \
            "\nSalary: " + str(self.salary)
    
    def __eq__(self, __value: object) -> bool:
        """Returns true if the badge numbers are the same"""
        if self.badge == __value.badge:
            return True
        else:
            return False
