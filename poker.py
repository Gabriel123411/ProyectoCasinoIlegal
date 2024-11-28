import random
from collections import Counter
from colorama import Fore, init

class Poker:
    def __init__(self):
        init(autoreset=True)
        self.palos = ['♠', '♥', '♦', '♣']
        self.valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def crear_mazo(self):
        mazo = [f'{valor}{palo}' for palo in self.palos for valor in self.valores]
        random.shuffle(mazo)
        return mazo

    def repartir_cartas(self, mazo, num_jugadores=2):
        manos = {f'Jugador {i}': [mazo.pop(), mazo.pop()] for i in range(1, num_jugadores + 1)}
        return manos

    def repartir_comunitarias(self, mazo):
        return [mazo.pop() for _ in range(5)]

    def mostrar_cartas(self, manos, comunitarias, jugador_activo=1):
        for jugador, mano in manos.items():
            if jugador == f'Jugador {jugador_activo}':
                print(f'{Fore.GREEN}{jugador} tiene: ', end="")
                for carta in mano:
                    print(f'{Fore.RED}{carta}', end=" ")
                print()
            else:
                print(f'{Fore.YELLOW}{jugador} tiene: **Oculto**')
        print(f'{Fore.YELLOW}Cartas comunitarias: ', end="")
        for carta in comunitarias:
            print(f'{Fore.BLUE}{carta}', end=" ")
        print()

    def evaluar_mano(self, cartas):
        valores_extraidos = [carta[:-1] for carta in cartas]
        valores_ordenados = sorted(valores_extraidos, key=lambda x: self.valores.index(x))
        palos = [carta[-1] for carta in cartas]
        contador_valores = Counter(valores_ordenados)
        contador_palos = Counter(palos)
        es_color = len(contador_palos) == 1
        es_escalera = False
        if len(contador_valores) == 5:
            indices_valores = [self.valores.index(valor) for valor in valores_ordenados]
            if indices_valores == list(range(min(indices_valores), max(indices_valores) + 1)):
                es_escalera = True
        es_escalera_real = es_escalera and es_color and valores_ordenados[-1] == 'A'
        es_escalera_color = es_escalera and es_color
        es_poker = max(contador_valores.values()) == 4
        es_full_house = sorted(contador_valores.values()) == [2, 3]
        es_trio = max(contador_valores.values()) == 3
        es_doble_pareja = sorted(contador_valores.values()) == [1, 2, 2]
        es_par = max(contador_valores.values()) == 2
        if es_escalera_real:
            return "Escalera Real"
        elif es_escalera_color:
            return "Escalera de Color"
        elif es_poker:
            return "Póker"
        elif es_full_house:
            return "Full House"
        elif es_color:
            return "Color"
        elif es_escalera:
            return "Escalera"
        elif es_trio:
            return "Trío"
        elif es_doble_pareja:
            return "Doble Pareja"
        elif es_par:
            return "Pareja"
        else:
            return "Carta Alta"

    def jugar(self, usuario):
        saldo = usuario[4]
        mazo = self.crear_mazo()
        num_jugadores = int(input('¿Cuántos jugadores (2-10)? '))
        if num_jugadores < 2 or num_jugadores > 10:
            print(Fore.RED + "El número de jugadores debe ser entre 2 y 10.")
            return
        manos = self.repartir_cartas(mazo, num_jugadores)
        comunitarias = self.repartir_comunitarias(mazo)
        jugador_activo = 1
        self.mostrar_cartas(manos, comunitarias, jugador_activo)
        manos_eval = {jugador: self.evaluar_mano(mano + comunitarias) for jugador, mano in manos.items()}
        print("\nEvaluación de manos:")
        for jugador, mano in manos_eval.items():
            print(f'{Fore.GREEN}{jugador}: {Fore.CYAN}{mano}')
        ganador = max(manos_eval, key=manos_eval.get)
        print(f"\n{Fore.YELLOW}El ganador es: {Fore.GREEN}{ganador} con una {manos_eval[ganador]}!")
        if ganador == f'Jugador {jugador_activo}':
            saldo += 10  # Ejemplo de ganancia
            print(f"¡Felicidades! Has ganado $10. Saldo actual: ${saldo}")
        else:
            saldo -= 10  # Ejemplo de pérdida
            print(f"Lo siento, has perdido $10. Saldo actual: ${saldo}")
        usuario = (usuario[0], usuario[1], usuario[2], usuario[3], saldo, usuario[5])
        return usuario