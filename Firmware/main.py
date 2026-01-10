from machine import Pin, SPI, unique_id
import utime

# ---- SPI SETUP (RP2040) ----
spi = SPI(
    0,
    baudrate=4_000_000,
    polarity=0,
    phase=0,
    sck=Pin(18),
    mosi=Pin(19),
    miso=None
)

# ---- LOAD CONFIG ----
badge_data = {
    "name": None,
    "pronouns": None,
    "slack_handle": None
}

configured = False
try:
    import json
    with open("config.json", "r") as f:
        config = json.load(f)
        badge_data["name"] = config.get("userName")
        badge_data["pronouns"] = config.get("userPronouns")
        badge_data["slack_handle"] = config.get("userHandle")
        configured = True
except Exception as e:
    print("No config file found or error reading it:", e)

# ---- E-INK DRIVER ----
from epd_1in54 import EPD

disp_cs   = Pin(24, Pin.OUT)
disp_dc   = Pin(25, Pin.OUT)
disp_rst  = Pin(26, Pin.OUT)
disp_busy = Pin(27, Pin.IN)

print("Initializing E-Ink display...")
display = EPD(spi, disp_cs, disp_dc, disp_rst, disp_busy)

print("Displaying name on badge...")
display.fill(1)  # white background

name_to_show = badge_data.get("name") or "badge self-test"

display.nice_text(
    name_to_show,
    x=0,
    y=0,
    color=0,
    center=True,
    center_vertical=True
)

display.display()
display.sleep()
