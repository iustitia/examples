def f():
    try:
        return "try"
    finally:
        return "finally"


f()


def f2():
    try:
        print("try - print")
        return "try"
    finally:
        print("finally - print")
        return "finally"


f2()
