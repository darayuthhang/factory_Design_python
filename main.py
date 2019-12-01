import abc

import mysql.connector
from mysql.connector import errorcode
from abc import ABC, abstractmethod

''' abstract method'''
''' find hourly rate of employee'''


class Person(ABC):

    @abstractmethod
    def getName(self):
        pass

    @abstractmethod
    def getAddress(self):
        pass

    @abstractmethod
    def getPhoneNumber(self):
        pass


class Employee(Person):
    '''
    @:param name name return name of employee
    @:param address address return address of employee
    @:param phone phone return phone of employee
    '''

    def __init__(self, name, address, phone_number, employee_id):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.employee_id = employee_id

    def getName(self):
        return self.name

    def getAddress(self):
        return self.address

    def getPhoneNumber(self):
        return self.phone_number

    def getEmployeeId(self):
        return self.employee_id


class Manager:
    '''
    @:param Employee return name, address, id, phoneNumber of manager
    @:param hourly_rate hourly_rate return the rate of current manager
    @:param salary salary return the salary of current manager
    '''

    def __init__(self, Employee, hourly_rate, salary):
        self.Employee = Employee
        self.hourly_rate = hourly_rate
        self.salary = salary

    def getEmployee(self):
        return self.Employee

    def getHourlyRate(self):
        return self.hourly_rate

    def getSalary(self):
        return self.salary


'''
EmployeeFactory is object to return to the type of worker
in the factory.
'''


class EmployeeFactory:
    @staticmethod
    def getEmployeeType(employeeType):
        try:
            if employeeType.casefold() == "manager":
                return Manager(Employee, hourly_rate="", salary="")
            raise AssertionError("Employee not found")
        except AssertionError as error:
            print(error)


if __name__ == '__main__':
    Employee = EmployeeFactory().getEmployeeType("manager")

    print("salary: {}, hourlyRate: {}".format(Employee.getSalary(), Employee.getHourlyRate()))
