# brute force approch 
def rearrange(nums):
    pos = [5,10,6]
    neg = [-3,-1,-10]
    for i in range(len(pos)):
        # this the  formula 
        # [2xi]  = positve 
        #[(2xi)+1] = negative 
        nums[2*i] = pos[i] 
        nums[(2*i)+1] = neg[i] 
    return nums
nums = [5,10,-3,-1,-10,6] 

print(rearrange(nums))
# time complexity = (n(n+1)/2) 
# space = o(n)
#-------------------------------------------------------------- 
# optimal 

def rearrange(nums):
   n = len(nums) 
   pos_index = 0 
   neg_index = 1 
   result = [0]*n
   for i in range(n):
       if nums[i] >= 0:
           result[pos_index] = nums[i]
           pos_index +=2
       else:
           result[neg_index] = nums[i]
           neg_index +=2 
           
   return result
nums = [5,10,-3,-1,-10,6] 
print(rearrange(nums))

#timecomplexity = O(n) 
#space = 0(n)
