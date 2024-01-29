f=open("data.txt","w")
#str1='''my name is akshay
#and i am god gifted'''
str1=input("Enter Data to file:")
for line in f:
    f.writelines(str1)
f.close()

f=open("data.txt","r")
print("Entered data was suceesfully written on file and data is:",f.read())
f.close()
