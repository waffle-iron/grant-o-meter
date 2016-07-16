import dateutil.parser


class GrumpyControl:
    def __init__(self):
        self.grumpyness = 0
        self.last_action = None
        self.timestamp = None

    def increase_grumpyness(self):
        if self.grumpyness > 500:
            self.grumpyness = 1000
        elif self.grumpyness > 0:
            self.grumpyness = self.grumpyness * 2
        else:
            self.grumpyness = 1

    def decrease_grumpyness(self):
        if self.grumpyness > 0 and self.grumpyness <= 1000:
            self.grumpyness = self.grumpyness - 50
        elif self.grumypness > 1000:
            self.grumpyness = 950

    def cool_down_grumpyness(self, now):
        action_timestamp = dateutil.parser.parse(now)
        delta_t = action_timestamp - self.timestamp
        print(delta_t)
        if delta_t.days > 0 or delta_t.seconds > 43200:
            self.grumpyness = 0
        elif delta_t.seconds > 39600:
            self.grumpyness = 1
        else:
            houres = delta_t.seconds // 3600
            new_grumpyness = self.grumpyness - houres * (10 + houres)
            if new_grumpyness > 0:
                self.grumpyness = new_grumpyness
            else:
                self.grumpyness = 2

    def query_grumpyness():
        pass
