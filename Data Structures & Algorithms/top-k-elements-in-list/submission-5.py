class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if nums != []:
            highest_element = nums[0]
            
            result={}
            elements={}

            for i in nums:
                if i in elements:
                    elements[i] = elements[i] +1
                    if elements[highest_element] < elements[i]:
                        highest_element = i
                else:
                    elements[i] =1

            shoted_data =top_k = [key for key, value in sorted(elements.items(), key=lambda item: item[1], reverse=True)[:k]]

            return shoted_data
        else:
            return []
        