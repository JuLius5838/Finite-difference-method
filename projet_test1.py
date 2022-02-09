import numpy as np 
import matplotlib.pyplot as plt 
from lib_projet import *

h =0.09
tau = 0.3
def u0(x):
	return np.exp(-(x**2))



N = int(round((20/h)-1))

t = np.array([0,0.5,1,1.5])

X1, T1, U1_n = centered_explicit(N, tau,u0)
plt.figure("Centered explicit")
for ti1 in t : 
	n = int(round(ti1/tau))
	plt.plot(X1, U1_n[n,:], label='t={:5.2f})'.format(T1[n]))
plt.title("Centered explicit")
plt.legend()


X2, T2, U2_n = decentered_explicit_left(N, tau,u0)
plt.figure("decentered explicit left")
for ti2 in t : 
	n = int(round(ti2/tau))
	plt.plot(X2, U2_n[n,:], label='t={:5.2f})'.format(T2[n]))
plt.title("Decentered explicit left")
plt.legend()


X3, T3, U3_n = centered_implicit(N, tau,u0)
plt.figure("centered_implicit")
for ti3 in t : 
	n = int(round(ti3/tau))
	plt.plot(X3, U3_n[n,:], label='t={:5.2f})'.format(T3[n]))
plt.title("Centered implicit")
plt.legend()


X4, T4, U4_n = decentered_implicit_left(N, tau,u0)
plt.figure("decentered implicit left")
for ti4 in t : 
	n = int(round(ti4/tau))
	plt.plot(X4, U4_n[n,:], label='t={:5.2f})'.format(T4[n]))
plt.title("Decentered implicit left")
plt.legend()

X5, T5, U5_n = decentered_implicit_left(N, tau,u0)
plt.figure("cetenred Cranck-Nicholson")
for ti5 in t : 
	n = int(round(ti5/tau))
	plt.plot(X5, U5_n[n,:], label='t={:5.2f})'.format(T5[n]))
plt.title("Centered Crank-Nicholson")
plt.legend()


X6, T6, U6_n = decentered_CN_left(N, tau,u0)
plt.figure("decentered_CN_left")
for ti6 in t : 
	n = int(round(ti6/tau))
	plt.plot(X6, U6_n[n,:], label='t={:5.2f})'.format(T6[n]))
plt.title("Decentered Crank-Nicholson")
plt.legend()
plt.show()

