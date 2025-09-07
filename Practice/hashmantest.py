from typing import List
nums = [15,20,25,7,100, 15]
target = 30

def twoSum(nums: List[int], target: int) -> List[int]:
    numMap = {}
    n = len(nums)

    # Build the hash table
    for i in range(n):
        numMap[nums[i]] = i

    # Find the complement
    for i in range(n):
        complement = target - nums[i]
        if complement in numMap and numMap[complement] != i:
            print(nums[i],nums[numMap[complement]])
            return [i, numMap[complement]]

print(twoSum(nums, target))