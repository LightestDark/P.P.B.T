"""
MicroPython library for Waveshare 1.54" E-Paper Display V2
RP2040 compatible
"""

import framebuf
import utime

EPD_WIDTH  = 200
EPD_HEIGHT = 200

DRIVER_OUTPUT_CONTROL                = 0x01
BOOSTER_SOFT_START_CONTROL           = 0x0C
GATE_SCAN_START_POSITION             = 0x0F
DEEP_SLEEP_MODE                      = 0x10
DATA_ENTRY_MODE_SETTING              = 0x11
SW_RESET                             = 0x12
MASTER_ACTIVATION                    = 0x20
DISPLAY_UPDATE_CONTROL_1             = 0x21
DISPLAY_UPDATE_CONTROL_2             = 0x22
WRITE_RAM                            = 0x24
WRITE_VCOM_REGISTER                  = 0x2C
WRITE_LUT_REGISTER                   = 0x32
SET_DUMMY_LINE_PERIOD                = 0x3A
SET_GATE_TIME                        = 0x3B
BORDER_WAVEFORM_CONTROL              = 0x3C
SET_RAM_X_ADDRESS_START_END_POSITION = 0x44
SET_RAM_Y_ADDRESS_START_END_POSITION = 0x45
SET_RAM_X_ADDRESS_COUNTER            = 0x4E
SET_RAM_Y_ADDRESS_COUNTER            = 0x4F

WF_FULL_1IN54 = bytearray([
    0x80,0x48,0x40,0,0,0,0,0,0,0,0,0,
    0x40,0x48,0x80,0,0,0,0,0,0,0,0,0,
    0x80,0x48,0x40,0,0,0,0,0,0,0,0,0,
    0x40,0x48,0x80,0,0,0,0,0,0,0,0,0,
    *([0x00] * 96),
    0x22,0x22,0x22,0x22,0x22,0x22,0x00,0x00,0x00,
    0x22,0x17,0x41,0x00,0x32,0x20
])

WF_PARTIAL_1IN54_0 = bytearray([
    0x00,0x40,0x00,0,0,0,0,0,0,0,0,0,
    0x80,0x80,0x00,0,0,0,0,0,0,0,0,0,
    0x40,0x40,0x00,0,0,0,0,0,0,0,0,0,
    *([0x00] * 108),
    0x22,0x22,0x22,0x22,0x22,0x22,0x00,0x00,0x00,
    0x02,0x17,0x41,0xB0,0x32,0x28
])

class EPD:
    def __init__(self, spi, cs, dc, rst, busy):
        self.spi = spi
        self.cs = cs
        self.dc = dc
        self.rst = rst
        self.busy = busy

        self.cs.init(self.cs.OUT, value=1)
        self.dc.init(self.dc.OUT, value=0)
        self.rst.init(self.rst.OUT, value=0)
        self.busy.init(self.busy.IN)

        self.buffer = bytearray((EPD_WIDTH // 8) * EPD_HEIGHT)
        self.fb = framebuf.FrameBuffer(
            self.buffer, EPD_WIDTH, EPD_HEIGHT, framebuf.MONO_HLSB
        )

        self.init()

    def send_command(self, c):
        self.dc.value(0)
        self.cs.value(0)
        self.spi.write(bytearray([c]))
        self.cs.value(1)

    def send_data(self, d):
        self.dc.value(1)
        self.cs.value(0)
        self.spi.write(bytearray([d]))
        self.cs.value(1)

    def wait_idle(self):
        while self.busy.value():
            utime.sleep_ms(50)

    def reset(self):
        self.rst.value(1)
        utime.sleep_ms(20)
        self.rst.value(0)
        utime.sleep_ms(5)
        self.rst.value(1)
        utime.sleep_ms(20)

    def init(self):
        self.reset()
        self.send_command(SW_RESET)
        self.wait_idle()

        self.send_command(DRIVER_OUTPUT_CONTROL)
        self.send_data(0xC7)
        self.send_data(0x00)
        self.send_data(0x01)

        self.send_command(DATA_ENTRY_MODE_SETTING)
        self.send_data(0x01)

        self.send_command(SET_RAM_X_ADDRESS_START_END_POSITION)
        self.send_data(0x00)
        self.send_data(0x18)

        self.send_command(SET_RAM_Y_ADDRESS_START_END_POSITION)
        self.send_data(0xC7)
        self.send_data(0x00)
        self.send_data(0x00)
        self.send_data(0x00)

        self.send_command(BORDER_WAVEFORM_CONTROL)
        self.send_data(0x01)

        self.set_lut(WF_FULL_1IN54)

    def set_lut(self, lut):
        self.send_command(WRITE_LUT_REGISTER)
        for i in range(153):
            self.send_data(lut[i])
        self.wait_idle()

    def display(self):
        self.send_command(WRITE_RAM)
        for b in self.buffer:
            self.send_data(b)

        self.send_command(DISPLAY_UPDATE_CONTROL_2)
        self.send_data(0xC7)
        self.send_command(MASTER_ACTIVATION)
        self.wait_idle()

    def clear(self):
        self.fb.fill(1)
        self.display()

    def sleep(self):
        self.send_command(DEEP_SLEEP_MODE)
        self.send_data(0x01)
        self.rst.value(0)

    # Drawing helpers
    def fill(self, c): self.fb.fill(c)
    def text(self, t, x, y, c=0): self.fb.text(t, x, y, c)
