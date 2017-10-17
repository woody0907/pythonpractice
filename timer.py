import time,sys
__author__ = 'woody'

def timer():return time.clock() if sys.platform[:3] == 'win' else time.time()

def total(reps,func,*pargs,**kargs):
    """
    Total time to run func() reps times
    :param reps:
    :param func:
    :param pargs:
    :param kargs:
    :return: (elapsed,lastResult)
    """
    replist = list(range(reps))
    start = timer()
    for i in replist:
        ret = func(*pargs,**kargs)
    elapesd = timer() - start
    return (elapesd,ret)

def bestof(reps,func,*pargs,**kargs):
    """
    bestof
    :param reps:
    :param func:
    :param pargs:
    :param kargs:
    :return:
    """
    replist = list(range(reps))
    best = 2 ** 32
    for i in replist:
        start = timer()
        ret = func(*pargs,**kargs)
        elapsed = timer() - start
        if elapsed < best: best = elapsed

    return (best,ret)


def bestoftotal(reps1,reps2,func,*pargs,**kargs):
    """
    bsetoftotal
    :param reps1:
    :param reps2:
    :param func:
    :param pargs:
    :param kargs:
    :return:
    """
    return bestof(reps1,total,reps2,func,*pargs,**kargs)







