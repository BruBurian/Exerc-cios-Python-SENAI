lst = [5, 6, 3, 9, 2, 12, 3, 8, 7]

max_index = 0
for i in range(len(lst)):
    if lst[i] > lst[max_index]:
        max_index = i

lst[max_index], lst[-1] = lst[-1], lst[max_index]

print(lst)

