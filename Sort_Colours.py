lass Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c0=c1=c2=0
        
        for i in nums:
            if i == 0:
                c0+=1
            elif i == 1:
                c1+=1
            elif i == 2:
                c2+=1
        
        for j in range(c0):
            nums[j] = 0
        for j in range(c1):
            nums[j+c0]=1
        for j in range(c2):
            nums[j+c0+c1] =2

        return nums
