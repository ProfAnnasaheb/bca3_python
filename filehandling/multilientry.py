numbers=[9,18,27,36]
def write1():
    f=open("myfile.txt","a")
    while True:
        line=input("enter line:")
        f.write(line)
        choice=input("are there more lines")
        if choice=="N":
            break
    f.close()
write1()
