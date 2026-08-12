# 2D matrix traverse 
matric = [[1,2,3],[4,5,6],[7,8,9]] # 3x3 = 9 
# itrate the matric 
rows = len(matric) 
col = len(matric[0])
for i in range(rows):
    for j in range(col):
        print(matric[i][j],end=" ") 
    print() 
    # basic 3D matric taraverse 

# ---------- print dignol triangle 

matric = [[1,2,3],[4,5,6],[7,8,9]] # 3x3 = 9 
# itrate the matric 
rows = len(matric) 
col = len(matric[0])
for i in range(rows):
    for j in range(col):
        if j>=i :
            print(matric[i][j],end=" ") 
        else:
            print("*",end=" ")
    print()  

# ------ lower triangle 


matric = [[1,2,3],[4,5,6],[7,8,9]] # 3x3 = 9 
# # itrate the matric 
rows = len(matric) 
col = len(matric[0])
for i in range(rows):
    for j in range(col):
        if i>=j :
            print(matric[i][j],end=" ") 
        else:
            print("*",end=" ")
    print() 
    

# print the ---- Diagonal 

matric = [[1,2,3],[4,5,6],[7,8,9]] # 3x3 = 9 
# itrate the matric 
rows = len(matric) 
col = len(matric[0])
for i in range(rows):
    for j in range(col):
        if j==i :
            print(matric[i][j],end=" ") 
        else:
            print("*",end=" ")
    print()  
    
    
#---------------------------- Trasform the matric 
matric = [[1,2,3],[4,5,6]] # 3x3 = 9 
# itrate the matric 
rows = len(matric) 
col = len(matric[0])
result = [[0]*rows for i in range(col)]
for i in range(rows):
    for j in range(col):
        result[j][i] = matric[i][j]
        
print(result) 
