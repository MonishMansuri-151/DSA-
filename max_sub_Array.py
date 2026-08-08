# brute force approch 
def fun (arr):
    maxi = float("-inf")
    for i in range(len(arr)):
        total = 0
        for j in range(i,len(arr)):
            total += arr[j]
            maxi =  max (maxi, total)
    return maxi
    
arr =[-2,1,-3,4,-1,2,1,-5,4]  
print(fun(arr))  

# optimal approch 
def fun (arr):
    maxi = float("-inf")
    total = 0
    for i in range(len(arr)):
       total += arr[i]
       maxi = max(maxi,total) 
       if total < 0:
           total =0
    return maxi
          
    
arr =[-2,1,-3,4,-1,2,1,-5,4]  
print(fun(arr))  

TM = (n)
space = (1)
