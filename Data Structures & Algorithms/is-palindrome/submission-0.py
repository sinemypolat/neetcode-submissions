class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(ch for ch in s if ch.isalnum()).lower()
        length = len(s)
        count = 0
        for i in range(length):
            if s[i] == s[length-i-1]:
                count+=1
        if count == length:
            return True
        else:
            return False

        