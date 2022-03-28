import threading

# TODO fix access of global var from separate threads
lock = threading.Lock()
hosts = []
