a=input("Enter the list of number")
a=a.split(',')
b=int(input("Enter the number you want to count"))
c=0

for i in a:
    if b==int(i):
        c+=1
    else:
        continue
print("Number count to :",c)
    
