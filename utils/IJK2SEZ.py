import numpy as np

def IJK2SEZ(r_IJK, ALPHA, DELTA):
  """
      Given a vector in the IJK fixed coordinate
      reference system and angles of rotation ascencion
      ALPHA and declination DELTA, returns the vector in
      SEZ reference system.
  """
    R3_ALPHA =   np.array([[np.cos(ALPHA), -np.sin(ALPHA),    0],
                         [np.sin(ALPHA),    np.cos(ALPHA),   0],
                         [0,               0,              1]]).transpose()
                         
    R1_DELTA  =   np.array([[1,  0,             0],
                          [0,  np.cos(DELTA),  -np.sin(DELTA)],
                          [0,  np.sin(DELTA),   np.cos(DELTA)]]).transpose()
    
    R = R3_DELTA.dot(R1_ALPHA)

    r_SEZ = R.dot(r_IJK)
    
    return r_SEZ
