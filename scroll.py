from hanover_flipdot import display
from hanover_flipdot import fonts
import time

display = display.Display("/dev/tty.usbserial-0001", 1, 96, 16, fonts.unscii_mcr, True, False)

text = "Hallo, wie geht es dir"
width = 12
max_offset = len(text) - width + 1

display.erase_all()
display.send()

for offset in range(max_offset):
    display.erase_all()
    display_text = text[offset:offset+width]
    display.write_text(display_text)
    display.write_text(time.strftime("%H:%M:%S"), line = 9, column = 1)
    display.send()
    time.sleep(1.2)

display.erase_all()
display.send()
time.sleep(3)
