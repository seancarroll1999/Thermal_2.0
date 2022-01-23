from Logic.Printer.printer import CustomPrinter
from flask import Blueprint, Flask, render_template, request, redirect, url_for, session

from Routes.WebController import app

from Logic.Printer.test_printer import Test_Printer

from Logic.Printer.PrintThread import *

from multiprocessing import Process, Value

if __name__ == "__main__":
    p = Process(target=StartPrinting, args=())
    p.start()
    app.run(host='0.0.0.0')
    p.join()
    

