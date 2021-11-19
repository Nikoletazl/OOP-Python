def squaress(n):
    return (x * x for x in range(1, n + 1))

def squares(n):
    for x in range(1, n + 1):
        yield x * x

print(list(squares(5)))