class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # Range-add / range-sum BIT (1-indexed) using two trees
        b1 = [0] * (n + 2)
        b2 = [0] * (n + 2)

        def upd(i, v1, v2):
            while i <= n:
                b1[i] += v1
                b2[i] += v2
                i += i & -i

        def prefix(i):
            s1 = s2 = 0
            k = i
            while k > 0:
                s1 += b1[k]
                s2 += b2[k]
                k -= k & -k
            return s1 * i - s2

        last = {}
        cur = 0   # current sum of d[i]^2 for i <= j
        ans = 0

        for j, x in enumerate(nums):
            l = last.get(x, -1) + 1      # 0-indexed start of the range
            L, R = l + 1, j + 1          # convert to 1-indexed
            rng_sum = prefix(R) - prefix(L - 1)

            cur += 2 * rng_sum + (R - L + 1)

            # range add +1 on [L, R]
            upd(L, 1, L - 1)
            if R + 1 <= n:
                upd(R + 1, -1, -R)

            last[x] = j
            ans += cur

        return ans % MOD
