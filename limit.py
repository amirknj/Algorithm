#در یک آرایه مقدار مینیمم و ماکزیمم رو دریافت کرده و عناصر بین آن دو رو برمیگرداند  
def limit(arr, min_lim=None, max_lim=None):
    min_check = lambda val: True if min_lim is None else (min_lim <= val)
    max_check = lambda val: True if max_lim is None else (val <= max_lim)

    return [val for val in arr if min_check(val) and max_check(val)]


print(limit([1, 2, 3, 4, 5], None, 3))
