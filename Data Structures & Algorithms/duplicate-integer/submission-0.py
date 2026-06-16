class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums1 = set(nums)

        return len(nums1) != len(nums)