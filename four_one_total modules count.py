# Using help to list available modules
import sys
help(sys.modules)

# Using dir to list available modules
import sys
print(dir(sys.modules))

print("===================================================")

import sys

# Get a list of module names in the standard library
module_names = list(sys.modules.keys())

# Count the total number of modules
total_modules = len(module_names)

print("Total number of modules in the Python standard library:",total_modules)

#print all keywords in python and length of keywords
import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))
