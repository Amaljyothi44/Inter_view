class Solutions():
    def to_array(self, string):
        arr=[]
        for item in string[1:-1].split(","):
            arr.append(int(item.strip()))
        return arr
    def Strip(self, arr,k):
        new_arr = [item for item in arr if item != k]
        count = len(arr)- len(new_arr)
        print(f"{count} num = {new_arr}")

    def __init__(self):
        self.string1 = input()
        self.arr = self.to_array(self.string1)
        self.k = int(input())
        self.Strip(self.arr, self.k)


if __name__ == "__main__" :
    solution = Solutions()
