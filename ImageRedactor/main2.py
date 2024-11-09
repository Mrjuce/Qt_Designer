from PIL import Image
from PIL import ImageFilter

class ImageEditor():
    def __init__(self , filename):
        self.filename = filename 
        self.changed = list()

    def open(self):
        try: 
            self.original = Image.open(self.filename)
        except:
            print("File is not found!")
        self.original.show()
    def do_kleft(self):
        rotated = self.original.transpose(Image.FLIP_LEFT_RIGHT)
        self.changed.append(rotated)

    #temp_filename = self.filename = self.split(".")