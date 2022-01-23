from Logic.Printer.test_printer import Test_Printer
from Logic.Printer.printer import CustomPrinter
import threading
from Logic.Printer.DatabasePrinter import *
import random
import string
import json

from Logic.Features.MorningMessage import *

def printMorningMessage():
    dateString = GetDate()
    attributes = {
        "justify": "C",
        "double_width": True,
        "double_height": True,
        "bold": True,
        "underline": 2
    }
    InsertPrintItem(3, dateString, "", json.dumps(attributes))
    return "Morning Message"

def printCrypto():
    print(" crypto")
    return "Crypto"

def printGoogleCalendar():
    print("Google Calrndar")
    return "Google Calendar"

def printSudoku():
    print(" sudoku")
    return "Sudoku"

def printSudokuAnswer():
    print(" sudoku answer")
    return "SudokuAnswer"

def printQuote():
    print("quote")
    return "Quote"


def GetRandomFileName():
        name = ""
        for i in range(10):
            name = name + random.choice(string.ascii_lowercase)
        return name + ".txt"

def printImage(base64Image, name):
    fileName = GetRandomFileName()
    path = "/home/pi/Desktop/Thermal_2.0/Logic/Printer/ImageQueue/{file_name}".format(file_name=fileName)
    f = open(path, "w")
    f.write(base64Image)
    f.close()
    InsertPrintItem(2, path, name, "")
    return "Done"

def printMessage(msg, name):
    InsertPrintItem(1, msg, name, "")
    return "Done"