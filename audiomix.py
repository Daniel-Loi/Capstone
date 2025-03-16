
from pydub import AudioSegment
from volume import *
import array

def mix_audio(file1, file2, transition_point1, transition_point2, vol=1, output_file="mixed_song.mp3"):
    song1 = AudioSegment.from_file(file1)
    song2 = AudioSegment.from_file(file2)
    
    part1 = song1[:int(transition_point1 * 1000)]
    part2 = song2[int(transition_point2 * 1000):]

    faded_pt1 = fade_out(part1.get_array_of_samples(),part1.frame_rate,2)
    faded_pt1 = array.array(song1.array_type, volume(faded_pt1,vol))
    faded_pt2 = fade_in(part2.get_array_of_samples(),part2.frame_rate,2)
    faded_pt2 = array.array(song2.array_type, volume(faded_pt2,vol))

    mixed = song1._spawn(faded_pt1) + song2._spawn(faded_pt2)
    mixed.export(output_file, format="mp3")
    print(f"Mixed audio saved as {output_file}")
