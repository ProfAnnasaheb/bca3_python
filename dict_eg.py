dict1={1:'akshay',2:'asmi',3:'annasaheb',4:'anil',5:'seema',7:'Ram'}
print("Data type of dict1:",type(dict1))
print('Keys only',dict1.keys())
print('Values only',dict1.values())
print('Accessing single element is dict=',dict1[7])
dict1[7]="Sachin"    #updating value through key
print(dict1)
dict1[8]='Virat'   #adding value through key
print(dict1)
del dict1[5]       #deleting value through key
print(dict1)      
print("=============Methods of Dictonary==========")

print('Length of dict:',len(dict1))#len of dict
print(dict1)
y=dict1.pop(1)
print('after pop element from dict:',y)
print(dict1)
x=dict1.popitem()#last element will poped from dict
print('after pop element from dict:',x)
print(dict1) 

dict2={'name':'akshay','desg':'asstprof','number':9860777401}
print('new dict is:',dict2)
dict2.clear()#all elements will removed or cleared from dict
print(dict2)
emtydict=dict1.copy()   #dict1 copied to dict 2
print(emtydict)
