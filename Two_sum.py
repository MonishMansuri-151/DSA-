# using two pointer approch 

# brute froce approch 
def tow_sum (arr,target):
    for i in range(len(arr)) :
        for j in range(len(arr)):
            total = 0 
            total = arr[i] + arr[j]
            if total == target:
                return [i,j]
        
arr=[5,9,1,2,4,15,6,3]
target = 13 
print(tow_sum(arr,target))        


#----------------------------------------------------------------
#optimal solution 

def tow_sum (arr,target):
  my_dict = {}
  for i in range(len(arr)):
      remaning = target - arr[i]
      if remaning in my_dict:
          return [my_dict[remaning],i]
      else:
          my_dict[arr[i]] = i 
        
arr=[5,9,1,2,4,15,6,3]
target = 13 
print(tow_sum(arr,target))    

# time and space complexity 

# Tc = (N) 
# space = (N)
