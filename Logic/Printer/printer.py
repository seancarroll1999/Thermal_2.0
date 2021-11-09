from PIL import Image
from Libaries.ThermalPrinter2.thermalprinter import ThermalPrinter


class CustomPrinter(ThermalPrinter):
    def __init__(self):
        self.value = "s"
        super().__init__()
        self.codepage()
        
    def print_image(self, image_path):
        size = 384, 384
        image = Image.open(image_path)
        image.thumbnail(size, Image.ANTIALIAS)
        self.image(image)
