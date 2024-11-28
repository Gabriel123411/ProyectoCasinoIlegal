import sqlite3
import bcrypt
from blackjack import Blackjack
from poker import Poker
from tragaperras import Tragaperras
from hipodromo import Hipodromo
from carrera_buses import CarreraBuses
from database import crear_tablas  # Importar la función crear_tablas

def conectar_bd():
    try:
        conn = sqlite3.connect('casino.db')
        return conn
    except sqlite3.Error as e:
        print(f"No ha sido posible conectarse con la base de datos: {e}")

def registrar_usuario():
    conn = conectar_bd()
    cursor = conn.cursor()
    while True:
        nombre = input("Ingrese su nombre: ")
        mail = input("Ingrese su correo electrónico: ")
        password = input("Ingrese su contraseña: ")
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        try:
            cursor.execute("INSERT INTO Usuarios (nombre, mail, password) VALUES (?, ?, ?)", (nombre, mail, hashed_password))
            conn.commit()
            print("Registro exitoso. Ahora puede iniciar sesión.")
            break
        except sqlite3.IntegrityError:
            print("El correo electrónico ya está registrado. Intente con otro.")

def iniciar_sesion():
    conn = conectar_bd()
    cursor = conn.cursor()
    while True:
        mail = input("Ingrese su correo electrónico: ")
        password = input("Ingrese su contraseña: ")
        cursor.execute("SELECT * FROM Usuarios WHERE mail = ?", (mail,))
        usuario = cursor.fetchone()
        if usuario and bcrypt.checkpw(password.encode('utf-8'), usuario[3]):
            print("Inicio de sesión exitoso.")
            return usuario
        else:
            print("Correo electrónico o contraseña incorrectos. Intente nuevamente.")

def menu_login():
    while True:
        print("1. Iniciar sesión")
        print("2. Registrarse")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            usuario = iniciar_sesion()
            if usuario:
                return usuario
        elif opcion == '2':
            registrar_usuario()
        else:
            print("Opción no válida. Intente nuevamente.")

def ingresar_dinero(usuario):
    conn = conectar_bd()
    cursor = conn.cursor()
    while True:
        try:
            monto = float(input("Ingrese el monto a depositar: "))
            if monto > 0:
                cursor.execute("UPDATE Usuarios SET saldo = saldo + ? WHERE id_usuario = ?", (monto, usuario[0]))
                conn.commit()
                print(f"Depósito exitoso. Su nuevo saldo es: {usuario[4] + monto}")
                usuario = (usuario[0], usuario[1], usuario[2], usuario[3], usuario[4] + monto, usuario[5])
                return usuario
            else:
                print("Ingrese un monto positivo.")
        except ValueError:
            print("Monto no válido. Intente nuevamente.")

def menu_principal(usuario):
    while True:
        print(f"\nSaldo actual: ${usuario[4]}")
        print("1. Ingresar dinero")
        print("2. Elegir juego")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            usuario = ingresar_dinero(usuario)
        elif opcion == '2':
            elegir_juego(usuario)
        elif opcion == '3':
            print("Gracias por jugar. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

def elegir_juego(usuario):
    print("Seleccione un juego:")
    print("1. Blackjack")
    print("2. Poker")
    print("3. Tragaperras")
    print("4. Hipodromo")
    print("5. Carrera de Buses")
    opcion = input("Seleccione una opción: ")
    if opcion == '1':
        juego = Blackjack()
    elif opcion == '2':
        juego = Poker()
    elif opcion == '3':
        juego = Tragaperras()
    elif opcion == '4':
        juego = Hipodromo()
    elif opcion == '5':
        juego = CarreraBuses()
    else:
        print("Opción no válida. Intente nuevamente.")
        return
    usuario = juego.jugar(usuario)

if __name__ == "__main__":
    crear_tablas()  # crea las tablitas al inicio 
    usuario = menu_login()
    if usuario:
        menu_principal(usuario)
        