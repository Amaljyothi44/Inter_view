class Solution:
    def to_arr(self , string):
        arr = []
        for item in string[1:-1].split(","):
           arr.append(int(item.strip()))
        return arr
    

    def __init__(self):
        self.string = input()
        num = self.to_arr(self.string)
        set_arr = set(num)
        No_rep_arr = list(set_arr)
        print(No_rep_arr)

if __name__ == "__main__":
    solution = Solution()