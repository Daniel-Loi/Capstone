import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.fft import fft, ifft
import scipy.fftpack as fftpk
from scipy.io import wavfile

def volume(signal,volume):
    new_signal = np.clip(signal * volume, -32768, 32767).astype(np.int16)
    return new_signal

def fade_in(signal,rate,duration):
    fade_in_samples = int(duration * rate)
    fade_in_mask = np.linspace(0, 1, fade_in_samples)
    signal[:fade_in_samples] *= fade_in_mask[:, np.newaxis] if signal.ndim > 1 else fade_in_mask

    return signal
    
def fade_out(signal,rate,duration):
    fade_out_samples = int(duration * rate)
    fade_out_mask = np.linspace(1, 0, fade_out_samples)
    signal[-fade_out_samples:] *= fade_out_mask[:, np.newaxis] if signal.ndim > 1 else fade_out_mask

    return signal


s_rate, signal = wavfile.read("Test.wav") 


signal = signal.astype(np.float32)
song_dur = len(signal)/s_rate

FFT = abs(fft(signal))
freqs = fftpk.fftfreq(len(FFT), (1.0/s_rate))


plt.plot(freqs[range(len(FFT)//2)], FFT[range(len(FFT)//2)])                                                          
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.show()


new_signal = fade_in(signal,s_rate,10)
new_signal = fade_out(new_signal,s_rate,20)
new_signal = volume(new_signal,2)

wavfile.write('output.wav', s_rate, new_signal)

FFT = abs(fft(new_signal))
freqs = fftpk.fftfreq(len(FFT), (1.0/s_rate))


plt.plot(freqs[range(len(FFT)//2)], FFT[range(len(FFT)//2)])  
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.show()