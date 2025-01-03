
#Convert given integer into a string
#Convert that string into a list (could have converted int to list but didnt know how yet)
#Convert string into list in reverse order (using '.reverse()')
#Compare the two lists

class Solution:
    def isPalindrome(self, x: int) -> bool:
        number = x
        stringnumber = str(x)
        n = len(stringnumber)

        forwardList = []
        backwardList = []

        for i in range (n):
            forwardList.append(stringnumber[i])

        backwardList = forwardList.copy()
        backwardList.reverse()

        return(backwardList == forwardList)

