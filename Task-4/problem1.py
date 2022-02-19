bottles = int(input(""))
bottles_arr = []
quantity = 0
mm = []
for lista in range(0,bottles):
    bottles_arr.append(input("").split())
    quantity = quantity + int(bottles_arr[lista][0])
    mm.append(bottles_arr[lista][1])
mm = sorted(mm)
if (int(mm[-1]) + int(mm[-2])) >= quantity:
    print("yes")
else:
    print("no")