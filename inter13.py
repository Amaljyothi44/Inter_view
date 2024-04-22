class Solution:
    def to_arr(self, string):
        arr = []
        for item in string[1:-1].split(","):
            arr.append(int(item.strip()))
        return arr
    def maxArea(self, array):
        new_arr = []
        for index1, value1 in enumerate(array):
            for index2, value2 in enumerate(array):
                if index1==index2 :
                    pass
                else :
                    new_arr.append(min(value1, value2)*abs(index1-index2))
        new_arr =sorted(new_arr ,reverse=True)
        return new_arr[0]
    
    def __init__ (self):
        self.string = input()
        array = self.to_arr(self.string)
        print(self.maxArea(array))

if __name__ == "__main__":
    solution = Solution()