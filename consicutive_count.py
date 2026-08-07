# consicutive max count in arrray 
count = 0 
arr = [1,0,1,0,1,0,1,0] 
max_count =0
for i in range(len(arr)-1):
    if arr[i] == arr[i+1]:
        count+=1
        max_count = max(max_count,count) 
    else:
        count = 0
print(max_count)
