# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

# brute force solution use extra variable 
# usign (n-1)-1 = formula n = 4-1 =3 and 3-i= 3-0 = 3 so on conitune reduce size   
#______________________________________  

def rotate_matrix(matrix):
    n = len(matrix) 
    m = len(matrix[0]) 
    result = [[0 for _ in range(n)] for _ in range(n)] 
    for i in range(n):
        for j in range(m):
            result[j][(n-1)-i] = matrix[i][j] 
    return result



matrix = [[1,2,3],[4,5,6],[7,8,9]] 
print(rotate_matrix(matrix)) 
# Time complexity = o(n 2) 
# space compexity = o(n 2) 
# ____________________ output 
# [[7, 4, 1],
# [8, 5, 2], 
# [9, 6, 3]] 

#------------------------------------------------------------------------------------------------>optimal solution 
# roated array inplace  

 
def rotate_matrix(matrix):
    n = len(matrix) 
    m = len(matrix[0]) 
    for i in range(n):
        for j in range(i+1,m):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        matrix[i].reverse() 
    return matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]] 
print(rotate_matrix(matrix))  

# [[7, 4, 1], 
#  [8, 5, 2],            output       <-------------------------------
#  [9, 6, 3]] 

# time complexity = o(nxm) + o(nxm) = o(n2) 
# space complexity = o(1)
