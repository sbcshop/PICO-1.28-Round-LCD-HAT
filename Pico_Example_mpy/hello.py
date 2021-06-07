import random
from machine import Pin, SPI
import gc9a01

import utime
import italicc

import vga1_bold_16x32 as font

#------joystck pin declaration----- 
joyRight = Pin(17,Pin.IN)
joyDown  = Pin(18,Pin.IN)
joySel   = Pin(19,Pin.IN)
joyLeft  = Pin(20,Pin.IN)
joyUp    = Pin(21,Pin.IN)


def main():
    spi = SPI(1, baudrate=40000000, sck=Pin(10), mosi=Pin(11))
    tft = gc9a01.GC9A01(
        spi,
        240,
        240,
        reset=Pin(12, Pin.OUT),
        cs=Pin(9, Pin.OUT),
        dc=Pin(8, Pin.OUT),
        backlight=Pin(13, Pin.OUT),
        rotation=0)

    tft.init()
    tft.rotation(0)
    tft.fill(gc9a01.BLACK)
    utime.sleep(0.5)
    
    tft.text(font, "Hello", 80, 100, gc9a01.RED)
    #tft.draw(italicc, "hello" , 100, 50, gc9a01.BLUE)
    #tft.fill_rect(120,120,200,200, gc9a01.BLUE)
    #tft.pixel(100, 50, gc9a01.BLUE)
    
    
    while True:
    
        if(joyRight.value() == 0):
            print("joyRight press")
            tft.fill(gc9a01.BLUE)
                  
        elif(joyDown.value() == 0):
            print("joyDown press")
            tft.fill(gc9a01.RED)

        elif(joySel.value() == 0):
            print("joySel press")
            tft.fill(gc9a01.GREEN)
            
        elif(joyLeft.value() == 0):
            print("joyLeft press")
            tft.fill(gc9a01.CYAN)
       
        elif(joyUp.value() == 0):
            print("joyUp press")
            tft.fill(gc9a01.MAGENTA)
    
    
main()