class custom_range:
    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step
        self.current_number = self.start

    def __iter__(self):
        return self

    def __next__(self):
        if self.step > 0 and self.current_number > self.end:
            raise StopIteration
        if self.step < 0 and self.current_number < self.end:
            raise StopIteration

        value_to_return = self.current_number
        self.current_number += self.step

        return value_to_return



one_to_ten = custom_range(1, 5, 3)
for num in one_to_ten:
    print(num)

