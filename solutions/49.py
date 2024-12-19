class Solution(object):
    def groupAnagrams(self, strs):
        
        groups = {}

        for str in strs:

            key = 0

            for char in str:
                key += ord(char)

            groups[key] = groups.get(key, [])

            groups[key].append(str)

        return list(groups.values())