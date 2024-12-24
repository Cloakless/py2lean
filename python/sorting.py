def bubble(lst):
    n = len(lst)
    bubbling = True
    while bubbling:
        bubbling = False
        for i in range(n-1):
            if lst[i] > lst[i+1]:
                bubbling = True
                lst[i], lst[i+1] = lst[i+1], lst[i]
    return lst

print(bubble([1,2,9,4,8,3]))
print(bubble([5,2,-6,0]))