# Consolidated Python code for the full system based on MATLAB scripts: pbc.m, sd.m, and sdc.m
# Uses classes and replaces variable `s` with `eta` to reflect concentration/phase-field notation

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class SpinodalBase:
    def __init__(self, n, nstep, d, AA=1.3):
        """
        Base class shared by both conserved and non-conserved simulations.

        Parameters:
        - n: lattice size (n x n)
        - nstep: number of simulation steps
        - d: diffusion coefficient
        - AA: strength of nonlinearity
        """
        self.n = n
        self.nstep = int(nstep)
        self.d = d
        self.AA = AA
        self.eta = 0.1 * (2 * np.random.rand(n, n) - 1)  # random initial field, [-0.1, 0.1)

        ### alternate initial concentration profiles ###

        ## non-parity concentration, [-0.4, -0.2)
        #self.eta = 0.1 * (2 * np.random.rand(n, n) - 4)  # random initial field
        
        ## seed in the middle, [-0.001, +0.001)
        #self.eta = 0.001 * (2 * np.random.rand(n, n) - 1)  # random initial field
        #mid=int(n/2)
        #self.eta[mid,mid] = 1.0


    def pbc_neighbors(self, field):
        """
        Compute nearest (A1) and next-nearest (A2) neighbors with periodic boundary conditions.
        """
        A1 = (np.roll(field, 1, axis=0) + np.roll(field, -1, axis=0) +
              np.roll(field, 1, axis=1) + np.roll(field, -1, axis=1))
        A2 = (np.roll(np.roll(field, 1, axis=0), 1, axis=1) +
              np.roll(np.roll(field, -1, axis=0), 1, axis=1) +
              np.roll(np.roll(field, 1, axis=0), -1, axis=1) +
              np.roll(np.roll(field, -1, axis=0), -1, axis=1))
        return A1, A2

    def animate(self, interval=100):
        """
        animation method for visualization.
        """
        fig, ax = plt.subplots()
        im = ax.imshow(self.eta, cmap='bwr', vmin = -1, vmax = 1, interpolation='none')
        plt.colorbar(im, ax=ax)
        plt.title(self.title)

        def update_plot(frame):
            self.step()
            im.set_data(self.eta.copy())
            return [im]

        anim = FuncAnimation(fig, update_plot, frames=range(self.nstep), interval=interval, blit=False)

        def on_close(event):
            anim.event_source.stop()
            plt.close('all')

        fig.canvas.mpl_connect('close_event', on_close)
        plt.show()


class SpinodalNonConserved(SpinodalBase):
    def __init__(self, n, nstep, d, AA=1.3):
        super().__init__(n, nstep, d, AA)
        self.title = "Spinodal Decomposition (Non-Conserved)"

    def step(self):
        A1, A2 = self.pbc_neighbors(self.eta)
        etat = self.AA * np.tanh(self.eta) + self.d * (A1 / 6 + A2 / 12 - self.eta)
        self.eta = etat.copy()

class SpinodalConserved(SpinodalBase):
    def __init__(self, n, nstep, d, AA=1.3):
        super().__init__(n, nstep, d, AA)
        self.title = "Spinodal Decomposition (Conserved)"

    def step(self):
        A1, A2 = self.pbc_neighbors(self.eta)
        st = self.AA * np.tanh(self.eta) + self.d * (A1 / 6 + A2 / 12 - self.eta)
        B1, B2 = self.pbc_neighbors(st)
        stt = st - (B1 - A1) / 6 - (B2 - A2) / 12
        self.eta = stt.copy()

