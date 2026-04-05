from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        
        for word in strs:
            # Sorted string tuple as the key
            key = tuple(sorted(word))
            anagram_map[key].append(word)
        
        return list(anagram_map.values())
        