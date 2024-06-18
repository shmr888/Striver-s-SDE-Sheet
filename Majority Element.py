class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict={}
        count = 0
        n=len(nums)

        for i in nums : 
            if i in dict:
                dict[i]+=1
            else :
                dict[i]=1

        for i in nums:
            if dict[i]>n//2:
                return i
