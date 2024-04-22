class Solution:
    def to_arr(self, string):
        arr = []
        for item in string[1:-1].split(","):
            arr.append(int(item.strip()))
        return arr
    
    def threesum(self, array):
        result_set= set()
        for index1, value1 in enumerate(array):
            for index2, value2 in enumerate(array):
                for index3, value3 in enumerate(array):
                    if index1 != index2 and index2 != index3 and index1 != index3:
                        sum = value1+value2+value3
                        if sum == 0:
                            result_set.add(tuple(sorted((value1, value2, value3))))
        return [list(item) for item in result_set]                  
   
    def __init__(self):
        self.string = input()
        array = self.to_arr(self.string)
        print(self.threesum(array))
        
if __name__ == "__main__":
    solution = Solution()