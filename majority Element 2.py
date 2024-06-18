class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        minCount = int(len(nums)/3)
        ret = []
        countMap = Counter(nums)
        for i in countMap:
            if countMap[i] > minCount:
                ret.append(i)
        return ret
