class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        mydict = {}
        for word in strs:
            sortedword = ''.join(sorted(word))
            if sortedword not in mydict:
                mydict[sortedword] = [word]
            else:
                mydict[sortedword] += [word]
        return(list(mydict.values()))

solution = Solution()
strs = [""] 
print(solution.groupAnagrams(strs))