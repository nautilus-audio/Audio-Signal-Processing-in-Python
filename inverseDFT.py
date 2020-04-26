import numpy as np


def iDFT(X):
	"""
	Input:
	X (numpy array) = input sequence (frequency spectrum) of length N
	Output:
	y (numpy array) = time-domain signal
	"""
	N = len(X)
	y = np.array([1.0/N * sum(X*genComplexSine(k, N)) for k in range(N)])
	return y


def genComplexSine(k, N):
	"""
	Inputs:
	k (integer) = frequency index of the complex sinusoid of the DFT
	N (integer) = length of complex sinusoid in samples
	Output:
	cSine (numpy array) = The generated complex sinusoid (length N)
	"""
	n = np.arange(N)
	cSine = np.exp(1j * 2 * np.pi * k * n / N)
	return cSine
