class Solution:
    """
    PATTERN: Hash Set (Existence check)
    AHA: len(set) < len(arr) means a duplicate exists.
    COMPLEXITY: O(n) Time | O(n) Space
    """
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)