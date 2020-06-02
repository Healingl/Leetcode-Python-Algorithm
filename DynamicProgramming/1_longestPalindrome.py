class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s is None:
            return s

        if len(s) == 0 or len(s) > 1000:
            return ''

        n = len(s)
        # 创建dp table
        dp = [[False] * n]*n

        ans = ""
        # 遍历dp table， l表示回文字符串长度
        for l in range(n):
            # 枚举子串的起始位置 i，这样可以通过 j=i+l 得到子串的结束位置
            for i in range(n):
                # 遍历右上角的dp table
                j = i + l

                # 边界条件
                if j >= len(s):
                    break

                # l == 0 时， j =i+0 =i，处于对角线
                if l == 0:
                    dp[i][j] = True
                # l == 1 时， j =i+1，字符串长度为2
                elif l == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (dp[i+1][j-1] and s[i] == s[j])

                # 如果dp table对应i，j坐标的值为true，并且回文字符串长度大于ans，则更新ans
                if dp[i][j] and l + 1 > len(ans):
                    ans = s[i:j + 1]

        return ans