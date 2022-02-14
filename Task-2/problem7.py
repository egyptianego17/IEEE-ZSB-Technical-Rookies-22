palinum = input("Please enter the size of array and it's items: ")  
c = 0
if str(palinum) == str(palinum)[::-1]:
        positive_num = input("")
        positive_num = positive_num.split()
        for lista in range(0,len(positive_num)):
            if int(positive_num[lista]) == abs(int(positive_num[lista])):
                c = c + 1
        if c == int(palinum):
            print("True")
        else:
            print("False")
else:
    print("Please enter palindromic number")