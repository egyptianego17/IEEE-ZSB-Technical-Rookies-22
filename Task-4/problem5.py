n = int(input("enter the number of rows and columns of the matrix: "))
matrix = []
first_diagonal = 0
second_diagonal = 0
for lista in range(0,n):
    matrix.append(input("").split())
for lista1 in range(0,n):
    first_diagonal = first_diagonal + int(matrix[lista1][lista1])
    second_diagonal = second_diagonal + int(matrix[n-lista1-1][lista1])
final_result = first_diagonal - second_diagonal
print(final_result)