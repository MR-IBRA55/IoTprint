import os.path
import time

from pymongo import MongoClient

from printrun import gcoder
from printrun.printcore import printcore


class Printer:
    def __init__(self, usb: str, budrate: int):
        """
        Linux: p = printcore('/dev/ttyUSB0',250000)
        Windows: p = printcore('COM6',250000)
        """
        self.client = MongoClient(host=os.getenv("MONGO_HOST"))
        self.db = self.client.iotp
        # self.p = printcore(usb, budrate)

    def grab_file(self) -> str:
        pass

    @classmethod
    def print_file(cls, file: str):
        print(f"[+] Printing of {file.split('/')[-1]} in progress...")
        # with open(file, "r") as f:
        #     gc_lines = [line.strip() for line in f.readlines()]
        # gcode_list = [gc_lines]
        # gcode = gcoder.LightGCode(gcode_list)
        # return self.p.startprint(gcode)  # this will start a print

    def get_next_order(self) -> str:
        order = self.db.orders.find_one({"status": "standby"}, {"_id": 0, "sketch": 1})
        if order:
            filename = self.db.sketches.find_one({"_id": order["sketch"]}, {"_id": 0, "filename": 1})
            return filename["filename"]
        print("No orders found")

    def get_file_path(self, filename):
        dir_path = "../server/sketches/"
        return f'{dir_path}' + f'{filename}'

    def extruder_temp(self):
        self.p.send_now("M105")  # Interact with the printer immediately

    def pause(self) -> None:
        self.p.pause()  # use these to pause the current print

    def resume(self):
        self.p.resume()  # use these to resume the current print

    def stop_and_disconnect(self):
        self.p.disconnect()  # disconnect and stop running prints

    def run(self):
        filename = print_runner.get_next_order()
        if filename:
            file_path = print_runner.get_file_path(filename)
            if os.path.exists(file_path):
                print_runner.print_file(file_path)


while True:
    try:
        print_runner = Printer('COM6', 250000)
        print_runner.run()
        time.sleep(10)
    except IOError:
        print('File not found or inaccessible')
        time.sleep(5)
