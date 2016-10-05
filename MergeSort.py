import math
from Merge import merge

def mergesort(x):

    ll = 0
    uu = len(x)
    mm = math.ceil((uu+ll)/2)
    numinv = 0

    if uu >1:
        x[ll:mm], numinv1 = mergesort(x[ll:mm])
        x[mm:uu], numinv2 = mergesort(x[mm:uu])
        x[:], numinv3 = merge(x, ll, mm, uu)
        numinv = numinv + numinv1 + numinv2 + numinv3

    return x, numinv
