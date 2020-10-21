#عناصر آرایه با بیشترین تکرار را برمیگرداند 

def top(arr):
    value = {}
    result = []
    f_max = 0

    for i in arr:
        value[i] = value.get(i, 0)+1
    # for i in arr:
    #     if i in value:
    #         value[i] += 1
    #     else:
    #         value[i] = 1

    f_max = max(value.values())
    # f_max = 0
    # for max_value in value.values():
    #     if f_max < max_value:
    #         f_max = max_value

    for i in value.keys():
        if value[i] == f_max:
            result.append(i)

    return result


print(top([1, 2, 1, 2, 3, 5]))
