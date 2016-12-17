from sys import stdout


def size():
    import fcntl, termios, struct
    h, w, hp, wp = struct.unpack(
        "HHHH",
        fcntl.ioctl(0, termios.TIOCGWINSZ, struct.pack("HHHH", 0, 0, 0, 0))
    )
    return w, h


def clear():
    stdout.write("\033c")
