def double(func):
    def wrapper(x):
        return func(x * 2)
    return wrapper

@double
def number(x):
    return x

print(number(5))  