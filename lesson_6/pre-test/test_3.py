def add_line_number(origin, destination):
    f_origin = open(origin, 'r')
    f_destination = open(destination, 'w')
    i = 1
    for line in f_origin.readlines():
        f_destination.write('{} {}'.format(i, line))
        i += 1
    f_origin.close()
    f_destination.close()
