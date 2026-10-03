class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_num_to_idx = {}
        for i, num in enumerate(nums):
            if (target-num) in map_num_to_idx:
                return [map_num_to_idx[target-num], i]
            map_num_to_idx[num] = i