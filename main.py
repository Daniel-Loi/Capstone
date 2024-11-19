from transition import * 
from audiomix import *


def main():
    #parser = argparse.ArgumentParser(description="Mix two songs with beat and energy matching.")
    #parser.add_argument("file1", help="Path to the first MP3 file")
    #parser.add_argument("file2", help="Path to the second MP3 file")
    #parser.add_argument("--output", default="mixed_song.mp3", help="Output file for the mixed song")
    #args = parser.parse_args()

    file_path1 = "Test.wav"
    file_path2 = "Test2.wav"
    # Analyze both songs
    print("Analyzing songs...")
    tempo1, beats1, y1, sr1, key1, energy1, energy_times1 = analyze_audio(file_path1)
    tempo2, beats2, y2, sr2, key2, energy2, energy_times2 = analyze_audio(file_path2)

    print(f"Song 1: Tempo={tempo1} BPM, Key={key1}")
    print(f"Song 2: Tempo={tempo2} BPM, Key={key2}")

    # Adjust tempo if needed
    #if abs(tempo1 - tempo2) > 5:
    #    print("Adjusting tempos for compatibility...")
    #    if tempo1 > tempo2:
    #        y1 = adjust_tempo(y1, tempo2, tempo1)
    #        tempo1 = tempo2
    #    else:
    #        y2 = adjust_tempo(y2, tempo1, tempo2)
    #        tempo2 = tempo1

    # Find transitions
    print("Finding transition points...")
    transitions = find_transition_points_dynamic(beats1, beats2)
    if not transitions:
        print("No suitable transitions found.")
        return

    print(f"Found {len(transitions)} transitions.")
    t1, t2 = transitions[0]  # Use the first transition point for simplicity

    # Visualize waveforms
    visualize_waveforms_advanced(y1, sr1, y2, sr2, transitions)

    # Mix and save audio
    print("Mixing audio...")
    mix_audio(file_path1, file_path2, t1, t2)


if __name__ == "__main__":
    main()
