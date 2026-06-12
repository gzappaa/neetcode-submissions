class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            counter = [0] * 26

            for ch in word:
                counter[ord(ch) - ord('a')] += 1

            key = tuple(counter)
            groups[key].append(word)
        return list(groups.values()) 
            

                