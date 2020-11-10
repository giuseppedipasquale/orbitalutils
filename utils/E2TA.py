def E2TA(ECC,E):
  TA = 0
  D_TA = 1e-3
  E0 = 0
  D_E = 1e-3
  while (E0>E+D_E) or (E0<E-D_E):
    if TA < np.pi:
      E0 = np.arccos((ECC+np.cos(TA))/(1+ECC*np.cos(TA)))
    else:
      E0 = 2*np.pi-np.arccos((ECC+np.cos(TA))/(1+ECC*np.cos(TA)))
    TA = TA + D_TA
  
  return TA
