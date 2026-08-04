class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        a = []
        s_index = 0

        for x in t:
            if s_index == len(s):
                break

            if x == s[s_index]:
                a.append(x)
                s_index += 1 

        b = "".join(a)
        if s == b:
            return True
        else:
            return False