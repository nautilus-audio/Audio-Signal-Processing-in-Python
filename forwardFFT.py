import numpy as np


def FFT(x):
	"""
	Input:
	x (numpy array) = input sequence of length N
	Output:
	The function should return a numpy array of length N
	X (numpy array) = The N point DFT of the input sequence x
	mX = magnitude spectrum
	pX = phase spectrum
	"""
	len_x = len(x)
	N = len(x)/2

	if N % 2 > 0:
		error_msg = "FFT size must be a power of 2."
		raise ValueError(error_msg)

	even_x = x[::2]
	odd_x = x[1::2]

	even_X = np.array([(np.sum(even_x*genComplexSine(k, N))) for k in range(N)])
	odd_X = np.array([(np.sum(odd_x*genComplexSine(k, N))) for k in range(N)])
	complex_exp = np.exp(-2j * np.pi * np.arange(len_x) / len_x)

	X = np.array([])
	X = np.concatenate([even_X + complex_exp[:N] * odd_X,
                               even_X + complex_exp[N:] * odd_X])

	mX = 20 * np.log10(abs(X))
	pX = np.angle(X)
	return X, mX, pX


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
	cSine = np.exp(-2j * np.pi * k * n / N)
	return cSine

