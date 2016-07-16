class GrumpyControl:
    def __init__(self):
        self.grumpyness = 0

    def increase_grumpyness(self):
        if self.grumpyness > 500:
            self.grumpyness = 1000
        elif self.grumpyness > 0:
            self.grumpyness = self.grumpyness * 2
        else:
            self.grumpyness = 1

    def decrease_grumpyness():
        pass

    def query_grumpyness():
        pass
