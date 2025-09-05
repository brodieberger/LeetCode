class Solution(object):
    def longestCommonPrefix(self, strs):

        for element in strs:
            if element == "":
                return("")

        if len(strs) == 1:
            return(strs[0])

        output = ""
        shortest_word = min(strs, key=len)
        current_value = shortest_word[0]

        # i = letter
        # j = word
        j = 0

        for i in range(len(shortest_word)): # loop through shortest string
            for j in range (len(strs)):
                if current_value != strs[j][i]:
                    return(output)
            output += current_value

            # catch if the shortest word was only one character
            if len(shortest_word) == i+1:
                return(output)
            current_value = shortest_word[i+1]
                
        return(output)
    
solution = Solution()
strs = ["flower","flower","flower","flower"]
print(solution.longestCommonPrefix(strs))