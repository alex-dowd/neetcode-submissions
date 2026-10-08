class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        list = {}
        for i in s:
            if i not in list:
                list[i] = 1
            else:
                list[i] += 1
        for i in t:
            if i not in list:
                return False
            else:
                list[i] -= 1
                if list[i] == -1:
                    return False
        return True
