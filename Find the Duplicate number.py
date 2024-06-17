def findDuplicate(nums):
    sample = {}
    for i in nums:
        print(sample)
        if i in sample:
            return i
        else:
            sample[i] = 1


sample_input = [2,4,3,4,1]
print(findDuplicate(sample_input))


