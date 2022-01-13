import matplotlib.pyplot as plt
import numpy as np
from time import time_ns, time

def sev_pow(n):
    res = 1
    for i in range(n):
        res = (res << 3) - res
    return res

def thr_pow(n):
    res = 1
    for i in range(n):
        res = (res << 2) - res
    return res

def sev_pow_thr_pow(n):
    return sev_pow(thr_pow(n))

n=11
arr_len = np.empty(n)
arr_t_algo = np.empty(n)
arr_t_python = np.empty(n)
for i in range(1,n+1):
    t0=time()
    val = sev_pow_thr_pow(i)
    t1=time()
    val=7**(3**i)
    t2 = time()
    arr_len[i-1] = len(str(val))
    arr_t_algo[i-1] = t1-t0
    arr_t_python[i-1] = t2-t1
    print(i)


fig, axs = plt.subplots(3)
fig.suptitle('length of answer, time of our algorithm, and time taken by python to find 7**3**n based on n')
axs[0].plot(np.arange(n), arr_len)
axs[1].plot(np.arange(n), arr_t_algo)
axs[2].plot(np.arange(n), arr_t_python)

plt.show()
