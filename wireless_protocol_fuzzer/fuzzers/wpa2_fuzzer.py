from core.mutation_engine import mutate_packet
from utils.logger import log
import time

def fuzz_wpa2():
    base_packet = b'\x01\x03\x00\x5f'

    for i in range(20):
        mutated = mutate_packet(base_packet)
        log(f"WPA2 Fuzzing iteration {i}")
        time.sleep(0.1)