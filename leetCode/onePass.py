class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #Titled previous map because it's basically every element that comes before the current one
        # We're going to map the value to the current index of that value
        prevMap = {} # val : index
        
        # We need the index as well as the value of that number
        for i, n in enumerate(nums):
            #Before we add it to our map lets check if the difference is already in the has map.
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return