import gc
import esp
import network
import webrepl

ap_if = network.WLAN(network.AP_IF)
ap_if.active(False)

gc.collect()
esp.osdebug(None)
webrepl.start()
