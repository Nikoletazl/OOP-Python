class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.element = 0
        self.passed_iteration = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.passed_iteration >= self.count:
            raise StopIteration

        self.passed_iteration += 1
        result = self.element
        self.element += self.step

        return result


numbers = take_skip(2, 6)
for number in numbers:
    print(number)
