class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        a = [i+extraCandies for i in candies]
        b = []
        for x in range(len(a)):
            if a[x]>=max(candies):
                b.append(True)
            else:
                b.append(False)
        return b