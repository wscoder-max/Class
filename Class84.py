scores = [12, 25, 33, 41, 50, 67, 72, 85, 91, 98]
n, target = len(scores), 98
print(f"=== Quiz Score Finder(n = {n} scores) ===")
print(f"Scores = {scores} | Target = {target}\n")

steps = 0
for i in range(n):
    steps += 1
    if scores[i] == target:
        print(f"Linear Search: index = {i}, Steps = {steps} | O(n)\n")
        break

lo, hi, steps = 0, n - 1, 0
while lo <= hi:
    mid = (lo + hi) // 2
    steps += 1
    if scores[mid] == target:
        print(f"Binary Search: index = {mid}, Steps = {steps} | O(log n)\n")
        break
    elif scores[mid] < target:
        lo = mid + 1
    else:
        hi = mid - 1
