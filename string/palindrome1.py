
# 문자열을 리스트로 변환 후
# 앞, 뒤에서 하나씩 pop 하여 비교
class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        print(strs)
        
        while len(strs) > 1:
            print(strs.pop(0), strs.pop())
            if strs.pop(0) != strs.pop():
                return False

        return True


a = Solution()
print(a.isPalindrome('1234'))