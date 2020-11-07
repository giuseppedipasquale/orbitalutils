import numpy as np
from numpy.linalg import norm

def rv2classical(r,v):
    """
        Calculates classical orbital elements starting
        from position vector r and velocity vector v.
    """
    
    # I,J,K fundamental versors
    I = np.array([1, 0, 0])
    J = np.array([0, 1, 0])
    K = np.array([0, 0, 1])

    # radius and velocity versors
    i_r = r/norm(r)
    i_v = v/norm(v)
    
    mi = 398600.4418                        # gravitational parameter
    E_g = (norm(v)**2)/2 - mi/norm(r)       # specific orbital energy
    SMA = - mi/(2*E_g)                      # semi-major axis

    # specific angular momentum vector h and versor i_h
    h = np.cross(r.reshape(1,-1),v.reshape(1,-1)).reshape(-1,1)
    i_h = h/norm(h)

    # eccentricity vector e
    e = 1/mi*((norm(v)**2-mi/norm(r))*r-norm(r.transpose().dot(v))*v)
    # eccentricity value ECC
    ECC = norm(e)
    i_e = e/norm(e) # eccentricity versor i_e

    # ascending node vector n and versor i_n
    n = np.cross(K,h.reshape(1,-1)).reshape(-1,1)
    if norm(n)==0:
        i_n = n
    else:
        i_n = n/norm(n)
        
    # inclination INC
    INC = norm(np.arccos(K.dot(i_h)))
    if np.isnan(INC):
        INC = 0

    # right ascension of ascending node RAAN
    if J.dot(i_n) >= 0:
        RAAN = norm(np.arccos(I.dot(i_n)))
    else:
        RAAN = 2*np.pi-norm(np.arccos(I.dot(i_n)))
    if np.isnan(RAAN) or INC == 0:
        RAAN = 0
        
    # true anomaly TA
    if r.transpose().dot(v) >=0:
        TA = norm(np.arccos(i_r.transpose().dot(i_e)))
    else:
        TA = 2*np.pi-norm(np.arccos(i_r.transpose().dot(i_e)))

    # argument of perigee AOP
    if K.dot(i_e) >= 0:
        AOP = norm(np.arccos(i_n.transpose().dot(i_e)))
    else:
        AOP = 2*np.pi-norm(np.arccos(i_n.transpose().dot(i_e)))
    if np.isnan(AOP):
        AOP = 0

    return [SMA,ECC,INC,RAAN,AOP,TA]
