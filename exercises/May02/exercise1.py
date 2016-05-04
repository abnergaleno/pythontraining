def pyramid(size):
    print('pyramid size = ' + str(size))

    for row in reversed(xrange(size)):
        print row/2*' ' + (size-row)*'*'

pyramid(5)
