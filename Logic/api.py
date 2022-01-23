from Logic.core import *

MethodDictionary = {
    'printMorningMessage': printMorningMessage,
    'printCrypto' : printCrypto,
    'printSudoku' : printSudoku,
    'printSudokuAnswer' : printSudokuAnswer,
    'printQuote' : printQuote,
    'printGoogleCalendar' : printGoogleCalendar
}

def ApiCallStructure(methodName):
    for key in MethodDictionary:
        if key == methodName:
            return MethodDictionary[methodName]()