# https://leetcode-cn.com/problems/string-to-integer-atoi/solution/zi-fu-chuan-zhuan-huan-zheng-shu-atoi-by-leetcode-/
class Solution:
    def get_col(self, c):
        if c.isspace():
            return 0
        if c.isdigit():
            return 1
        if c == "+" or c == "-":
            return 2
        return 3

    def myAtoi(self, s: str) -> int:
        if not s or len(s) == 0:
            return 0
        start = 0
        res = 0
        sign = 1
        now_stage = 0
        # 0-start, 1-sign,2-num,3-end
        stage = [[0, 2, 1, 3], [3, 2, 3, 3], [3, 2, 3, 3], [3, 3, 3, 3]]
        while start < len(s):
            val = s[start]
            val_type = self.get_col(val)
            now_stage = stage[now_stage][val_type]
            if now_stage == 0:
                pass
            elif now_stage == 1:
                if val == "+":
                    sign = 1
                else:
                    sign = -1
            elif now_stage == 2:
                res = res * 10 + int(val)
            else:
                return min(max(sign * res,-2**31),2**31-1)
            start += 1
        
        return min(max(sign * res,-2**31),2**31-1)

# class Solution:
#     def myAtoi(self, s: str) -> int:
#         return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 2**31 - 1), -2**31)

# 作者：QQqun902025048
# 链接：https://leetcode-cn.com/problems/string-to-integer-atoi/solution/python-1xing-zheng-ze-biao-da-shi-by-knifezhu/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
solu = Solution()
t =  "-91283472332"
print(solu.myAtoi(t))
