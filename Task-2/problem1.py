n = int(input("Enter the num: "))
if n>1:
    for num in range(1,n):
        for lista in range(2,num):
            if num % lista == 0:
                break
            else:
                print(num)
                break
else:
    print("Please enter valid number")