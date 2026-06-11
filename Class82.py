names = ["A", "B", "C", "D", "E"]
scores = [90, 80, 70, 60, 50]
n = len(scores)
print(f"=== Score Tracker - n = {n} ===")
for i in range(n):
    print(f"{i + 1}. {names[i]}: {scores[i]}", sep="")
print()

steps = 1
print(f"Score at [0]: {scores[0]} | steps = {steps} | Θ(1)")
print()

target = "A"
steps = 0
for name in names:
    steps += 1
    if name == target:
        break
print(f"Search for '{target}' | steps = {steps} | Ω(n)")
print()

target = "E"
steps = 0
for name in names:
    steps += 1
    if name == target:
        break
print(f"Search for '{target}' | steps = {steps} | O(n)")
print()

steps = 0
target_sum = 150
print(f"Total Score: {target_sum}")
for i in range(n):
    for j in range(i + 1, n):
        steps += 1
        if scores[i] + scores[j] == target_sum:
            print(f"names[{i}] + names[{j}] = {target_sum} | steps = {steps} | O(n^2)")
print()

print("=== Asymptotic Summary ===")
print("Θ(1): index access - always 1 step, tight bound.")
print("Ω(1): best case - found in 1 step, lower bound.")
print(f"O(n): worst case - found after {n} steps, upper bound.")
print(f"O(n^2): pair check - {n * n - 1 // 2} comparisions.")
print()
print("Drop contestants. Keep the dominant term. That is asymptotic analysis!")

