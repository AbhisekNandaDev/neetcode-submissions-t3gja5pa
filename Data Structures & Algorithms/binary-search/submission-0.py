class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start=0
        end = len(nums)-1

        while start <= end:

            mid = start+(end-start)//2
            print(mid)

            if target > nums[mid]:
                start = mid+1
                print("second half")
            elif target < nums[mid]:
                end = mid-1
                print("first half")


            else:
                return mid

        return -1

        