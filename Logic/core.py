from Logic.Printer.test_printer import Test_Printer
from Logic.Printer.printer import CustomPrinter
import threading
from Logic.Printer.DatabasePrinter import *
import random
import string


customPrinter = CustomPrinter()
customPrinter.flush()

def printMorningMessage():
    return "Morning Message"

def printCrypto():
    return "Crypto"

def GetRandomFileName():
        name = ""
        for i in range(10):
            name = name + random.choice(string.ascii_lowercase)
        return name + ".txt"

def printImage(base64Image, name):
    #return customPrinter.print_base64_image(base64Image)
    fileName = GetRandomFileName()
    path = "/home/pi/Desktop/Thermal_2.0/Logic/Printer/ImageQueue/{file_name}".format(file_name=fileName)
    f = open(path, "w")
    f.write(base64Image)
    f.close()
    InsertPrintItem(2, path, name, "")
    return "Done"

    

def printMessage(msg, name):
    #return customPrinter.print_message(msg, name)
    InsertPrintItem(1, msg, name, "")
    return "Done"