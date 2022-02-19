word = input("")
n = int(input(""))
c = 0
word = word * n * 10
for lista in range(0,n):
    if word[lista] == "r":
        c +=1 
print(c)