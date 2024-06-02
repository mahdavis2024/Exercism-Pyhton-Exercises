def score(word):
    s_score = 0
    for l in word.upper():
        if l in ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T']:
            s_score += 1
        elif l in ['D', 'G']:
            s_score = s_score + 2
        elif l in ['B', 'C', 'M', 'P']:
            s_score = s_score + 3
        elif l in ['F', 'H', 'V', 'W', 'Y']:
            s_score = s_score + 4
        elif l in ['K']:
            s_score = s_score + 5
        elif l in ['J', 'X']:
            s_score = s_score + 8
        else:
            s_score = s_score + 10
    return s_score
