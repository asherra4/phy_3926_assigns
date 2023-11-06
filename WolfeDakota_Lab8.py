import numpy as np
import matplotlib.pyplot as plt

def diffusion_ftcs(nspace, ntime, tau_rel, args)
  L, kappa = args

  h = L/(nspace-1) 
  t_sigma = h**2/2*kappa
  tau = t_sigma*tau_rel # tau_rel = tau / t_sigma
  coeff = kappa*tau/h**2
  if coeff < 0.5 :
      print('Solution is expected to be stable')
  else:
      print('WARNING: Solution is expected to be unstable')
