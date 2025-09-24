from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nummap = {}
        res = []

        for i in range (len(nums)):
            if nums[i] not in nummap:
                nummap[nums[i]] = 1
            else:
                nummap[nums[i]] += 1

        sortedlist = sorted(nummap.items(), key=lambda x: x[1], reverse=True)

        for i in range(k):        
            res.append(sortedlist[i][0])

        return(res)
            
solution = Solution()

mylist = [1,2,2,3,3,3]
k = 2

print(solution.topKFrequent(mylist, k))