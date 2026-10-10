class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums = set(numbers)
        for num in nums:
            if target - num in nums:
                if target - num == num and numbers.count(num) >1:
                    temp = numbers.index(num)
                    numbers.pop(numbers.index(num))
                    if numbers.index(num) >= temp:
                        return [temp+1,numbers.index(num) +2]
                    else:
                        return [numbers.index(num)+1, temp+1]
                elif target - num == num and numbers.count(num) == 1:
                    continue
                else:
                    return [min(numbers.index(num)+1,numbers.index(target - num)+1), max(numbers.index(num)+1,numbers.index(target - num)+1)]