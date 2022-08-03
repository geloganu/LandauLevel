import numpy as np
from constants import *
from hamiltonian import *
from particles import *

def harmonic_oscillator(particle):

	kx = 0.02 
	ky = 0.02
	return 0.5 * kx * particle.x**2   +    0.5 * ky * particle.y**2 

H = hamiltonian(N = 1, spacing = 100, potential = harmonic_oscillator, extent = 28.345891869386552, dim = 2)

eigVal, eigVec = H.solve(max_state=30)

print('Ground state energy: ', eigVal[0])
print('Ground state: ', eigVec[0])