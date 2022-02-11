from hashlib import new


sar = int(input("Enter the size of array and it's items:\n "))
iar = input("")
n=0
newar = iar.split()
for lista in range(0,sar):
    n += int(newar[lista])
print("The sum is: "+str(n))