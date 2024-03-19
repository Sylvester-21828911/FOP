import time

LINE_UP = '\033[1A'
LINE_CLEAR = '\x1b[2K'
numlines = 4
s = " "
g = 0

while True:
    for i in range(50):
        print(g * s, " \\")
        print(g * s, "\\/\\")
        print(g * s, "/\\/")
        print(g * s, " /")
        time.sleep(0.1)
        g += 1
        for j in range(numlines):
            print(LINE_UP, end=LINE_CLEAR)

    for i in range(50):
        print(g * s, " /")
        print(g * s, "/\\/")
        print(g * s, "\\/\\")
        print(g * s, " \\")
        time.sleep(0.1)
        g -= 1
        for j in range(numlines):
            print(LINE_UP, end=LINE_CLEAR)
