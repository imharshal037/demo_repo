lst = [64,25,11,78,44]

for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i] > lst[j]:
            lst[i],lst[j] = lst[j],lst[i]

print("Sorted List :", lst)