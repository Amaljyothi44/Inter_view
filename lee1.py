def swapchar():
    wd1 = input("Enter the String :")
    wd2 = input("Enter the string :")

    n = len(wd1) if len(wd1)>len(wd2) else len(wd2)
    word=[]
    for i in range(n):
        print(i)
        if len(wd1)>i:
            word.append(wd1[i])
        else:
            pass
        if len(wd2)>i:
            word.append(wd2[i])
        else :
            pass
    output= "".join(word)
    print(output)

swapchar()


