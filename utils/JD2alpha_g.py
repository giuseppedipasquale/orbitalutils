def JD2alpha_g(JD):
"""
    Given Julian Day (JD), returns
    the Greenwich meridian angle (alpha_g)
    with respect to the Earth-fixed X-axis.
"""
    d = JD - dmy2JD(1,1,2000)
    t = d/36525
    alpha_g_t = 280.46061837 + 360.985647*d + 0.0003875*t**2 -t**3/(38710000)
    alpha_g = alpha_g_t%360
    return alpha_g
