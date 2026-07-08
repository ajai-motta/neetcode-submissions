class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen=set(nums)
        for num in seen:
            nums.remove(num)
        if nums:
            return True
        else:
            return False
        