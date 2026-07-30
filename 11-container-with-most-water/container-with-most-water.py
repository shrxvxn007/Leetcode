class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        ma =0
        ma = min(height[l], height[r]) * (r-l)
        while l <r :
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
            ma2 = min(height[l], height[r]) * (r-l)
            if ma2 > ma:
                ma = ma2
        return ma
