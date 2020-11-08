from numpy import floor

def JD2dmy(JD):
"""
    Given Julian Day JD, returns
    day:month:year (dd:mm:yyyy).
    
    Example of usage:
    >> print(JD2dmy(2458058))
    >> [ 31, 10, 2017 ]
"""
    g = floor(floor((JD-4479.5)/36524.25)*0.75+0.5)-37
    N = JD+g
    yyyy = floor(N/365.25)-4712
    d = floor((N-59.25)%365.25)
    mm = (floor((d+0.5)/30.6)+2)%12+1
    dd = floor((d+0.5)%30.6)+1
    
    return [dd,mm,yyyy]
