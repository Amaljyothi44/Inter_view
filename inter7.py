class Solution:
    def to_arr(self, string):
        arr = []
        for item in string[1:-1].split(","):
            arr.append(int(item.strip()))
        return arr
    
    def maxProfit (self, array) :
        min_value = min(array)
        for index, value in enumerate(array):
            if value == min_value:
                day = index
        if day == (len(array)-1):
            new_arr = array[: -1]
            min_value = min(new_arr)
            if min_value == new_arr[-1]:
                new_arr= [0]
        else :
            new_arr = array[day:]
        if len(new_arr)>1 :
            max_value = max(new_arr)
        else :
            max_value = 0
        
        if max_value != 0 :
            profit = max_value - min_value
        else :
            profit = 0

        return profit
     
    def __init__(self):
        self.string = input()
        array = self.to_arr(self.string)
        print(self.maxProfit(array))


if __name__ == "__main__":
    solution = Solution()