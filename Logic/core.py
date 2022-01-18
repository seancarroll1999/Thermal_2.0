from Logic.Printer.test_printer import Test_Printer
from Logic.Printer.printer import CustomPrinter
import threading

customPrinter = CustomPrinter()
customPrinter.flush()

def printMorningMessage():
    return "Morning Message"

def printCrypto():
    return "Crypto"

def printImage(base64Image):
    return customPrinter.print_base64_image(base64Image)