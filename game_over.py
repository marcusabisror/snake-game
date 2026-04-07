import wave
import struct
import math

filename = "game_over.wav"
sample_rate = 44100
duration = 0.6       # A bit longer for drama
start_freq = 440.0   # Start at Middle A
end_freq = 110.0     # Drop to a low, heavy rumble
volume = 32767 * 0.5

with wave.open(filename, 'w') as wav_file:
    wav_file.setnchannels(1)
    wav_file.setsampwidth(2)
    wav_file.setframerate(sample_rate)
    
    num_samples = int(sample_rate * duration)
    
    for i in range(num_samples):
        # Calculate the current frequency (sliding down)
        fraction = i / num_samples
        current_freq = start_freq + (end_freq - start_freq) * fraction
        
        # Calculate time and phase to prevent "clicking"
        t = i / sample_rate
        # Generate a "sawtooth" wave for a grittier, retro game-over feel
        value = int(volume * (2 * (t * current_freq - math.floor(0.5 + t * current_freq))))
        
        data = struct.pack('<h', value)
        wav_file.writeframesraw(data)

print(f"Generated {filename}. RIP to the snake!")
