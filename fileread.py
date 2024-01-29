##f=open("filedata.txt","r")
##data=f.read()
##print("Read method:",data)   #read all data from file
##data1=f.readline()
##print("Readline method:",data1)  #read single line from file
##data2=f.readlines() 
##print("Readlines method:",data2)  #read all data and return in format of list
##f.close()


##f=open("filedata.txt","r")
##print(f.tell())
##f.read(3)
##print(f.tell())
##print(f.seek(0))
##f.read()
##f.close()

try:
    f=open("filedata2.txt","w")
    str1=input ("enter data:")
    f.write(str1 + '\n')
    print("data write succesfuuly")
    f.close()
except:
  print("An exception occurred")

##f=open("filedata2.txt","w")
##list1=['akshay','ram']
##f.writelines(list1)
##print("data write succesfuuly")
##f.close()
