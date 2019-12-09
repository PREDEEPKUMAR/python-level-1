# Combination of *args & **kwargs
# Non-Keyword Arguments First and Keyword Arguments Second
def Combination(*args, **kwargs):
    sum = 0
    for i in args:
        sum = i + sum
    print(sum)
    for k,v in kwargs.items():
        print(k,v)

t = [1,2,3,5,6,7,8,12,32]
key_arg = {'a':'1','b':'2'}

Combination(1,2,3,4,a=1,b=2,c=3)
Combination(*t,**key_arg)