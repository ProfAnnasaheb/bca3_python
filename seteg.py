s={10,20,30,40,50,60,70,80,90,'akshay','sham'}
print(s)
s1=set([1,1,2,2,334,4,555,'vikram'])
print(s1)
s2=set()#empty set creation
print(type(s2))

print("============SET OPERATIONS=========")
# Creating a set
my_set = {1, 2, 3}

# Adding elements to the set
my_set.add(4)

print(my_set)

# Removing elements from the set
my_set.remove(2)

#updating the elemets
my_set.update(['TATA'])
#print(my_set)

# The set after adding and removing elements
print(my_set)  # Output: {1, 3, 4}
#Here we can prove sets are mutable

print("============Proof of After the adding elements set elements are immutable=========")
#my_set[0]=43434  #'set' object does not support item assignment error will occur

#element = my_set[0]
#print(element) #'set' object is not subscriptable error will occur Hence indexing and slicing not possible

