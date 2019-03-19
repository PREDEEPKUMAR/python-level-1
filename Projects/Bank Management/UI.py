import controller as c
import time
import validation as v


def main_menu():
    print("\tBANK *************")
    print("\tMAIN MENU")
    print("\t1. REGISTER")
    print("\t2. LOGIN")
    print("\t3. EXIT")
    print("\tSelect Your Option (1-3) ")
    option = input()
    if v.validate_int(option):
        return int(option)
    else:
        print('Invalid Selection!!!!')
        return 0


def login_details():
    print('Login Successful')
    print("\t1. VIEW DETAILS")
    print("\t2. DEPOSIT AMOUNT")
    print("\t3. WITHDRAW AMOUNT")
    print("\t4. EXIT")
    print("\tSelect Your Option (1-3) ")
    option = input()
    if v.validate_int(option):
        return int(option)
    else:
        print('Invalid Selection!!!!')
        return 0


while True:
    ch = main_menu()

    if ch == 1:
        acc_id = c.register()
        print('\tAccount has been created. Account ID: ', acc_id)
        print('...........Re-directing to Home Page.............')
        time.sleep(15)

    elif ch == 2:
        id = (input('ACCOUNT ID: '))

        if c.validate_login(int(id)):
            obj = c.obj_creation(int(id))
            while True:
                ch = login_details()

                if ch == 4:
                    break

                elif ch == 1 or ch == 2 or ch == 3:
                    c.control(obj, int(id), int(ch))

        else:
            print('Invalid Login')
        print('...........Re-directing to Home Page.............')
        time.sleep(5)

    elif ch == 3:
        break

    elif ch == 0:
        print('Invalid Selection!!!!!!!!!!!')

