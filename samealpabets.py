def same_alp():
    name1 = input("Enter the Name 1 :")
    name2 =  input("Enter the Name2 : ")
    s1 = set(name1.lower())
    s2 = set(name2.lower())

    same = s1 & s2
    print(same)

same_alp()