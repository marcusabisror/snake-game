import wave
import struct
import math

filename = "bg_loop.wav"
sample_rate = 44100
duration = 2.0  # 2-second loop
volume = 32767 * 0.3

def get_sine(freq, t):
    return math.sin(2 * math.pi * freq * t)

def get_square(freq, t):
    return 1.0 if math.sin(2 * math.pi * freq * t) > 0 else -1.0

with wave.open(filename, 'w') as wav_file:
    wav_file.setnchannels(1)
    wav_file.setsampwidth(2)
    wav_file.setframerate(sample_rate)
    
    for i in range(int(sample_rate * duration)):
        t = i / sample_rate
        
        # 1. THE BASS (A steady rhythmic pulse)
        # Low frequency pulse every 0.5 seconds
        bass_kick = get_sine(60, t) * math.exp(-5 * (t % 0.5))
        
        # 2. THE MELODY (A retro chiptune "ping")
        # Plays a note on the 2nd and 4th beats
        melody = 0
        if (t % 1.0) > 0.5:
            melody = get_square(440, t) * math.exp(-3 * (t % 0.25))
            
        # Combine and scale
        combined = (bass_kick * 0.7) + (melody * 0.3)
        value = int(combined * volume)
        
        data = struct.pack('<h', value)
        wav_file.writeframesraw(data)

print(f"Generated {filename}. Set it to loop in your game!")
