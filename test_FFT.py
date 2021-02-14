import forwardFFT, inverseFFT
import numpy as np

x = np.arange(8)
X = forwardFFT.FFT(x)
y = inverseFFT.iFFT(X)
print np.allclose(x,y)