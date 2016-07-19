import dateutil.parser

class GrumpyControl:
    '''The grumpy controller is responsible to increase or decrease the
    total grumpyness. Also the grumpy controller is responsible for the cool
    down and the provide access to the grumpyness.

    The grumpyness scales from 0 to 110 %, so we can measure it from 1 to 11,
    with some more precision.
    '''
    def __init__(self):
        self.grumpyness = 0
        self.timestamp = None
        self.MAXGRUMPY = 110

    def increase_grumpyness(self):
        '''Increases the grumpyness by a factor of two by each call, until
        it reaches 50. After that it sets the grumpyness to the maximum'''
        if self.grumpyness > 50:
            self.grumpyness = self.MAXGRUMPY
        elif self.grumpyness > 0:
            self.grumpyness = self.grumpyness * 2
        else:
            self.grumpyness = 1

    def decrease_grumpyness(self):
        '''Decreases the grumpyness linearly'''
        if self.grumpyness > 0:
            if self.grumpyness <= 100:
                self.grumpyness = self.grumpyness - 6.25
            else:
                self.grumpyness = 100

    def cool_down_grumpyness(self, now):
        '''Cool down the grumpyness. Use with a time iso8601 time stamp:
        :param now: a timestamp in iso8601

        the grumpyness is either calculated by delta t**2 * 0.75 or set
        directely to 0'''
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

    def save_grumpyness():
        pass



