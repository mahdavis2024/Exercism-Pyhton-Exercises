def tally(rows):
    row_list = [row.split(';') for row in rows]
    tab = ["Team                           | MP |  W |  D |  L |  P"]
    table = []
    mp, w, d, l = {}, {}, {}, {}
    for match in row_list:
	    mp[match[0]] = mp.get(match[0],0) + 1
	    mp[match[1]] = mp.get(match[1],0) + 1
        
	    if match[2] == "win":
		    w[match[0]] = w.get(match[0],0) + 1
		    l[match[1]] = l.get(match[1],0) + 1
	    elif match[2] == "draw":
		    d[match[0]] = d.get(match[0],0) + 1
		    d[match[1]] = d.get(match[1],0) + 1
	    else:
		    l[match[0]] = l.get(match[0],0) + 1
		    w[match[1]] = w.get(match[1],0) + 1
            
    p = {key: 3* w.get(key,0) + d.get(key,0) for key in list(mp.keys())}
    for k in list(mp.keys()):	        
	    table.append("{0:31}|{1:>3} |{2:>3} |{3:>3} |{4:>3} |{5:>3}".format(k,mp.get(k,0),w.get(k,0),d.get(k,0),l.get(k,0),p.get(k,0)))

    table = sorted(table, key =lambda line: (-int(line[-2:]), line[0]))
    tab.extend(table)
    return tab
    