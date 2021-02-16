import forwardFFT, inverseFFT
import numpy as np
import os
import soundfile as sf

def test_file(path_to_file):
	x, fs = sf.read(path_to_file)
	N = len(x)

	# If file has odd number of samples, remove last one.
	if N % 2 > 0: 
		x = x[:len(x)-1]

	for dim in range(x.ndim):
		single_channel = forwardFFT.FFT(x[:,dim])
		if (dim==0):
			X = np.zeros((len(single_channel), x.ndim), dtype=complex)
		X[:,dim].real = single_channel.real
		X[:,dim].imag = single_channel.imag

	for ydim in range(X.ndim):
		single_channel_inv = inverseFFT.iFFT(X[:,ydim])
		if (ydim==0):
			y = np.zeros((len(single_channel_inv), X.ndim), dtype=complex)
		y[:,ydim].real = single_channel_inv.real
		y[:,ydim].imag = single_channel_inv.imag

	return np.allclose(x,y)

