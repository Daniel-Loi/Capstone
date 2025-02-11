import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt

# def load_and_analyze_song(filename):
#
#     y, sr = librosa.load(filename)
#
#     tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
#     beat_times = librosa.frames_to_time(beat_frames, sr=sr)
#
#     onset_env = librosa.onset.onset_strength(y=y, sr=sr)
#     onsets = librosa.onset.onset_detect(onset_envelope=onset_env, sr=sr)
#     onset_times = librosa.frames_to_time(onsets, sr=sr)
#
#     rms = librosa.feature.rms(y=y)[0]
#     times = librosa.times_like(rms, sr=sr)
#
#
#     silence_threshold = 0.1
#     non_silent_indices = np.where(rms > silence_threshold)[0]
#
#     non_silent_beat_times = [beat_time for beat_time in beat_times if any(abs(times[non_silent_indices] - beat_time) < 0.1)]
#     non_silent_onset_times = [onset_time for onset_time in onset_times if any(abs(times[non_silent_indices] - onset_time) < 0.1)]
#
#     hop_length = 512
#     oenv = librosa.onset.onset_strength(y=y, sr=sr, hop_length=hop_length)
#     local_tempo = librosa.feature.rhythm.tempo(onset_envelope=oenv, sr=sr, aggregate=None)
#     times_tempogram = librosa.frames_to_time(np.arange(len(local_tempo)), sr=sr, hop_length=hop_length)
#
#
#     return {
#         'y': y,
#         'sr': sr, #sample rate
#         'tempo': tempo, #beats per minute of song
#         'beat_times': non_silent_beat_times,
#         'onset_times': non_silent_onset_times,
#         'rms': rms, #measure of energy, how loud or intense sound is
#         'times': times, #timestamps related to rms
#         'local_tempo': local_tempo,
#         'times_local': times_tempogram,
#     }
#
#
# def find_best_mashup_point(song1_data, song2_data):
#
#     bpm_diff = abs(song1_data['tempo'] - song2_data['tempo'])
#     if bpm_diff > 20:
#         print("BPMs are too different for a smooth mashup.")
#         return None
#
#     beat_diff_threshold = 0.05
#     best_match = None
#     min_energy_diff = float('inf')
#
#     for beat1 in song1_data['beat_times']:
#         for beat2 in song2_data['beat_times']:
#             if abs(beat1 - beat2) < beat_diff_threshold:
#
#                 energy1 = np.interp(beat1, song1_data['times'], song1_data['rms'])
#                 energy2 = np.interp(beat2, song2_data['times'], song2_data['rms'])
#
#                 energy_diff = abs(energy1 - energy2)
#
#                 if energy_diff < min_energy_diff:
#                     min_energy_diff = energy_diff
#                     best_match = (beat1, beat2)
#
#     return best_match
#
# # def find_best_mashup_point(song1_data, song2_data):
#
# #     tempo_threshold = 5
# #
# #     best_match = None
# #     min_energy_diff = float('inf')
# #
# #
# #     best_time_song1 = None
# #     best_time_song2 = None
# #
# #
# #     for i, (tempo1, time1) in enumerate(zip(song1_data['local_tempo'], song1_data['times_local'])):
# #         for j, (tempo2, time2) in enumerate(zip(song2_data['local_tempo'], song2_data['times_local'])):
# #             if abs(tempo1 - tempo2) < tempo_threshold:
# #
# #                 energy1 = np.interp(time1, song1_data['times'], song1_data['rms'])
# #                 energy2 = np.interp(time2, song2_data['times'], song2_data['rms'])
# #
# #
# #                 energy_diff = abs(energy1 - energy2)
# #
# #
# #                 if energy_diff < min_energy_diff:
# #                     min_energy_diff = energy_diff
# #                     best_match = (tempo1, tempo2)
# #                     best_time_song1 = time1
# #                     best_time_song2 = time2
# #
# #
# #     if best_match is None:
# #         print("No suitable mashup point found based on tempo alignment.")
# #         return None
# #
# #     print(f"Best mashup point found with matching tempos:")
# #     print(f" - Tempo1: {best_match[0]:.2f} BPM ")
# #     print(f" - Tempo2: {best_match[1]:.2f} BPM ")
# #
# #     return best_time_song1, best_time_song2
#
# def mashup_songs(song1_path, song2_path):
#
#     song1_data = load_and_analyze_song(song1_path)
#     song2_data = load_and_analyze_song(song2_path)
#
#     mashup_point = find_best_mashup_point(song1_data, song2_data)
#
#     if mashup_point:
#         print(f"Best mashup point found at:\n - Song 1 at {mashup_point[0]:.2f}s\n - Song 2 at {mashup_point[1]:.2f}s")
#     else:
#         print("No suitable mashup point found.")
#
# # Example usage:
song1_path = 'ShapeOfYou.mp3'
song2_path = 'CantStopTheFeeling.mp3'
# mashup_songs(song1_path, song2_path)
# Load audio file
y, sr = librosa.load(song1_path)

# Compute the STFT
n_fft = 1028  # Number of FFT components
hop_length = 256  # Number of samples between successive frames
stft = librosa.stft(y, n_fft=n_fft, hop_length=hop_length)

# Convert the complex STFT to magnitude
magnitude = np.abs(stft)

# Convert to decibels for better visualization
db_magnitude = librosa.amplitude_to_db(magnitude, ref=np.max)

# Plot the spectrogram
plt.figure(figsize=(12, 6))
librosa.display.specshow(db_magnitude, sr=sr, hop_length=hop_length, x_axis='time', y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title('Spectrogram (STFT)')
plt.xlabel('Time (s)')
plt.ylabel('Frequency (Hz)')
plt.show()

# def find_low_frequency_point(audio_path, frequency_threshold=150, duration_threshold=20, db_threshold=-40):
#     # Load the audio file
#     y, sr = librosa.load(audio_path)
#
#     # Perform STFT
#     S = np.abs(librosa.stft(y))
#     S_db = librosa.amplitude_to_db(S)
#
#     # Compute frequencies corresponding to the rows in the spectrogram
#     frequencies = librosa.fft_frequencies(sr=sr)
#
#     # Select only the low frequencies
#     low_freq_indices = frequencies <= frequency_threshold
#     low_freq_spectrogram = S_db[low_freq_indices]
#
#     # Compute the average dB in the low-frequency range over time
#     avg_low_freq_db = np.mean(low_freq_spectrogram, axis=0)
#
#     # Convert frames to time
#     times = librosa.frames_to_time(range(len(avg_low_freq_db)), sr=sr)
#
#     # Find regions where the dB level is below the threshold
#     below_threshold_indices = np.where(avg_low_freq_db < db_threshold)[0]
#
#     # Identify continuous regions lasting at least `duration_threshold` seconds
#     if len(below_threshold_indices) > 0:
#         continuous_regions = []
#         start_idx = below_threshold_indices[0]
#         for i in range(1, len(below_threshold_indices)):
#             # Check if the frames are contiguous
#             if below_threshold_indices[i] != below_threshold_indices[i - 1] + 1:
#                 end_idx = below_threshold_indices[i - 1]
#                 continuous_regions.append((start_idx, end_idx))
#                 start_idx = below_threshold_indices[i]
#         # Add the final region
#         continuous_regions.append((start_idx, below_threshold_indices[-1]))
#
#         # Check which region satisfies the duration threshold
#         for start_idx, end_idx in continuous_regions:
#             start_time = times[start_idx]
#             end_time = times[end_idx]
#             duration = end_time - start_time
#             if duration >= duration_threshold:
#                 return start_time
#
#     # If no suitable region is found, return None
#     return None
#
# def process_audio_files(audio_path1, audio_path2, frequency_threshold=150, duration_threshold=20, db_threshold=-20):
#     start_point1 = find_low_frequency_point(audio_path1, frequency_threshold, duration_threshold, db_threshold)
#     start_point2 = find_low_frequency_point(audio_path2, frequency_threshold, duration_threshold, db_threshold)
#
#     return {
#         "Song 1 Low-Frequency Start Point": start_point1,
#         "Song 2 Low-Frequency Start Point": start_point2,
#     }
#
# # Example usage
# # audio_path1 = 'song1.mp3'
# # audio_path2 = 'song2.mp3'
# start_points = process_audio_files(song1_path, song2_path)
# print(start_points)

