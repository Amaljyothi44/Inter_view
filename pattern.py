n = int(input("Enter the value of n: "))
for i in range(n):
    for j in range(i):
        print("  ", end="")
    for k in range(i, n):
        print(k + 1, end="  ")
    print()
for i in range(n - 2, -1, -1):
    for j in range(i):
        print("  ", end="")
    for k in range(i, n):
        print(k + 1, end="  ")
    print()
