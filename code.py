import board
import digitalio
import time
import neopixel
from adafruit_circuitplayground import cp

try:
    from audiocore import WaveFile
except ImportError:
    from audioio import WaveFile

try:
    from audioio import AudioOut
except ImportError:
    try:
        from audiopwmio import PWMAudioOut as AudioOut
    except ImportError:
        pass  # not always supported by every board!

def play_file(filename):
    print("Playing file: " + filename)
    wave_file = open(filename, "rb")
    with WaveFile(wave_file) as wave:
        with AudioOut(board.SPEAKER) as audio:
            audio.play(wave)
            while audio.playing:
                pass
    print("Finished")

check = 0
while True:
    x, y, z = cp.acceleration
    print((x, y, z))
    print(check)
    if abs(y)>9:
        check=0
    if abs(y)<9 :
        check+=1
    if check>50:
        print("No!")
        cp.play_file("clock_short.wav")
        check = 0
        time.sleep(10)
    time.sleep(0.1)