import wave
import random
import struct

noise_output = wave.open('noise.wav', 'w')
noise_output.setparams((2, 2, 44100, 0, 'NONE', 'not compressed'))

for i in range(0, 50000):
    value = random.randint(-256*127, 256*127)
    packed_value = struct.pack('h', value)
    noise_output.writeframes(packed_value)
    noise_output.writeframes(packed_value)

noise_output.close()
