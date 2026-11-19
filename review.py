INTERVALS = [1, 3, 7, 21]


def next_interval(current, correct):
    if not correct:
        return 1
    else:
        for w in range(len(INTERVALS)):
            if w==len(INTERVALS)-1:
                return None
            if INTERVALS[w]==current:
                return INTERVALS[w+1]
               
            