class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        largest_side=0
        
        largest_perimeter=float(-inf)
        for i in range(0,len(nums)-2):
            largest_side=nums[i]
            two_sum=nums[i+1] + nums[i+2]
            if two_sum > largest_side:
                largest_perimeter=max(largest_perimeter,two_sum+largest_side)
                break
        if largest_perimeter<0:
            return 0
        else:
            return largest_perimeter


       