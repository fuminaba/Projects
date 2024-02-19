import time
import logging
import numpy as np


# =========================== # 
# >>> Decorator Functions <<< #
# =========================== #
def log_run_duration(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        runtime = end_time - start_time
        runtime_units = 'seconds'
        if 3600 > runtime >= 60:
            runtime = round(runtime / 60, 4)
            runtime_units = 'minutes'
        if runtime >= 3600:
            runtime = round(runtime / 3600)
            runtime_units = 'hours'
        message = (f"Function '{func.__name__}' took "
                   f"{runtime} {runtime_units} to execute.")
        logging.info(message)
        return result
    return wrapper