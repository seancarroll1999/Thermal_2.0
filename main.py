from Logic.Printer.printer import CustomPrinter
from flask import Blueprint, Flask, render_template, request, redirect, url_for, session

from Routes.WebController import app

from Logic.Printer.test_printer import Test_Printer


if __name__ == "__main__":
    #x = CustomPrinter()
    #x.print_image('solved.png')
    #x.feed(2)
    app.run(host='0.0.0.0')
    #x = Test_Printer()
    #x.print_image('test_land.png')
    

