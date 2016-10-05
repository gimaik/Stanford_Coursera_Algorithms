def merge(x, ll, mm, uu):

    L = x[ll:mm]
    R = x[mm:uu]
    Lremain = len(L)

    y = []
    i = 0
    j = 0
    numinv = 0

    for k in range(0, uu):
        if i > len(L)-1:
            y.append(R[j])
            j += 1
        elif j > len(R)-1:
            y.append(L[i])
            i += 1
        elif L[i] < R[j]:
            y.append(L[i])
            i += 1
            Lremain -= 1
        else:
            y.append(R[j])
            j += 1
            numinv += Lremain

    return y, numinv
