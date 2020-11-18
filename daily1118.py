class Solution:
    def find_location(self, array, x):
        columns = len(array[0])  # 列数
        for index, item in enumerate(array):
            if array[index][columns - 1] < x:
                continue
            if array[index][columns - 1] == x:
                return [index, columns - 1]
            result = self.find_in_list(array[index], x)
            if result:
                return [index, result]
        return False

    def find_in_list(self, list, x):
        # 二分法
        mid = len(list) // 2
        left = 0
        right = len(list) - 1
        while left != mid and right != mid:
            if list[mid] == x:
                return mid
            elif list[mid] < x:
                left = mid
                mid += len(list[mid:right + 1]) // 2
            elif list[mid] > x:
                right = mid
                mid -= len(list[left:mid + 1]) // 2
        return False


a = [[1, 2, 3, 4, 6],
     [2, 5, 6, 7, 9],
     [4, 11, 12, 15, 25],
     [14, 19, 21, 24, 26],
     [16, 52, 65, 78, 99]]
print(Solution().find_location(a,21))