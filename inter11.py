
def isSubsequence(t_set, s_set):
    if all(char in t_set for char in s_set):
        return True
    else:
        return False
    
def main():
    string1 = input()
    string2 = input()
    s_set = set(string1)
    t_set = set(string2)
    print(isSubsequence(t_set, s_set))

if __name__ == "__main__":
    main()
