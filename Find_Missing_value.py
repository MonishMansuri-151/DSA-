
def missing (nums):
    #== brute force approch 
    for i in range(len(nums)):
        if i not in nums:
            return i
    
nums = [9,6,4,2,3,5,7,0,1]
print(missing(nums))  

# batter approch 
def fun (nums):
    dicts = {} 
    for i in range(len(nums)):
        dicts[i] = 0 
    for i in nums:
        dicts[i] = 1 
    for k,v in dicts.items():
        if v == 0:
            return k 

nums  = [9,6,4,2,3,5,7,0,1]
print(fun(nums))


# optimal solution 
def missing (nums):
    n = len(nums)
    return (n*(n+1))//2 - sum(nums)
    
nums  = [9,6,4,2,3,5,7,0,1]
print(missing(nums))
