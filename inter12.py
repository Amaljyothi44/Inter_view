def to_arr(string):
    arr = []
    for item in string[1:-1].split(","):
        arr.append(int(item.strip()))
    return arr

def twoSum(array, target):
    for index1, value1 in enumerate(array):
        for index2, value2 in enumerate(array):
            if value1 + value2 == target and index1 != index2:
                return [index1, index2]
    return "can't find"
                

def main():
    string = input()
    array = to_arr(string)
    target = int(input())
    print(twoSum(array, target))

if __name__ == "__main__":
    main()