def intersection(arrays):

	"""
	YOUR CODE HERE
	"""
	cache = {}
	result = []

	for array in arrays:
		for number in array:
			if number not in cache:
				cache[number] = 1
			elif number in array:
				cache[number] += 1
			if cache[number] == len(arrays):
				result.append(number)
	return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000,2000000)) + [1,2,3])
    arrays.append(list(range(2000000,3000000)) + [1,2,3])
    arrays.append(list(range(3000000,4000000)) + [1,2,3])

    print(intersection(arrays))
