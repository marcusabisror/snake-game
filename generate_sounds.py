import wave, struct, math

def make_sound(filename, freq, duration):
    sample_rate = 44100
    volume = 32767 * 0.5

    with wave.open(filename, 'w') as f:
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(sample_rate)

        for i in range(int(sample_rate * duration)):
            t = i / sample_rate
            val = int(volume * math.sin(2 * math.pi * freq * t))
            f.writeframes(struct.pack('<h', val))

# NORMAL EAT
make_sound("sounds/eat_beep.wav", 880, 0.1)

# EVERY 10 POINTS (deeper + longer)
make_sound("sounds/eat10.wav", 440, 0.25)

# WIN SOUND (multi-tone)
make_sound("sounds/win.wav", 660, 0.4)

print("All sounds generated!")
