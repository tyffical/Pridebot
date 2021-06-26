















from codebug_tether import CodeBug
import time
print("1")
cb = CodeBug('/dev/tty.usbmodem146301')

print("2")
#this would activate when PRIDEBOT <3 sends a text message to the Twilio API,
#rather than being while True.
while True:
    cb.set_row(4,0b11110)
    cb.set_row(3,0b10001)
    cb.set_row(2,0b11110)
    cb.set_row(1,0b10000)
    cb.set_row(0,0b10000)
    time.sleep(1)
    cb.set_row(4,0b11110)
    cb.set_row(3,0b10001)
    cb.set_row(2,0b11110)
    cb.set_row(1,0b10010)
    cb.set_row(0,0b10001)
    time.sleep(1)
    cb.set_row(4,0b11111)
    cb.set_row(3,0b00100)
    cb.set_row(2,0b00100)
    cb.set_row(1,0b00100)
    cb.set_row(0,0b11111)
    time.sleep(1)
    cb.set_row(4,0b11110)
    cb.set_row(3,0b10001)
    cb.set_row(2,0b10001)
    cb.set_row(1,0b10001)
    cb.set_row(0,0b11110)
    time.sleep(1)
    cb.set_row(4,0b11111)
    cb.set_row(3,0b10000)
    cb.set_row(2,0b11110)
    cb.set_row(1,0b10000)
    cb.set_row(0,0b11111)
    time.sleep(1)
print("3")
