def add_two_integers(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a+b
    else:
        raise TypeError("Only integers are allowed")