import math


class Solution:
    # def convert(self, s: str, numRows: int) -> str:
    #     if numRows == 1 or len(s) == 1:
    #         return s
    #     cols = math.ceil(len(s) / (2 * numRows - 2)) * (numRows - 1)
    #     stringMatrix = [[" "] * cols for _ in range(numRows)]

    #     up_down = 1
    #     left_right = 0
    #     i = j = 0
    #     for ix in range(len(s)):
    #         stringMatrix[i][j] = s[ix]
    #         i = i + up_down
    #         j = j + left_right
    #         if i == numRows - 1:
    #             up_down = -1
    #             left_right = 1
    #         if i == 0:
    #             up_down = 1
    #             left_right = 0
    #     res = []
    #     for i in range(numRows):
    #         for j in range(cols):
    #             if stringMatrix[i][j] != " ":
    #                 res.append(stringMatrix[i][j])
    #     return "".join(res)

     def convert(self, s: str, numRows: int) -> str:
        if numRows < 2: return s
        res = ["" for _ in range(numRows)]
        i, flag = 0, -1
        for c in s:
            res[i] += c   #填充？？抛弃没有意义的占位符
            if i == 0 or i == numRows - 1: flag = -flag
            i += flag
        return "".join(res)


solution = Solution()
s = "PAYPALISHIRING"
print(solution.convert(s, 1))
