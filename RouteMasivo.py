import os
from time import sleep

def extract_rtsp():

    with open('ip') as archivo:
        for linea in archivo:
            ip = str(linea.strip().split(".")[0:3]).replace(",", ".").replace("'", "").replace(" ", "").replace("[","").replace("]", "")
            print(ip)
            os.system(f"sudo ip route add {ip}/24 via 10.5.123.157 dev eth0")

if __name__ == '__main__':
    extract_rtsp()