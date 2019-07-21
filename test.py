import asyncio
import pyworxcloud
import time

from sys import exit
from pprint import pprint

def test_func(message):
    print(message)
    print()

async def main():
    worx = pyworxcloud.WorxCloud()
    await worx.initialize("morten@trab.dk","Cm69dofz!", 0)

    if not worx:
        exit(0)

    attrs = vars(worx)
    for item in attrs:
        print(item , ':' , attrs[item])


asyncio.get_event_loop().run_until_complete(main())

#while 1:
#    print(worx.updated)
#    time.sleep(10)
#    worx.update()
#print(worx.mac_address)
#print(worx.serial_number)
#worx.update()
#worx.return_home()