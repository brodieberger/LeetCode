nums = [13,11,22,554,61,78,2,1,6,7,-3,-5]

# i is index of number we are moving
# j is index for comparing previous elements
for i in range (1, len(nums), 1):
    current_val = nums[i]
    current_index = i

    for j in range (i-1, -1, -1):
        if nums[j] > current_val:
            nums[current_index] = nums[j]
            nums[j] = current_val
            current_index -= 1
    
print(nums)

