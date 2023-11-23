import numpy as np
from functools import wraps

def auto_fp16(out_fp32=False):
    def auto_fp16_wrapper(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            new_args=[np.float16(a) for a in args]
            result = func(*new_args,**kwargs)
            if out_fp32:
                result=np.float32(result)
            return result
        return wrapper
    return auto_fp16_wrapper

@auto_fp16()
def add(x,y):
    return x+y

print(f"addの本名->{add.__name__}")
ret = add(np.float32(1.0),np.float32(2.0))
print(f"出力: {ret}({ret.dtype})")
