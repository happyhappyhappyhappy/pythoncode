# フェルマーの小定理の確認
# import collections
import math

MOD = 11


def felmerMod(input_value, mod_num):
    #    pow_value = input_value**(mod_num-1)
    pow_value = math.pow(input_value, (mod_num-1))
    return pow_value % mod_num


if __name__ == "__main__":
    p = MOD
    for x in range(1, MOD, +1):
        value = felmerMod(x, MOD)
        print("{} ** {} mod {} ->{}".format(x, MOD-1, MOD, value))
