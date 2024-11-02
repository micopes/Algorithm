from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)
        for s in strs:
            list_s = list(s)
            list_s.sort()
            key = "".join(list_s)
            anagram_dict[key].append(s)
        
        result = []
        for val in anagram_dict.values():
            val.sort()
            result.append(val)
        return result
