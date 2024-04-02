import heapq

def merge_sorted_lists(lists):
  """Merges multiple sorted lists into a single sorted list.

  Args:
    lists: A list of m sorted lists.

  Returns:
    A new list containing all elements of the input lists sorted in ascending order.
  """

  heap = []
  for i, lst in enumerate(lists):
    heap.append((lst[0], i, 0))
  heapq.heapify(heap)

  result = []
  while heap:
    val, list_idx, element_idx = heapq.heappop(heap)
    result.append(val)
    if element_idx < len(lists[list_idx]) - 1:
      heapq.heappush(heap, (lists[list_idx][element_idx + 1], list_idx, element_idx + 1))

  return result

# Example usage
lists = [[10, 20, 30, 40], [15, 25, 35], [27, 29, 37, 48, 93], [32, 33]]
sorted_list = merge_sorted_lists(lists)
print(sorted_list)
