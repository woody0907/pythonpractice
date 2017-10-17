__author__ = 'woody'
def gensquares(N):
    for i in range(N):
        yield i ** 2



# def mymap(func,*seqs):
#     res = []
#     for args in zip(*seqs):
#         res.append(func(*args))
#     return res

def mymap(func,*seqs):
    return [func(*args) for args in zip(*seqs)]


def myzip(*seqs):
    res = []
    seqs = [list(S) for S in seqs]
    while all(seqs):
        print(seqs)
        res.append(tuple(S.pop(0) for S in seqs))
    return res
S1,S2 = 'abc','xyz123'
print(myzip(S1,S2))