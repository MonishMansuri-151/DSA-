# 3 sum brute froce solution   
# Given an integer array nums, return all the triplets 
# [nums[i], nums[j], nums[k]] such that i != j, i != k,
# and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.
# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
def triplets (nums):
    n= len(nums)
    my_set = set() 
    for i in range(0,n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if nums[i] + nums[j] + nums[k] == 0:
                    temp =[nums[i],nums[j],nums[k]] 
                    my_set.add(tuple(temp)) 
    return [list(ans) for ans in my_set]


nums = [-1,0,1,2,-1,-4] 
print(triplets(nums))  

# time complexity  = o(n 3)  cube 

#=============================================================== 
# optimal solution 

class Solution(object):
    def threeSum(self, lis):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        lis.sort()
        size = len(lis)
        ans = []
        for i in range(size):
            if i > 0 and lis[i] == lis[i - 1]:
                continue
            j = i + 1
            sum = 0
            k = len(lis) - 1
            while j < k:
                sum = lis[i] + lis[j] + lis[k]
                if sum < 0:
                    j = j + 1
                elif sum > 0:
                    k = k - 1
                else:
                    ans.append([lis[i], lis[j], lis[k]])
                    j = j + 1
                    k = k - 1
                    while j < k and lis[j] == lis[j - 1]:
                        j = j + 1
        return ans
