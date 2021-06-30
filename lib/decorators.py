import time

__all__ = ['timer']

def timer(original_func):

    def _wrapper():
        st = time.time()
        _return = original_func()
        exe_time = time.time() - st
        print('Function \'{fn}\' executed in {t} seconds'.format(fn=original_func.__name__, t=exe_time))
        return _return

    return _wrapper