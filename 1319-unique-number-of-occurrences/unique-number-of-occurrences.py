class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        a = list(set(arr))
        b = []
        for x in a:
            b.append(arr.count(x))
        for y in b:
            if b.count(y) > 1:
                return False
        return True