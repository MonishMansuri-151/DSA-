# Description:
# This program implements the Merge Sort algorithm using recursion. The mergeSort() 
# function divides the input array into two halves until each subarray contains only one element.
# After dividing, the merge_Array() function merges the sorted subarrays into a single sorted array by comparing elements one by one. 
# Finally, the completely sorted array is returned.
class Solution:
    def mergeSort(self, arr):
    # code here
        # merge sort  
        if len(arr)<=1 :
            return arr
        mid = len(arr)//2 # convert two array 
        left_half = arr[:mid]
        right_half = arr[mid:]
        left =self.mergeSort(left_half) # using recursion 
        right = self.mergeSort(right_half)
        return self.merge_Array(left,right)
        
    def merge_Array(self ,left,right): 
        n = len(left) 
        m = len(right)
        i =0 
        j =0
        res = [] 
        while i < n and j < m :
            if left[i] < right[j]:
                res.append(left[i])
                i = i+1
            else:
                res.append(right[j]) 
                j=j+1
        if i<n:
            while i < n:
                res.append(left[i]) 
                i=i+1
        if j < m:
            while j < m:
                res.append(right[j])
                j =j+1
        return res  
        
        
arr = [4,1,3,9,7]
obj = Solution() 
print(obj.mergeSort(arr))
