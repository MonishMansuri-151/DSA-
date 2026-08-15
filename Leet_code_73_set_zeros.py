# leet code 73 medium problem set metrix zeroes   
def set_infinity(matrix,rows,cols):
    n  = len(matrix) 
    m = len(matrix[0]) 
    for i in range (0,n):
        if matrix[i][cols] != 0:
            matrix[i][cols] = float("inf") 
    for j in range(0 ,m):
        if matrix[rows][j] !=0:
            matrix[rows][j] = float("inf") 
        
def set_zeros(matrix): 
    n = len(matrix) 
    m = len(matrix[0]) 
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                set_infinity(matrix,i,j)
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == float("inf"):
                matrix[i][j] = 0  
    return matrix

matrix = [[1,1,1],[1,0,1],[1,1,1]]  
print(set_zeros(matrix))   

# time complexity = o((n + m) x (n x m)) + (nxm) 
# -------------------------------------------------------------------------------------------------------
# optimal solution of set matrix zeros 

def set_zeros(matrix): 
    row = len(matrix) 
    col = len(matrix[0])
    row_trak = [0 for _ in range(row)] 
    col_trak = [0 for _ in range(col)]  
    for i in range(row):
        for j in range(col):
            if matrix [i][j] == 0:
                row_trak[i] =-1
                col_trak[j] = -1
    for i in range(row):
        for j in range(col):
            if row_trak [i] == -1 or col_trak[j] == -1:
                matrix[i][j] =0
    return matrix 
    
matrix = [[1,1,1],[1,0,1],[1,1,1]]  
print(set_zeros(matrix))  

# ========================== both code ouput same 
# output -> [[1, 0, 1]
#           [0, 0, 0],
#           [1, 0, 1]] 


# optimal code time compelxity :- o(2(row x col)) => o(row x col)
# space complexity => (row + col) 

# Brute force: For every zero, I traverse its entire row and column and mark the elements as infinity. 
# Then I convert all infinity values to zero. This takes O(n × m × (n + m)) time.

# Better approach: I first store which rows and columns contain zero using two tracking arrays.
# Then I traverse the matrix again and set an element to zero if its row or column is marked.
# This reduces the time complexity to O(n × m), with O(n + m) extra space.
