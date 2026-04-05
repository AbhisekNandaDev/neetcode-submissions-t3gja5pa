class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        unique_items=[]

        for i in nums:
            if i in unique_items:
                return True
            else:
                unique_items.append(i)
        
        return False

         