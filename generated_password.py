

import random
import string


def generate_password(lenght: int = 14):
    alphbit = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(alphbit) for j in range(lenght))
    return password


password = generate_password()
print(f"Here is your generated password {password}")
