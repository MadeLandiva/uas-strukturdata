def merge_sort_descending(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    left_half = merge_sort_descending(left_half)
    right_half = merge_sort_descending(right_half)
    
    return merge_descending(left_half, right_half)


def merge_descending(left, right):
    result = []
    x = 0
    y = 0 
    
    while x < len(left) and y < len(right):
        if left[x] > right[y]:
            result.append(left[x])
            x += 1
        else:
            result.append(right[y])
            y += 1
    
    while x < len(left):
        result.append(left[x])
        x += 1
    
    while y < len(right):
        result.append(right[y])
        y += 1
    
    return result

data = input("Masukkan elemen-elemen data: ").split()
data = [int(i) for i in data]

sorted_data = merge_sort_descending(data)

print("Data terurut secara descending atau dari besar ke kecil:", sorted_data)