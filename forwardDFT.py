import numpy as np


def DFT(x):
	"""
	Input:
	x (numpy array) = input sequence of length N
	Output:
	X (numpy array) = The N point DFT of the input sequence x
	mX = magnitude spectrum
	pX = phase spectrum
	"""
	N = len(x)
	X = np.array([(np.sum(x*genComplexSine(k, N))) for k in range(N)])
	# mX = np.abs(X)
	# pX = np.angle(X)
	return X


def genComplexSine(k, N):
	"""
	Inputs:
	k (integer) = frequency index of the complex sinusoid of the DFT
	N (integer) = length of complex sinusoid in samples
	Output:
	cSine (numpy array) = The generated complex sinusoid (length N)
	"""
	n = np.arange(N)
	cSine = np.exp(-1j * 2 * np.pi * k * n / N)
	return cSine
