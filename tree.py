def tree(row):
    for i in range(row):
        print(' ' * (row-i) + '*' * ((i*2)+1))
    for j in range(2):
        print(' ' * (row-j) + '*' * ((j*2)+1))


tree(4)