ids = int(input("Please enter the number of types: "))
ids_count = input("")
ids_count = sorted(ids_count.split())
c = 1
c_dash = 1
high_id = []
final_list = []
for lista in range(0,ids-1):
    if ids_count[lista] == ids_count[lista+1]:
        c += 1
        continue
    high_id.append(c)
    c = 1
high_id = max(high_id)
for lista in range(0,ids-1):
    if ids_count[lista] == ids_count[lista+1]:
        c_dash += 1
        continue
    if high_id == c_dash :
        final_list.append(ids_count[lista])
    c_dash = 1
print(min(final_list))