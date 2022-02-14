word = str(input("Please enter ur sentence: "))
nlist = word.split()
first = nlist[0]
last = nlist[-1]
list1 = []
for i in range(0,len(nlist)):
    list1.append(len(nlist[i]))
list1.sort()
length = int(list1[len(list1)-1]) + 2
print("*" * length)
for lista in range(0, len(nlist)):
    spaces = -len(nlist[lista]) + length - 2
    print("*"+nlist[lista]+spaces*" "+"*")
print("*" * length)