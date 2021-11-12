class Guitar:
    def play(self):
        return "Playing the guitar"


guitar = Guitar()


class Children:
    def play(self):
        return "Children are playing"


children = Children()


def start_playing(i_can_play):
    return i_can_play.play()

print(start_playing(guitar))
print(start_playing(children))
