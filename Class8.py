user_input = input("Enter numbers separated by spaces: ")

nums = []
for n in user_input.split():
    nums.append(int(n))

squares = []
for s in nums:
    squares.append(s * s)

evens = []
odds = []
for e in squares:
    if e % 2 == 0:
        evens.append(e)
    else:
        odds.append(e)

print("Original List:", nums)
print("Squared List:", squares)
print("Even Squares:", evens)
print("Odd Squares:", odds)

