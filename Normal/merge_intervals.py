from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        previous = intervals[0]
        new_intervals = [intervals[0]]

        for interval in intervals[1:]:
            if interval[0] <= previous[1] or interval == previous:
                new_intervals.pop()
                new_intervals.append([min(previous[0], interval[0]), max(previous[1], interval[1])])
            else:
                new_intervals.append(interval)
            previous = new_intervals[-1]
        return(new_intervals)
    
solution = Solution()
inputs = [[1,3],[2,6],[8,10],[15,18]]
print(solution.merge(inputs))
