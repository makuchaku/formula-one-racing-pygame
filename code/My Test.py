class Master:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)

class Child(Master):
    def __init__(self, name):
        super().__init__(name)
        self.name="Adwaith"

        # self.name = "Modified " + name

ch = Child("Sujith")
print(ch.name)
ch.print_name()
