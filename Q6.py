class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        if (m + n - 1) % 2 == 1:
            return False
        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False

        cap = (m + n - 1) // 2
        mask = (1 << (cap + 1)) - 1   # keep balances 0..cap

        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    reach = 1          # balance 0 before the first char
                else:
                    reach = 0
                    if i > 0:
                        reach |= dp[i - 1][j]
                    if j > 0:
                        reach |= dp[i][j - 1]

                if grid[i][j] == '(':
                    reach = (reach << 1) & mask
                else:
                    reach >>= 1

                dp[i][j] = reach

        return (dp[m - 1][n - 1] & 1) == 1   # balance 0 at the end
