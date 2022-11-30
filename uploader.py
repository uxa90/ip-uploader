import socket
import qrcode
import os

os.system("git pull")

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

ip_addr = get_ip_address()

print("Found IP address: " + ip_addr)

img = qrcode.make('http://{}:50000/'.format(ip_addr))

img.save("/home/pi/ip-uploader/qrcode.png")

os.system("git add .")

os.system("git commit -m \"New QR Code\"")

os.system("git push")
