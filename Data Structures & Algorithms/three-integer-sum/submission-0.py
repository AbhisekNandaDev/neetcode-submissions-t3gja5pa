from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                total = a + nums[l] + nums[r]

                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    # found a triplet
                    res.append([a, nums[l], nums[r]])

                    # move both pointers
                    l += 1
                    r -= 1

                    # skip duplicates for left pointer
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    # skip duplicates for right pointer
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

        return res
