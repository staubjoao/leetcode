from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:  # O(n²)
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return [i, j]


s = Solution
print(s.twoSum(s, [3, 2, 4], 6))
