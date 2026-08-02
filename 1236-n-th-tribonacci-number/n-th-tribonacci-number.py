class Solution:
    def tribonacci(self, n: int) -> int:
        a =[0,1,1]
        for x in range(n-2):
            a.append(a[x]+a[x+1]+a[x+2])
        return a[n]