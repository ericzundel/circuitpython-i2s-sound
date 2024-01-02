# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# Example for how to play a .wav file using the Raspberry Pi Pico and the MAX98357 breakout board.
# Derived from: https://learn.adafruit.com/adafruit-max98357-i2s-class-d-mono-amp/circuitpython-wiring-test
#
# See README.md for notes.

import audiocore
import board
import audiobusio

# Wav file must be 16bit, <= 22 Khz. You can convert your file using the Audacity app
# See also https://learn.adafruit.com/adafruit-wave-shield-audio-shield-for-arduino/convert-files
wave_file = open("batman_theme_x_11khz.wav", "rb")
wave = audiocore.WaveFile(wave_file)

# For Raspberry Pi Pico I used GP2 = data(DIN), GP3 = bit clock(BCLK), GP4 = word select (LRC)
audio = audiobusio.I2SOut(board.GP3, board.GP4, board.GP2)
# Or you can use different pins, just make sure the first 2 pins are next to each other
#audio = audiobusio.I2SOut(board.GP14, board.GP15, board.GP2)


while True:
    audio.play(wave)
    while audio.playing:
        pass
