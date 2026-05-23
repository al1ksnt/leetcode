class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int] | None:
        seen = dict()
        for i, n in enumerate(nums):
            goal = target - n
            if goal in seen:
                return [seen[goal], i]
            seen[n] = i
