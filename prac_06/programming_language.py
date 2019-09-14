class ProgrammingLanguage:

    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dyanmic(self):
        return self.typing == "Dynamic"

    def __str__(self):
        return "{}, {} typing, reflection={}, First appeared in {}".format(self.name, self.year, self.reflection,
                                                                           self.year)

