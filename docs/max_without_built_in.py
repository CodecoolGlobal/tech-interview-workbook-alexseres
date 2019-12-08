def maximum(lst):
    maxi = lst[0]
    for num in lst:
        if maxi < num:
            maxi = num
    return maxi

a = maximum([2,5,6,3,9,8])
print(a)