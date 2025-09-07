class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        n = len(digits)
        for i in range(n-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return(digits)
            else:
                digits[i] = 0
        digits.insert(0,1)
        return(digits)
    
solution = Solution()

print(solution.plusOne([9,9,9]))