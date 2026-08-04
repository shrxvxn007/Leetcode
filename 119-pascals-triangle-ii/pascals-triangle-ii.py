class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        a = [[1], [1,1]]
        for x in range(rowIndex-1):
            b= [1]
            for y in range(len(a[-1])-1):
                b.append(a[-1][y]+a[-1][y+1])
            b.append(1)
            a.append(b)

        return a[rowIndex]