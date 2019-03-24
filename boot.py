# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import uos, machine
#uos.dupterm(None, 1) # disable REPL on UART(0)
import gc
import webrepl
import esp

webrepl.start()
gc.collect()

def do_connect():
    import network
    import os
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('reading connection info...')
        f = open('wifi.secret', 'r')
        ssid = f.readline().strip()
        password = f.readline().strip()
        f.close()
        print('connecting to network...')
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())
    ap_if = network.WLAN(network.AP_IF)
    ap_if.active(False)

esp.osdebug(None)

do_connect()
