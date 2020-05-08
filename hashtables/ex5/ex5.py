def finder(files, queries):

    """
    YOUR CODE HERE
    """
    result = []
    cache = {}

    for query in queries:
        if query not in cache:
            cache[query] = False

    for file in files:
        last_file = file.split('/')[-1]
        if last_file in cache:
            result.append(file)
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
