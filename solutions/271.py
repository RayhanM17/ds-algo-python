class Solution:

    def encode(self, strs: List[str]) -> str:
        # Use a delimiter to separate strings
        res = ""
        for s in strs:
            # Prefix each string with its length and a delimiter
            res += f"{len(s)}#{s}"
        return res



    def decode(self, s: str) -> List[str]:

        res = []
        index = 0

        while index < len(s):
            # Extract the length of the next string
            d_index = index
            while s[d_index] != "#":
                d_index += 1

            length = int(s[index:d_index])
            
            # Extract the actual string based on the length
            start = d_index + 1
            end = start + length
            res.append(s[start:end])
            
            # Move the index past the extracted string
            index = end
        
        return res