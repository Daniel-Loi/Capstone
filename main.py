from audiomix import analyze_audio, find_transition_points_dynamic, dynamic_crossfade
from pydub import AudioSegment
from Ai_DJ_DB import save_audio_to_mongodb
import numpy as np
import os

# Set FFmpeg path
#ffmpeg_dir = r"C:\Users\Owner\OneDrive\Desktop\ffmpeg-2025-03-17-git-5b9356f18e-full_build\bin"
#os.environ["PATH"] = ffmpeg_dir + os.pathsep + os.environ["PATH"]

def main(file_path1, file_path2):
    # Analyze songs
    print("Analyzing songs...")
    tempo1, beats1, y1, sr1, key1, energy1, energy_times1 = analyze_audio(file_path1)
    tempo2, beats2, y2, sr2, key2, energy2, energy_times2 = analyze_audio(file_path2)

    print(f"Song 1: Tempo={tempo1} BPM, Key={key1}, Duration={len(y1) / sr1} seconds")
    print(f"Song 2: Tempo={tempo2} BPM, Key={key2}, Duration={len(y2) / sr2} seconds")

    # Find transition points
    print("Finding transition points...")
    transitions = find_transition_points_dynamic(beats1, beats2, energy1, energy_times1, min_transition_time=15.0)

    if transitions:
        transition_point = transitions[0][0]  # Use the first detected transition point
        print(f"Transition point at: {transition_point} seconds")
    else:
        print("No transition points found.")
        return

    # Load the songs
    print("Loading songs...")
    try:
        song1 = AudioSegment.from_file(file_path1)
        song2 = AudioSegment.from_file(file_path2)
        print("Successfully loaded both songs")
    except Exception as e:
        print(f"Error loading songs: {str(e)}")
        return

    # Mixing audio
    print("Mixing audio...")
    try:
        mixed = dynamic_crossfade(song1, song2, transition_point)
        
        # Save final mixed output to MongoDB with metadata
        print("Saving mixed output to MongoDB...")
        song_metadata = {
            "original_songs": [os.path.basename(file_path1), os.path.basename(file_path2)],
            "tempo1": float(tempo1[0]) if isinstance(tempo1, np.ndarray) else float(tempo1),
            "tempo2": float(tempo2[0]) if isinstance(tempo2, np.ndarray) else float(tempo2),
            "key1": int(key1),
            "key2": int(key2),
            "transition_point": float(transition_point)
        }
        save_audio_to_mongodb("mixed_output.mp3", "mixed_output.mp3", song_metadata)
        print("Mixed output saved to MongoDB.")

    except ValueError as e:
        print(e)

if __name__ == "__main__":
    song1_path = "test_songs/CantStopTheFeeling.mp3"
    song2_path = "test_songs/ShapeOfYou.mp3"
    main(song1_path, song2_path)
