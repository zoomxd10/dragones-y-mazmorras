####  Dragones y mazmorras                 Antonio Galván Gerona ####
#####################################################################

import random
import time

###############
###FUNCIONES###
###############

# Funcion para tirar los dados
def tirar_dado(lados):
    """
    Función para simular la tirada de un dado.
    param:lados (int): El número de caras del dado (ej. 4, 6, 8, 12, 20).
    return:int: Un número aleatorio entre 1 y el número de caras del dado.
    """
    return random.randint(1, lados)


# Definimos las razas de personajes disponibles
razas = ["humano", "enano", "elfo", "mediano"]


# Función para calcular el ataque
#El modificador_ataque lo que hace es poder sumar o restar numeros a la tirada (Ejemplo: 15 en dado de 20 + modificador_ataque=+2 --> tirada=17)
def tirada_ataque(clase_armadura_enemigo, modificador_ataque=0):
    """
    Calcula si el ataque impacta o falla, basado en una tirada de un dado de 20 caras.
    param:clase_armadura_enemigo (int): La clase de armadura del enemigo que determina la dificultad del impacto.
    modificador_ataque (int, opcional): Un modificador que se suma o resta a la tirada del dado (por defecto es 0).
    return:El primer valor indica si el ataque se acertó (True) o fue fallado (False)
    """
    resultado_dado = tirar_dado(20)  # Tiramos un dado de 20 caras
    resultado_final = resultado_dado + modificador_ataque  # Sumamos el modificador de ataque

    # Si sacas un 1, es una pifia (fallo crítico)
    if resultado_dado == 1:
        return False, "Pifia: El ataque falla automáticamente."

    # Si sacas un 20, es un golpe crítico (siempre impacta)
    if resultado_dado == 20:
        return True, "¡Golpe crítico! El ataque impacta automáticamente."

    # Si el resultado final es mayor o igual que la clase de armadura del enemigo, el ataque impacta
    if resultado_final >= clase_armadura_enemigo:
        return True, f"El ataque impacta con una tirada de {resultado_final}."
    else:
        # Si no supera la clase de armadura, el ataque falla
        return False, f"El ataque falla con una tirada de {resultado_final}."


# Función para calcular el daño basado en el arma
#El modidficador_daño puede sumar o restar a la tirada final del ataque (Esto sin puntos de vida es un poco inutil pero asi muestra el daño total inflingido)
def calcular_daño(arma, modificador_daño=0):
    """
    Calcula el daño que inflige el personaje basado en el arma utilizada y un modificador adicional.
    param:arma (str): El tipo de arma utilizada ("daga", "espada corta", "espada larga", "espadón", "mangual").
    modificador_daño (int, opcional): Un modificador que se suma o resta al daño base (por defecto es 0).
    return:int: El daño total infligido por el ataque .
    """
    # Definimos el daño base según el tipo de arma
    if arma == "daga":
        daño = tirar_dado(4)
    elif arma == "espada corta":
        daño = tirar_dado(6)
    elif arma == "espada larga":
        daño = tirar_dado(8)
    elif arma == "espadón":
        daño = tirar_dado(12)
    elif arma == "mangual":
        daño = tirar_dado(4) + tirar_dado(4)
    else:
        print("Arma no válida.")
        return 0
    return max(daño + modificador_daño, 0)

########################
###PROGRAMA PRINCIPAL###
########################

# Bienvenida al jugador
print("Bienvenido a Dragones y Mazmorras. ¿Estás listo para iniciar la aventura?")
time.sleep(1)
numero_jugadores = int(input("Introduce el número de jugadores (hasta 2 jugadores): "))

# Validamos si el número de jugadores es 1 o 2
if numero_jugadores not in [1, 2]:
    print("Número de jugadores no válido.")
    exit()  # Si el número de jugadores no es válido, finalizamos el programa

# Selección de raza y creación del personaje para 1 jugador
if numero_jugadores == 1:
    raza_personaje = random.choice(razas)  # Elegimos una raza aleatoria para el jugador
    print(f"Eres un joven {raza_personaje}, habitante de un pequeño poblado cercano al reino de Impiltur.")
    time.sleep(3)
    print("Un anciano te propone una peligrosa misión para sacar a tu familia de la pobreza.")
    time.sleep(3)
    print(f"Tu misión es llevar unos amuletos sagrados al reino de Calimshan, para ello solo te entregan una espada corta en caso de tener que defenderte.")
    time.sleep(4)
    print("Te diriges al reino de Sembia para pasar la noche, pero un ogro intenta robarte los amuletos, ")
    time.sleep(4)
    print("aunque al haber conseguido descansar y comer bien has ganado un pequeño bonificador de 2.")
    time.sleep(5)

    # Pregunta si el jugador desea luchar o huir
    lucha_1 = input("Te encuentras cara a cara contra el ogro, ¿decides luchar o huir? ").lower()

    if lucha_1 == "luchar":
        time.sleep(2)
        print("Te preparas para el combate...")
        clase_armadura_ogro = 6  # Clase de armadura del ogro
        arma_personaje = "espada corta"  # El jugador tiene una espada corta

        # Realizamos la tirada de ataque
        exito_ataque, mensaje_ataque = tirada_ataque(clase_armadura_ogro, modificador_ataque=2)
        time.sleep(2)
        print(mensaje_ataque)

        # Si el ataque tiene éxito, calculamos el daño
        if exito_ataque:
            time.sleep(3)
            daño = calcular_daño(arma_personaje, modificador_daño=2)
            print(f"Tu ataque inflige {daño} puntos de daño al ogro.")
            time.sleep(2)
            print("¡Has derrotado al ogro y sigues tu misión!")
            #Seguimos la historia
            time.sleep(4)
            print("Tras una intensa lucha contra el ogro decides seguir tu camino de madrugada,")
            print(" lo que no te esperabas es que un grupo de bandidos te acorralaria, quitandote la opcion de huir.")
            time.sleep(3)
            print("Por suerte tras derrotar al ogro te hiciste con su mangual, de gran utilidad aunque al estar cansado tu modificador está en -1.")
            time.sleep(6)
            arma_personaje = "mangual"
            print("Te preparas para el combate...")
            clase_armadura_bandidos = 10  # Clase de armadura del ogro
            # Realizamos la tirada de ataque, iniciando la funcion y dandole el valor de esta a las variables de exito_ataque y mensaje_ataque
            exito_ataque, mensaje_ataque = tirada_ataque(clase_armadura_bandidos, modificador_ataque=-1)
            time.sleep(4)
            print(mensaje_ataque)

            # Si el ataque tiene éxito, calculamos el daño
            if exito_ataque:
                time.sleep(3)
                daño = calcular_daño(arma_personaje, modificador_daño=-1)
                print(f"Tu ataque inflige {daño} puntos de daño a los bandidos.")
                time.sleep(3)
                print("Lograste matar a dos de los bandidos y el resto huyeron. ¡Enhorabuena!")
                time.sleep(3)
                print("El resto de la historia está en desarrollo para un futuro, espero que te esté gustando :) ")
            else:
                time.sleep(3)
                print("Los bandidos te han vencido y robado todo ¡Has fallado la misión!")

        else:
            time.sleep(3)
            print("El ogro te golpea y te roba los amuletos. ¡Has fallado la misión!")

    elif lucha_1 == "huir":
        time.sleep(2)
        print("Decides huir para proteger tu vida, pero pierdes los amuletos en la fuga.")
        time.sleep(2)
        print("¡Tu misión ha fracasado!")
    else:
        print("Decisión no válida. Fin del juego.")

# Si se elige 2 jugadores (modo en desarrollo)
elif numero_jugadores == 2:
    print("En desarrollo para hacer en un futuro")
else:
    print("Número de jugadores no válido.")
    exit()
