from fileHotel import Hotel

if __name__ == '__main__':
    stdroom = Hotel(200)
    bigroom = Hotel(230, 0.9)
    print(stdroom.calc_all())
    print(stdroom.calc_all(2))
    print(bigroom.calc_all())
    print(bigroom.calc_all(3))

print(__name__)
