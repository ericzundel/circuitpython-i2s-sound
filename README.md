# circuitpython-i2s-sound
Example of how to use a MAX98357 amplifier with a Raspberri Pi Pico and Circuit Python.

## Summary

This repo contains two python files derived from the Adafruit learning website:
https://learn.adafruit.com/adafruit-max98357-i2s-class-d-mono-amp

It shows how to wire up the breakout board to the Pico and 
has adapted the Adafruit examples for how to play a WAV file or a sine wave.

# Hardware

You will need a MAX98357 chip, usually on a breakout board and a 4 ohm or 8 ohm speaker. I used 8 ohm speakers.

A Max98357 breakout board and speaker can be purchased from Adafruit, but if you need many, there are cheaper options on amazon where you can get a pack of 5 boards for around $15.  Ditto with the speakers. 

## Wiring

This DAC and amplifier uses the I2S protocol to be able to stream audio out to a speaker.

My Wiring:
   VIN to 3.3V on the pico
   GND to GND on the pico
   DIN to GP2
   BCLK to GP3
   LRC to GP4

You can change the GPIO pins on the pico if you want to change the wiring, but you
 must make BCLK and LRC adjacent pins

You can leave the GAIN pin disconnected for default output if you are using 3.3V and an 8Ohm speaker.

