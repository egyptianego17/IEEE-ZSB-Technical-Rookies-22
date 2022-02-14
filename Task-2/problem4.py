items = input("Please input your list: ")
lista = items.split()
output = []
s = 0
print(lista)
for num1 in range(0,len(lista)):
    for num2 in range(0,len(lista)):
        if int(lista[num1]) == int(lista[num2]) and (num1-num2) > 0:
            output.append(num1-num2)
            break
print(min(output))