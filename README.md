#  Wireless Protocol Fuzzing Framework

A modular cybersecurity project designed to identify vulnerabilities in wireless protocol implementations using fuzz testing techniques. This framework targets **WPA2, BLE, and IoT (MQTT)** protocols by generating malformed packets and monitoring system behavior.

---

##  Overview

Wireless communication protocols are widely used in modern systems such as Wi-Fi routers, Bluetooth devices, and IoT ecosystems. However, these protocols often contain complex parsing logic, making them vulnerable to malformed inputs.

This project implements a **multi-protocol fuzzing framework** that:

* Generates mutated packets
* Sends them to real protocol implementations
* Monitors for crashes or abnormal behavior
* Produces structured fuzzing reports

---

##  Key Features

*  Multi-protocol fuzzing (WPA2, BLE, MQTT)
*  Modular architecture for easy extension
*  Automated packet mutation engine
*  Integration with real-world services
*  Crash monitoring and reporting system

---

##  System Architecture

```
Wireless Protocol Fuzzer (main.py)
                │
                ▼
     Packet Mutation Engine
                │
     ┌──────────┼──────────┐
     ▼          ▼          ▼
 WPA2       BLE        MQTT
 Fuzzer     Fuzzer     Fuzzer
     │          │          │
     ▼          ▼          ▼
 hostapd   bluetoothd   Mosquitto
     │          │          │
     └──────────┴──────────┘
                │
                ▼
        Crash Monitoring
                │
                ▼
        Reporting Module
```

---

## 🛠️ Technologies Used

| Component    | Technology          |
| ------------ | ------------------- |
| Language     | Python              |
| OS           | Ubuntu / Kali Linux |
| WPA2 Stack   | hostapd             |
| BLE Stack    | BlueZ (bluetoothd)  |
| IoT Protocol | Mosquitto MQTT      |
| Libraries    | paho-mqtt, psutil   |

---

##  Project Structure

```
wireless_protocol_fuzzer/
│
├── main.py
├── config.py
│
├── core/
│   ├── mutation_engine.py
│   ├── packet_sender.py
│
├── fuzzers/
│   ├── wpa2_fuzzer.py
│   ├── ble_fuzzer.py
│   ├── mqtt_fuzzer.py
│
├── services/
│   ├── hostapd_service.py
│   ├── mosquitto_service.py
│   ├── bluetooth_service.py
│
├── utils/
│   ├── logger.py
│   ├── crash_monitor.py
│
├── configs/
│   └── hostapd.conf
│
├── reports/
│   └── report.txt
│
└── requirements.txt
```

---

##  Installation

###  Update System

```bash
sudo apt update
```

###  Install Required Services

```bash
sudo apt install hostapd mosquitto bluez -y
```

###  Install Python Dependencies

```bash
pip3 install -r requirements.txt
```

---
# Configuration

Edit the file:
configs/hostapd.conf

Update the network interface:
interface=your_interface_name

---
# Important Notes:

Replace your_interface_name with your actual wireless interface

## Check your interface using:

```bash
ip a
```

Common interface names:

* wlan0
* wlp2s0
* wlan1 (USB adapter)

---
# VM Users (Very Important)

If you are using VMware / VirtualBox, your default WiFi adapter:

❌ will NOT work with hostapd

To properly run WPA2 fuzzing, you need:

USB WiFi adapter with monitor mode support
OR run on a real machine (not VM)

Without this, WPA2 fuzzing will run only in simulation mode

---

##  Usage

Run the fuzzing framework:

```bash
sudo python3 main.py
```

---

##  Sample Output

```
Wireless Protocol Fuzzer Started

Starting hostapd...

====== FUZZING REPORT ======
Target: WPA2-hostapd
Total Crashes Detected: 1
Crash: hostapd crashed at iteration 0

Starting Mosquitto...

====== FUZZING REPORT ======
Target: MQTT-Mosquitto
Total Crashes Detected: 0

Checking bluetoothd...

====== FUZZING REPORT ======
Target: BlueZ-BLE
Total Crashes Detected: 0

Fuzzing Completed
```

---

##  Results

| Protocol | Target    | Result            |
| -------- | --------- | ----------------- |
| WPA2     | hostapd   |  Crash detected   |
| BLE      | BlueZ     |  Stable           |
| MQTT     | Mosquitto |  Stable           |

---

##  Limitations

* Requires compatible wireless hardware for full WPA2 testing
* BLE fuzzing limited without external Bluetooth adapter
* Basic mutation strategy (not coverage-guided)

---

##  Future Enhancements

* Coverage-guided fuzzing (AFL-style)
* Real packet injection using Scapy
* GUI dashboard for monitoring
* Automated vulnerability classification

---

##  Conclusion

This project demonstrates how fuzz testing can be applied to wireless protocol stacks to uncover vulnerabilities. The framework successfully identifies weaknesses by injecting malformed packets into real-world services.

---

##  Author

Avinash
