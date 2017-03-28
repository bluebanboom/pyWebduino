# coding:utf-8

# message command bytes (128-255/0x80-0xFF)
START_SYSEX                 = 0xF0
SET_PIN_MODE                = 0xF4
RESET                       = 0xFF
END_SYSEX                   = 0xF7
REPORT_VERSION              = 0xF9 # report firmware version

# extended command set using sysex (0-127/0x00-0x7F)
# 0x00-0x0F reserved for user-defined commands
REPORT_ANALOG               = 0xC0 # query for analog pin
REPORT_DIGITAL              = 0xD0 # query for digital pin
ANALOG_MESSAGE              = 0xE0 # data for a analog pin

REPORT_FIRMWARE             = 0x79 # report name and version of the firmware
DIGITAL_MESSAGE             = 0x90 # data for a digital port

RESERVED_COMMAND            = 0x00 # 2nd SysEx data byte is a chip-specific command (AVR, PIC, TI, etc).
ANALOG_MAPPING_QUERY        = 0x69 # ask for mapping of analog to pin numbers
ANALOG_MAPPING_RESPONSE     = 0x6A # reply with mapping info
CAPABILITY_QUERY            = 0x6B # ask for supported modes and resolution of all pins
CAPABILITY_RESPONSE         = 0x6C # reply with supported modes and resolution
PIN_STATE_QUERY             = 0x6D # ask for a pin's current mode and value
PIN_STATE_RESPONSE          = 0x6E # reply with a pin's current mode and value
EXTENDED_ANALOG             = 0x6F # analog write (PWM, Servo, etc) to any pin
SERVO_CONFIG                = 0x70 # set max angle, minPulse, maxPulse, freq
STRING_DATA                 = 0x71 # a string message with 14-bits per char
SHIFT_DATA                  = 0x75 # shiftOut config/data message (34 bits)
I2C_REQUEST                 = 0x76 # I2C request messages from a host to an I/O board
I2C_REPLY                   = 0x77 # I2C reply messages from an I/O board to a host
I2C_CONFIG                  = 0x78 # Configure special I2C settings such as power pins and delay times
SAMPLING_INTERVAL           = 0x7A # sampling interval
SYSEX_NON_REALTIME          = 0x7E # MIDI Reserved for non-realtime messages
SYSEX_REALTIME              = 0x7F # MIDI Reserved for realtime messages

# PIN Supported Modes
PIN_DIGITAL_INPUT           = 0x00
PIN_DIGITAL_OUTPUT          = 0x01
PIN_ANALOG_INPUT            = 0x02
PIN_PWM                     = 0x03
PIN_SERVO                   = 0x04
PIN_SHIFT                   = 0x05
PIN_I2C                     = 0x06
PIN_ONEWIRE                 = 0x07
PIN_STEPPER                 = 0x08
PIN_ENCODER                 = 0x09
PIN_SERIAL                  = 0x0A
PIN_INPUT_PULLUP            = 0x0B
