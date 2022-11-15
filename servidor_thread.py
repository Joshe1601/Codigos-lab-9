import socket
from threading import Thread
import pickle

SOCK_BUFFER = 1024 #Constante que indica el tamaño del Buffer de mi Socket

   

def informacion_paciente(lista_datos):
    while True:
        print("Esperando conexiones...")
        conn, client_address = sock.accept()
        print(f"Conexion desde {client_address}")
        try:
            lista_datos= pickle.dumps(lista_datos)
            conn.sendall(lista_datos)
                        
            #for datos in lista_datos:
            #    datos= datos.encode("utf-8")
            #    conn.sendall(datos)               
                
        finally:
            print("El cliente ha cerrado la conexion")
            conn.close()

def lectura_archivo():
#if __name__ == "__main__":
    with open("datos_pacientes.csv","r") as f:
        contenido= f.read()
        
    filas = contenido.split('\n')
    lista_datos= []
    for fila in filas[1:]:
        lista_datos.append(fila)
    
    thread2= Thread(target=informacion_paciente, args=(lista_datos, ))
    thread2.start()
'''    
    print(lista_datos)
    print(type(lista_datos))
lectura_archivo()
'''        
    


if __name__ == "__main__":
    # crea el objeto socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('127.0.0.1', 5001) # asocia la Ip que tengas al servidor
    print(f"Iniciando servidor en {server_address[0]}:{server_address[1]}")

    # asociamos la direccion y puerto al objeto socket
    sock.bind(server_address)

    # iniciamos la esucha de conexiones
    sock.listen(5)

    thread1= Thread(target=lectura_archivo)
    thread1.start()


    


