class Solution:
   
    def isPalindrome(self , string):
        clr_string = string.replace(" ", "").replace(",", "").replace(":","").lower()
        print(clr_string)
        print(clr_string[::-1])
        if clr_string == clr_string[::-1]:
            return True
        else:
            return False

    def __init__(self):
        self.string = str(input())
        
        print(self.isPalindrome(self.string))
        
if __name__ == "__main__":
    solution = Solution()