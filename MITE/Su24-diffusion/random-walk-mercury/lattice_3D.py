# Random walk on 3D lattice

import numpy as np

def random_walk(nt,latt_type):
    """
    Random walk on a 3D lattice
    Inputs:
        nt [integer] = number of desired jumps (i.e., time steps)
        latt_type [string] = choose the lattice geometry
                             current options: "cubic" and "fcc"
    Outputs:
        rs2 [array] = square displacement at each time step
        x   [array] = x-coordinate at each time step
        y   [array] = y-coordinate at each time step
        z   [array] = z-coordinate at each time step
    """
    x = np.zeros(nt+1)
    y = np.zeros(nt+1)
    z = np.zeros(nt+1)
    rs2 = np.zeros(nt+1)

    x[0] = 0
    y[0] = 0
    z[0] = 0
    rs2[0] = 0

    if latt_type == "cubic":
        # cubic lattice
        fd = np.floor(6 * np.random.rand(nt))
        delx = np.array([1, -1, 0, 0, 0, 0])
        dely = np.array([0, 0, 1, -1, 0, 0])
        delz = np.array([0, 0, 0, 0, 1, -1])
    elif latt_type == "fcc":
        # fcc lattice- 12 nearest neighbors
        fd = np.floor(12.* np.random.rand(nt)); # list with nt entries, 12 nearest neighbors
        delx = 0.5*np.array([1, 1, 0, -1, -1, -1, 0, 1, 0, -1, 1, 0]); # these three lines define the jumps on the FCC lattice
        dely = 0.5*np.array([1, 0, 1, 1, 0, 0, 1, 0, -1, -1, -1, -1]);
        delz = 0.5*np.array([0, 1, 1, 0, -1, 1, -1, -1, 1, 0, 0, -1]); 
    else:
    	raise ValueError("Lattice type not implemented! See lattice_3d.py")

    #sum over nt jumps
    for j in range(nt):
        x[j+1] = x[j] + delx[int(fd[j]) - 1] # x position at j+1 jump
        y[j+1] = y[j] + dely[int(fd[j]) - 1] # y position at j+1 jump
        z[j+1] = z[j] + delz[int(fd[j]) - 1] # z position at j+1 jump

        # square displacement position at j+1 jump in 3D
        rs2[j+1] = x[j+1]**2 + y[j+1]**2 + z[j+1]**2

    return rs2, x, y, z

