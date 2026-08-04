class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        a = []
        for x in range(min(nums), max(nums)):
            if x not in nums:
                a.append(x)
        return a 