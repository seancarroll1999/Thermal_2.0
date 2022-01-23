from Logic.Printer.DatabasePrinter import *
import time
from Logic.Printer.printer import CustomPrinter
import os

customPrinter = CustomPrinter()
customPrinter.flush()

def print_txt(data, attributes):
    #return customPrinter.print_message(msg, name)
    for att in attributes:
        try:
            getattr(customPrinter, att)(attributes[att])
        except TypeError as te:
            print(te)
            pass
    customPrinter.out(data)
    customPrinter.reset()


def print_message(print_item):
    print_txt(print_item['data'], "")
    print_txt("- " + print_item['sender'], {"justify": "R"})
    customPrinter.feed(3)

def print_image(print_item):
    #customPrinter.print_base64_image(base64Image)
    path = print_item['data']
    f = open(path, "r")
    base64Image = f.read()
    customPrinter.print_base64_image(base64Image)
    customPrinter.feed(2)
    os.remove(path)
    DeletePrintItem(print_item['print_id'])

def StartPrinting():
    while True:
        print_queue = GetPrintQueue()
        if print_queue is not None:
            for print_item in print_queue:
                if print_item['function_id'] == 1: #PrintMessage
                    print_message(print_item)
                
                if print_item['function_id'] == 2: #PrintImage
                    print_image(print_item)
                
                DeletePrintItem(print_item['print_id'])
        
        time.sleep(10)