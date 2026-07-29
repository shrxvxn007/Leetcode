class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split()
        a.reverse()
        b = []
        for x in a:
            b.append(x)
            b.append(" ")
        b.pop()
        return "".join(b)