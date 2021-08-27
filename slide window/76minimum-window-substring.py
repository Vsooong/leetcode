from collections import Counter


# class Solution:
# #   https://leetcode-cn.com/problems/minimum-window-substring/solution/zui-xiao-fu-gai-zi-chuan-by-leetcode-solution/

#     def minWindow(self, s: str, t: str) -> str:
#         min_len = float("inf")
#         min_start = -1
#         start = 0
#         end = 0
#         tCounter = Counter(t)
#         cCounter = Counter()

#         while end < len(s):
#             val = s[end]
#             if val in tCounter:
#                 cCounter[val] += 1
#                 while len(tCounter - cCounter) == 0:
#                     cur_len = end - start
#                     if cur_len < min_len:
#                         min_len = cur_len
#                         min_start = start
#                     if s[start] in tCounter:
#                         cCounter[s[start]] -= 1
#                     start += 1


#             end += 1
#         if min_start > -1:
#             return s[min_start: min_start + min_len+1]
#         return ""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_len = float("inf")
        min_start = -1
        start = 0
        end = 0
        tCounter = Counter(t)
        n = len(t)
        while end < len(s):
            val = s[end]
            if tCounter[val] > 0:
                n -= 1
            tCounter[val] -= 1

            while n == 0:
                cur_len = end - start
                if cur_len < min_len:
                    min_len = cur_len
                    min_start = start
                if tCounter[s[start]] ==0:
                    n += 1
                tCounter[s[start]]+=1
                start += 1

            end += 1

        if min_start > -1:
            return s[min_start : min_start + min_len + 1]
        return ""


solution = Solution()

s = "ADOBECODEBANC"
t = "ABC"
print(solution.minWindow(s, t))
