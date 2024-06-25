# Random walk on a 2D square lattice

# UT MITE 2024 Summer activity

#------------------------------------------------

# import relevant libraries, 
#  contains useful functions already implemented
import numpy as np
import matplotlib.pyplot as plt

# we define a function that encapsulates all the code related to
#  generating the path for a random walker
def random_walk(nt):
    """
    Random walk on a 2D square lattice
    Inputs:
        nt [integer] = number of desired jumps (i.e., time steps)
    Outputs:
        x   [array] = x-coordinate at each time step
        y   [array] = y-coordinate at each time step
    """
    # array for x- and y-coordinates along hopping path
    x = np.zeros(nt+1)
    y = np.zeros(nt+1)

    # particle starts at origin
    x[0] = 0 
    y[0] = 0

    # create a list of random numbers from 1 to 4 with nt entries
    fd = np.floor(4 * np.random.rand(nt))

    # ==== FILL ME IN ====== #
    # next two lines define the jumps on the square lattice:
    #   right, up, left, down
    delx = np.array([1,0,?,?])
    dely = np.array([0,1,?,?])
         
    # loop over nt jumps, add the jump vector as generated randomly in fd
    #sum over nt jumps
    for j in range(nt):
        x[j+1] = x[j] + delx[int(fd[j])] # x position at j+1 jump
        y[j+1] = y[j] + dely[int(fd[j])] # y position at j+1 jump

    return x, y


# this portion of the code gets executed when the script is run
if __name__ == '__main__':

   # Plot two different trajectories and compare
   # Here two trajectories with nt = 1,000 and nt = 10,000
   nts = [100, 1000]
   numtraj = len(nts)
   
   for i in range(numtraj):
       x, y = random_walk(nts[i])  
   
       # plotting
       label = 'n = {}'.format(nts[i])
       plt.figure()
       plt.plot(x, y)
       plt.legend([label], loc='center', bbox_to_anchor=(0.8, 0.9), borderaxespad=0.)
       plt.xlabel('x position')
       plt.ylabel('y position')
   
   plt.show()
   
   
