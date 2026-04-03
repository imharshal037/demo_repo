class employee:
    company_name = "TCS"
    def __init__(self,name):
        self.name=name
       # self.company_name=name

    def show(self):
        print("Employee Name :",self.name)
        print("Company Name :",self.company_name)

    @classmethod
    def class_show(cls,company_name):
        print("Company Name :",cls.company_name)
        cls.company_name = company_name
        print("Company Name :",cls.company_name)


e1=employee("John")
e2=employee("Alice")
e1.show()
e2.show()

e3 = employee("Bob")
e3.company_name = "Wipro"
print(e3.company_name)
#e3.company_name="LTIMindtree"
#employee.company_name="LTIMindtree"
employee.class_show("Infosys")
print("e1",e1.company_name)
print("e2",e2.company_name)
print(e3.company_name)
print(employee.company_name)
employee.company_name="NICE"
print(employee.company_name)

e4 = employee("John")
print(e4.company_name)
print(e3.company_name)