import random
import string
def generate_password():
    length = int(input("Enter the length of the password: "))
    if length<4:
        print("Password must be at least 4 characters long.")
    else:
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(length))
        print("Generated Password:", password)
generate_password()