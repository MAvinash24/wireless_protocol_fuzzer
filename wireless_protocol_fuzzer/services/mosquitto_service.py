import subprocess

def start_mosquitto():
    return subprocess.Popen(
        ["mosquitto"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )