#! /usr/bin/python3
from pydub import AudioSegment
from pydub.playback import play

import pydub.effects as eff 

song = AudioSegment.from_mp3("bruh.mp3")


# boost volume by i dB
result = song

for i in range(1, 3, 1):
    new_part = song + i    
    print(i)
    #result = result + new_part
    result.overlay(new_part)

play(result)

result_rev=result.reverse()
play(result_rev)


speed = eff.speedup(result, 1.5)

play(speed)


