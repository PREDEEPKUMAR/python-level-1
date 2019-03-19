import re
import datetime
# print('Phone No Format is +91-**********')
# user_input = input('Provide your Phone Number')
with open('Phone_ValidationLog.txt','a') as fp:
    try:
        with open('input_file.txt', 'r') as fo:
            lines = fo.read().splitlines()

        with open('phone.txt','a') as phone:
            for phone_no in lines:
            # validate
                try:
                    if phone_no != None:
                        phone_pattern = '^\+\d{2}-\d{10}$'
                        match = re.search(phone_pattern, phone_no)
                        if match:
                            log_string = phone_no + ' is a Valid No\n'
                            fp.write(log_string)
                            phone.write(phone_no + '\n')
                        else:
                            log_string = phone_no + ' is Not a Valid No\n'
                            fp.write(log_string)
                except:
                    print('Exception Raised')

    except FileNotFoundError as err:
        currentDT = datetime.datetime.now()
        time_str = currentDT.strftime("%Y-%m-%d %H:%M:%S")
        fp.write(time_str + '  ERROR: Input File is missing at the location\n')