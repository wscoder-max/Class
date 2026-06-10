n = 4
print(f"=== Counting Game Points: {n} === ")
print()

total = n * (n + 1) // 2
print(f"Formula: Total = {total} | steps = 1")

total = 0
steps = 0
for round_num in range(1, n + 1):
    for point in range(1, round_num + 1):
        total += point
        steps += 1
print(f"Nested Loop: Total = {total} | steps = {steps}")

total = 0
steps = 0
for round_num in range(1, n + 1):
    total += round_num
    steps += 1
print(f"Loop: Total = {total} | steps = {steps}")

total = 0
steps = 0
for round_num in range(1, n + 1):
    n = 10
    nested_steps = 0
    for round_num in range(1, n + 1):
        for point in range(1, round_num + 1):
            nested_steps += 1
print(f"Nested Loop Steps for n = {n}: {nested_steps}")

print()
print(f"=== Now with n = {n} rounds ===")
print("Formula Steps: 1")
print(f"Nested Loop Steps: {nested_steps}")
print(f"Loop Steps: {n}\n")
print("Summary: Same answers, but very different steps. This is time complexity in action!")
