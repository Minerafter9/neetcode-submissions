class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = defaultdict(list)
        for i in range(len(strs)):
            count = [0] * 26
            for j in strs[i]:
                count[ord(j) - ord("a")] += 1
            store[tuple(count)].append(strs[i])
        return list(store.values())
        


        