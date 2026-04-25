from core.mutation_engine import mutate_packet
from utils.logger import log
import time

def fuzz_ble():
    base_packet = b'\x02\x00\x00\x00'

    for i in range(20):
        mutated = mutate_packet(base_packet)
        log(f"BLE Fuzzing iteration {i}")
        time.sleep(0.1)