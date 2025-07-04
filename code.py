import numpy as np
import scipy.linalg as sp
import matplotlib.pyplot as plt

 # Constants
hcut = 197300 # Reduced Planck's constant in eV * pm
m = 0.511e6 # Electron mass in eV/c^2
ee = 1439.964547 # e^2/(4 * pi * epsilon_0) in eV * pm

 # Potential function

def v(x):
 return-ee / x

 # Discretization parameters

 xmin = 0.00
 xmax = 2000
 N = 1000
 dx = (xmax- xmin) / N
 x = np.linspace(xmin, xmax, N+1)

 # Solving the eigenvalue problem

 val, vec = sp.eigh_tridiagonal(pdiag, sdiag)

 # Convert eigenvalues to physical units

 # Setting up the Hamiltonian matrix (diagonal and off-diagonal elements)

 pdiag = 1 / dx**2 + (m / (hcut**2)) * v(x[1:-1]) # Avoid singularity at r = 0
 sdiag = (-1 / (2 * dx**2)) * np.ones(len(pdiag)- 1)

 for i1 in range (3):
   eigval1 = (val[i1] * hcut**2) / m
   eigval11 = round(eigval1,2)
   print(f"For n = {i1+1} energy = {eigval11} eV ")

 # Plotting the wave functions for ground and first excited state

 linestyle = ['solid', 'dashed', 'dashdot', 'dotted']
 for i1 in range (3):
  plt.plot(x[1:-1], vec[:, i1]**2, label="n = %d"%(i1+1),ls=linestyle[i1],lw=2)
  plt.title('Wave Functions for the Hydrogen Atom')
  plt.xlabel('r (picometer (pm))')  
  plt.ylabel('|u(r)|^2')
  plt.legend()
  plt.show()