from typing import List


class Solution:
    def reverseString(self, s):

        str = ''
        for i in range(len(s)-1, -1, -1):
            str = str + s[i]
        
        return str
    
    def reverseString2(self, s: List[str]):
        s.reverse()


a = Solution()
print(a.reverseString('abc'))
print(a.reverseString2('abc'))