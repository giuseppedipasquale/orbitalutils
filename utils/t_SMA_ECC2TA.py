def t_SMA_ECC2TA(t, SMA, ECC):
"""
    Given time t, semi-major axis SMA and
    eccentricity ECC, returns the true
    anomaly TA.
"""
  E = t_SMA_ECC2E(t, SMA, ECC)
  TA = E2TA(ECC,E)
  return TA
