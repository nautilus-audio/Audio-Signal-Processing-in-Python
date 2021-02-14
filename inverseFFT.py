import numpy as np
from forwardFFT import FFT


def iFFT(X):
	"""
	Input:
	x (numpy array) = input sequence of length N
	Output:
	The function should return a numpy array of length N
	X (numpy array) = The N point DFT of the input sequence x
	"""

	x = np.array([])

	# conjugate complex nums
	X = np.conj(X)

	# forward FFT
	x = FFT(X)

	# conjugate again
	x = np.conj(x)

	# Scale
	x /= x.size

	return x


def genComplexSine(k, N):
	"""
	Inputs:
	k (integer) = frequency index of the complex sinusoid of the DFT
	N (integer) = length of complex sinusoid in samples
	Output:
	The function should return a numpy array
	cSine (numpy array) = The generated complex sinusoid (length N)
	"""
	n = np.arange(N)
	cSine = np.exp(1j * 2 * np.pi * k * n / N)
	return cSine

