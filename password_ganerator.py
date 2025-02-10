import random
import string 
def generate_password(length):
    characters = string.ascii_lowercase + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password
password_length = 12
print("Generated Password:", generate_password(password_length))

