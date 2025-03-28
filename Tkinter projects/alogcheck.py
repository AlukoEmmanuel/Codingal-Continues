def largest_number(L):
	if len(L) == 0:
		return None
	largest = L[0]
	for item in L:
		if item > largest:
			largest = item
	return largest

# Example usage
numbers = [3, 5, 2, 9, 1]
print(largest_number(numbers)) # Output: 9