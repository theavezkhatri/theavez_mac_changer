#!/usr/bin/env python
import optparse
import subprocess

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="interface to change it's MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    print("Format For Example : python theavez_mac_changer.py -i INTERFACE_NAME -m NEW_MAC")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] please specify an interface ; use --help or -h for more info")
    elif not options.new_mac:
        parser.error("[-] please specify a new mac address ; use --help or -h for more info")
    return options


def change_mac(interface, new_mac):
    print("[+] changing mac address for " + interface + " to " + new_mac)

    subprocess.call(["sudo", "ifconfig", interface, "down"])
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["sudo", "ifconfig", interface, "up"])
    print(" [-][-][-] If there is no error , then MAC address is changed to " + new_mac)





options = get_arguments()
change_mac(options.interface, options.new_mac)



