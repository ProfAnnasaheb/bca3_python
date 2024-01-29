##import sys
##sys.path.append('C:/Users/akshay/Desktop')

import four_two_moduledemo
x=four_two_moduledemo.add(10,20)
print(x)

#using alise name... alter module calling name
import four_two_moduledemo as m
print(m.add(30,30))

# using from no need to module name every time
from four_two_moduledemo import add
print(add(10,40))

#using * method
from four_two_moduledemo import *
print(add(70,40))


