# coding:utf-8

from board import *
import firmata
import time

boardURL = 'ws://'

class LCD1602(object):
    """docstring for LCD1602."""
    def __init__(self, url, sda, scl):
        super(LCD1602, self).__init__()
        self.board = Board(url)
        self.board.reset()
        self.board.samplingInterval(50)
        # 初始化
        self.board.sendPacket(firmata.START_SYSEX, 0x04, 0x18, 0x00, sda, scl, firmata.END_SYSEX)

    def cursor(self, col, row):
        self.board.sendPacket(firmata.START_SYSEX, 0x04, 0x18, 0x01, col, row, firmata.END_SYSEX)

    def clear(self):
        self.board.sendPacket(firmata.START_SYSEX, 0x04, 0x18, 0x03, firmata.END_SYSEX)

    def show(self, text):
        data = chr(firmata.START_SYSEX) + '0x04' + '0x18' + '0x01' + '0x02'
        for t in text:
            v = ord(t)
            high = (v >> 4) & 0xF0
            low = v & 0xF0
            data += chr(high)
            data += chr(low)
        data += chr(firmata.END_SYSEX)
        self.board.send(data)


def main():
    if len(boardURL) <= 6:
        print '请使用有效的websocket地址'
        return

    # smart的sda是4号，scl是5号，但是不是很肯定
    lcd = LCD1602(boardURL, 0x04, 0x05)
    lcd.cursor(0, 0)
    lcd.show("Hello")
    lcd.cursor(0, 1)
    lcd.show("Smart")
    time.sleep(10)
    lcd.board.close()

if __name__ == '__main__':
    main()
