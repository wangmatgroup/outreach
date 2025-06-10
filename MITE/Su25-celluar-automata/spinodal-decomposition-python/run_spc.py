from spinodal_decomp import *

# Inputs
#    n (integer) = array size, 
#    nstep (integer) = number of iterations, 
#    d (float) = diffusivity, AA (float) = non-linear interaction parameter
sim = SpinodalConserved(n=100, nstep=300, d=0.5, AA = 1.3)
sim.animate()
