numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
result = map(lambda x, y: x + y, numbers1, numbers2)
print("Concatenation of two lists:", list(result))


nums = [1, 2, 3, 4, 5]
def sq(x):
    return x * x
square = list(map(sq, nums))
print("Square of numbers:", square)