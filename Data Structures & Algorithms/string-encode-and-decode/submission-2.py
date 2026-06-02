class Solution:

    def encode(self, strs: List[str]) -> str:
        sizes, encoded = [], ""
        for s in strs:
            encoded += str(len(s))
            encoded += ","
        encoded += "#"

        for s in strs:
            encoded += s

        return encoded    
        

    def decode(self, s: str) -> List[str]:
        
        sizes, decoded, i = [], [], 0
        while s[i] != "#":
            cur = ""
            while s[i] != ",":
                cur += s[i]
                i += 1
            sizes.append(int(cur))
            i+=1
        i+=1
        for sz in sizes:
            decoded.append(s[i:i+sz])
            i+=sz
        return decoded
        
