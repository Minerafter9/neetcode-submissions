class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        list1 = []
        checkList = []
        for i in strs:
            if i not in checkList:
                tmpList = []
                for j in range(len(strs)):
                    if anagram(i, strs[j]) == True:
                        tmpList.append(strs[j])
                        checkList.append(strs[j])
                list1.append(list(tmpList))
                
        return list1

                
            



def anagram(word1, word2):
    if len(word1) != len(word2):
        return False
    table1 = {}
    table2 = {}
    for i in word1:
        if i in table1:
            table1[i] += 1
        else:
            table1[i] = 1
    for i in word2:
        if i in table2:
            table2[i] += 1
        else:
            table2[i] = 1
    for i in word1:
        try:
            if table1[i] != table2[i]:
                return False
        except KeyError:
            return False
    return True