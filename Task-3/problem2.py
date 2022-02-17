i = input("Enter ur list: ")
i = i.split()
S = 0
for lista in range(0,len(i)-1):
    if str(i[lista-S]) == str(i[lista+1-S]):
        i.remove(i[lista-S])
        S = S + 1
print(i)