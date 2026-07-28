class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = {}
        for i, j in enumerate(strs):
            tmp = list(j)
            tmp.sort()
            tmp = ''.join(tmp)
            if tmp not in store:
                store[tmp] = [j]
            elif tmp  in store:
                store[tmp].append(j)
        return list(store.values())
        


            
        