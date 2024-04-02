import time
import random
import matplotlib.pyplot as plt

# Function to perform linear search
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

# Function to perform binary search
def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Generate random array
arr = [random.randint(1, 1000) for _ in range(10000)]
arr.sort()  # Binary search requires sorted array

# Perform searches and measure time
search_keys = [random.randint(1, 1000) for _ in range(5)]
linear_times = []
binary_times = []

for key in search_keys:
    start_time = time.time() * 1000  # Convert to milliseconds
    linear_search(arr, key)
    end_time = time.time() * 1000
    linear_times.append(end_time - start_time)

for key in search_keys:
    start_time = time.time() * 1000  # Convert to milliseconds
    binary_search(arr, key)
    end_time = time.time() * 1000
    binary_times.append(end_time - start_time)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(search_keys, linear_times, label='Linear Search')
plt.plot(search_keys, binary_times, label='Binary Search')
plt.xlabel('Search Key')
plt.ylabel('Time (milliseconds)')
plt.title('Time taken for Linear and Binary Search')
plt.legend()
plt.grid(True)
plt.show()
