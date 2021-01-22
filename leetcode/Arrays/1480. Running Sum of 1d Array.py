#https://leetcode.com/problems/running-sum-of-1d-array/
 
class Solution(object):
    def runningSum(self, nums):
        
        a = 0
        lst = []
        for i in nums:
            a = i+a
            lst.append(a)
        return(lst)    