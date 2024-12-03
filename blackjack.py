import random
import time

class Blackjack:
    suits = ("Spades ♠", "Clubs ♣", "Hearts ♥", "Diamonds ♦")
    ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
    values = {
        "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
        "J": 10, "Q": 10, "K": 10, "A": 11  # Los ases se ajustan en Hand.adjust_for_ace()
    }
    playing = True

    class Card:
        def __init__(self, suit, rank):
            self.suit = suit
            self.rank = rank

        def __str__(self):
            return self.rank + " of " + self.suit

    class Deck:
        def __init__(self):
            self.deck = []  # Empieza con una lista vacía
            for suit in Blackjack.suits:
                for rank in Blackjack.ranks:
                    self.deck.append(Blackjack.Card(suit, rank))

        def __str__(self):
            deck_comp = ""  # Comienza con una cadena vacía
            for card in self.deck:
                deck_comp += "\n " + card.__str__()  # Agrega la cadena de impresión de cada objeto carta
            return "The deck has:" + deck_comp

        def shuffle(self):
            random.shuffle(self.deck)

        def deal(self):
            single_card = self.deck.pop()
            return single_card

    class Hand:
        def __init__(self):
            self.cards = []  # Comienza con una lista vacía como hicimos en la clase Deck
            self.value = 0  # Comienza con un valor de 0
            self.aces = 0  # Agrega un atributo para realizar un seguimiento de los ases

        def add_card(self, card):
            self.cards.append(card)
            self.value += Blackjack.values[card.rank]
            if card.rank == "A":
                self.aces += 1  # Añadir a self.aces

        def adjust_for_ace(self):
            while self.value > 21 and self.aces:
                self.value -= 10
                self.aces -= 1

    def hit(self, deck, hand):
        hand.add_card(deck.deal())
        hand.adjust_for_ace()

    def hit_or_stand(self, deck, hand):
        while True:
            x = input("\n¿Desea pedir o plantarse? ingrese [h/s]")
            if x[0].lower() == "h":
                self.hit(deck, hand)  # hit() definida arriba
            elif x[0].lower() == "s":
                print("El jugador se planta. El Dealer juega.")
                self.playing = False
            else:
                print("Perdon, letra incorrecta. Por favor ingrese [h/s].")
                continue
            break

    def show_some(self, player, dealer):
        print("\nMano del jugador:", *player.cards, sep="\n ")
        print("Mano del jugador =", player.value)
        print("\nMano del Dealer:")
        print(" <Tarjeta oculta>")
        print("", dealer.cards[1])

    def show_all(self, player, dealer):
        print("\nMano del jugador:", *player.cards, sep="\n ")
        print("Mano del jugador =", player.value)
        print("\nMano del Dealer:", *dealer.cards, sep="\n ")
        print("Mano del Dealer =", dealer.value)

    def player_busts(self, player, dealer):
        print("\n--- Fallaste! ---")

    def player_wins(self, player, dealer):
        print("\n--- ¡Ganaste! ---")

    def dealer_busts(self, player, dealer):
        print("\n--- El dealer falló, ¡Ganaste! ---")

    def dealer_wins(self, player, dealer):
        print("\n--- El dealer ganó! ---")

    def push(self, player, dealer):
        print("\nEs un empate!")

    def jugar(self, usuario):
        saldo = usuario[4]
        while True:
            print(f"\nSaldo actual: ${saldo}")
            print("\n----------------------------------------------------------------")
            print(" ♠♣♥♦ ¡BIENVENIDO AL BLACKJACK! ♠♣♥♦")
            print("----------------------------------------------------------------")
            print(
                "Reglas del juego: Acércate lo más que puedas a 21 sin pasarte!\n"
                "El dealer pide cartas hasta llegar a 17.\n"
                "S = Te plantas / H = Pedir.\n"
                "Aces cuentas como 1 u 11."
            )
            # Crea y baraja el mazo, reparte dos cartas a cada jugador
            deck = self.Deck()
            deck.shuffle()
            player_hand = self.Hand()
            player_hand.add_card(deck.deal())
            player_hand.add_card(deck.deal())
            dealer_hand = self.Hand()
            dealer_hand.add_card(deck.deal())
            dealer_hand.add_card(deck.deal())
            # Mostrar las cartas:
            self.show_some(player_hand, dealer_hand)
            while self.playing:  # Recupera esta variable de nuestra función hit_or_stand
                # Aviso para que el jugador solicite pedir carta o plantarse
                self.hit_or_stand(deck, player_hand)
                self.show_some(player_hand, dealer_hand)
                if player_hand.value > 21:
                    self.player_busts(player_hand, dealer_hand)
                    break
            # Si el jugador no se ha pasado, juega la mano del dealer
            if player_hand.value <= 21:
                while dealer_hand.value < 17:
                    self.hit(deck, dealer_hand)
                # Muestra todas las cartas
                time.sleep(1)
                print("\n----------------------------------------------------------------")
                print(" ★ Resultado Final ★")
                print("----------------------------------------------------------------")
                self.show_all(player_hand, dealer_hand)
                # Prueba diferentes escenarios
                if dealer_hand.value > 21:
                    self.dealer_busts(player_hand, dealer_hand)
                elif dealer_hand.value > player_hand.value:
                    self.dealer_wins(player_hand, dealer_hand)
                elif dealer_hand.value < player_hand.value:
                    self.player_wins(player_hand, dealer_hand)
                else:
                    self.push(player_hand, dealer_hand)
            # Pregunta si quiere jugar de nuevo
            new_game = input("\n¿Jugar otra mano? [Y/N] ")
            while new_game.lower() not in ["y", "n"]:
                new_game = input("Letra no válida. Selecciona 'y' o 'n' ")
            if new_game[0].lower() == "y":
                self.playing = True
                continue
            else:
                print("\n------------------------¡Gracias por jugar!---------------------\n")
                break
        usuario = (usuario[0], usuario[1], usuario[2], usuario[3], saldo, usuario[5])
        return usuario
