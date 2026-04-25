import subprocess
from config import HOSTAPD_CONFIG

def start_hostapd():
    return subprocess.Popen(
        ["hostapd", HOSTAPD_CONFIG],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )