def write1():
    while True:
        f=open("abc.txt","w")
        line=input("enter line:")
        f.write(line + '\n')
        choice=input("are there more line? if yes press enter to continue otherwise press N")

        if choice=='N':
            break
        else:
            pass
        f.close()
write1()

f=open("abc.txt","r")
print("Your data on file is:")
data=f.read()
print(data)
