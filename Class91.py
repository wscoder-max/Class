large_number = int(input("Enter the larger number: "))
small_number = int(input("Enter the smaller number: "))

while small_number:
    store_number = large_number % small_number
    large_number = small_number
    small_number = store_number

print(f"The HCF is {large_number}")
