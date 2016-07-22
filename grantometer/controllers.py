#import dateutil.parser


MAXGRUMPY = 110


def increase_grumpiness(grumpiness):
    '''Increases the grumpiness by a factor of two by each call, until
    it reaches 50. After that it sets the grumpiness to the maximum'''
    if grumpiness > 50:
        grumpiness = MAXGRUMPY
    elif grumpiness > 0:
        grumpiness = grumpiness * 2
    else:
        grumpiness = 1
    return grumpiness


def decrease_grumpiness(grumpiness):
    '''Decreases the grumpiness linearly'''
    if grumpiness > 0:
        if grumpiness <= 100:
            grumpiness = grumpiness - 6.25
        else:
            grumpiness = 100
    return grumpiness


def cool_down_grumpiness(grumpiness, now, then):
    '''Cool down the grumpiness. Use with a time iso8601 time stamp:
    :param now: a timestamp in iso8601

    the grumpiness is either calculated by delta t**2 * 0.75 or set
    directely to 0'''
    delta_t = now - then
    hours = delta_t.seconds // 3600 + delta_t.days * 24
    if hours > 12:
        grumpiness = 0
    else:
        new_grumpiness = grumpiness - hours * hours * 0.75
        if new_grumpiness > 0:
            grumpiness = new_grumpiness
        else:
            grumpiness = 0
    return grumpiness
