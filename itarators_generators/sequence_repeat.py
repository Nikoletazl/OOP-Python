class sequence_repeat:
    def __init__(self, text, count):
        self.text = text
        self.count = count
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == 0:
            raise StopIteration
        ch = self.text[self.idx]
        self.count -= 1
        self.idx += 1

        if self.idx >= len(self.text):
            self.idx = 0
        return ch


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')
result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')
