import socket
from threading import Thread
import pickle

SOCK_BUFFER = 1024
'''
def procesa_data(lista_datos):
    print(lista_datos)
'''
def recibir_data():
    #lista_datos=[]
    datos = sock.recv(SOCK_BUFFER) # espero a recibir 
    datos= pickle.loads(datos) #lo que recibí lo convierto en lista
    print(datos)
    print()
    #lista_datos.append(datos)
    #lista_datos=datos.split(',')
    #thread2= Thread(target=(procesa_data), args=(lista_datos, ))
    #thread2.start()

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('127.0.0.1', 5001) # acá si se pone la dirección específica

    print(f"Conectando a {server_address[0]}:{server_address[1]}")

    sock.connect(server_address) # Se conecta a esa dirección del servidor para enviar datos

    try:
        thread1= Thread(target=(recibir_data))
        thread1.start()
    finally:
        print("Cerrando socket")
        sock.close()

