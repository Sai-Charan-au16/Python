#  https://leetcode.com/problems/shuffle-the-array/

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        mid = n
        i = 0
        ans = []
        while i < n:
            ans.append(nums[i])
            i += 1
            ans.append(nums[mid])
            mid += 1
        return ans   