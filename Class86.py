number = int(input("Enter your number: "))
digits = len(str(number))
result_number = 0
temp = number

while temp > 0:
    digit = temp % 10
    result_number += digit ** digits
    temp //= 10

if number == result_number:
    print(f"{number} is an Armstrong Number.")
else:
    print(f"{number} is not an Armstrong Number.")