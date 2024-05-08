class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n=len(nums)
        nums.append(target)
#        for i in range(n):
 #           for j in range(0,n-i-1)
  #              if(nums[j])
        nums.sort()
        return nums.index(target) 