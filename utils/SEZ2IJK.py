import numpy as np

def SEZ2IJK(r_SEZ, ALPHA, DELTA):
  """
      Given a vector in the South-East-Z coordinate
      reference system and angles of rotation ascencion
      ALPHA and declination DELTA, returns the vector in
      IJK fixed reference system.
  """
    R3_ALPHA =   np.array([[np.cos(ALPHA), -np.sin(ALPHA),    0],
                         [np.sin(ALPHA),    np.cos(ALPHA),   0],
                         [0,               0,              1]])
                         
    R1_DELTA  =   np.array([[1,  0,             0],
                          [0,  np.cos(DELTA),  -np.sin(DELTA)],
                          [0,  np.sin(DELTA),   np.cos(DELTA)]])
    
    R = R3_ALTA.dot(R1_DELTA)

    r_IJK = R.dot(r_SEZ)
    
    return r_IJK
