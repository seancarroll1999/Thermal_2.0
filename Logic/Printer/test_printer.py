from PIL import Image, ExifTags, ImageOps
from Libaries.ThermalPrinter2.thermalprinter import ThermalPrinter
from io import BytesIO
import base64

class Test_Printer():
    def __init__(self):
        self.value = "s"

        
    def print_image(self, image_path):
        image = Image.open(image_path)
        image = self.change_orientation(image)
        image = self.resize(image)
        image.save("Test.png")
        image.close()
    
    def print_base64_image(self, base64String):
        image = Image.open(BytesIO(base64.b64decode(base64String)))
        image = self.change_orientation(image)
        image = self.resize(image)
        image.save("Test.png")
        image.close()
        
        return "Done"

    def resize(self, image):
        width, height = image.size
        ratio = width / height
        new_width = 384
        new_height = int(ratio * new_width)
        return image.resize((new_height, new_width))

    def change_orientation(self, image):
        image = ImageOps.exif_transpose(image)
        width, height = image.size
        
        if width > height:
            image = image.rotate(90, expand=True)
            
        return image