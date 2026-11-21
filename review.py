INTERVALS = [1, 3, 7, 21]


def next_interval(current, correct):
    if current not in INTERVALS:
        raise ValueError("interval must be 1, 3, 7 or 21")
    if not correct:
        return 1 
    else:
        for w in range(len(INTERVALS)):
            if w==len(INTERVALS)-1:
                return None
            if INTERVALS[w]==current:
                return INTERVALS[w+1]
               
            