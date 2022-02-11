K = 0
num = int(input("Please enter the number: "))
if num >= 2:
    for sumnum in range(1,num+1):
        K = K + sumnum
else:
    print("Error, Please restart and enter a valid number.")
print(K)