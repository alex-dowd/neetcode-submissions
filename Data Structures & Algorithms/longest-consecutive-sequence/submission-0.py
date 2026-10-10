class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = sorted(set(nums))

        streak = 1
        longest = 1

        for i in range(len(nums) - 1):
            if nums[i] + 1 == nums[i + 1]:
                streak += 1
            else:
                longest = max(longest, streak)
                streak = 1

        longest = max(longest, streak)

        return longest
          
        
            


