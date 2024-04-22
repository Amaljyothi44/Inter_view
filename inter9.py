from inter8 import Solution

class Solution9:

    def productExceptSelf(self, array):
        new_arr = []
        for i in range(len(array)):
            mult = 1
            for item in array:
                if item == array[i]:
                    pass
                else:
                    mult *= item
            new_arr.append(mult) 
        return new_arr                    

    def __init__(self):
        self.string = input()
        array = Solution.to_arr(self,self.string)
        print(array)
        print(self.productExceptSelf(array))


if __name__ == "__main__":
    solution9 = Solution9()
