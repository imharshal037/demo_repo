lst = [5,9,1,4,7,3,8]

def merge_sort(lst):
    if len(lst) <=1 :
        return lst
        
    mid = len(lst)//2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    
    result = []
    i=j=0
    
    while i<len(left) and j< len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i +=1
        else:
            result.append(right[j])
            j +=1
            
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result
    
    
result = merge_sort(lst)

print(result)