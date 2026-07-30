class Solution:
    def quickSort(self, arr, low, high):
        # code here 
        if low < high:
            indx_j = self.partition(arr,low,high)
            
            self.quickSort(arr,low,indx_j-1)
            self.quickSort(arr,indx_j+1,high)

    def partition(self, arr, low, high):
        # code here 
        i = low 
        j = high 
        pivot = arr[low] 
        while i < j :
            while arr[i] < pivot and arr[i] < high-1:
                 i+=1
            while arr[j] > pivot  and arr[j] > low+1:
                j = j-1
                
            if i < j:
                
                arr[i],arr[j] = arr[j],arr[i] 
        arr[low],arr[j] = arr[j],arr[low]
        return j 
        
arr = [4,1,3,9,7]
obj = Solution() 
print(obj.quickSort(arr,0,len(arr)-1)) 

output = 1 3 4 7 9 
time complexity =  (n log n) best case 
time complexity = (n 2) worset case 

