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

    def coord_space(self, H): #deprecated
        if H.dim ==1:
            self.x = np.linspace(-H.extent/2, H.extent/2, H.spacing)
            H.observable_count = 1

        elif H.dim == 2:
            x = np.linspace(-H.extent/2, H.extent/2, H.spacing)
            y = np.linspace(-H.extent/2, H.extent/2, H.spacing)
            self.x, self.y = np.meshgrid(x,y)
            
    def matrix_operators(self, H):
        if H.dim == 2:
            #defining x and y coord
            x_space = np.linspace(-H.extent/2, H.extent/2, H.spacing)
            y_space = np.linspace(-H.extent/2, H.extent/2, H.spacing)

            #creating respective matrix
            x = np.diag(x_space,0)
            y = np.diag(y_space,0)

            I = np.eye(H.spacing)

            self.x = np.kron(I,x)
            self.y = np.kron(y,I)

            #delta matrix foundation
            delta_matrix = (np.diag(np.ones(H.spacing-1),1) - np.diag(np.ones(H.spacing-1),-1))*1/(2*H.dx)

            #x, y momentum operators (finite difference matrix)
            self.px = np.kron(I, - hbar *1j * delta_matrix)
            self.py = np.kron(- hbar *1j * delta_matrix, I)

            self.I = np.kron(I,I)
    
    def kinetic_term(self, H):
        I = np.eye(H.spacing)
        T_temp = 0.5*hbar**2/(2*me) * (-np.diag(np.ones(H.spacing-1),-1)+2*np.diag(np.ones(H.spacing),0)+np.diag(np.ones(H.spacing-1),1))

        if H.N == 1:
            T = T_temp
        
        elif H.N == 2:
            T = np.kron(T_temp,I) + np.kron(I,T_temp)
        
        return T
            


'''    
class multi_particle:
    def __init__(self, m = me, spin = None):

        N: number of particles (for N != 1)
        m: mass of electron set to %me by default
        spin: set to 'None' if spin polarized


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
'''