import sys
import traceback

def inner_func(str_value):
    return int(str_value)

def outer_func(str_value):
    inner_func(str_value)

if __name__ == "__main__":
    try:
        outer_func('abc')
    except Exception, e:
        traceback.print_exc(file=sys.stderr)
        exit(1)
