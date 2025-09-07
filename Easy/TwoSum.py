class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        
        mydict = {}
        for i in range(n):
            mydict[nums[i]] = i 

        for i in range(n):
            complement = target-nums[i]
            if complement in mydict and i != mydict[complement]:
                return([i,mydict[complement]])

solution = Solution()
nums = [1,3,4,2]
target = 6

print(solution.twoSum(nums,target))