from account import Account
import db_connection as db


def register():
    obj = Account.create_account()
    conn = db.create_connection('bank.db')
    sql = f'INSERT INTO accounts (account_name,account_type,city,national_id,balance,date_created,flag)' \
        f' VALUES(?,?,?,?,?,?,1)'
    acc_sql = (obj.account_name, obj.account_type, obj.city, obj.national_id, obj.get_balance(), obj.date_created)
    with conn:
        cur = conn.cursor()
        cur.execute(sql, acc_sql)
        return cur.lastrowid


def get_details(id):
    conn = db.create_connection('bank.db')
    sql = 'SELECT * FROM accounts WHERE acc_no=?'
    with conn:
        cur = conn.execute(sql, (id,))
        rows = cur.fetchall()
        return rows


def obj_creation(id):
    detail = get_details(id)
    obj = Account.get_details(detail[0])
    return obj


def control(obj, id, ch):
    if ch == 1:
        obj.display_details()
    elif ch == 2:
        amount = input('Deposit Amount: ')
        d_or_w(obj, id, int(amount), 'D')
    elif ch == 3:
        withdraw = input('Withdrawal Amount: ')
        if obj.get_balance()> withdraw:
            d_or_w(obj, id, int(withdraw), 'W')
        else:
            print('Withdrawal Not Possible')


def d_or_w(obj, id, amount, type):
    sql = f'UPDATE accounts SET balance=? WHERE acc_no=?'
    conn = db.create_connection('bank.db')
    with conn:
        if type == 'D':
            conn.execute(sql, (obj.deposit(amount), id))
        elif type == 'W':
            conn.execute(sql, (obj.withdrawal(amount), id))
        print('Deposit/Withdrawal Done')


def validate_login(id):
    conn = db.create_connection('bank.db')
    sql = 'SELECT acc_no FROM accounts WHERE acc_no=?'
    with conn:
        cur = conn.execute(sql, (int(id),))
        rows = cur.fetchall()
        if rows[0][0]==int(id):
            return True
        else:
            return False



