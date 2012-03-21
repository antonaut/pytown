#!/usr/bin/python3

def closure(attrs, fds):
    new_fds = set()
    closure = attrs

    for fd in fds:
        new_fds = new_fds | fd.split()

    done = False

    while not done:
        done = True # assume we are done
        for fd in new_fds:
            if fd.left() < closure and not fd.right() < closure:
                closure = closure | fd.right()
                done = False


    return closure


def projection():
    pass
