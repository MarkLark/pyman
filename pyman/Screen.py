from sys import stdout


def size():
    import fcntl, termios, struct
    h, w, hp, wp = struct.unpack(
        "HHHH",
        fcntl.ioctl(0, termios.TIOCGWINSZ, struct.pack("HHHH", 0, 0, 0, 0))
    )
    return w, h


def clear():
    write("\033c")


def user_input(prompt = ""):
    """Get the user input

    This is required for Python2/3 compatability
    """
    try:
        return raw_input(prompt)
    except NameError:
        return input(prompt)


def write(output):
    stdout.write(output)