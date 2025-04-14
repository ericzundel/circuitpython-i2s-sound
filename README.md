# circuitpython-i2s-sound
This is a project that shows you how to play sound using Circuit Python. This example uses the environment we use in our engineering classes (Raspberry Pi Pico W) along with a MAX98357 amplifier chip.

![MAX98357 Wiring photo](https://ericzundel.github.io/circuitpython-i2s-sound/MAX98357-wiring.jpg)

![Fritzring diagram of circuit](https://ericzundel.github.io/circuitpython-i2s-sound/fritzring-circuit.png)
## Summary

This repo contains two python files derived from the 
[Adafruit learning website](https://learn.adafruit.com/adafruit-max98357-i2s-class-d-mono-amp).

It shows how to wire up the breakout board to the Pico and has adapted the Adafruit examples for how to play a WAV file or a sine wave.

When using CircuitPython with this chip you can stream WAV or MP3 data to a speaker. Because the Raspberry Pi Pico looks like an external drive to your computer, it's very easy to add sound to your project by just saving audio files in the right format and adding a few lines of code.  Also, the audio streams asyncronously, freeing up the python main loop so you can do other things.

# Hardware

You will need a Raspberry Pi Pico or Pico W, a MAX98357 chip, usually on a breakout board and a 4 ohm or 8 ohm speaker. I used 8 ohm speakers.

A Max98357 breakout board and speaker can be purchased from Adafruit.  Please suppor them! Having said that, if you need many for a class project, this is a very common chip and there are cheaper options. You can find them on AliExpress/Temu or on Amazon where you can get a pack of 5 boards for around $15.  Ditto with the speakers. 

## Wiring

A simple pushbutton is used to trigger the audio

Switch:
-   GP16 to Switch  
-   Switch to GND

This DAC and amplifier uses the I2S protocol to be able to stream audio out to a speaker.

My Wiring:
-   VIN to 3.3V on the pico
-   GND to GND on the pico
-   DIN to GP2
-   BCLK to GP3
-   LRC to GP4


You can change the GPIO pins on the pico if you want to change the wiring, but you
 must make BCLK and LRC adjacent pins

You can leave the GAIN pin disconnected for default output if you are using 3.3V and an 8 ohm speaker.
