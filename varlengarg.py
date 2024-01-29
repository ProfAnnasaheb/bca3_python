# #*args   non keyword args pass like tuple
# def add(*args):
#     add=0
#     for i in args:
#         add=add+i
#     print (add)

# add(10,20,30)
# add(10,20)

#**kwargs    pass key value pair means dictornary
def add(**args):
    add=0
    for key in args:
        add=add+args[key]
    print (add)

add(a=10,b=20,c=30)
add(a=10,b=20)
