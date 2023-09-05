import os
from time import sleep

def extract_rtsp():

    with open('Agatha') as archivo:
        for linea in archivo:
            ip = str(linea.strip().split(".")[0:3]).replace(",", ".").replace("'", "").replace(" ", "").replace("[","").replace("]", "")
            print(ip)
            os.system(f"sudo ip route add {ip}/24 via 192.168.220.1 dev CAMARAS")
    sleep(1800)
extract_rtsp()

if __name__ == '__main__':
    extract_rtsp()


