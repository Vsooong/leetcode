class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        slide_window = set()
        max_len = 0
        length = len(s)
        cur_len = 0
        left = 0
        for i in range(length):
            cur_len += 1
            if s[i] in slide_window:
                while s[i] in slide_window:
                    slide_window.remove(s[left])
                    left += 1
                    cur_len -= 1

            slide_window.add(s[i])
            if cur_len > max_len:
                max_len = cur_len

        return max_len


# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/solution/hua-dong-chuang-kou-by-powcai/

solution = Solution()
s = "sdfsdee"
print(solution.lengthOfLongestSubstring(s))
