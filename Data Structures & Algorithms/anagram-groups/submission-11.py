class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for i, word in enumerate(strs):
            sortedWord = "".join(sorted(word))
            if sortedWord in map:
                map[sortedWord].append(strs[i])
            else:
                map[sortedWord] = [strs[i]]
        return list(map.values())