from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_mp3("bruh.mp3")


# boost volume by 6dB
beginning = song + 6

# reduce volume by 3dB
end = song - 3
#Concatenate audio (add one file to the end of another)

without_the_middle = beginning + end
#How long is it?

without_the_middle.duration_seconds == 15.0
#AudioSegments are immutable

# song is not modified
backwards = song.reverse()
#Crossfade (again, beginning and end are not modified)

# 1.5 second crossfade
with_style = beginning.append(end, crossfade=song.duration_seconds*1000-1)
#Repeat

# repeat the clip twice
do_it_over = with_style * 2
#Fade (note that you can chain operations because everything returns an AudioSegment)

# 2 sec fade in, 3 sec fade out
awesome = do_it_over.fade_in(3000).fade_out(4000)
#Save the results (again whatever ffmpeg supports)

awesome.export("mashup.mp3", format="mp3")


mashup = AudioSegment.from_mp3("mashup.mp3")
play(mashup)