def is_isogram(string):
    thestring = string.lower()
    thelist = []
    for letter in thestring:
        if letter not in [' ', '-']:
            thelist.append(letter)
    theset = set(thelist)
    if len(thelist) == len(theset):
        return True
    else: return False
