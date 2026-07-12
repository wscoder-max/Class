secret_code = 13
access_key = 9

print("=== My Secret Code Bit Scanner ===")

print("Secret Code: 13")
print("Access Key: 9")

print("Secret Code in Binary: ", format(secret_code, '0b'))
print("Access Key in Binary: ", format(access_key, '0b'))

and_result = secret_code & access_key
or_result = secret_code | access_key
print("AND Result: ", and_result)
print("OR Result: ", or_result)

not_result = ~(secret_code) & 0b1111
xor_result = secret_code ^ access_key
print("NOT Result: ", not_result)
print("XOR Result: ", xor_result)

left_shift = secret_code << 1
right_shift = secret_code >> 1
print("Left Shift Result: ", left_shift, "Binary:", format(left_shift, '0b'))
print("Right Shift Result: ", right_shift, "Binary:", format(right_shift, '0b'))

xor_check = secret_code ^ 1
print("XOR with 1 Result: ", xor_check)
if xor_check ==  secret_code - 1:
    print(f"{secret_code} is odd.")
else:
    print(f"{secret_code} is even.")

bit_count = secret_code.bit_count()
print("Number of 1 bits in Secret Code: ", bit_count)

print("=== Summary ===")
print(f"Secret Code: {secret_code}, Binary: {format(secret_code, '0b')}")
print(f"Access Key: {access_key}, Binary: {format(access_key, '0b')}")
print(f"& Result: {and_result}")
print(f"| Result: {or_result}")
print(f"~ Result: {not_result}")
print(f"^ Result: {xor_result}")
print(f"<< Result: {left_shift}")
print(f">> Result: {right_shift}")
print(f"XOR with 1 Result: {xor_check}")
print(f"Bit Count: {bit_count}")
