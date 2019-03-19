import datetime


class Account:

    def __init__(self, name, ac_type, city, national_id, balance, date_created, flag):
        self.account_name = name
        self.account_type = ac_type
        self.city = city
        self.national_id = national_id
        self.__balance = balance
        self.date_created = date_created
        self.flag = flag

    def get_balance(self):
        return self.__balance

    def display_details(self):
        print('Account Name: ', self.account_name)
        print('Account Type: ', self.account_type)
        print('Account City: ', self.city)
        print('National ID: ', self.national_id)
        print('Balance: Rs.', self.__balance)
        if self.flag ==1:
            print('Account Status: Active')
        elif self.flag ==2:
            print('Account Status: InActive')

    def deposit(self, amount):
        self.__balance += amount
        return self.__balance

    def withdrawal(self, amount):
        if int(self.__balance) >= int(amount):
            self.__balance -= amount
            return self.__balance
        else:
            return self.__balance

    @classmethod
    def create_account(cls):
        name = input("Enter the account name : ")
        ac_type = input("Account Type (C/S) : ")
        city = input("Account City : ")
        national_id = input("National ID : ")
        balance = 0
        if ac_type == 'S':
            balance = 500.0
            print('Default Balance for Creation of Savings Account is Rs.500/-')
        elif ac_type == 'C':
            balance = 1000.0
            print('Default Balance for Creation of Current Account is Rs.1000/-')
        currentdt = datetime.datetime.now()
        date_created = currentdt.strftime("%Y-%m-%d %H:%M:%S")
        flag = 1
        return cls(name, ac_type, city, national_id, balance, date_created, flag)

    @classmethod
    def get_details(cls, detail):
        acc_id, name, ac_type = detail[0], detail[1], detail[2]
        city, national_id, balance = detail[3], detail[4], detail[5]
        date_created, flag = detail[6], detail[7]
        return cls(name, ac_type, city, national_id, balance, date_created, flag)
