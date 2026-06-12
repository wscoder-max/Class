print("=== Quiz Checker ===")

quiz_scores = [45, 74, 81, 93, 64, 27, 30, 77]

first_score = quiz_scores[0]
print()
print("Time Complexity: O(1) | Θ(1)")

target_score = 27
steps = 0
for scores in quiz_scores:
    steps += 1
    if scores == target_score:
        print()
        print(f"Target Score Found: {target_score}")
print(f"Time Complexity: O(n) | Steps Taken: {steps}")

pair_steps = 0
for score1 in quiz_scores:
    for score2 in quiz_scores:
        pair_steps += 1
print()
print(f"Time Complexity: O(n^2) | Total Pair Checks: {pair_steps}")

print()
print("Best Case: 45")
print("Average Cases: 93, 64")
print("Worst Case: 77")

print()
print("=== Summary ===")
print("O(1): Direct access is fastest.")
print("O(n): Linear search grows with the number of scores.")
print("O(n^2): Nested loops grow much faster.")
print("Ω(1): Best case for search when the target is found first.")
print("Θ(1): Direct access always takes constant time.")
print("Big-O shows the upper/worst-case growth.")
