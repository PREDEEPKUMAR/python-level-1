import re

# Metacharacters

# search_string = 'Predeep'
# pattern = 'e$'
#
# obj = re.search(pattern, search_string)
# print(obj.group())
#
# if obj:
#   print("Search successful.")
# else:
#   print("Search unsuccessful.")


phone_no = '(512)-123-1234'
phone_pattern = '^\(\d{3}\)-\d{3}-\d{4}$'

obj = re.search(phone_pattern, phone_no)

if obj:
   print("Valid.")
else:
   print("Not Valid.")

ip_id = '122.113.234.123'
ip_pattern = '^\d{2}\.\d{3}\.\d{3}\.\d{3}$'
ipp = re.match(ip_pattern, ip_id)

if ipp:
    b = [x for x in ip_id.split('.')]
    v = all(map((lambda n: 0<=int(n) <=255), b))

print('Valid IP', bool(ipp) and bool(v))

password = 'Man@123isn'