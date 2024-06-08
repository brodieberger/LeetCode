from pyclbr import Class
from typing import List
import time


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        print("The list is " + str(nums) + "\nSearching for two numbers that add up to " + str(target))

        length = len(nums)
        for i in range (length):
            #print("\nouter: " + str(nums[i])) #DEBUG CODE
            for x in range (i+1,length):
                #print(str(nums[i]) + "," + str(nums[x]) + " = " + str((int(nums[i]) + int(nums[x])))) #DEBUG CODE
                if (nums[i]) + (nums[x]) == target:
                    print("\nTarget found: the two numbers are: " + str(nums[i]) + " and " + str(nums[x]))
                    return{i,x}

nums = [3,2,4,15,123,6,546,456,234,12,3,6,8567,5,1231,23,13,45645,64,6,546,4564,6456,5234,234,59,5,43,24,123,213,15,4,6,645757,4745,74,53,4,7,8,798,9856,74564,352,41,2563748,596,678574,63524,5678]
target = 684252
length = len(nums)          

solution = Solution()

start = time.time()
print(solution.twoSum(nums, target))
end = time.time()

print(end-start)