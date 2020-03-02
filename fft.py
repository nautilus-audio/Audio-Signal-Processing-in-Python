import numpy as np
import math
from scipy.signal import get_window
import time


def FFT(x, fs, a_time):
	"""
	Input:
	x (numpy array) = input sequence of length N
	fs (int) = sampling frequency in Hz
	a_time (float) = time index in seconds
	Output:
	The function should return a numpy array of length N
	X (numpy array) = The N point DFT of the input sequence x
	mX (numpy array) = magnitude spectrum
	pX (numpy array) = phase spectrum
	"""
	start_time = time.time()
	fftbuffer = zeroPadZeroPhase(x, fs, a_time)
	N = len(fftbuffer)
	X = np.array([(np.sum(fftbuffer*genComplexSine(k, N))) for k in range(N)])
	mX = 20 * np.log10(abs(X))
	pX = np.angle(X)
	end_time = time.time() - start_time 
	print end_time
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
	cSine = np.exp(-1j * 2 * np.pi * k * n / N)
	return cSine


def zeroPadZeroPhase(x, fs, a_time):
    """
    Inputs:
        x (numpy array) = input signal of length M
        fs (float) = sampling frequency in Hz
        a_time (float) = time index in seconds
    Output:
        The function should return
        fftbuffer (numpy array) = windowed signal of N size
    """
    O = 511
    w = get_window("blackman", O)

    # Allocate and populate buffer
    M = len(x)
    N = 8 * O
    sample = int(a_time*fs) # get sample
    x1 = x[sample:sample+O] 
    fft_size = 1024
    hM1 = (w.size+1)//2
    hM2 = int(math.floor(w.size/2))
    fftbuffer = np.zeros(N)
    xw = x1*w 
    fftbuffer[:hM1] = xw[hM2:]
    fftbuffer[-hM2:] = xw[:hM2] 
    return fftbuffer
