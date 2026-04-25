from services.hostapd_service import start_hostapd
from services.mosquitto_service import start_mosquitto
from services.bluetooth_service import start_bluetooth

from fuzzers.wpa2_fuzzer import fuzz_wpa2
from fuzzers.ble_fuzzer import fuzz_ble
from fuzzers.mqtt_fuzzer import fuzz_mqtt

from utils.logger import log
from utils.crash_monitor import is_process_running

import time

def report(target, crashes):
    print("\n====== FUZZING REPORT ======")
    print(f"Target: {target}")
    print(f"Total Crashes Detected: {len(crashes)}")
    for c in crashes:
        print(f"Crash: {c}")

def main():
    log("Wireless Protocol Fuzzer Started")

    # WPA2
    log("Starting hostapd...")
    hostapd = start_hostapd()
    time.sleep(2)

    crashes = []
    if not is_process_running("hostapd"):
        crashes.append("hostapd crashed at iteration 0")

    fuzz_wpa2()
    report("WPA2-hostapd", crashes)

    # MQTT
    log("Starting Mosquitto...")
    mosq = start_mosquitto()
    time.sleep(2)

    crashes = []
    fuzz_mqtt()

    if not is_process_running("mosquitto"):
        crashes.append("mosquitto crashed")

    report("MQTT-Mosquitto", crashes)

    # BLE
    log("Checking bluetoothd...")
    crashes = []

    if not is_process_running("bluetoothd"):
        crashes.append("bluetoothd not running")
    else:
        log("Fuzzing BlueZ L2CAP layer...")
        fuzz_ble()

    report("BlueZ-BLE", crashes)

    log("Fuzzing Completed")

if __name__ == "__main__":
    main()