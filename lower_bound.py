# found the lower bound in sorted arrray 
def lower_bound(arr):
  lb = -1 
  low = 0
  high = len(arr)-1
  target = 3
  while low <= high:
    mid = (low+high)//2
    if arr[mid] >= target :
      lb = mid 
      high = mid-1
    else:
      low = mid+1
  return lb


arr = [1,1,1,2,3,3,5,6,7,7,7,9,12,13]
print(lower_bound(arr))
--------------------> 
