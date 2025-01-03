from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        leftside = 0
        rightside = (len(height) - 1)
        
        while leftside < rightside:
            currentArea = min(height[leftside], height[rightside]) * (rightside - leftside)
            if currentArea > maxArea:
                maxArea = currentArea
            if height[leftside] > height[rightside]:
                rightside -= 1
            else:
                leftside += 1                    
        return maxArea

solution = Solution()
inputs = [1,8,6,2,5,4,8,3,7]
print(solution.maxArea(inputs))












































class GivenSolution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxArea = 0

        while left < right:
            currentArea = min(height[left], height[right]) * (right - left)
            maxArea = max(maxArea, currentArea)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxArea


