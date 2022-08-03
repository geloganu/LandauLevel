import numpy as np
from constants import *
from hamiltonian import *
from particles import *

def free(particle):
    return 0

def harmonic_oscillator(particle):

	kx = 0.02 
	ky = 0.02
	return 0.5 * kx * particle.x**2    +    0.5 * ky * particle.y**2


H = hamiltonian(N = 1, spacing = 100, potential = harmonic_oscillator, extent = 15*Å, dim = 2)

v,w = H.solve(max_state = 30)

print(v)