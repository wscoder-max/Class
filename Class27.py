import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
symbols = "!@#$%^&*()-_=+[]{};:,.<>?/"

all_characters = letters + digits + symbols

def generate_password(length = 12):
    password = " "
    for i in range(length):
        password += random.choice(all_characters)
    return password

while True:
    answer = input("Generate a new password? (yes/no): ").strip().lower()
    
    if answer == "yes" or answer == "y" or answer == "Yes":
        print("Your password:", generate_password())
    else:
        print("Okay, stopping.")
        break
