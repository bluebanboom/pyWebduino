# coding:utf-8
from websocket import create_connection
from websocket import ABNF
import threading
import time
from firmata import *

class Board(object):
    def __init__(self, url):
        super(Board, self).__init__()
        self.ws = create_connection(url)
        self.recvThread = threading.Thread(target=self.recv)
        self.recvThread.start()
        self.buf = ''
        self.version = ''

    def send(self, data):
        self.ws.send(data, ABNF.OPCODE_BINARY)

    def recv(self):
        while True:
            try:
                data = self.ws.recv()
                self.parseData(data)
            except Exception as e:
                print 'Recv data error:', e
                break

    def parseData(self, data):
        print data

    def parseSysex(self, data):
        pass

    def parseCommand(self, data):
        pass

    def close(self):
        self.ws.close()

    def sendPacket(self, val, *vals):
        data = ''
        data += chr(val)
        for v in vals:
            data += chr(v)
        self.send(data)

    def reportVersion(self):
        self.sendPacket(REPORT_VERSION)

    def queryCapability(self):
        self.sendPacket(START_SYSEX, CAPABILITY_QUERY, END_SYSEX)

    def setPinMode(self, pin, mode):
        self.sendPacket(SET_PIN_MODE, pin, mode)

    def reset(self):
        self.sendPacket(RESET)

    def samplingInterval(self, val):
        self.sendPacket(START_SYSEX, SAMPLING_INTERVAL, val & 0x007F, (val >> 7) & 0x007F, END_SYSEX)

    def sendAnalogData(self, pin, val):
        self.sendPacket(ANALOG_MESSAGE | (pin & 0x0F), val & 0x007F, (val >> 7) & 0x007F)
