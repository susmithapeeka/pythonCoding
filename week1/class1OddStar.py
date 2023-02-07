n=5
m=5
for i in range(m,-1,-2):
    print(' '*n, end='') # repet space for n times
    print('* '*(i)) # repeat stars for i times
    n+=2
