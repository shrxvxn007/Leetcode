class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = []
        for x in nums:
            if x not in a:
                a.append(x)
        b = []
        c = []
        for y in a:
            b.append(nums.count(y))
        for z in range(k):
            c.append(a[b.index(max(b))])
            b[b.index(max(b))] = -1
        return c