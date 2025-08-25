import sys
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        max_sum = -sys.maxsize
        for i in range(n-k+1):
            current = 0 
            for j in range(k):
                current += arr[i+j]
            
            max_sum = max(current,max_sum)
        return max_sum
    
nums = [1,5,4,2,9,9,9]
k = 3