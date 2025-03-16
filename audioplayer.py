import soundfile as sf
import numpy as np
import pyaudio
import threading


class AudioPlayer:
    def __init__(self, filename, speed=1.0):
        self.filename = filename
        self.speed = speed
        self.data, self.samplerate = sf.read(filename, dtype='float32')
        self.new_rate = int(self.samplerate * speed)
        self.paused = threading.Event()
        self.paused.set()  # Start unpaused
        self.stopped = threading.Event()
        self.playback_thread = None

        # Initialize PyAudio
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=pyaudio.paFloat32,
                                  channels=1 if len(self.data.shape) == 1 else self.data.shape[1],
                                  rate=self.new_rate,
                                  output=True)

    def play(self):
        """Plays the audio in a separate thread."""
        def playback():
            for i in range(0, len(self.data), 1024):
                if self.stopped.is_set():
                    return  # Exit thread safely
                self.paused.wait()  # Pause handling
                self.stream.write(self.data[i:i+1024].tobytes())


        if self.playback_thread is None or not self.playback_thread.is_alive():
            self.stopped.clear()
            self.playback_thread = threading.Thread(target=playback, daemon=True)
            self.playback_thread.start()

    def pause(self):
        """Pauses playback."""
        self.paused.clear()

    def resume(self):
        """Resumes playback."""
        self.paused.set()

    def stop(self):
        """Stops playback and cleans up resources."""
        if not self.stopped.is_set():
            self.stopped.set()
            self.paused.set()  # Unpause to allow thread to exit
            if self.playback_thread and threading.current_thread() != self.playback_thread:
                self.playback_thread.join()  # Only join if called from main thread

        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()

# Example usage
#if __name__ == "__main__":
#    player = AudioPlayer("output.wav", speed=1.5)
#    player.play()
#
#    while True:
#        cmd = input("Enter 'p' to pause, 'r' to resume, 'q' to quit: ").strip().lower()
#        if cmd == 'p':
#            player.pause()
#            print("Paused.")
#        elif cmd == 'r':
#            player.resume()
#            print("Resumed.")
#        elif cmd == 'q':
#            player.stop()
#            print("Stopped.")
#            break
