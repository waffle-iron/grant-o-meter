import dateutil.parser


class GrumpyControl:
    def __init__(self):
        self.grumpyness = 0
        self.last_action = None
        self.timestamp = None

    def increase_grumpyness(self):
        if self.grumpyness > 50:
            self.grumpyness = 110
        elif self.grumpyness > 0:
            self.grumpyness = self.grumpyness * 2
        else:
            self.grumpyness = 1

    def decrease_grumpyness(self):
        if self.grumpyness > 0:
            if self.grumpyness <= 100:
                self.grumpyness = self.grumpyness - 6.25
            else:
                self.grumpyness = 100

    def cool_down_grumpyness(self, now):
        action_timestamp = dateutil.parser.parse(now)
        delta_t = action_timestamp - self.timestamp
        hours = delta_t.seconds // 3600 + delta_t.days * 24
        if hours > 12:
            self.grumpyness = 0
        else:
            new_grumpyness = self.grumpyness - hours * hours * 0.75
            if new_grumpyness > 0:
                self.grumpyness = new_grumpyness
            else:
                new_grumpyness = 0

    def query_grumpyness():
        pass
