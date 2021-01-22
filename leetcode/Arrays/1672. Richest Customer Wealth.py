 #   https://leetcode.com/problems/richest-customer-wealth/


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        rich = 0
        N = len(accounts)
        
        for i in accounts:
            rich = max(rich, sum(i))
        
        return rich