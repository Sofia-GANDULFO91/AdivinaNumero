# adivina.py
import random

def jugar():
    print("🎯 Adivina el número")
    print("1) Fácil (1-10, 10 intentos)")
    print("2) Medio (1-50, 7 intentos)")
    print("3) Difícil (1-100, 5 intentos)")
    print("4) Extremo (1-150, 3 intentos)  # NUEVO")

    opcion = input("Elige nivel (1-4): ").strip()
    if opcion == "1":
        low, high, max_intentos = 1, 10, 10
    elif opcion == "2":
        low, high, max_intentos = 1, 50, 7
    elif opcion == "3":
        low, high, max_intentos = 1, 100, 5
    elif opcion == "4":
        low, high, max_intentos = 1, 150, 3
    else:
        print("⚠️ Opción inválida.")
        return

    secreto = random.randint(low, high)
    intentos = 0
    acertado = False

    print(f"Adivina un número entre {low} y {high}. Tienes {max_intentos} intentos.")

    while intentos < max_intentos and not acertado:
        entrada = input(f"Intento {intentos+1}/{max_intentos}: ")
        try:
            intento = int(entrada)
        except ValueError:
            print("⚠️ Ingresa un número entero válido.")
            continue  

        intentos += 1

        if intento == secreto:
            print(f"🎉 ¡Felicidades! Adivinaste en {intentos} intentos.")
            acertado = True
        elif intento < secreto:
            print("🔼 Demasiado bajo.")
        else:
            print("🔽 Demasiado alto.")

        # Pista : par o impar
        if not acertado:
            pista = "PAR" if secreto % 2 == 0 else "IMPAR"
            print(f"Pista: el número secreto es {pista}.\n")

    if not acertado:
        print(f"😢 Se acabaron los intentos. El número era {secreto}.")

if __name__ == "__main__":
    jugar()
