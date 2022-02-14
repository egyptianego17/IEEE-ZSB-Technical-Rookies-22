from re import I


n = int(input("Enter the limit: "))
k = 0
l = 1
print(0)
if n > 0:
    while n >= k:
        k = k + l
        print(k) and print(l)
        l = k -l
else:
    print("Please enter valid number")