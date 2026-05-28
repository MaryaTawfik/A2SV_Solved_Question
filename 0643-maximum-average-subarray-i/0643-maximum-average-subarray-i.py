class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum=0
        for i in range(k):
            max_sum+=nums[i]

        left=0

        current_sum=max_sum
        for right in range(k,len(nums)):
            current_sum+=nums[right]
            current_sum-=nums[left]
            left+=1
            max_sum = max(current_sum,max_sum)
        
        return max_sum/k


        
        







