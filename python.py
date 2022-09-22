from ast import JoinedStr
import random

# JUEGO DE DOS JUGADORES CON UN DADO DE DOS CARAS ( 1 Y 2). AL SALIR 1, ATACA JUGADOR 1. AL SALIR 2 ATACA JUGADOR 2

# definimos funcion para tirar el dado


def tirar_dado(numero):
    return random.randint(1, numero)

# Creamos la clase jugador


class Jugador:
    def __init__(self, nombre, ataque, medicina):
        self.nombre = nombre
        self.ataque = ataque
        self.medicina = medicina
        self.vida = 100

    def ganar(self):
        print(self.nombre + " GANO ESTA PARTIDA!")


# creamos cada jugador
jugador1 = Jugador(input("Jugador 1: "), 10)
jugador2 = Jugador(input("Jugador 2: "), 10)

# inicializamos valores
jugador1.vida = 100
jugador2.vida = 100


print("\n---------------------------\n      Comienza el juego      \n")
print("         " + jugador1.nombre + " VS " + jugador2.nombre +
      "          \n " + "\n ---------------------------\n ")
print("REGLAS: TIRAR EL DADO DE DOS CARAS. AL SACAR 1 EL JUGADOR 1 ATACA AL OTRO JUGADOR. AL SACAR 2, EL JUGADOR 2 ATACA AL OTRO. GANA CUANDO UN JUGADOR SE QUEDA SIN VIDA")
print(input("Apreta una tecla para tirar el dado"))


while jugador1.vida > 0 and jugador2.vida > 0:
    turno = tirar_dado(2)
    if turno == 1:
        print("Resultado dado: " + str(turno))
        jugador2.vida = jugador2.vida - jugador1.ataque
        print(jugador1.nombre + " está atacando. " + jugador2.nombre +
              " ahora tiene " + str(jugador2.vida) + " de vida.")
        print("\n ----- Proxima partida -----")
        print(input("Tirar dado"))
    elif turno == 2:
        print("Resultado dado: " + str(turno))
        jugador1.vida = jugador1.vida - jugador2.ataque
        print(jugador2.nombre + " está atacando. " + jugador1.nombre +
              " ahora tiene " + str(jugador1.vida) + " de vida.")
        print("\n----- Proxima partida -----")
        print(input("Tirar dado"))


if jugador1.vida <= 0:
    jugador2.ganar()
else:
    jugador1.ganar()


print("\n----- RESULTADOS -----")
print("VIDA JUGADOR 1: " + jugador1.vida)
print("VIDA JUGADOR 1: " + jugador2.vida)
