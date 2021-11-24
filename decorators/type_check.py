def type_check(type):
    def decorator(func):
        def wrapper(arg):
            if isinstance(arg, type):
                return func(arg)
            else:
                return "Bad Type"

        return wrapper

    return decorator


@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
