def star_scratch():
    h = int(input('please insert the height'))
    l = int(input('please insert the length'))
    print(' ' * h, '* ' * l)
    for i in reversed(range(1, h - 1)):
        print(' ' * (i + 1), '* ', ' ' * l, '*')
    print(' ', '* ' * l)
