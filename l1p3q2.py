def max_product_pair(arr):
    # Initialize variables to store the largest positive and negative numbers
    max_pos1, max_pos2 = arr[0],arr[0]
    max_neg1, max_neg2 = arr[0],arr[0]
    
    # Find the two largest positive and two largest negative numbers
    for num in arr:
        if num > max_pos1:
            max_pos2 = max_pos1
            max_pos1 = num
        elif num > max_pos2:
            max_pos2 = num
        
        if num < 0 and abs(num) < abs(max_neg1):
            max_neg2 = max_neg1
            max_neg1 = num
        elif num < 0 and abs(num) < abs(max_neg2):
            max_neg2 = num
    
    # Calculate the products of pairs
    product1 = max_pos1 * max_pos2
    product2 = max_neg1 * max_neg2
    
    # Determine the pair with the maximum product
    if product1 > product2:
        max_pair = (max_pos1, max_pos2)
    else:
        max_pair = (max_neg1, max_neg2)
    
    # Return the maximum product and the pair
    return max_pair, max(product1, product2)

# Example usage:
arr = [1, 7, 4, 2, 8, 6, 3, 9, 5]
pair, result = max_product_pair(arr)
print("Maximum product pair:", pair, "with product:", result)
