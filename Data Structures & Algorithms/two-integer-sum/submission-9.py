class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        two_map = {}

        for i, n in enumerate(nums):
            d = target - n
            if d in two_map:
                return [two_map[d], i]
            two_map[n] = i