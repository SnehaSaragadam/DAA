def segregate_zeros_and_ones(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        if arr[left] == 1:
            arr[left], arr[right] = arr[right], arr[left]
            right -= 1
        else:
            left += 1

    return arr

# Input binary array of 0's and 1's
binary_array = [0, 1, 0, 1, 0, 1]

segregated_array = segregate_zeros_and_ones(binary_array)
print("Array after segregating 0's and 1's:")
print(segregated_array)
