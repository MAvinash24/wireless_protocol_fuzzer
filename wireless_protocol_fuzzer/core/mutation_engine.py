import random

def mutate_packet(base_packet):
    packet = bytearray(base_packet)

    for i in range(len(packet)):
        if random.random() < 0.3:
            packet[i] = random.randint(0, 255)

    return bytes(packet)