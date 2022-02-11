import random
import math
c = 1; p = True
r = round((random.random()*10))
print(r)
ans = float(input("Geuss the number ^_^: "))
while p:
    if ans == r:
        print("You got it after "+str(c)+" tries!!")
        p = False
    else:
        c+=1
        print(str(ans)+" is a wrong geuss, try again.")
        ans = float(input("Geuss the number ^_^: "))