class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_anagrams = []

        seen = []
        for i in range(len(strs)):
            this_group = [strs[i]]
            if i in seen:
                continue
            seen.append(i)
            for j in range(len(strs)):
                if i==j:
                    continue
                if sorted(strs[i]) == sorted(strs[j]):
                    this_group.append(strs[j])
                    seen.append(j)
            group_anagrams.append(this_group)
        
        return group_anagrams


        