class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = 0
        currentset = set('')
        count = 0
        maxcount = 0
        for right in range(len(s)):
            maxcount = max(count,maxcount)
            while s[right] in currentset:
                count -= 1
                currentset.remove(s[left])
                left += 1
            if s[right] not in currentset:
                currentset.add(s[right])
                count += 1            
        maxcount = max(count,maxcount)
        return(maxcount)
    
solution = Solution()
print(solution.lengthOfLongestSubstring("hello"))