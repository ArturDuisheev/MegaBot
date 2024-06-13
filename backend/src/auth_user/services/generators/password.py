import random
import string


def generate_password():
    return ''.join(random.choices(''.join(string.digits + string.ascii_lowercase + string.ascii_uppercase)
                                  + string.digits, k=10))
