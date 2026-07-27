# my first code insertion sort in DSA series 
class Solution(object):
    def sortArray(self, nums):
        for i in range(1,len(nums)):
            key = nums[i]
            j = i-1
            while j >=0 and nums[j]>key:
                nums[j+1] = nums[j]
                j=j-1
            nums[j+1] = key 
        return nums  
nums = [1,4,6,7,2,3,70,32]
obj = Solution()
print(obj.sortArray(nums))
