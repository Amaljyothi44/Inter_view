class Solution:
    def to_arr(self, string):
        arr=[]
        for item in string[1:-1].split(","):
            arr.append(int(item.strip()))
        return arr
    def duplication(self,arr):
        for item in arr :
            index_arr= [index for index, value in enumerate(arr) if value == item]
            n = len(index_arr)
            if n >2:
                for index in index_arr[2:n]:
                    arr.pop(index)
        return arr
    
    def __init__(self):
        self.string = input()
        arr = self.to_arr(self.string)
        dup_arr = self.duplication(arr)
        print(dup_arr)

if __name__ == "__main__":
    solution = Solution()

        
    