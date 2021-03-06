import logging
import os
import time

import requests
from pymongo import MongoClient

# from printrun import gcoder
# from printrun.printcore import printcore


API_URL = "http://restapi:5000/api"


class Printer:
    def __init__(self, usb: str, budrate: int):
        """
        Linux: p = printcore('/dev/ttyUSB0',250000)
        Windows: p = printcore('COM6',250000)
        """
        logging.warning(f"[-] Connecting to database... ")
        self.client = MongoClient(host=os.getenv('MONGO_HOST'))
        self.db = self.client.iotp
        logging.warning('[+] Successfully Connected to database')
        # self.p = printcore(usb, budrate)

    def get_first_order(self) -> [str, bool]:
        order = self.db.orders.find_one({"status": "standby"}, {"_id": 0, "sketch": 1})
        if order:
            logging.warning("[+] Found an order to print...  ")
            filename = self.db.sketches.find_one({"_id": order["sketch"]}, {"_id": 0, "filename": 1})
            return filename["filename"]
        return False

    # def get_sketch(self):
    #     order = self.db.sketches.find_one()
    #     if order:
    #         filename = self.db.sketches.find_one({}, {"_id": 0, "filename": 1})
    #         return filename["filename"]
    #     return False

    def get_file_path(self, filename):
        response = requests.get(f'{API_URL}/files/{filename}')
        os.chdir('downloads')
        with open(f'{filename}', 'w') as file:
            file.write(response.text)
        os.chdir('../')
        return f'{os.getcwd()}/downloads/{filename}'

    def print_file(self, file: str) -> bool:
        # with open(file, "r") as f:
        #     gc_list = [line.strip() for line in f.readlines()]
        # gcode = gcoder.LightGCode(gc_list)
        # if self.p.startprint(gcode):
        #     print(f"[+] Printing {file.split('/')[-1]} in progress...")
        #     return True
        # print("[-] The printer is now busy o offline")  # this will start a print
        # return False
        logging.warning(f"[+] Printing {file.split('/')[-1]} inside print_file")  # todo remove this line
        return True

    def change_order_status_to_printing(self):
        logging.warning("[+] Changing state to printing...")
        self.db.orders.update_one({"status": "standby"}, {"$set": {"status": "printing"}})

    # def extruder_temp(self):
    #     self.p.send_now("M105")  # Interact with the printer immediately
    #
    # def pause(self) -> None:
    #     self.p.pause()  # use these to pause the current print
    #
    # def resume(self):
    #     self.p.resume()  # use these to resume the current print
    #
    # def stop_and_disconnect(self):
    #     self.p.disconnect()  # disconnect and stop running prints

    def run(self):
        filename = print_runner.get_first_order()
        # filename = print_runner.get_sketch()
        if filename:
            file_path = print_runner.get_file_path(filename)
            try:
                if os.path.exists(file_path):
                    print_runner.print_file(file_path)
                    print_runner.change_order_status_to_printing()
                    return True
            except IOError:
                logging.warning('[-] File not found or inaccessible')
                return False
        return False


print_runner = Printer('COM6', 250000)
while True:
    if print_runner.run():
        pass
    else:
        logging.critical("[-] Printer is Busy or Offline. ")
    time.sleep(10)
