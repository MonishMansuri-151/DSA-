class Solution :
    def merge_sort(self,num1,num2): # two arr 
        n = len(num1)
        m = len(num2)
        i = 0
        j =0 
        res =[] # sotre the result 
        
        while i < n and j < m: 
            if num1[i] <= num2[j]:
                if len(res) == 0 or res[-1] != num1[i]: # check end element of result and check result =0
                    res.append(num1[i]) # add element answer
                i+=1 
                
            else:
                if len(res) == 0 or res[-1] != num2[j]: # agin check if agar j < i he to 
                    res.append(num2[j]) # add element 
                j+=1 
        if i < n :
            while i < n: # remaing element i  add result 
                  if len(res) == 0 or res[-1] != num1[i]:
                      res.append(num1[i])
                  i+=1 
                
        if j < m :
            while j <m:
                if len(res) == 0 or res[-1] != num2[j]:
                    res.append(num2[j])
                j+=1 
        return res
        
arr1=[1,1,1,2,4,6,7]
arr2=[1,2,3,4,5,6,7,8,9,10]
obj = Solution()
print(obj.merge_sort(arr1,arr2)) # call 
