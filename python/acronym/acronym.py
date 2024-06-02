def abbreviate(words):
    replaced = words.replace('-',' ')
    rep = replaced.replace('_',' ')
    upp = rep.upper()
    words_list = upp.split()
    acronym = []
    for i in words_list:
        acronym.append(i[0])
    return ''.join(acronym)
            
    
    
