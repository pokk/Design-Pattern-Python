""" Created by wu.jieyi on 2016/03/23. """
import copy
from abc import ABCMeta


# Cloneable.
class IClone(metaclass=ABCMeta):
    def shallow_copy(self, name):
        obj = copy.copy(self)
        print("Test of shallow copy: %s/%s" % (id(self), id(obj)))
        obj.name = name
        return obj

    def deep_copy(self, name):
        obj = Resume(name)
        obj.sex = self.sex
        obj.age = self.age
        obj.work_exp.companies = []
        for company in self.work_exp.companies:
            obj.work_exp.companies.append(copy.deepcopy(company))
        print("Test of deepcopy: %s/%s" % (id(self), id(obj)))
        obj.name = name
        return obj


class Company:
    def __init__(self, work_data, name, phone):
        self.work_data = work_data
        self.name = name
        self.phone = phone


class WorkExperience:
    def __init__(self):
        self.companies = []


# Product.
class Resume(IClone):
    def __init__(self, name):
        self.age = 0
        self.sex = ''
        self.name = name
        self.work_exp = WorkExperience()

    def set_person_info(self, sex, age):
        self.sex = sex
        self.age = age

    def set_work_exp(self, work_data, company_name, company_number):
        company = Company(work_data, company_name, company_number)
        self.work_exp.companies.append(company)

    def add_company(self, name, phone):
        company = Company(name, phone)
        self.work_exp.companies.append(company)

    def display(self):
        print('%s, %s, %d|%s' % (self.name, self.sex, self.age, id(self)))
        for c in self.work_exp.companies:
            print("%s:" % (c.work_data))
            print("\t%s (%s)|%s" % (c.name, c.phone, id(c)))
        print('')


def main():
    a = Resume('Tom')
    a.set_person_info('m', 29)
    a.set_work_exp("1998-2000", "ABC.COM", "09123")

    b = a.shallow_copy('Mary')
    b.set_person_info('f', 18)
    b.set_work_exp("2000-2006", "QQ.COM", "098")

    c = a.deep_copy('John')
    c.set_person_info('m', 36)
    c.set_work_exp("2006-2009", "360.COM", "765")

    a.display()
    b.display()
    c.display()


if __name__ == '__main__':
    main()
