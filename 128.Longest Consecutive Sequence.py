
def longestConsecutive(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #nums.sort()

        nums=set(nums)
        counter = 0
        
        if len(nums) == 0:
            return 0
        for i in nums:
            if i-1 not in nums:
                new_count=1
                while i+1 in nums:
                    i+=1
                    new_count +=1
                counter = max(counter,new_count)

                    

        return counter
