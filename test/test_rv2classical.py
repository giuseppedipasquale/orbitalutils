import numpy as np
import pytest
import rv2classical

# Tests the Semi-Major Axis calculation using GMAT 
def testSMA:
  r = np.array([1000,200,-30]).reshape(-1,1)
  v = np.array([5,-1,-2]).reshape(-1,1)
  par = rv2classical(r,v)
  assert np.allclose(par[0],1250.349,rtol=1e-6)
  
