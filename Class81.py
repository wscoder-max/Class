n = 5
print("=== Running Lap Tracker ===")

total = n * (n + 1) // 2
print(f"Formula: Total = {total} | steps = 1")

total = 0
steps = 0
for lap in range(1, n + 1):
    total += lap
    steps += 1
print(f"Loop: Total = {total} | steps = {steps}")

total = 0
steps = 0
for lap in range(1, n + 1):
    for point in range(1, lap + 1):
        total += point
        steps += 1
print(f"Nested Loop: Total = {total} | steps = {steps}")

print()
print(f"=== Now with n = {n} laps ===")
print("Formula Steps: 1")
print(f"Loop Steps: {steps // n}")
print(f"Nested Loop Steps: {steps}\n")
print("Summary: The formula gives us the answer in constant time, while the loops take linear and quadratic time respectively. This illustrates how different approaches can lead to vastly different time complexities!")