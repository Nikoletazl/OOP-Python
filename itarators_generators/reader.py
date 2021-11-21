def read_next(*args):
    for iterable in args:
        for el in iterable:
            yield el


for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)
