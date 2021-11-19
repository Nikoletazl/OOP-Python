def reverse_text(text):
    return (text[i] for i in range(len(text) -1, -1, -1))


for char in reverse_text("step"):
    print(char, end='')
