import random
import time
import os
from colorama import Fore, init

class Hipodromo:
    def __init__(self):
        init(autoreset=True)
        self.caballos = ["🐎 Caballo 1", "🐎 Caballo 2", "🐎 Caballo 3", "🐎 Caballo 4"]
        self.meta = 30
        self.longitud_barra = 30

    def crear_barra(self, progreso, caballo_idx):
        colores = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.CYAN]
        color = colores[caballo_idx % len(colores)]
        barra = color + "#" * progreso + "-" * (self.longitud_barra - progreso)
        return barra

    def limpiar_pantalla(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def mostrar_dinero(self, dinero):
        print(Fore.GREEN + f"Dinero disponible: ${dinero}")

    def mostrar_arte_ascii(self):
         print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣴⣤⣼⣷⣶⣦⣿⣶⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣞⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢒⡾⣫⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠤⣴⡾⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠛⠛⠿⠿⢿⣿⡿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣤⣀⠀⢀⣀⣤⣤⣤⣤⣤⣤⣤⣀⣀⣀⡀⠀⠀⢴⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠔⣿⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣶⣶⣿⣿⣿⣿⠁⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣬⣽⣿⣿⣿⣿⣿⣿⠋⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢰⡿⣿⡿⠟⣽⠟⢡⠋⠈⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢰⣿⠹⠁⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣹⣿⣿⣿⣿⣿⡟⠛⠻⠿⠿⠿⠿⠿⠿⠻⢿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⣿⢿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⠇⠈⠻⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⠋⠀⢿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣷⡀⠀⠈⠻⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⣴⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣷⡀⠀⠀⠈⢻⣷⡆⠀⠀⠀⠀⠀⣀⣴⡾⠛⠁⢀⣤⡿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣾⡟⠀⠀⠀⠀⠀⢿⣷⠀⠀⠀⣾⠿⠛⠉⠀⠀⠀⠈⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠋⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        """)

    def carrera_de_caballos(self, dinero):
        self.mostrar_arte_ascii()
        print(Fore.MAGENTA + "¡Bienvenido a la carrera de caballos! 🎉")
        self.mostrar_dinero(dinero)
        while True:
            apuesta = input(Fore.YELLOW + "¿Cuánto deseas apostar? $")
            if not apuesta.isdigit() or int(apuesta) <= 0:
                print(Fore.RED + "Por favor, ingresa una cantidad válida de dinero para apostar.")
                continue
            apuesta = int(apuesta)
            if apuesta > dinero:
                print(Fore.RED + "No tienes suficiente dinero para apostar esa cantidad.")
                continue
            else:
                dinero -= apuesta
                break
        print("\nElige un caballo para apostar:")
        for idx, caballo in enumerate(self.caballos):
            print(f"{idx + 1}. {caballo}")
        while True:
            eleccion = input(Fore.YELLOW + "¿En qué caballo quieres apostar (1-4)? ")
            if eleccion.isdigit() and 1 <= int(eleccion) <= 4:
                eleccion = int(eleccion) - 1
                break
            else:
                print(Fore.RED + "Por favor, elige un número entre 1 y 4.")
        print(f"\nHas apostado ${apuesta} al {self.caballos[eleccion]}.")
        posiciones = {caballo: 0 for caballo in self.caballos}
        carrera_en_progreso = True
        time.sleep(1)
        while carrera_en_progreso:
            self.limpiar_pantalla()
            for idx, caballo in enumerate(self.caballos):
                avance = random.randint(1, 3)
                posiciones[caballo] += avance
                if posiciones[caballo] > self.meta:
                    posiciones[caballo] = self.meta
                print(f"{Fore.YELLOW}{caballo}: {self.crear_barra(posiciones[caballo], idx)} {posiciones[caballo]}/{self.meta}")
            for caballo in self.caballos:
                if posiciones[caballo] >= self.meta:
                    print(f"\n{Fore.GREEN}{caballo} ¡Ha ganado la carrera! 🎉")
                    if caballo == self.caballos[eleccion]:
                        print(Fore.CYAN + f"¡Felicidades! Ganaste ${apuesta * 2} por tu apuesta.")
                        dinero += apuesta * 2
                    else:
                        print(Fore.RED + f"Lo siento, el caballo que elegiste no ganó. Has perdido tu apuesta.")
                    carrera_en_progreso = False
                    break
            time.sleep(0.5)
        print("\n¡Fin de la carrera! 👏")
        self.mostrar_dinero(dinero)
        return dinero

    def jugar(self, usuario):
        dinero = usuario[4]
        while dinero > 0:
            dinero = self.carrera_de_caballos(dinero)
            if dinero <= 0:
                print(Fore.RED + "¡Te has quedado sin dinero, fin del juego!")
                break
            continuar = input(Fore.GREEN + "¿Quieres seguir apostando? (s/n): ").lower()
            if continuar != 's':
                print(Fore.MAGENTA + f"¡Gracias por jugar! Tu saldo final es ${dinero}.")
                break
        usuario = (usuario[0], usuario[1], usuario[2], usuario[3], dinero, usuario[5])
        return usuario