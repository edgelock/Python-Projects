from pprint import pprint


#Dictionary representing a device
device = {
    "name": "basic-device-name",
    "vendor": "cisco",
    "model": "Nexus9000 C9300v Chassis",
    "os": "nxos",
    "version":  "9.3(3)",
    "ip":"10.1.1.1",
}

#Simple Print
print("\n_____SIMPLE PRINT__________")
print("device:", device)
print("device name:", device["name"])

#Pretty print
print("\n____PRETTY PRINT_____")
pprint(device)

#For loop with a niceley formatted print
#The >16s determines how many spaces you'd like to put around the : in the middle of the key and pair when the items are printed.
print("\n____FOR LOOP, USING F-STRING_____")
for key, value in device.items():
    print(f"{key:>16s} : {value}")