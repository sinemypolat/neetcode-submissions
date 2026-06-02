class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(ch for ch in s if ch.isalnum()).lower()
        length = len(s)
        result = True
        for i in range(length):
            if not s[i] == s[length-i-1]:
                result = False
        return result

        