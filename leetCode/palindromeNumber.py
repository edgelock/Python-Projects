class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        #Basic check to see if the number is less than 0
        if x < 0: return False
        #Set the divider value.
        #It could be 10,100...

        div = 1
        #If our x is greater than 10 time the div we'll increase the div
        while x >= 10 * div:
            div *= 10 
        
        while x:
            #How to get the right digit
            right = x % 10
            #How to get the left digit
            left = x // div
            #Check if left does NOT equal right
            if left != right: return False
            #Chop off the left and right digit
            x = (x % div) // 10
            #Chop off 2 digits from the div
            div = div / 100 
        return True