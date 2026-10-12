from math import ceil as ceil
from math import floor as floor
class Solution:
    def findMin(self, nums: List[int]) -> int:
        ep1 = 0
        epm = math.floor(len(nums)/2)
        ep2 = len(nums) - 1
        while True:
            if nums[epm] > nums[ep2]:
                if abs(epm - ep2) <= 1:
                    return min(nums[epm],nums[ep2])
                ep1 = epm
                epm = math.floor((ep2 + epm) /2)
            else:
                if abs(epm - ep1) <= 1:
                    return min(nums[ep1],nums[epm])
                ep2 = epm
                epm = math.floor((epm + ep1) /2)
            
                





        