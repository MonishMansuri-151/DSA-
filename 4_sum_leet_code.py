# this is my brute force solution 
# 4 sum leet code problem 
class Solution :
    def sum_array(self,nums):
        my_set = set()
        my_list = []
        n = len(nums)
        for i in range(0,n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    for l in range(k+1,n):
                        if nums[i] + nums[j] + nums[k]+nums[l] == 0:
                            my_list = [nums[i],nums[j],nums[k],nums[l]] 
                            my_list.sort()
                            my_set.add((tuple(my_list)))
        result =[]                    
        for ans in my_set:
            result.append(ans) 
        return result    
    
nums = [1,0,-1,0,-2,2] 
obj = Solution() 
print(obj.sum_array(nums)) 

# ---------------------------------------- optimal solution --------------------------------------------------------------
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n = len(nums) 
        ans = []
        nums.sort() 
        for i in range(0,n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,n):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue 
                k = j+1
                l = n-1
                while k < l:
                    total = nums[i]+nums[j]+nums[k]+nums[l]
                    if total == target :
                        ans.append([nums[i],nums[j],nums[k],nums[l]])
                        k = k+1
                        l = l-1
                        while k < l and nums[k] == nums[k-1]:
                            k+=1
                        while l > k and nums[l] == nums[l+1]:
                            l-=1 
                    elif total < target:
                        k+=1
                    else:
                        l-=1
        return ans   
    
nums = [-3,-2,-1,0,0,1,2,3] 
target = 0
obj = Solution()
print(obj.fourSum(nums,target)) 

# time complexity = o(n2xn) = o(n)
# sapce = o(ans)
