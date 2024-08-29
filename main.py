import network
import time
from machine import Pin
import urequests


def main():
    print('Initialization of the LAN interface')
    lan = network.LAN(mdc=Pin(23), mdio=Pin(18), phy_type=network.PHY_LAN8720, phy_addr=1, power=Pin(16), id=0)
    lan.active(True)

    print("Waiting for network...")
    lan.ifconfig('dhcp')

    #ip = "192.168.1.10"
    #subnet = "255.255.255.0"
    #gateway = "192.168.1.1"
    #dns = "192.168.1.1"
    #lan.ifconfig((ip, subnet, gateway, dns))

    while not lan.isconnected():
        time.sleep(1)
        print("Waiting connect...")

    print("Parameters of LAN:")
    ip, subnet, gateway, dns = lan.ifconfig()
    print(f"IP: {ip}")
    print(f"Mask: {subnet}")
    print(f"Gateway: {gateway}")
    print(f"DNS: {dns}")

    while lan.isconnected():
        try:
            response = urequests.get(f"http://{'www.tplinkwifi.net'}")
            print("The answer:")
            print(response.text)
            response.close()
        except Exception as e:
            print(f"ERROR: {e}")


if __name__=="__main__":
    main()

