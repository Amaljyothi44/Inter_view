
class Solution:
    def to_arr(self, string):
        num = []
        for item in string[1:-1].split(","): #split and remove ","
            if item.strip(): #remove white space
                num.append(int(item))
        return num
    
    def merge(self,num1,num2, n,m ):
        d = 0
        while ( d < m):
            for i in range(n,n+m):
                num1[i] = num2[d]
                d+=1
        return sorted(num1)
    
    def __init__(self):
        string1 = input("Enter the arr :")
        num1 = self.to_arr(string1)
        n =  int(input("Enter the n :"))
        string2 = input("Enter the arr 2 :")
        num2 = self.to_arr(string2)
        m =  int(input("Enter the m :"))
        print(self.merge(num1,num2,n,m))

if __name__ == "__main__": #guard to ensure that the code within '__init__' get executed only when the script is running directly, not it is imported as a module
    solution = Solution()

    


