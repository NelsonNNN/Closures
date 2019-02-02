def square(x):
    return x * x

def sqr(squared, ar_list):
    results = []
    for i in ar_list:
        results.append(squared(i))
    return results

result = sqr(square, [1, 2, 3, 4, 5])

print(result)
