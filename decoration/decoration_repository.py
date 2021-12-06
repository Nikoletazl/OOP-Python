class DecorationRepository:
    def __init__(self):
        self.decorations = []

    def add(self, decoration):
        self.decorations.append(decoration)

    def remove(self, decoration):
        for decor in self.decorations:
            if decor == decoration:
                self.decorations.remove(decoration)
                return True

        return False

    def find_by_type(self, decoration_type: str):
        for decoration in self.decorations:
            if decoration == decoration_type:
                return self.decorations[decoration]

        return None

