def dmy2JD(dd,mm,yyyy):
"""
  Given date as day:month:year (dd:mm:yyyy),
  returns Julian Day (JD)
"""
    a = floor((14-mm)/12)
    y = yyyy+4800-a
    m = mm + 12*a-3
    
    JD = dd + floor((153*m+2)/5) + 365*y + floor(y/4) - floor(y/100) + floor(y/400) - 32045;
    return JD

