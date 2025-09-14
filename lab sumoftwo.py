from itertools import *
# nums = [2,7,11,15]
# target = 9

nums = [3, 3] 
target = 6
def sumoftwo(nums, target):
    combs = list(combinations(nums, 2))
    sum_combs = [sum(i) for i in combs]
    if target in sum_combs:
        ind_tar = sum_combs.index(target)
        res = combs[ind_tar]
        if len(set(res)) > 1:
            return [nums.index(res[0]), nums.index(res[1])]
        else:
            return [0, 1]
    else:
        return'impossible'

print(sumoftwo([3, 3], 6))




