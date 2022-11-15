def xor_right_shift(x, a):
    if a >= 0:
        return (x ^ (x >> a)) % (1<<32)
    else:
        a = -a
        return (x ^ (x << a)) % (1<<32)

def xor_right_shift_reverse(x, a):
    if a >= 0:
        
        i = 1
        while i * a <= 32:
            x ^= x >> (i * a)
            i <<= 1
        return x
    else:
        a = -a
        while a < 32:
            x =( x ^ (x << a)) % (1<<32)
            a *= 2
        return x

def advance_seed(hex_seed):
    seed = int(hex_seed, 16)
    seed = xor_right_shift(seed, -13)
    seed = xor_right_shift(seed, 17)
    seed = xor_right_shift(seed, -5)
    hex_seed = hex(seed% (1<<32))
    return hex_seed

def backtrack_seed(hex_seed):
    seed = int(hex_seed, 16)
    seed = xor_right_shift_reverse(seed, -5)
    seed = xor_right_shift_reverse(seed, 17)
    seed = xor_right_shift_reverse(seed, -13)
    hex_seed = hex(seed% (1<<32))
    return hex_seed

def check_last_kth_seed(hex_seed, k):
    seed = hex_seed
    for _ in range(k):
        seed = backtrack_seed(seed)
    return seed

## Usage:
print(check_last_kth_seed("0x4080601", 3)) # This will give you the seed 3 advance ahead 
