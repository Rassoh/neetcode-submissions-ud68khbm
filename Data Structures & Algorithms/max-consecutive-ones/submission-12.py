class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxc = 0
        for n in nums:
            if n == 0:
                count = 0 
            elif n == 1:
                count+=1
            if count > maxc:
                maxc = count
            print(count)
        return maxc