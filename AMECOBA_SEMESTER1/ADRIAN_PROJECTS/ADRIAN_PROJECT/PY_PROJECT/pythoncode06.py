lists = []

rap = ['a1', 'b1', 'c1' ,'d1' ,'e1']
rock = ['a2', 'b2' ,'c2', 'd2', 'e2']
djs = ['a3', 'b3', 'c3', 'd3', 'e3']


lists.append(rap)
lists.append(rock)
lists.append(djs)


for list in lists:
    for lst in list:
        print(lst)