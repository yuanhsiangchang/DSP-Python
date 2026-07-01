import numpy as np
import wave
from scipy.io.wavfile import read, write
import struct
import pywt

def wavelet_lowpass_filtering( x ):
	cA, cD = pywt.dwt( x, "db4" )
	cD.fill( 0 )
	y = pywt.idwt( cA, cD, "db4" )
	return y

def wavelet_highpass_filtering( x ):
	cA, cD = pywt.dwt( x, "db4" )
	cA.fill( 0 )
	y = pywt.idwt( cA, cD, "db4" )
	return y
	
def main( ):
	infile  = input( "Input File: " )	
	outfile = input( "Output File: " )
	
	# ----------------------------------------------------
	#  輸入模組
	# ----------------------------------------------------	
	wav = wave.open( infile, 'rb' )
	num_channels = wav.getnchannels( )	# 通道數
	sampwidth	 = wav.getsampwidth( )	# 樣本寬度
	fs			 = wav.getframerate( )	# 取樣頻率(Hz)
	num_frames	 = wav.getnframes( )	# 音框數 = 樣本數
	comptype	 = wav.getcomptype( )	# 壓縮型態
	compname	 = wav.getcompname( )	# 無壓縮
	wav.close( )

	sampling_rate, x = read( infile )	# 輸入訊號

	# ----------------------------------------------------
	#  DSP 模組
	# ----------------------------------------------------	
	print( "(1) Lowpass Filtering using Wavelet Transform" )
	print( "(2) Highpass Filtering using Wavelet Transform" )
	choice = eval( input() )
	if choice == 1:
		y = wavelet_lowpass_filtering( x )
	if choice == 2:
		y = wavelet_highpass_filtering( x )
	
	# ----------------------------------------------------
	#  輸出模組
	# ----------------------------------------------------		
	wav_file = wave.open( outfile, 'w' )
	wav_file.setparams(( num_channels, sampwidth, fs, num_frames, comptype, compname )) 

	for s in y:
		wav_file.writeframes( struct.pack( 'h', int ( s ) ) )

	wav_file.close( ) 
	
main( )