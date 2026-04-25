import subprocess

def start_bluetooth():
    return subprocess.Popen(
        ["bluetoothd", "-n"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )