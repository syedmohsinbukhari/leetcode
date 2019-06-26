class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_store = {}
        for i in range(len(nums)):
            index_store[target - nums[i]] = i
        for i in range(len(nums)):
            if (nums[i] in index_store.keys()):
                return [i, index_store[nums[i]]]
        return [-1, -1]  # solution does not exist
