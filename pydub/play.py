from pydub import AudioSegment
from pydub.playback import play

import pydub.effects as eff 

song = AudioSegment.from_mp3("bruh.mp3")

# boost volume by i dB
result = song

for i in range(1, 3, 1):
    new_part = song + i    
    #result = result + new_part
    result.overlay(new_part)

result.export('boosted.mp3', format='mp3')
play(result)

result_rev=result.reverse()
play(result_rev)



speed = eff.speedup(result, 1.5)

play(speed)

##############################################




from pydub import generators



#pydub.utils.

pulse_gen = generators.Pulse(523.25)

sine_gen = generators.Sine(435)

sine_sound = sine_gen.to_audio_segment()


play(sine_sound)




