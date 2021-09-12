import time
import functools

def timer(num_times: int):
    """Decorator function that times the inputted function.
    Runs the inputted function num_times, then prints and
    returns average time taken

    @type num_times: int
    @param num_times: Number of times to run the function.
    @rtype: float
    @returns: Average time taken to run function across
    num_times iterations.
    """
    # required for arg num_times in decorator
    def decorator_timer(func):
        @functools.wraps(func)
        def wrapper_timer(*args, **kwargs):
            sum_times = 0
            for i in range(num_times):
                start_time = time.perf_counter()
                func(*args, **kwargs)
                end_time = time.perf_counter()
                run_time = end_time - start_time
                sum_times += run_time
            value = sum_times / num_times
            print(f"Average run time of {func.__name__!r}: {value:.4f} s")
            return value
        return wrapper_timer
    return decorator_timer
