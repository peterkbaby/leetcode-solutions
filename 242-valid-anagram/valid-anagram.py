class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}
        for i in s:
            if i in count:
                count[i] = count[i]+1
            else:
                count[i] = 1
        for j in t:
            if j not in count or count[j] == 0:
                return False
            else:
                count[j] -= 1
        return True
