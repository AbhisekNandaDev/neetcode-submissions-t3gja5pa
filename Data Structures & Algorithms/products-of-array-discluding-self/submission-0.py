import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lens=len(nums)
        i=0
        res=[]
        while i<lens:
            if i!=0:

                before = nums[:i]
                after = nums[i+1:]
                res.append(math.prod(before+after))
            else:
                after = nums[1:]
                res.append(math.prod(after))

            i=i+1
        return res

        
