# collect user preferences 
# - length
# - should contain uppercase
# - should contain special 
# - should contain digits

# get all available charecters
# randomly pick charecters up to length
# ensure we have at least one of each charecter type
# ensure length is valid 


import random
import string

def generate_password():
    length = int(input("Enter the desired password length: ").strip())
    include_uppercase = input("Include uppercase latters(yes/no)").strip().lower()
    include_special = input("Include special charecters (yes/no)").strip().lower()
    include_digits = input("Include digits (yes/no)").strip().lower()

    if length < 4:
        print(" Password length must be at least 4 charecters.")
        return
    
    lower = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase == "yes" else ""
    special = string.punctuation if include_special == "yes" else ""
    digits = string.digits if include_digits == "yes" else ""
    all_characters = lower + uppercase + special + digits

    required_charecters = []
    if include_uppercase == "yes":
        required_charecters.append(random.choice(uppercase))
    if include_special == "yes":
        required_charecters.append(random.choice(special))
    if include_digits == "yes":
        required_charecters.append(random.choice(digits))

    remaining_length = length - len(required_charecters)
    password = required_charecters

    for _ in range(remaining_length):
        character = random.choice(all_characters)
        password.append(character)

    random.shuffle(password)

    str_password = "".join(password)
    return str_password

password = generate_password()
print(password)