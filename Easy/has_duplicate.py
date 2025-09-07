class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        myset = set()
        for element in nums:
            if element in myset:
                return(False)
            myset.add(element)
        return(True)

solution = Solution()
print(solution.hasDuplicate([1,2,3,1]))