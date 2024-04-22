class Solution:
    def to_arr(self, string):
        arr = []
        for item in string[1:-1].split(","):
            arr.append(int(item.strip()))
        return arr
    def count(self,arr):
        count= {}
        for item in arr:
            count[item] = count.get(item, 0) + 1
        sort_count = sorted(count.items(), key = lambda x : x[1], reverse=True)
        max_count = sort_count[0][1]
        max_item = [item for item , count in sort_count if count == max_count]
        print(max_item)

    def __init__(self):
        self.string = input()
        array = self.to_arr(self.string)
        self.count(array)

if __name__ == "__main__":
    solution = Solution()
    