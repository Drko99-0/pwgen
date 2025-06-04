import random
import string

def generar_contraseña(longitud=8, incluir_simbolos=False):
    caracteres = string.ascii_letters + string.digits
    if incluir_simbolos:
        caracteres += "!@#$%^&*()-_=+[]{};:,.<>?/"

    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

if __name__ == '__main__':
    print("== Generador de Contraseñas Básico ==")
    while True:
        entrada = input('Longitud de la contraseña (mínimo 4, por defecto 8): ')
        if entrada == '':
            longitud = 8
            break
        if entrada.isdigit() and int(entrada) >= 4:
            longitud = int(entrada)
            break
        print("Por favor, ingresa un número válido mayor o igual a 4.")

    simbolos = input('¿Incluir símbolos? (s/n): ').lower()
    incluir_simbolos = simbolos == 's'

    print('Contraseña generada:', generar_contraseña(longitud, incluir_simbolos))
