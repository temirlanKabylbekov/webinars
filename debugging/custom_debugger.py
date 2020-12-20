import sys


def trace_calls(frame, event, args):
    """
    :param frame: locals() + globals()
    :param event: line + exception + return
    :param args: function args
    :return:
    """
    print(f'called {frame.f_code.co_name}, from {frame.f_code.co_filename}, line {frame.f_lineno}, event {event}')
    return trace_calls


sys.settrace(trace_calls)


def a():
    print('in a()')


def b():
    print('in b()')


def c():
    print('in c()')
    a()
    b()


c()
