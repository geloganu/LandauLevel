import numpy as np
from constants import *
from hamiltonian import *
from particles import *

def free(particle):
    return 0

def harmonic_oscillator(particle):
	kx = 0.02 
	ky = 0.02

	return 0.5 * kx * np.dot(particle.x,particle.x) + 0.5 * ky * np.dot(particle.y,particle.y)


H = hamiltonian(N = 1, spacing = 100, potential = harmonic_oscillator, extent = 10, dim = 2)

v,w = H.solve(20)

print(v)