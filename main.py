"""
CMPS 2200  Recitation 3.
See recitation-03.md for details.
"""
import time

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n))
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.

def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    # e.g., [1,0] vs [1]
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y

def quadratic_multiply(x, y):
    # this just converts the result from a BinaryNumber to a regular int
    return _quadratic_multiply(x,y).decimal_val

def _quadratic_multiply(x, y):
    xvec = BinaryNumber(x).binary_vec
    yvec = BinaryNumber(y).binary_vec
    (xvec, yvec) = pad(xvec,yvec)

    if x<=1 and y <= 1:
        return BinaryNumber(x*y)
        
    xleft, xright = split_number(xvec)
    
    yleft, yright = split_number(yvec)
    
    ##xleft = bit_shift(xleft, len(xright.binary_vec)).binary_vec
    ##yleft = bit_shift(yleft, len(yright.binary_vec)).binary_vec
    
    n = len(xvec)
    p1 = _quadratic_multiply(xleft.decimal_val, yleft.decimal_val)
    p2 = _quadratic_multiply(xleft.decimal_val, yright.decimal_val)
    p3 = _quadratic_multiply(xright.decimal_val, yleft.decimal_val)
    p4 = _quadratic_multiply(xright.decimal_val, yright.decimal_val)

    return BinaryNumber(
        bit_shift(p1, n).decimal_val + 
        bit_shift(p2, n//2).decimal_val +
        bit_shift(p3, n//2).decimal_val +
        p4.decimal_val
    )
    



    
    
def test_quadratic_multiply(x, y, f):
    start = time.time()
    result = f(x, y)
    
    return (time.time() - start)*1000


    
    

