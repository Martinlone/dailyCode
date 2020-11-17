source_list = [1,2,2,3,4,11,11,15,16,16,16,17,17,52]

# 找不重复的
def find_target(source_list):
    slt_length = len(source_list)
    if len(source_list) < 2:
        return source_list
    else:
        fast = 0
        target_list = []
        while fast < slt_length:
            slow = fast
            target_list.append(source_list[slow])

            while fast < slt_length and source_list[fast] == source_list[slow]:
                fast += 1
        return target_list
# target_list = [1,2,3,4,11,15,16,17,52]
print(find_target(source_list))

# 找没有重复元素的元素
def find_single(source_list):
    slt_length = len(source_list)
    if len(source_list) < 2:
        return source_list
    else:
        fast = 1
        slow = 0
        target_list = []
        while fast < slt_length:
            count = 0
            while fast < slt_length and source_list[fast] == source_list[slow]:
                count += 1
                fast += 1
            if count == 0:
                target_list.append(source_list[slow])
            slow = fast
            fast += 1
        # 最后一个元素没法判断
        if source_list[-1] !=source_list[-2]:
            target_list.append(source_list[-1])
    return target_list
print(find_single(source_list))