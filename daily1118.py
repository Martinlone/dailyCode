class Solution:
    def find_location(self, array, x):
        if not array or not array[0]:
            return False
        columns = len(array[0])  # 列数
        for index, item in enumerate(array):
            if array[index][columns - 1] < x:
                continue
            if array[index][columns - 1] == x:
                # return [index, columns - 1]
                return True
            if array[index][columns - 1] > x and array[index][0] <= x:
                result = self.find_in_list(array[index], x)
                if type(result) == int:
                    # return [index, result]
                    return True
        return False

    def find_in_list(self, list, x):
        # 二分法
        left = 0
        right = len(list) - 1
        while left <= right:
            mid = (right + left) // 2
            print(left,mid,right)
            if list[mid] == x:
                return mid
            elif list[mid] < x:
                left = mid + 1
            elif list[mid] > x:
                right = mid - 1
        return False



a = [[-1,3]]

print(Solution().find_location(a, -1))
