def move_zeros_to_end(arr):
    result = [x for x in arr if x != 0] + [0] * arr.count(0)
    return result

arr = [4, 5, 0, 1, 9, 0, 5, 0]
result = move_zeros_to_end(arr)
print("Array after moving zeros to the end:", result)
