import sys 
# https://leetcode-cn.com/problems/reverse-integer/solution/zheng-shu-fan-zhuan-by-leetcode-solution-bccn/
class Solution:
    def reverse(self, x: int) -> int:
        dir=1
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if x<0:
            dir=-1
            string=str(x)[1:]
        else:
            string=str(x)
        string = string[::-1]
        res=int(string)*dir
        if res<INT_MIN or res> INT_MAX:
            res=0 
        return res 
    
    def math_reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        rev = 0
        while x != 0:
            # INT_MIN 也是一个负数，不能写成 rev < INT_MIN // 10
            if rev < INT_MIN // 10 + 1 or rev > INT_MAX // 10:
                return 0
            digit = x % 10
            # Python3 的取模运算在 x 为负数时也会返回 [0, 9) 以内的结果，因此这里需要进行特殊判断
            if x < 0 and digit > 0:
                digit -= 10

            # 同理，Python3 的整数除法在 x 为负数时会向下（更小的负数）取整，因此不能写成 x //= 10
            x = (x - digit) // 10
            rev = rev * 10 + digit
        
        return rev

solu=Solution()
t=-12340000
print(solu.reverse(t))