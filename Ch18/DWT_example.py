import numpy as np
import pywt

x = np.array( [ 16, 12, 8, 4, 5, 7, 3, 1 ] )

print( "Haar Wavelet" )                # Haar小波
cA, cD = pywt.dwt( x, "db1" )
print( "DWT Coefficients: ", cA, cD )
xp = pywt.idwt( cA, cD, "db1" )
print( "Reconstruction: ", xp )

print( "Daubechies Wavelet (4-Tap)" )  # Daubechies小波(4-Tap)
cA, cD = pywt.dwt( x, "db2" )
print( "DWT Coefficients: ", cA, cD )
xp = pywt.idwt( cA, cD, "db2" )
print( "Reconstruction: ", xp )

print( "Daubechies Wavelet (8-Tap)" )  # Daubechies小波(8-Tap)
cA, cD = pywt.dwt( x, "db4" )
print( "DWT Coefficients: ", cA, cD )
xp = pywt.idwt( cA, cD, "db4" )
print( "Reconstruction: ", xp )