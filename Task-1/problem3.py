K = 0
num = int(input("Please enter the number: "))
if num >= 2:
    for lista in range(1, num+1):
        if lista%3 == 0 or lista%5 == 0:
            K = K + lista
else:
    print("Error, Please restart and enter a valid number.")
print(K)