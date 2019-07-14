from pydub import AudioSegment
from pydub.playback import play

def start_alarm():
    alarm = AudioSegment.from_mp3('audio/alarm.mp3')
    play(alarm)
