import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def get_input(prompt, type_=str, min_=None, max_=None):
    while True:
        try:
            value = type_(input(prompt))
            if (min_ is not None and value < min_) or (max_ is not None and value > max_):
                raise ValueError(f"Value must be between {min_} and {max_}.")
            return value
        except ValueError as e:
            print(e)
