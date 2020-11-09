import numpy as np

def classical2rv(paremeters):
"""
    Given the classical orbital elements,
    returns radius and velocity vectors in IJK.
    
    Example of usage:
    >> par = [7000, 0.1, 0.03, 3.22, 2.1, 0]
    >> [r,v] = classical2rv(par)
    >> print(r)
    >> [[1500],[5200], [450]] *check first
"""
    SMA,ECC,INC,RAAN,AOP,TA = parameters
    mi = 398600.4418
     
     r_mag = (SMA*(1-ECC**2))/(1+ECC*np.cos(TA)) 
     r_pqw = np.array([[r_mag*np.cos(TA)],
                       [r_mag*np.sin(TA)],
                       [0]])
     r = pqw2IJK(r_pqw,RAAN,INC,AOP)
     
     p = SMA*(1-ECC**2)
     v_pqw = np.array([[-np.sqrt(mi/p)*np.sin(TA)],
                       [np.sqrt(mi/p)*(ECC+np.cos(TA))],
                       [0]])
      v = pqw2IJK(v_pqw,RAAN,INC,AOP)
      
      return [r,v]
