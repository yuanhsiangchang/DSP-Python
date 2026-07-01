import numpy as np
import matplotlib.pyplot as plt
import pywt

wavelet_name = "db4"           # 定義小波名稱
wavelet = pywt.Wavelet( wavelet_name )

plt.figure( 1 )                # 繪圖
coefficients = wavelet.dec_lo  # 分解濾波器(低頻)
plt.stem( x, coefficients )
plt.xlabel( "Tap" )
plt.ylabel( "Coefficients" )

plt.figure( 2 )
coefficients = wavelet.dec_hi  # 分解濾波器(高頻)
plt.stem( coefficients )
plt.xlabel( "Tap" )
plt.ylabel( "Coefficients" )

plt.show()