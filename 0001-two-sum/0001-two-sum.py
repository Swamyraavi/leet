class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        j=0
        k=[]
        for i in range(0,len(nums)-1):
            for j in range(1,len(nums)):
                if(i==j):
                    j=j+1;
                if(nums[i]+nums[j]==target):
                    k.append(i)
                    k.append(j)
                    return k