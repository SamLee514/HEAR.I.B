from pydub import AudioSegment
from pydub.playback import play

# import files, match it with the correct microphones
mic1 = AudioSegment.from_wav("02-190915_1206.wav")
mic1len = AudioSegment.__len__(mic1)
mic2 = AudioSegment.from_wav("04-190915_1206.wav")
mic2len = AudioSegment.__len__(mic2)
mic3 = AudioSegment.from_wav("01-190915_1206.wav")
mic3len = AudioSegment.__len__(mic3)
mic4 = AudioSegment.from_wav("03-190915_1206.wav")
mic4len = AudioSegment.__len__(mic4)


def createOverlay(angle, firstDelay, secondDelay, thirdDelay):
    if angle == "left":
        tmpsound = mic4.overlay(mic3, firstDelay)
        tmpsound2 = tmpsound.overlay(mic2, secondDelay)
        output = tmpsound2.overlay(mic1, thirdDelay)

    elif angle == "center":
        tmpsound = mic3.overlay(mic2, 0)
        tmpsound2 = tmpsound.overlay(mic1, secondDelay)
        output = tmpsound2.overlay(mic4, secondDelay)

    elif angle == "right":
        tmpsound = mic1.overlay(mic2, firstDelay)
        tmpsound2 = tmpsound.overlay(mic3, secondDelay)
        output = tmpsound2.overlay(mic4, thirdDelay)

    play(output)
    return 0

if __name__ == "__main__":

    x = createOverlay("center", 40, 60, 100)










