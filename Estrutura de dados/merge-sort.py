def merge_sort(array):
    if len(array) > 1:
        div = len(array) // 2
        left = array[:div]
        right = array[div:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            
            else:
                array[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
        return array
r = merge_sort([22,34,6,5,7,9,12,69])
print(r)