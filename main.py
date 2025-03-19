from audiomix import *
from pydub import AudioSegment
import numpy as np

def main(file_path1, file_path2):
    # Analyze songs
    print("Analyzing songs...")
    tempo1, beats1, y1, sr1, key1, energy1, energy_times1 = analyze_audio(file_path1)
    tempo2, beats2, y2, sr2, key2, energy2, energy_times2 = analyze_audio(file_path2)

    # Ensure tempo1 and tempo2 are scalar values
    if isinstance(tempo1, np.ndarray):
        tempo1 = tempo1[0]
    if isinstance(tempo2, np.ndarray):
        tempo2 = tempo2[0]

    print(f"Song 1: Tempo={tempo1} BPM, Key={key1}, Duration={len(y1) / sr1} seconds")
    print(f"Song 2: Tempo={tempo2} BPM, Key={key2}, Duration={len(y2) / sr2} seconds")

    # Adjust tempos for compatibility
    print("Adjusting tempos for compatibility...")
    adjusted_tempo2 = tempo2 * (tempo1 / tempo2)  # Adjust Song 2 tempo to match Song 1's tempo
    print(f"Adjusted Tempo: Song 1={tempo1} BPM, Song 2={adjusted_tempo2} BPM")

    # Create a tempo-adjusted version of Song 2
    tempo_adjusted_output_path = "test_songs/ShapeOfYou_TempoAdjusted.mp3"
    target_tempo = adjusted_tempo2
    create_tempo_adjusted_version(file_path2, tempo_adjusted_output_path, tempo2, target_tempo)

    # Load the tempo-adjusted version of Song 2
    song2_adjusted = AudioSegment.from_file(tempo_adjusted_output_path)

    # Adjust pitch for key compatibility
    print("Adjusting pitch for key compatibility...")
    pitch_shift = key2 - key1  # Shift pitch by the difference in key
    print(f"Adjusted Key: Shifted by {pitch_shift} semitones")

    # Apply pitch shift to the tempo-adjusted version of Song 2
    # if pitch_shift != 0:
    #     song2_adjusted = song2_adjusted._spawn(song2_adjusted.raw_data, overrides={
    #         "frame_rate": int(song2_adjusted.frame_rate * (2 ** (pitch_shift / 12)))
    #     }).set_frame_rate(song2_adjusted.frame_rate)

    # Find transition points
    print("Finding transition points...")
    transitions = find_transition_points_dynamic(beats1, beats2, energy1, energy_times1, min_transition_time=15.0)  # Pass energy1 and energy_times1

    if transitions:
        print(f"Found {len(transitions)} transitions.")
        # transition_point = transitions[0][0]  # Use the first detected transition point
        transition_point = (len(y1) / sr1) - 6
        print(f"Transition point at: {transition_point} seconds")
    else:
        print("No transition points found.")
        return

    # Load the songs
    song1 = AudioSegment.from_file(file_path1)

    # Plot waveforms of Song 1 and Song 2 (Tempo-Adjusted)
    print("Plotting waveforms of Song 1 and Song 2 (Tempo-Adjusted)...")
    # plot_waveform(song1, "Waveform of Song 1")
    # plot_waveform(song2_adjusted, "Waveform of Song 2 (Tempo-Adjusted)")

    # Mixing audio
    print("Mixing audio...")
    try:
        mixed_song = dynamic_crossfade(song1, song2_adjusted, transition_point)  # Use the tempo-adjusted version
        output_file = "mixed_output_tempo_adjusted.mp3"
        mixed_song.export(output_file, format="mp3")
        print(f"Mixed audio saved as {output_file}")
        
        # Plot the waveform of the mixed song
        # plot_waveform(mixed_song, "Waveform of Mixed Song (Tempo-Adjusted)")
        
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    song1_path = "test_songs/CantStopTheFeeling.mp3"
    song2_path = "test_songs/ShapeOfYou.mp3"
    main(song1_path, song2_path)