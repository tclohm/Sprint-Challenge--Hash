def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # two items that equal the weight limit, length is length of the list (can be ignored)
    cache = {}
    for index in range(0, length):
    	if limit - weights[index] in cache:
    		return [index, cache[limit - weights[index]]]
    	if weights[index] not in cache:
    		cache[weights[index]] = index

    return None


weights_3 = [4, 6, 10, 15, 16]
print(get_indices_of_item_weights(weights_3, 5, 21))

weights_4 = [12, 6, 7, 14, 19, 3, 0, 25, 40]
print(get_indices_of_item_weights(weights_4, 9, 7))