def rectangle(m, n):
   
    for i in range(m):
        print('*' * n)


m = int(input("Enter the number of rows (m): "))
n = int(input("Enter the number of columns (n): "))


rectangle(m, n)