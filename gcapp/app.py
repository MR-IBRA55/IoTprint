import os.path
import time
import logging

from pymongo import MongoClient

# from printrun import gcoder
# from printrun.printcore import printcore


class Printer:
    def __init__(self, usb: str, budrate: int):
        """
        Linux: p = printcore('/dev/ttyUSB0',250000)
        Windows: p = printcore('COM6',250000)
        """
        logging.debug('[-] Connecting to database.. ')
        self.client = MongoClient(host=os.getenv("MONGO_HOST"))
        logging.debug('[+] Successfully Connected')
        self.db = self.client.iotp
        # self.p = printcore(usb, budrate)

    # def get_next_order(self) -> [str, bool]:
    #     order = self.db.orders.find_one({"status": "standby"}, {"_id": 0, "sketch": 1})
    #     if order:
    #         filename = self.db.sketches.find_one({"_id": order["sketch"]}, {"_id": 0, "filename": 1})
    #         return filename["filename"]
    #     return False

    def get_file_path(self, filename):
        dir_path = "../server/sketches/"
        return f'{dir_path}' + f'{filename}'

    def print_file(self, file: str) -> bool:
        # with open(file, "r") as f:
        #     gc_list = [line.strip() for line in f.readlines()]
        # gcode = gcoder.LightGCode(gc_list)
        # if self.p.startprint(gcode):
        #     print(f"[+] Printing {file.split('/')[-1]} in progress...")
        #     return True
        # print("[-] The printer is now busy o offline")  # this will start a print
        # return False
        print(f"[+] Printing {file.split('/')[-1]} in progress...")  # todo remove this line
        return True

    def delete_file(self, file_path) -> None:
        os.remove(file_path)

    def change_status_to_printing(self):
        print("[+] Changing state to printing...")
        pass

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
        # filename = print_runner.get_next_order()
        files = os.listdir("../server/sketches") # todo ftp dir
        if files:
            file_path = print_runner.get_file_path(files[0])
            try:
                if os.path.exists(file_path):
                    print_runner.print_file(file_path)
                    print_runner.delete_file(file_path)
                    return True
            except IOError:
                print('File not found or inaccessible')
                return False
        return False


while True:
    print_runner = Printer('COM6', 250000)
    if print_runner.run():
        # print_runner.change_status_to_printing()
        print("[+] Starting printing process... ")
    else:
        print("[-] Printer is Busy or Offline")
    time.sleep(10)
