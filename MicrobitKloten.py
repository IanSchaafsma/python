from microbit import *
import speech

while True:
    
    if accelerometer.was_gesture('shake'):
        display.show(Image.SAD)
        speech.say('Stop man!')
        sleep(2000)
    if accelerometer.was_gesture('face up'):
        display.show(Image.HAPPY)
    if accelerometer.was_gesture('left'):
        display.show('<')
    if accelerometer.was_gesture('right'):
        display.show('>')
while True:
    if pin_logo.is_touched():
        display.show(Image.SURPRISED)