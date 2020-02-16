import os.path
from pprint import pprint

from pymongo import MongoClient

from printrun import gcoder
from printrun.printcore import printcore


class Printer:
    def __init__(self, usb: str, budrate: int):
        """
        Linux: p = printcore('/dev/ttyUSB0',250000)
        Windows: p = printcore('COM6',250000)
        """
        self.p = printcore(usb, budrate)

    def grab_file(self) -> str:
        pass

    def print_file(self, filename: str) -> bool:
        with open(filename, "r") as f:
            gc_lines = [line.strip() for line in f.readlines()]
        gcode_list = [gc_lines]
        gcode = gcoder.LightGCode(gcode_list)
        return self.p.startprint(gcode)  # this will start a print

    def extruder_temp(self):
        self.p.send_now("M105")  # Interact with the printer immediately

    def pause(self) -> None:
        self.p.pause()  # use these to pause the current print

    def resume(self):
        self.p.resume()  # use these to resume the current print

    def stop_and_disconnect(self):
        self.p.disconnect()  # disconnect and stop running prints


# print_runner = Printer('COM6', 250000)
# print_runner.print_file('filename.gcode')

client = MongoClient(host=os.getenv("MONGO_URI"))
db = client.iotp

order = db.orders.find_one({"status": "standby"}, {"_id": 0, "sketch": 1})
filename = db.sketches.find_one({"_id": order["sketch"]})
pprint(order)
pprint(filename)


file_path = os.path.exists(f'../server/sketches/{filename["filename"]}')
print(file_path)
try:
    f = open(f'../server/sketches/{filename["filename"]}')
    f.close()
    print(f'File {filename["filename"]} is accessible')
except IOError:
    print('File not found or inaccessible')

# gcodes = [i.strip() for i in open(file)]
# print(gcodes)
