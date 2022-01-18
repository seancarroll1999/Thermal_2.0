from Logic.Printer.test_printer import Test_Printer

def printMorningMessage():
    return "Morning Message"

def printCrypto():
    return "Crypto"

def printImage(base64Image):
    x = Test_Printer()
    return x.print_base64_image(base64Image)