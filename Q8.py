class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes = set()
        for x in arr1:
            while x:
                prefixes.add(x)
                x //= 10

        best = 0
        for y in arr2:
            while y:
                if y in prefixes:
                    best = max(best, len(str(y)))
                    break
                y //= 10
        return best
