class Solution:
    def reverseVowels(self, s: str) -> str:
        v = ["a", "e", "i", "o", "u"]
        a = []
        for x in s:
            if x.lower() in v:
                a.append(x)
        a.reverse()
        b = []
        c= 0
        for y in s:
            if y.lower() in v:
                b.append(a[c])
                c+=1
            else:
                b.append(y)
        return "".join(b)