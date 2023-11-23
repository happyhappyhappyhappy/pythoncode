import numpy as np
def auto_fp16(func):
    def wrapper(*args,**kwargs):
        new_args=[np.float16(a) for a in args]
        result = func(*new_args,**kwargs)
        return result
    return wrapper

@auto_fp16
def add(x,y):
    return x+y

ret = add(np.float32(1.0),np.float32(2.0))
print(f"output: {ret} ({ret.dtype})")
