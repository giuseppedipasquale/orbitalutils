import numpy as np

def t_SMA_ECC2E(t,SMA,ECC):
"""
    Given time t, semi-major axis SMA and
    eccentricity ECC, returns the eccentric
    anomaly E.
"""
    n = 20
    mi = 398600.4418
    
    E = np.ones((n,1))
    f = np.ones((n,1))
    df = np.ones((n,1))
    
    M = t*np.sqrt(mi/(SMA)**3)
    E[0] = M
    E_RES = 0
    
    err = 1
    tol = 1e-7
    i = 1
    
    while err > tol:
        f[i] = E[i-1]-ECC*np.sin(E[i-1])
        df[i] = 1 - ECC*np.cos(E[i-1])
        E[i] = E[i-1] - (f[i]-M)/df[i]
        err = abs(E[i]-E[i-1])
        E_RES = E[i]
        i = i+1
    
    return E_RES
