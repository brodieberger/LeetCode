nums = [1,2,2,3,3,3,3]
k = 2
nummap = {}
res = []

for i in range (len(nums)):
    if nums[i] not in nummap:
        nummap[nums[i]] = 1
    else:
        nummap[nums[i]] += 1

for i in range(k):        
    currentval = (max(nummap, key=nummap.get)) # type: ignore
    nummap.pop(currentval)
    res.append(currentval)

print(res)