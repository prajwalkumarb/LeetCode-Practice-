number = [2,7,11,15]
target = 9

def two_sum(number,target):
    mapper = {}
    for ind, val in enumerate(number):
        rem_val = target - val
        if rem_val in mapper:
            return [mapper[rem_val], ind]
        mapper[val] = ind
    return []

print(two_sum(number,target))
