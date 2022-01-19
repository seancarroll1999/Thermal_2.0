from PIL import Image, ExifTags, ImageOps
from Libaries.ThermalPrinter2.thermalprinter import ThermalPrinter
from io import BytesIO
import base64
from threading import Thread

class CustomPrinter(ThermalPrinter):
    def __init__(self):
        self.value = "s"
        self.busy = False
        self.printThread = Thread(target=self.print_base64_thread, args=())
        super().__init__()
        self.codepage()
            
    def print_base64_image(self, base64String):
        busy = self.printThread.is_alive()
        if busy:
            return "Busy"
        else:
            self.printThread = Thread(target=self.print_base64_thread, args=(base64String, ))
            self.printThread.start()

        return "Done"

    def print_base64_thread(self, base64String):
        image = Image.open(BytesIO(base64.b64decode(base64String)))
        image = self.change_orientation(image)
        image = self.resize(image)  
        self.image(image)
        self.feed(3)
        image.close()

    def resize(self, image):
        new_width = 384
        wPercentage= (new_width / float(image.size[0]))
        hSize = int((float(image.size[1]) * float(wPercentage)))
        return image.resize((new_width, hSize), Image.ANTIALIAS)


    def change_orientation(self, image):
        image = ImageOps.exif_transpose(image)
        width, height = image.size
        
        if width > height:
            image = image.rotate(90, expand=True)
            
        return image
    
    def print_message(self, msg, name):
        busy = self.printThread.is_alive()
        if busy:
            return "Busy"
        else:
            self.printThread = Thread(target=self.print_message_thread, args=(msg, name, ))
            self.printThread.start()
        return "Done"

    def print_message_thread(self, msg, name):
        self.out(msg)
        self.out("- " + name, justify='R')
        self.feed(3)

