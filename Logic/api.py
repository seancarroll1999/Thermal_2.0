from Logic.core import *

MethodDictionary = {
    'printMorningMessage': printMorningMessage(),
    'printCrypto' : printCrypto()
}

def ApiCallStructure(methodName):
    for key in MethodDictionary:
        if key == methodName:
            return MethodDictionary[methodName]