import threading

def saludar(x):
    print(f"Te saluda el thread {x}")

for i in range(3):
    t = threading.Thread(target=saludar, args=(i+1,))
    t.start()