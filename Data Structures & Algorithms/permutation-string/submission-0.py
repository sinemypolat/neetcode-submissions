class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26
        window_count = [0] * 26

        # counts for s1 and the first window in s2
        for i in range(len(s1)):
            s1_index = ord(s1[i]) - ord("a")
            s2_index = ord(s2[i]) - ord("a")

            s1_count[s1_index] += 1
            window_count[s2_index] += 1

        # check the first window
        if s1_count == window_count:
            return True

        left = 0

        # slide the window over s2
        for right in range(len(s1), len(s2)):
            # add new right character
            right_index = ord(s2[right]) - ord("a")
            window_count[right_index] += 1

            # remove old left character
            left_index = ord(s2[left]) - ord("a")
            window_count[left_index] -= 1

            left += 1

            if s1_count == window_count:
                return True

        return False