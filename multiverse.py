import RPi.GPIO as gpio
import time

led=15
gpio.setmode(gpio.BOARD)
gpio.setup(led,gpio.OUT)
while True:
    gpio.output(led,gpio.HIGH if input("Enter Input:")=="Y" else gpio.LOW)
