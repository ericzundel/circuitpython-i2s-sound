# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# Example for how to play a .wav file using the Raspberry Pi Pico and the MAX98357 breakout board.
# Derived from: https://learn.adafruit.com/adafruit-max98357-i2s-class-d-mono-amp/circuitpython-wiring-test
#
# See README.md for notes.

import board

import audiocore   # To play a .wav file
import audiomp3    # To play an mp3 file

import audiobusio
from digitalio import DigitalInOut, Direction, Pull

# Initialize the flipper button as an input
button = DigitalInOut(board.GP16)
button.direction = Direction.INPUT
button.pull = Pull.UP

# Wav file must be 16bit, <= 22 Khz. You can convert your file using the Audacity app
# See also https://learn.adafruit.com/adafruit-wave-shield-audio-shield-for-arduino/convert-files
#wave_file = open("batman_theme_x_11khz.wav", "rb")
#sound_clip = audiocore.WaveFile(wave_file)

# Here's how you play an mp3 file.  Much smaller than a .wav file!
sound_clip = audiomp3.MP3Decoder("mario_11khz.mp3")

# For Raspberry Pi Pico I used GP2 = data(DIN), GP3 = bit clock(BCLK), GP4 = word select (LRC)
audio = audiobusio.I2SOut(board.GP3, board.GP4, board.GP2)
# Or you can use different pins, just make sure the first 2 pins are next to each other
#audio = audiobusio.I2SOut(board.GP14, board.GP15, board.GP2)

while True:
    # Wait for the user to press a button
    if (button.value == False) :
        # Each time you call audio.play() the currently playing sound clip
        # will stop and it will start playing the new sound.
        audio.play(sound_clip)

        # This loop waits until the audio is finished playing.
        # The entire program pauses during this loop, so you might
        # want to omit it for a project where you want to continue
        # responding to other inputs.
        while audio.playing:
            pass
