from machine import Pin, I2C, PWM
from i2c_lcd import I2cLcd
from keypad import Keypad
from time import sleep

# --- LCD I2C ---
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000)
lcd = I2cLcd(i2c, 0x27, 2, 16)

# --- LEDs ---
led_green = Pin(2, Pin.OUT)
led_red = Pin(4, Pin.OUT)

# --- Buzzer ---
buzzer = Pin(18, Pin.OUT)

# --- Servo ---
servo = PWM(Pin(15), freq=50)
def servo_angle(angle):
    duty = int((angle/180)*102 + 26)
    servo.duty(duty)

# --- Clavier 4x4 ---
rows = [Pin(32, Pin.IN, Pin.PULL_UP),
        Pin(33, Pin.IN, Pin.PULL_UP),
        Pin(25, Pin.IN, Pin.PULL_UP),
        Pin(26, Pin.IN, Pin.PULL_UP)]

cols = [Pin(27, Pin.OUT),
        Pin(14, Pin.OUT),
        Pin(12, Pin.OUT),
        Pin(13, Pin.OUT)]

keys = [["1","2","3","A"],
        ["4","5","6","B"],
        ["7","8","9","C"],
        ["*","0","#","D"]]

kp = Keypad(rows, cols, keys)

# --- Code d'accès ---
PASSWORD = "1234"
input_code = ""

lcd.putstr("Entrez Code :")

while True:
    key = kp.read_keypad()
    if key:
        if key.isdigit():
            input_code += key
            lcd.clear()
            lcd.putstr("Code: " + "*" * len(input_code))
            sleep(0.3)
        elif key == "#":  # Valider
            lcd.clear()
            if input_code == PASSWORD:
                lcd.putstr("ACCES AUTORISE")
                led_green.on()
                led_red.off()
                buzzer.off()
                servo_angle(90)
                sleep(3)
                servo_angle(0)
            else:
                lcd.putstr("ACCES REFUSE")
                led_green.off()
                led_red.on()
                # Buzzer alerte
                for _ in range(3):
                    buzzer.on()
                    sleep(0.2)
                    buzzer.off()
                    sleep(0.2)
            input_code = ""
            lcd.clear()
            lcd.putstr("Entrez Code :")
        elif key == "*":  # Reset
            input_code = ""
            lcd.clear()
            lcd.putstr("Entrez Code :")
from machine import Pin, I2C, PWM
from i2c_lcd import I2cLcd
from keypad import Keypad
from time import sleep

# --- LCD I2C ---
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000)
lcd = I2cLcd(i2c, 0x27, 2, 16)

# --- LEDs ---
led_green = Pin(2, Pin.OUT)
led_red = Pin(4, Pin.OUT)

# --- Buzzer ---
buzzer = Pin(18, Pin.OUT)

# --- Servo ---
servo = PWM(Pin(15), freq=50)
def servo_angle(angle):
    duty = int((angle/180)*102 + 26)
    servo.duty(duty)

# --- Clavier 4x4 ---
rows = [Pin(32, Pin.IN, Pin.PULL_UP),
        Pin(33, Pin.IN, Pin.PULL_UP),
        Pin(25, Pin.IN, Pin.PULL_UP),
        Pin(26, Pin.IN, Pin.PULL_UP)]

cols = [Pin(27, Pin.OUT),
        Pin(14, Pin.OUT),
        Pin(12, Pin.OUT),
        Pin(13, Pin.OUT)]

keys = [["1","2","3","A"],
        ["4","5","6","B"],
        ["7","8","9","C"],
        ["*","0","#","D"]]

kp = Keypad(rows, cols, keys)

# --- Code d'accès ---
PASSWORD = "1234"
input_code = ""

lcd.putstr("Entrez Code :")

while True:
    key = kp.read_keypad()
    if key:
        if key.isdigit():
            input_code += key
            lcd.clear()
            lcd.putstr("Code: " + "*" * len(input_code))
            sleep(0.3)
        elif key == "#":  # Valider
            lcd.clear()
            if input_code == PASSWORD:
                lcd.putstr("ACCES AUTORISE")
                led_green.on()
                led_red.off()
                buzzer.off()
                servo_angle(90)
                sleep(3)
                servo_angle(0)
            else:
                lcd.putstr("ACCES REFUSE")
                led_green.off()
                led_red.on()
                # Buzzer alerte
                for _ in range(3):
                    buzzer.on()
                    sleep(0.2)
                    buzzer.off()
                    sleep(0.2)
            input_code = ""
            lcd.clear()
            lcd.putstr("Entrez Code :")
        elif key == "*":  # Reset
            input_code = ""
            lcd.clear()
            lcd.putstr("Entrez Code :")
from machine import Pin, I2C, PWM
from i2c_lcd import I2cLcd
from keypad import Keypad
from time import sleep

# --- LCD I2C ---
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000)
lcd = I2cLcd(i2c, 0x27, 2, 16)

# --- LEDs ---
led_green = Pin(2, Pin.OUT)
led_red = Pin(4, Pin.OUT)

# --- Buzzer ---
buzzer = Pin(18, Pin.OUT)

# --- Servo ---
servo = PWM(Pin(15), freq=50)
def servo_angle(angle):
    duty = int((angle/180)*102 + 26)
    servo.duty(duty)

# --- Clavier 4x4 ---
rows = [Pin(32, Pin.IN, Pin.PULL_UP),
        Pin(33, Pin.IN, Pin.PULL_UP),
        Pin(25, Pin.IN, Pin.PULL_UP),
        Pin(26, Pin.IN, Pin.PULL_UP)]

cols = [Pin(27, Pin.OUT),
        Pin(14, Pin.OUT),
        Pin(12, Pin.OUT),
        Pin(13, Pin.OUT)]

keys = [["1","2","3","A"],
        ["4","5","6","B"],
        ["7","8","9","C"],
        ["*","0","#","D"]]

kp = Keypad(rows, cols, keys)

# --- Code d'accès ---
PASSWORD = "1234"
input_code = ""

lcd.putstr("Entrez Code :")

while True:
    key = kp.read_keypad()
    if key:
        if key.isdigit():
            input_code += key
            lcd.clear()
            lcd.putstr("Code: " + "*" * len(input_code))
            sleep(0.3)
        elif key == "#":  # Valider
            lcd.clear()
            if input_code == PASSWORD:
                lcd.putstr("ACCES AUTORISE")
                led_green.on()
                led_red.off()
                buzzer.off()
                servo_angle(90)
                sleep(3)
                servo_angle(0)
            else:
                lcd.putstr("ACCES REFUSE")
                led_green.off()
                led_red.on()
                # Buzzer alerte
                for _ in range(3):
                    buzzer.on()
                    sleep(0.2)
                    buzzer.off()
                    sleep(0.2)
            input_code = ""
            lcd.clear()
            lcd.putstr("Entrez Code :")
        elif key == "*":  # Reset
            input_code = ""
            lcd.clear()
            lcd.putstr("Entrez Code :")
