dict1={1:'akshay',2:'asmi',3:99.96,4:9860777401}
print(dict1)
print(type(dict1))
dict2={'name':'asmi','education':['MBBS MD','LLB']}
print(dict2)
print(type(dict2))
#list1=(list(dict2))
#print(list1)
#print(type(list1))
print(dict2.keys())
print(dict2.values())

####list methods
##list1=[1,2,3,4,5,6,7,8,9,10,'a','b','c','d']
##print(list1)
##del(list1[1])#deletes index 1 element
##print(list1)
##list1.append(11)#append element at last
##print(list1)
##list2=[100,101,102]
##list1.extend(list2)
##print(list1)#list2 copied into list1
##list1.insert(1,'asmi')#at index 1 value will added into list1
##print(list1)
##list1.pop()#last element will pop or pop(2) then 2nd index element will poped
##print(list1)
##x=list1.pop(5)#poped element will save into x var
##print(list1)
##print("poped element:",x)
##list1.remove(100)#removed specified element here 100
##print(list1)
##list1.reverse()
##print('reversed list:',list1)#reversed list will displayed
##list3=[45,56,23,1,45,654,34]
##print('normal list:',list3)
##list3.sort(reverse=True)
##print('desending sorted list:',list3)#sorted desending list will displayed
##list3.sort()
##print('asending sorted list:',list3)#sorted asending list will displayed

##import sys
##import timeit
##
### Creating a tuple and a list with the same elements
##my_tuple = (1, 2, 3, 4, 5)
##my_list = [1, 2, 3, 4, 5]
##
### Memory usage comparison
##tuple_size = sys.getsizeof(my_tuple)
##list_size = sys.getsizeof(my_list)
##
##print(f"Tuple size: {tuple_size} bytes")
##print(f"List size: {list_size} bytes")
##
### Time efficiency comparison when accessing elements
##def access_elements_tuple():
##    return my_tuple[2]
##
##def access_elements_list():
##    return my_list[2]
##
##tuple_time = timeit.timeit(access_elements_tuple, number=1000000)
##list_time = timeit.timeit(access_elements_list, number=1000000)
##
##print(f"Access time for tuple: {tuple_time} seconds")
##print(f"Access time for list: {list_time} seconds")

