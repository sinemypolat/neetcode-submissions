class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        
        result_indices = [-1, -1]
        min_len = float("infinity")
        left = 0
        
        t_chars, window_chars = {}, {}

        for char in t:
            t_chars[char] = t_chars.get(char, 0) + 1

        have, need = 0, len(t_chars)

        for right in range(len(s)):
            char = s[right]
            window_chars[char] = window_chars.get(char, 0) + 1

            if char in t_chars and window_chars[char] == t_chars[char]:
                have += 1
            
            while have == need:
                # update the result
                if (right - left + 1) < min_len:
                    min_len = right - left + 1
                    result_indices = [left, right]
                
                # move left
                window_chars[s[left]] -= 1
                if s[left] in t_chars and window_chars[s[left]] < t_chars[s[left]]:
                    have -= 1
                left += 1
        left, right = result_indices
        return s[left: right+1] if min_len != float("infinity") else ""


        
        