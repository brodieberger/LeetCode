from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        prev = nums[0]
        i = 0
        k = 0

        for num in nums:
            if i == 0 or nums[i] == "_":
                i += 1
                k += 1
            elif nums[i] == prev:
                prev = nums[i-1]
                nums.pop(i)
                nums.append("_")

            else:
                prev = nums[i]
                i += 1
                k += 1
        print(nums)
        return(k)
            
solution = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
print(solution.removeDuplicates(nums))