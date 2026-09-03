class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapp = {}
        
        for ind, n in enumerate(nums):
            diff = target - n
            if diff in mapp:
                return [mapp[diff], ind]
            mapp[n] = ind
