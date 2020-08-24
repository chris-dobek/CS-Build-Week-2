'''
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
'''
def containsDuplicate(self, nums: [int]) -> bool:
        d = {}
        for number in nums:
            if number not in d: 
                d[number] = 1
            else:
                d[number] += 1
                return True
        return False
        

