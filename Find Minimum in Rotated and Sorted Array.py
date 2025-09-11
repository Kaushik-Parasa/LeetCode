#Find Minimum in Rotated and Sorted Array
class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums.sort()
        return nums[0]
    