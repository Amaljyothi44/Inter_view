for i in range(5 - 2, -1, -1):
    for j in range(i):
        print("  ", end="")
    for k in range(i, 5):
        print(k + 1, end="  ")
    print()