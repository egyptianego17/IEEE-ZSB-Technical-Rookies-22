nums = input("").split()
key = 0
i=0
for lista in range(1,len(nums)):
    key = nums[lista]
    i = lista - 1
    while i>=0 and nums[i]>key:
        nums[i+1]=nums[i]
        nums[i] = key
        i = i-1
    nums[i+1] = key
print(nums)