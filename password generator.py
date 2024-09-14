import random
import string

def password_generator():
    print("Password Generator")
    length = int(input("Enter the length of the password: "))

    include_lowercase = input("Include lowercase letters? (yes/no): ")
    include_uppercase = input("Include uppercase letters? (yes/no): ")
    include_numbers = input("Include numbers? (yes/no): ")
    include_special_chars = input("Include special characters? (yes/no): ")

    characters = ""

    if include_lowercase.lower() == "yes":
        characters += string.ascii_lowercase
    if include_uppercase.lower() == "yes":
        characters += string.ascii_uppercase
    if include_numbers.lower() == "yes":
        characters += string.digits
    if include_special_chars.lower() == "yes":
        characters += string.punctuation

    if characters == "":
        print("Please select at least one character type.")
        return

    password = "".join(random.choice(characters) for i in range(length))
    print("Generated password: ", password)

password_generator()
