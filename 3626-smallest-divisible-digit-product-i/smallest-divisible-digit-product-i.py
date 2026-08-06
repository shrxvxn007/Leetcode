class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        d = False
        while not d:
            a = prod([int(x) for x in str(n)])
            if a % t ==0:
                return n
            else:
                n+=1