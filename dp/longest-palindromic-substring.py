class Solution:
    def longestPalindrome(self, s: str) -> str:
        begin = 0
        max_len = 1
        n = len(s)
        if n == 1:
            return s
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        for L in range(2, n + 1):
            for i in range(n):
                j = i + L - 1
                if j >= n:
                    break
                if s[i] == s[j]:
                    if j - i <3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = False
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    begin = i

        # return dp
        return s[begin : begin + max_len]


solution = Solution()
s = "cbbadllhlldaedd"
print(solution.longestPalindrome(s))
