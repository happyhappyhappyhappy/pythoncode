import numpy as np

def auto_fp16(out_fp32=False):
    def auto_fp16_wrapper(func):
        def wrapper(*args,**kargs):
            new_args=[np.float16(a) for a in args]
            result = func(*new_args,**kargs)
            if out_fp32:
                result = np.float32(result)
            return result
        return wrapper
    return auto_fp16_wrapper

# @auto_fp16(out_fp32=True)
@auto_fp16()
def add(x,y):
    return x+y

print(f"addの名前->{add.__name__}")
ret = add(np.float32(1.0),np.float32(2.0))
print(f"output: {ret}({ret.dtype})")
