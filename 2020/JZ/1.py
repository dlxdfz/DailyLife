# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        if not matrix:
            return []
        res = []
        n, m = len(matrix), len(matrix[0])
        x, y = 0, 0
        while n and m:
            if n==1:
                for i in range(y, y + m):
                    res.append(matrix[x][i])
                break
            if m==1:
                for i in range(x, x + n):
                    res.append(matrix[i][y])
                break
            for i in range(y, y + m): res.append(matrix[x][i])
            for i in range(x + 1, x + n): res.append(matrix[i][y+m-1])
            for i in range(y + m - 2, y, -1): res.append(matrix[x+n-1][i])
            for i in range(x + n - 1, x, -1): res.append(matrix[i][y])
            m -= 2
            n -= 2
            x += 1
            y += 1
        return res

if __name__=="__main__":
    import pdb
    s = Solution()
    m = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    pdb.set_trace()
    res = s.printMatrix(m)
    print(res)
