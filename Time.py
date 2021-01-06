from time import time

def performance(func):
    def wrapper_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'took {t2-t1} ms')
        return result
    return wrapper_func

@performance
def how_long():
    print('1')
    for i in range(100000000):
        i*5
@performance
def how_long2():
    print('2')
    for i in list(range(100000000)):
        i*5

how_long()
how_long2()