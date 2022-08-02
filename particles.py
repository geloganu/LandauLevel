import numpy as np
from hamiltonian import *
from constants import *

#particle builder for hamiltonian builder

#single particle case N=1
class single_particle:
    def __init__(self, m = me, spin = None):
        '''
        m: mass of electron set to %me by default
        spin: set to 'None' if spin polarized
        '''

        self.m = m
        self.spin = spin

    def coord_space(self, H):
        if H.dim ==1:
            self.x = np.linspace(-H.extent/2, H.extent/2, H.spacing)
            H.observable_count = 1

        elif H.dim == 2:
            x = np.linspace(-H.extent/2, H.extent/2, H.spacing)
            y = np.linspace(-H.extent/2, H.extent/2, H.spacing)
            self.x, self.y = np.meshgrid(x,y)
            H.bservable_count = 2
    
class multi_particle:
    def __init__(self, m = me, spin = None):
        '''
        N: number of particles (for N != 1)
        m: mass of electron set to %me by default
        spin: set to 'None' if spin polarized
        '''

        self.m = m
        self.spin = spin

    def coord_space(self, H, N):
        if H.dim ==1:
            self.x = np.linspace(-H.extent/2, H.extent/2, H.spacing)
            H.observable_count = 1

        elif H.dim == 2:
            x = np.linspace(-H.extent/2, H.extent/2, H.spacing)
            y = np.linspace(-H.extent/2, H.extent/2, H.spacing)
            self.x, self.y = np.meshgrid(x,y)
            H.bservable_count = 2
