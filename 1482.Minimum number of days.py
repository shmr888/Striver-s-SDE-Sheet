class Solution(object):
    def possible(self,arr, day, m, k):
        n = len(arr)  
        cnt = 0
        noOfB = 0
        
        for i in range(n):
            if arr[i] <= day:
                cnt += 1
            else:
                noOfB += cnt // k
                cnt = 0
        noOfB += cnt // k
        return noOfB >= m

    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """

        val = m * k
        n = len(bloomDay)  # size of the array
        if val > n:
            return -1  # impossible case

        mini = float('inf')
        maxi = float('-inf')
        for i in range(n):
            mini = min(mini, bloomDay[i])
            maxi = max(maxi, bloomDay[i])


        low = mini
        high = maxi
        while low <= high:
            mid = (low + high) // 2
            if self.possible(bloomDay, mid, m, k):
                high = mid - 1
            else:
                low = mid + 1
        return low
