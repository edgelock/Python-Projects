from random import choice
import string
from tabulate import tabulate #You must do a pip3 install tabulate for this library
from operator import itemgetter
from pprint import pprint

devices = list () #Empty list to hold the devices

#For loop to create large number number of devices from 1 to 100
for index in range (1,10):

    #Create device dictionary
    device = dict()

    #Random device name
    device["name"] = (
        choice(["r2", "r3", "r4", "r6", "r10"])
        + choice(["L", "U"])
        + choice(string.ascii_letters)
    )

    #Random Vendor from choice of Cisco, Juniper, Arista
    device["vendor"] = choice(["cisco", "juniper", "arista"])
    if device["vendor"] == "cisco":
        device["os"] = choice (["ios", "iosxe", "iosxr", "nexus"])
        device["version"] = choice(["12.1(T).04", "14.07X", "8.12(s).010"])
    elif device["vendor"] == "juniper":
        device["os"] = "junos"
        device["version"] = choice(["2.45", "2.55", "2.92.145", "3.02"])
    elif device["vendor"] == "arista":
        device["os"] = "eos"
        device["version"] = choice(["2.45", "2.55", "2.92.145", "3.01"])
    device["ip"] = "10.0.0" + str(index)

    #Nicely print the creation of the random devices
    print()
    for key, value in device.items():
        print(f"{key:>16} : {value}")

    devices.append(device)

#Print the Data as-is
print("\n -----------DEVICES AS LIST OF DICTS---------------")
pprint(devices)

#Use 'tabulate to print table of devices
print("\n ---SORTED DEVICES IN TABULAR FORMAT----------")
sorted_devices = sorted(devices, key=itemgetter("vendor", "os", "version"))
print(tabulate(sorted_devices, headers="keys"))
    