import wave
import struct
import math

# Sound Settings
filename = "eat_beep.wav"
sample_rate = 44100
duration = 0.15      # 150 milliseconds (a quick, satisfying beep)
frequency = 880.0    # High pitch (A5 note)
volume = 32767 * 0.5 # 50% volume so it doesn't blast your ears

# Create the wav file
with wave.open(filename, 'w') as wav_file:
    wav_file.setnchannels(1) # Mono sound
    wav_file.setsampwidth(2) # 2 bytes per sample
    wav_file.setframerate(sample_rate)
    
    # Generate an 8-bit style square wave
    for i in range(int(sample_rate * duration)):
        t = i / sample_rate
        # Square wave math: if sine is positive, go high; if negative, go low
        value = int(volume if math.sin(2 * math.pi * frequency * t) > 0 else -volume)
        data = struct.pack('<h', value)
        wav_file.writeframesraw(data)

print(f"Generated {filename}! Time to feed the snake.")
