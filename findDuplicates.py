def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        d = {}
        
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
                return num