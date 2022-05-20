import numpy as np 

V = 1
nu = (1/20)
T_max = 4


def default_matrix(N,d,v,w):
	M = d*np.eye(N)
	for i in range(N-1):
		M[i,i+1]=v
		M[i+1,i]=w
	print(M)
	return M


def centered_explicit (N,tau,u):
	h = 20./(N+1)
	c = (nu*tau)/(h**2)
	d = (V*tau)/h
	X = np.linspace(-10,10,N+2)
	nmax = int(T_max/tau)
	T = np.linspace(0.,tau*nmax,nmax+1)
	U_n = np.zeros((nmax+1,N+2))
	M = default_matrix(N,1-2*c, c-(d/2), c+(d/2))
	un = u(X[1:N+1])
	U_n[0,1:N+1] = un
	for i in range (nmax):
		un = M@un
		U_n[i+1, 1:N+1] = un 
	return X,T,U_n


def decentered_explicit_left(N,tau,u):
	h = 20./(N+1)
	c = (nu*tau)/(h**2)
	d = (V*tau)/h
	X = np.linspace(-10,10,N+2)
	nmax = int(T_max/tau)
	T = np.linspace(0.,tau*nmax,nmax+1)
	U_n = np.zeros((nmax+1,N+2))
	M = default_matrix(N,1-d-2*c, c, d+c)
	un = u(X[1:N+1])
	U_n[0,1:N+1] = un
	for i in range (nmax):
		un = M@un
		U_n[i+1, 1:N+1] = un 
	return X,T,U_n


def centered_implicit(N,tau,u):
	h = 20./(N+1)
	c = (nu*tau)/(h**2)
	d = (V*tau)/h
	X = np.linspace(-10,10,N+2)
	nmax = int(T_max/tau)
	T = np.linspace(0.,tau*nmax,nmax+1)
	U_n = np.zeros((nmax+1,N+2))
	M = default_matrix(N,1+2*c, (d/2)-c, -c-(d/2))
	un = u(X[1:N+1])
	U_n[0,1:N+1] = un
	for i in range (nmax):
		un = np.linalg.solve(M,un)
		U_n[i+1, 1:N+1] = un 
	return X,T,U_n	


def decentered_implicit_left(N,tau,u):
	h = 20./(N+1)
	c = (nu*tau)/(h**2)
	d = (V*tau)/h
	X = np.linspace(-10,10,N+2)
	nmax = int(T_max/tau)
	T = np.linspace(0.,tau*nmax,nmax+1)
	U_n = np.zeros((nmax+1,N+2))
	M = default_matrix(N,(1+d+2*c), -c, -(d+c))
	un = u(X[1:N+1])
	U_n[0,1:N+1] = un
	for i in range (nmax):
		un = np.linalg.solve(M,un)
		U_n[i+1, 1:N+1] = un 
	return X,T,U_n	


def centered_CN(N,tau,u):
	h = 20./(N+1)
	c = (nu*tau)/(h**2)
	d = (V*tau)/h
	X = np.linspace(-10,10,N+2)
	nmax = int(T_max/tau)
	T = np.linspace(0.,tau*nmax,nmax+1)
	U_n = np.zeros((nmax+1,N+2))
	M1 = default_matrix(N,(1+c),((d/4)-(c/2)),-(1+(c/2)))
	M2 = default_matrix(N,(1-c),((c/2)-(d/4)),((d/4)+(c/2)))
	un = u(X[1:N+1])
	U_n[0,1:N+1] = un
	for i in range (nmax):
		un = np.linalg.solve(M1,M2@un)
		U_n[i+1, 1:N+1] = un 
	return X,T,U_n
	

def decentered_CN_left(N,tau,u):		
	h = 20./(N+1)
	c = (nu*tau)/(h**2)
	d = (V*tau)/h
	X = np.linspace(-10,10,N+2)
	nmax = int(T_max/tau)
	T = np.linspace(0.,tau*nmax,nmax+1)
	U_n = np.zeros((nmax+1,N+2))
	M1 = default_matrix(N,(1+(d/2)+c),-(c/2),-((d/2)+(c/2)))
	M2 = default_matrix(N,(1-(d/2)-c),(c/2),((d/2)+(c/2)))
	un = u(X[1:N+1])
	U_n[0,1:N+1] = un
	for i in range (nmax):
		un = np.linalg.solve(M1,M2@un)
		U_n[i+1, 1:N+1] = un 
	return X,T,U_n
