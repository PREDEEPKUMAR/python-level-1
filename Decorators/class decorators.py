class Employee:
    '''Contains the information of the Employee'''

    # Initializing Methods / Constructor
    def __init__(self, name, location, phone_no):
        self.name = name
        self.location = location
        self.phone_no = phone_no

    # Instance Methods
    def get_phone(self):
        print(self.phone_no)

    @staticmethod
    def get_details():
        print('Details of Class Displayed')

    @classmethod
    def from_string(cls, emp_str):
        nam, loc, no = emp_str.split('-')
        return cls(nam, loc, no)

    @classmethod
    def get_det(cls):
        print('From Class Method')

emp1 = 'Predeep-India-7708745902'
obj1 = Employee.from_string(emp1)
obj1.get_phone()

emp2 = 'Predeep-India-77087415902'
obj2 = Employee.from_string(emp2)
obj2.get_phone()

obj3 = Employee('Mahesh','Kar','123')
print(type(Employee.get_phone(obj3)))
print(type(obj3.get_det()))
