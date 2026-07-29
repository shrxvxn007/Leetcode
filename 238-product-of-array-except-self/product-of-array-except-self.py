class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        count_zeroes = 0
        index_zero = -1
        product_without_zero = 1
        for i in range(n):
            if nums[i] == 0:
                count_zeroes += 1
                index_zero = i
            else:
                product_without_zero *= nums[i]
        output = [0] * n
        if count_zeroes == 0:
            for i in range(n):
                output[i] = product_without_zero // nums[i]
        elif count_zeroes == 1:
            output[index_zero] = product_without_zero
            
        return output