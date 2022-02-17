sorted_items = input("Please input ur items: ")
s_item = input("")
sorted_items = sorted_items.split()
low_index = 0
high_index = len(sorted_items)-1
for lista in range(0,len(sorted_items)):
    midpoint = low_index + (high_index - low_index) // 2
    if sorted_items[midpoint] == s_item:
        print(midpoint)
        break
    elif s_item < sorted_items[midpoint]:
        high_index = midpoint - 1
    else: 
        low_index = midpoint + 1