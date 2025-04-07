import time

class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.conexiones = []

    def agregar_conexion(self, nodo):
        self.conexiones.append(nodo)

    def eliminar_conexion(self, nodo):
        if nodo in self.conexiones:
            self.conexiones.remove(nodo)

    def enviar_mensaje(self, mensaje):
        print(f"{self.nombre} envía: {mensaje}")
        for nodo in self.conexiones:
            nodo.recibir_mensaje(mensaje)

    def recibir_mensaje(self, mensaje):
        print(f"{self.nombre} recibe: {mensaje}")

servidor = Nodo("Servidor")
cliente1 = Nodo("Cliente 1")
cliente2 = Nodo("Cliente 2")
cliente3 = Nodo("Cliente 3")

servidor.agregar_conexion(cliente1)
servidor.agregar_conexion(cliente2)
servidor.agregar_conexion(cliente3)

cliente1.agregar_conexion(servidor)
cliente2.agregar_conexion(servidor)
cliente3.agregar_conexion(servidor)

servidor.enviar_mensaje("¡Hola a todos!")

servidor.eliminar_conexion(cliente2)
cliente2.eliminar_conexion(servidor)

time.sleep(2)

print("\nSimulando desconexión y reconexión dinámica...\n")

servidor.agregar_conexion(cliente2)
cliente2.agregar_conexion(servidor)

servidor.enviar_mensaje("¡Hola de nuevo a todos!")
