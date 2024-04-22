class Solution:
    def to_arr(self, string):
        arr = []
        for item in string[1:-1].split(","):
            arr.append(int(item.strip()))
        return arr

    def canJump(self, array):
        if array is None or len(array) == 0:
            return False
        if array[0] == 0 and n == 1:
            return True
        position = 0
        n = len(array)
        if array[0] == 0:
            return True
        while position < n:
            value = array[position]
            if value == 0 :
                return False
            position += value
            if position >= n :
                return False
            elif array[position] == array[-1]:
                return True
            else : 
                pass
        
    def __init__(self):
        self.string = input()
        array = self.to_arr(self.string)
        print(self.canJump(array))

if __name__ == "__main__":
    solution = Solution()
