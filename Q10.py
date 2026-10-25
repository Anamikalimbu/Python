class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        less = sum(1 for n in nums if n < target)
        equal = sum(1 for n in nums if n == target)
        return list(range(less, less + equal))
