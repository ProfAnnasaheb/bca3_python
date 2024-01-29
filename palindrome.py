no=int(input("Enter Number:"))
temp=no
#print(temp)
rev=0

while(temp>0):
    r=temp%10
    rev=(rev*10)+r
    temp=temp//10

print(rev)

if(rev==no):
    print("Number is Palindrome")
else:
    print("NOT")
