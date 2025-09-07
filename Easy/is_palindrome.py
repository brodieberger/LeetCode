class Solution:
    def isPalindromeSlice(self, s: str) -> bool:
        s = s.lower()
        mystr = ""
        for letter in range(len(s)):
            if s[letter].isalnum():
                mystr += str(s[letter])
        return(mystr == mystr[::-1])

    def isPalindromePointer(self, s: str) -> bool:
        s = s.lower()
        mystr = ""
        for letter in range(len(s)):
            if s[letter].isalnum():
                mystr += str(s[letter])
        n = len(mystr)
        left = 0
        right = n-1
        while left < right:
            if mystr[left] != mystr[right]:
                return(False)
            left +=1
            right -= 1
        return(True)
        

solution = Solution()
s="A man, a plan, a canal: Panama"
print(solution.isPalindromePointer(s))
