
'''
两列表取交集
list(set(a).intersection(set(b))
并集
list(set(a).union(set(b)))
差集
list(set(b).difference(set(a)) # b中有而a中没有的      非常高效！  若an本有就有序，集合操作则不会改变顺序！


'''


class Solution:
    def find_lack(self, lacked_list):
        start = lacked_list[0]
        end = lacked_list[-1]
        full = [x for x in range(start, end+1)]
        return list(set(full).difference(set(lacked_list)))
a = [1,4,5,6,7,8,10,15,16]
print(Solution().find_lack(a))
