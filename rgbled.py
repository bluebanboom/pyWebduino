# coding:utf-8

from board import *
import firmata
import time

boardURL = 'ws://'

def main():
    if len(boardURL) <= 6:
        print '请使用有效的websocket地址'
        return
    board = Board(boardURL)
    board.reset()
    board.samplingInterval(50)

    redPin   = 15
    greenPin = 12
    bluePin  = 13

    board.setPinMode(redPin, firmata.PIN_PWM)
    board.setPinMode(greenPin, firmata.PIN_PWM)
    board.setPinMode(bluePin, firmata.PIN_PWM)

    board.sendAnalogData(redPin, 0)
    board.sendAnalogData(greenPin, 0)
    board.sendAnalogData(bluePin, 0)

    for i in range(5):
        # red
        board.sendAnalogData(redPin, 0xFF)
        board.sendAnalogData(greenPin, 0)
        board.sendAnalogData(bluePin, 0)
        time.sleep(1)
        # green
        board.sendAnalogData(redPin, 0)
        board.sendAnalogData(greenPin, 0xFF)
        board.sendAnalogData(bluePin, 0)
        time.sleep(1)
        # blue
        board.sendAnalogData(redPin, 0)
        board.sendAnalogData(greenPin, 0)
        board.sendAnalogData(bluePin, 0xFF)
        time.sleep(1)

    board.close()

if __name__ == '__main__':
    main()
