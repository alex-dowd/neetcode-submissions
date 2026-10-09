class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        zero = 0
        prod = 1
        for i in nums:
            if i != 0:
                prod = prod * i
            else:
                zero +=1
        for i in nums:
            if zero == 1 and i == 0:
                out.append(prod)
            elif zero >1:
                out.append(0)
            elif zero == 1 and i != 0:
                out.append(0)
            else:
                out.append(int(prod/i))
        return out

        