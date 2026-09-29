class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        set1 = set()
        list1 = []
        dict1 = {}

        for i in range(len(strs)):
            if tuple(sorted(strs[i])) in dict1:
                dict1[tuple(sorted(strs[i]))].append(strs[i])
            else:
                dict1[tuple(sorted(strs[i]))] = [strs[i]]
        out = []
        for i in dict1:
            out.append(dict1[i])
        return out

            
        
        