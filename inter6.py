class Solution:
    def to_arr(self, string):
        arr = []
        for item in string[1:-1].split(","):
            arr.append(int(item.strip()))
        return arr
    def Right_rotate(self , array, k):
        n = len(array)
        new_arr = array.copy()
        for index, value in enumerate(array):
            check = index+k+1
            if check > n:
                val_index = check-n-1
                new_arr[val_index]=value
            else :
                val_index = index + k
                new_arr[val_index]= value

        print(new_arr)

    def __init__(self):
        self.string = input()
        array = self.to_arr(self.string)
        self.k = int(input())
        self.Right_rotate(array, self.k)

if __name__ == "__main__":
    solution = Solution()
