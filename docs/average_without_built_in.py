def average(lst):
    
    summ = 0
    lenn = 0
    
    for i in lst:
        summ += i
        lenn += 1

    average = summ // lenn
    return average
print(average([1,2,3,4,5]))

    
