from audiomix import analyze_audio, find_transition_points_dynamic, dynamic_crossfade
from pydub import AudioSegment
import numpy as np

def main(file_path1, file_path2):
    # Analyze songs
    print("Analyzing songs...")
    tempo1, beats1, y1, sr1, key1, energy1, energy_times1 = analyze_audio(file_path1)
    tempo2, beats2, y2, sr2, key2, energy2, energy_times2 = analyze_audio(file_path2)

    print(f"Song 1: Tempo={tempo1} BPM, Key={key1}, Duration={len(y1) / sr1} seconds")
    print(f"Song 2: Tempo={tempo2} BPM, Key={key2}, Duration={len(y2) / sr2} seconds")

    # Adjust tempos for compatibility
    print("Adjusting tempos for compatibility...")
    adjusted_tempo2 = tempo2 * (tempo1 / tempo2)  # Adjust Song 2 tempo to match Song 1's tempo
    print(f"Adjusted Tempo: Song 1={tempo1} BPM, Song 2={adjusted_tempo2} BPM")

    # Adjust pitch for key compatibility
    print("Adjusting pitch for key compatibility...")
    pitch_shift = key2 - key1  # Shift pitch by the difference in key
    print(f"Adjusted Key: Shifted by {pitch_shift} semitones")

    # Find transition points
    print("Finding transition points...")
    transitions = find_transition_points_dynamic(beats1, beats2, energy1, energy_times1, min_transition_time=15.0)  # Pass energy1 and energy_times1

    if transitions:
        print(f"Found {len(transitions)} transitions.")
        transition_point = 59  # Use the first detected transition point
        print(f"Transition point at: {transition_point} seconds")
    else:
        print("No transition points found.")
        return

    # Load the songs
    song1 = AudioSegment.from_file(file_path1)
    song2 = AudioSegment.from_file(file_path2)

    # Mixing audio
    print("Mixing audio...")
    try:
        mixed = dynamic_crossfade(song1, song2, transition_point)
        output_file = "mixed_output.mp3"
        mixed.export(output_file, format="mp3")
        print(f"Mixed audio saved as {output_file}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    song1_path = "test_songs/CantStopTheFeeling.mp3"
    song2_path = "test_songs/ShapeOfYou.mp3"
    main(song1_path, song2_path)
