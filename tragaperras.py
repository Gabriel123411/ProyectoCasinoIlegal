import random

class Tragaperras:
    def __init__(self):
        self.simbolos = ['🍋', '🍒', '🍀', '🍉', '🍊', '🍓', '7️⃣']
        self.costo_tirada = 1.00

    def generar_fila(self):
        return [random.choice(self.simbolos) for _ in range(5)]

    def jugar(self, usuario):
        saldo = usuario[4]
        while True:
            if saldo < self.costo_tirada:
                print("No tienes suficiente dinero para jugar.")
                break

            print(f"Saldo actual: ${saldo:.2f}")
            input("Presiona Enter para hacer girar la máquina...")
            saldo -= self.costo_tirada
            fila = self.generar_fila()
            print(" ".join(fila))

            premios = self.calcular_premio(fila)
            saldo += premios
            print(f"Has ganado ${premios:.2f}. Saldo actual: ${saldo:.2f}")

            if saldo < self.costo_tirada:
                print("No tienes suficiente dinero para seguir jugando.")
                break

            continuar = input("¿Quieres seguir jugando? (s/n): ").lower()
            if continuar != 's':
                break

        usuario = (usuario[0], usuario[1], usuario[2], usuario[3], saldo, usuario[5])
        return usuario

    def calcular_premio(self, fila):
        contador = {simbolo: fila.count(simbolo) for simbolo in set(fila)}
        premio = 0
        for simbolo, cuenta in contador.items():
            if cuenta == 5:
                premio += 10.00
            elif cuenta == 4:
                premio += 5.00
            elif cuenta == 3:
                premio += 2.00
            elif cuenta == 2:
                premio += 0.50
        return premio