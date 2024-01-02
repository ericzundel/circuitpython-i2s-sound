# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# Example for how to play a .wav file using the Raspberry Pi Pico and the MAX98357 breakout board.GP2

# This DAC and amplifier uses the I2S protocol to be able to stream audio out to a speaker.
# My Wiring:
#   VIN to 3.3V on the pico
#   GND to GND on the pico
#   DIN to GP2
#   BCLK to GP3
#   LRC to GP4
#
# You can change the GPIO pins on the pico if you want to change the wiring, but you
# must make BCLK and LRC adjacent pins
#
# You can leave the GAIN pin disconnected for default output if you are using 3.3V and an 8Ohm speaker.
#
import audiocore
import board
import audiobusio

# Wav file must be 16bit, <= 22 Khz. You can convert your file using the Audacity app
# See also https://learn.adafruit.com/adafruit-wave-shield-audio-shield-for-arduino/convert-files
wave_file = open("batman_theme_x_11khz.wav", "rb")
wave = audiocore.WaveFile(wave_file)

# For Raspberry Pi Pico I used GP2 = data(DIN), GP3 = bit clock(BCLK), GP4 = word select (LRC)
#audio = audiobusio.I2SOut(board.GP3, board.GP4, board.GP2)
audio = audiobusio.I2SOut(board.GP14, board.GP15, board.GP2)


while True:
    audio.play(wave)
    while audio.playing:
        pass
