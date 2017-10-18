#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

"""
Print a grid
"""



def print_grid(h, w):
    hor_line = "+" + "-" * w + "+" + "-" * w + "+"
    ver_line = "|" + " " * w + "|" + " " * w + "|\n"
    print(hor_line)
    print(ver_line * h, end='')
    print(hor_line)
    print(ver_line * h, end='')
    print(hor_line)


print_grid(3, 9)
