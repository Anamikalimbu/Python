class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""
        nines, rem = divmod(sum, 9)
        digits = "9" * nines
        if rem:
            digits += str(rem)
        digits += "0" * (num - len(digits))
        return digits
