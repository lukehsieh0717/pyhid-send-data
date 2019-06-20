import os
import usb1
import usb.core
import usb.util
import threading
import time

from usb.backend import libusb1
be = libusb1.get_backend()
usb.core.find()

def main():
	send_data()

def send_data():

	vendor_id = 0x258a
	product_id = 0x1004
	cmmd = [ 0x01, 0x02, 0x03, 0x04, 0x05, 0x06 ]

	while True:
		DEVS = usb.core.find(find_all=True, idVendor=vendor_id, idProduct=product_id)
		if DEVS is not None :
			for dev in DEVS:
				try: 
					reattach = False

					if dev.is_kernel_driver_active(0):
						reattach = True
						dev.detach_kernel_driver(0)

					usb.util.claim_interface(dev, interface=0)

					# 0x21 : HID descriptor type, 0x09 : SET_REPORT
					dev.ctrl_transfer(0x21, 0x09, 0, 0, cmmd)

					usb.util.dispose_resources(dev)

					if reattach:
						dev.attach_kernel_driver(0)

				except usb.core.USBError as e:
					print "Device disconnected."

		time.sleep( 1 )

main()