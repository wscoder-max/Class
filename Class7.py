L = [4, 5, 1, 2, 9, 7, 10, 8, ]
print("Original List: ", L)

count = 0
for i in L:
    count += 1

avg = count / len(L)

print(f"Sum = {count}")
print(f"Average = {avg}")

L.sort()

print(f"Smallest Number = {L[0]}")
print(f"Largest Number = {L[-1]}")