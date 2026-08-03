# brute froce approch 

# arr = [1,0,2,4,3,0,0,3,5,1] 
# temp = []
# for i in range(len(arr)):
#     if arr[i] != 0:
#         temp.append(arr[i]) 
# for j in range(len(temp)): 
#     arr[j] = temp[j]  

# for j in range(len(temp),len(arr)):
#     arr[j] = 0
        
# print(arr) 

# -- optimal two pointer approch 

def fun (arr):
  right =0
  left =0 
  while left < (len(arr)):
      if arr[left] == 0:
        break
      left +=1
  if left == len(arr):
    return 
  right = left+1
  while right < len(arr):
      if arr[right] != 0:
          arr[left],arr[right] = arr[right],arr[left] 
          left +=1
      right+=1
  return arr
arr = [1,0,2,4,3,0,0,3,5,1]  
print (fun(arr))
