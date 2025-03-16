import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt

def load_audio(file_path):
    """Load an audio file and return the signal and sample rate."""
    return librosa.load(file_path)

def compute_spectrogram(y, sr, n_fft=1028, hop_length=256):
    """Compute and return the spectrogram of the audio signal."""

    stft = librosa.stft(y, n_fft=n_fft, hop_length=hop_length)

    magnitude = np.abs(stft)

    db_magnitude = librosa.amplitude_to_db(magnitude, ref=np.max)
    return db_magnitude, hop_length

def get_frequency_time_info(db_magnitude, sr, hop_length=256, n_fft=1028):
    """Compute the frequency bins and time values for the spectrogram."""
    frequencies = librosa.fft_frequencies(sr=sr, n_fft=n_fft)  # Frequency axis (Hz)
    times = librosa.frames_to_time(np.arange(db_magnitude.shape[1]), sr=sr, hop_length=hop_length)  # Time axis (s)
    return frequencies, times

def plot_spectrogram(db_magnitude, sr, hop_length):
    """Plot the spectrogram."""
    plt.figure(figsize=(12, 6))
    librosa.display.specshow(db_magnitude, sr=sr, hop_length=hop_length, 
        x_axis='time', y_axis='log')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Spectrogram (STFT)')
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')
    plt.show()

def analyze_frequency_bands(y, sr, n_fft=2048, hop_length=512):
    """
    Analyze specific frequency bands in the audio signal.
    
    """
    # Compute STFT
    stft = librosa.stft(y, n_fft=n_fft, hop_length=hop_length)
    magnitude = np.abs(stft)
    
    # Get frequency bins
    freqs = librosa.fft_frequencies(sr=sr, n_fft=n_fft)
    
    # Define frequency bands
    bands = {
        'sub_bass': (20, 60),
        'bass': (60, 250),
        'low_mids': (250, 500),
        'mids': (500, 2000),
        'high_mids': (2000, 4000),
        'highs': (4000, 20000)
    }
    
    # Extract and analyze each frequency band
    band_energies = {}
    for band_name, (low_freq, high_freq) in bands.items():
        # Find the frequency bin indices for this band
        band_mask = (freqs >= low_freq) & (freqs <= high_freq)
        # Extract the magnitudes for this frequency band
        band_magnitudes = magnitude[band_mask]
        # Calculate the energy in this band over time
        band_energy = np.sum(band_magnitudes, axis=0)
        band_energies[band_name] = band_energy
    
    return band_energies, freqs, magnitude

def find_magnitude_range(db_magnitude, hop_length, sr):
    # Convert hop length to time
    time_points = librosa.frames_to_time(np.arange(db_magnitude.shape[1]), 
                                        sr=sr, 
                                        hop_length=hop_length)
    
    # Create mask for values between 0 and -10 dB
    magnitude_mask = (db_magnitude > -2) & (db_magnitude < 0)
    
    # Get timestamps where condition is met
    timestamps = time_points[np.any(magnitude_mask, axis=0)]
    
    return timestamps

def main():
    # File paths
    song1_path = 'test_songs/ShapeOfYou.mp3'
    song2_path = 'test_songs/CantStopTheFeeling.mp3'
    
    # Load audio
    y, sr = load_audio(song1_path)
    
    # Compute spectrogram
    db_magnitude, hop_length = compute_spectrogram(y, sr)

    frequencies, times = get_frequency_time_info(db_magnitude, sr, hop_length=256, n_fft=1028)

    # Get timestamps where magnitude is in target range
    target_timestamps = find_magnitude_range(db_magnitude, hop_length,sr)
    print(f"Found {len(target_timestamps)} timestamps with magnitude between 0 and -10 dB")
    
    # Plot the results
    plot_spectrogram(db_magnitude, sr, hop_length)

    # Analyze frequency bands
    band_energies, freqs, magnitude = analyze_frequency_bands(y, sr)


if __name__ == "__main__":
    main()

