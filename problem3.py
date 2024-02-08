# Revision 1 BEGIN 2024-02-07
## Begin Andrew Sassine here (2024-02-07)

import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

def password_acceptable(password):
    return any(char in string.punctuation for char in password) and len(password) >= 8

accepted_passwords = []
for _ in range(40):
    password = generate_password()
    if password_acceptable(password):
        accepted_passwords.append(password)
    # Unacceptable passwords are ignored, thus "deleted"

print(f"Accepted Passwords: {accepted_passwords}")

## End Andrew Sassine (2024-02-07)
# Revision 1 FINAL DATE 2024-02-07
