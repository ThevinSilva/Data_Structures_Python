from timeit import default_timer

class RunTime(object):
    def __init__(self, func):
        """
        class that returns the time elapased in running a program
            :param self: object
            :param func: wrapped function
        """   
        self.func = func
    def __call__(self,*args,**kw):
        SCALE = 1000000    # the scale right now is a micro second
        t = default_timer() * SCALE
        result = self.func(*args,**kw)
        print(f"{self.func.__name__.upper()} ran for {(default_timer() * SCALE) - t } μs")
        return result 

if __name__ == "__main__":
    pass