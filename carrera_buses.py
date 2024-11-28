import os
import random
import time
from colorama import Fore, init

class CarreraBuses:
    def __init__(self):
        init(autoreset=True)
        self.GREN = "\033[32m"
        self.END = "\033[0m"

    def buses(self, n1, n2):
        output = []
        output.append(115 * "-")
        output.append((n1 * " ") + "_______________  " + ((100 - n1) * " ") + "|")
        output.append((n1 * " ") + "|__|__|__|__|__|___ " + ((97  - n1) * " ") + "|")
        output.append((n1 * " ") + "|    RED BULL     |)" + ((96  - n1) * " ") + "|")
        output.append((n1 * " ") + "|~~~@~~~~~~~~~@~~~|)" + ((95  - n1) * " ") + "|")
        output.append(115 * "_")
        output.append((n2 * " ") + "_______________  " + ((100 - n2) * " ") + "|")
        output.append((n2 * " ") + "|__|__|__|__|__|___ " + ((97  - n2) * " ") + "|")
        output.append((n2 * " ") + "|    MONSTER      |)" + ((96  - n2) * " ") + "|")
        output.append((n2 * " ") + "|~~~@~~~~~~~~~@~~~|)" + ((95  - n2) * " ") + "|")
        output.append(115 * "_")
        return "\n".join(output)

    def jugar(self, usuario):
        saldo = usuario[4]
        a = 0
        b = 0
        gano = None
        os.system("cls" if os.name == "nt" else "clear")
        presentacion = """
 <<<<<<<<<<< carrera de buses >>>>>>>>>>
 RED BULL VS MONSTER """
        print(presentacion)
        time.sleep(3)
        while a < 97 and b < 97:
            c = random.randint(1, 2)
            if c == 1:
                a += 1
            if c == 2:
                b += 1
            os.system("cls" if os.name == "nt" else "clear")
            print(self.buses(a, b))
            time.sleep(0.07)
        if a >= 97:
            gano = "RED BULL"
        if b >= 97:
            gano = "MONSTER"
        print(f"{self.GREN}GANÓ LA CARRERA: {gano}{self.END}")
        if gano == "RED BULL":
            saldo += 10  # Ejemplo de ganancia
        else:
            saldo -= 10  # Ejemplo de pérdida
        print(f"Saldo actual: ${saldo}")
        usuario = (usuario[0], usuario[1], usuario[2], usuario[3], saldo, usuario[5])
        return usuario