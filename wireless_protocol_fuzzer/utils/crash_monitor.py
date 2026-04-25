import psutil

def is_process_running(name):
    for proc in psutil.process_iter(['name']):
        if name in proc.info['name']:
            return True
    return False