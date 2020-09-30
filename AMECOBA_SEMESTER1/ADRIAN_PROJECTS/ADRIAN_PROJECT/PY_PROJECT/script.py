scores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a_list = []
b_list = []
c_list = []
d_list = []


for i in scores:
    if i >= 8:
        a_list.append(i)
    elif i >= 6:
        b_list.append(i)
    elif i >= 4:
        c_list.append(i)
    else:
        d_list.append(i)

print(a_list)
print(b_list)
print(c_list)
print(d_list)