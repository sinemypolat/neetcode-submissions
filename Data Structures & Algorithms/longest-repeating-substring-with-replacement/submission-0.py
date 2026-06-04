class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_counts = {}
        result = 0
        left = 0

        for right in range(len(s)):
            char_counts[s[right]] = char_counts.get(s[right], 0) + 1

            # if invalid
            while (right - left + 1) - max(char_counts.values()) > k:
                char_counts[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)
        
        return result
            

        
        