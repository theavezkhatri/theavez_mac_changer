#!/usr/bin/env python

                                     #THIS CODE IS WRITTEN BY THE AVEZ KHATRI !!!
import optparse
import subprocess
import re


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

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["sudo", "ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-]Error : could not read MAC Address")

options = get_arguments()
current_mac = get_current_mac(options.interface)
print("Current MAC =" + str(current_mac))

change_mac(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("MAC Address has been successfully changed to " +current_mac)
else:
    print("MAC Address did NOT get changed !!")




