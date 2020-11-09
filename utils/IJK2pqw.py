import numpy as np

def IJK2pqw(r_IJK, RAAN, INC, AOP):
    """ Transforms a vector in the IJK frame (r_IJK),
        into a vector in the pqw frame (r_pqw)
        rotating around the Z-axis by AOP,
        around the X-axis by INC; and around the
        Z-axis by RAAN.
    """
    R3_RAAN =   np.array([[np.cos(RAAN), -np.sin(RAAN),    0],
                         [np.sin(RAAN),    np.cos(RAAN),   0],
                         [0,               0,              1]]).transpose()
                         
    R1_INC  =   np.array([[1,  0,             0],
                          [0,  np.cos(INC),  -np.sin(INC)],
                          [0,  np.sin(INC),   np.cos(INC)]]).transpose()
    
    R3_AOP =    np.array([[np.cos(AOP), -np.sin(AOP),   0],
                         [np.sin(AOP),   np.cos(AOP),   0],
                         [0,             0,             1]]).transpose()

    R = R3_AOP.dot(R1_INC.dot(R3_RAAN))

    r_pqw = R.dot(r_IJK)
    
    return r_pqw
