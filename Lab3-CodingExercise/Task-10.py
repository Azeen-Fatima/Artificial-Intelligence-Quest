m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))
array = [[i*j for j in range(n)] for i in range(m)]
print(array)