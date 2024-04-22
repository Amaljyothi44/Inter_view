class Solution:
    def to_arr(self, string):
        arr = []
        for item in string[1:-1].split(","):
            arr.append(int(item.strip()))
        return arr
    def minSubArrayLen(self, array, t):
        if any(t in item for item in array):
            return 1
        for i in range(2, len(array)+1):
            for k in range(i):
                pass

    def __init__(self):
        self.string = input()
        array = self.to_arr(self.string)
        self.t = input()


if __name__ == "__main__":
    solution = Solution()