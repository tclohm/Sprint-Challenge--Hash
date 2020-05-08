def has_negatives(a):

    """
    YOUR CODE HERE
    """
    cache = {}
    result = []
    for index in a:
    	absolute = abs(index)
    	if absolute in cache:
    		cache[absolute] += 1
    	if absolute not in cache:
    		cache[absolute] = 0
    	if cache[absolute] > 0:
    		result.append(absolute)
    return result


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
