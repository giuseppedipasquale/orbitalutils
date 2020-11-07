def pqw2IJK(r_pqw, RAAN, INC, AOP):
    """ Transforms a vector in the pqw frame (r_pqw),
        into a vector in the IJK frame (r_IJK)
        rotating around the Z-axis by RAAN,
        around the X-axis by INC; and around the
        Z-axis by AOP.
    """
    R3_RAAN =   np.array([[np.cos(RAAN), -np.sin(RAAN),    0],
                         [np.sin(RAAN),    np.cos(RAAN),   0],
                         [0,               0,              1]])
                         
    R1_INC  =   np.array([[1,  0,             0],
                          [0,  np.cos(INC),  -np.sin(INC)],
                          [0,  np.sin(INC),   np.cos(INC)]])
    
    R3_AOP =    np.array([[np.cos(AOP), -np.sin(AOP),   0],
                         [np.sin(AOP),   np.cos(AOP),   0],
                         [0,             0,             1]])

    R = R3_RAAN.dot(R1_INC.dot(R3_AOP))

    r_IJK = R.dot(r_pqw)
    
    return r_IJK
