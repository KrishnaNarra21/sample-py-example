# def greet():
#     print("Hello")
#     print("Good Morning")
# greet()

# def mul_div(x,y):
#     a=x*y
#     b=x/y
#     # print(a, b)
#     return a,b
# result1, result2 = mul_div(9,6)
# print(result1, result2)

# Formal Arguments
# Actual Arguments : position, keyword, default, variable length

# def sum(name,age):
#     print(name)
#     print(age)
# sum('krish',18)  # calling with position

# def sum(name,age):
#     print(name)
#     print(age)
# sum(age=18,name='krish') # calling with keyword

# def person(name,age=18):
#     print(name)
#     print(age)
# person('krish',)   # if you  not pass any value it will take DEFAULT value

# def sum(a,*b):
#    c = a
#    for i in b:
#        c=c+i
#    print(c)
# sum(7,4,7,9,5)  #  Variable length argument

# variable length keyworded argument
# def person(name,**data):
#     print(name)
#     for i,j in data.items():
#         print(i,j)
#
# person('krish',age='23',Mob=94900,city='ong')

# global & local variables

# a=10 # global variable
# def something():
#     global a  #
#     a=14 # defining global variable in local
#     print("inside",a)
#
# something()
# print("outside",a)


a=10 # global variable
print(id(a))
def something():
    a = 9
    x = globals()['a']  # defining global variable in local
    print(id(x))
    print("inside",a)
    globals()['a']=15   # changing global variable locally
something()
print("outside",a)