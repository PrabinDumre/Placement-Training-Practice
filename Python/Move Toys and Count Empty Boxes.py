def move_empty_boxes(arr):
    result = [x for x in arr if x != 0] + [0] * arr.count(0)
    empty_count = arr.count(0)
    return result, empty_count

boxes = [1, 0, 2, 0, 3, 4, 0, 5]
result, empty_count = move_empty_boxes(boxes)
print("Array after moving empty boxes to the end:", result)
print("Number of empty boxes:", empty_count)
