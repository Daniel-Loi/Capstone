import librosa
import numpy as np
import matplotlib.pyplot as plt
import argparse

# 1. Analyze Audio Features
def analyze_audio(file_path):
    y, sr = librosa.load(file_path, sr=None, mono=True)
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    beats = librosa.frames_to_time(beat_frames, sr=sr)
    chroma = librosa.feature.chroma_stft(y=y, sr=sr)
    key = np.argmax(np.mean(chroma, axis=1))  # Simplistic key detection
    energy = librosa.feature.rms(y=y)[0]
    energy_times = librosa.frames_to_time(range(len(energy)), sr=sr)
    return tempo, beats, y, sr, key, energy, energy_times

# 2. Dynamic Beat Matching
def find_transition_points_dynamic(beats1, beats2, threshold_factor=0.1):
    transition_points = []
    avg_interval1 = np.mean(np.diff(beats1)) if len(beats1) > 1 else 0.5
    avg_interval2 = np.mean(np.diff(beats2)) if len(beats2) > 1 else 0.5
    threshold = min(avg_interval1, avg_interval2) * threshold_factor
    for beat1 in beats1:
        for beat2 in beats2:
            if abs(beat1 - beat2) < threshold:
                transition_points.append((beat1, beat2))
    return transition_points

# 3. Tempo Adjustment
#def adjust_tempo(y, target_tempo, current_tempo):
#    factor = target_tempo / current_tempo
#    return librosa.effects.time_stretch(y, factor)

# 4. Visualize Waveforms with Transitions
def visualize_waveforms_advanced(y1, sr1, y2, sr2, transitions):
    plt.figure(figsize=(15, 8))
    librosa.display.waveshow(y1, sr=sr1, alpha=0.6, color='blue', label="Song 1")
    librosa.display.waveshow(y2, sr=sr2, alpha=0.6, color='orange', label="Song 2")
    for t1, t2 in transitions:
        plt.axvline(x=t1, color='green', linestyle='--', label="Transition Point (Song 1)")
        plt.axvline(x=t2, color='red', linestyle='--', label="Transition Point (Song 2)")
    plt.legend()
    plt.title("Waveform Overlap with Transitions")
    plt.tight_layout()
    plt.show()


