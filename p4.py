import socket
import time
import threading
HOST = '157.245.83.163'
PORT = 5000

def funcionThread1():
    with socket.socket (socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect ((HOST, PORT))    
        print(f"Conectado a {HOST}")
        while(True):
            s.sendall(("GET").encode())
            respuesta = s.recv(1024)
            respuesta = respuesta.decode()
            potenciaActiva = float(respuesta.split(',')[1])
            potencias.append(potenciaActiva)
            print(potenciaActiva)
            time.sleep(5)

def funcionThread2():
    global cambioMaximo
    global potencias
    global maximo
    while(True):
        if len(potencias) > 0:
            cur_max = max(potencias)
            if cur_max > maximo:
                cambioMaximo = True
            maximo = cur_max
            # print(f"La maxima potencia hasta el momento es {maximo}")
        time.sleep(1)
        
def funcionThread3():
    global cambioMaximo
    global maximo
    LOCALHOST='127.0.0.1'
    LOCALPORT = 4000 
    with socket.socket (socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect ((LOCALHOST, LOCALPORT))    
        print(f"Conectado a {LOCALHOST}")
        while(True):
            if cambioMaximo:
                cambioMaximo = False
                s.sendall((str(maximo)).encode())
            time.sleep(1)

maximo = 0
cambioMaximo = False
potencias = []

t1 = threading.Thread(target=funcionThread1)
t2 = threading.Thread(target=funcionThread2)
t3 = threading.Thread(target=funcionThread3)
t1.start()
t2.start()
t3.start()
