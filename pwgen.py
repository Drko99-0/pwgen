import random
import string

def generar_contraseña(longitud=8):
    caracteres = string.ascii_letters + string.digits
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

if __name__ == '__main__':
    longitud = input('Longitud de la contraseña (por defecto 8): ')
    longitud = int(longitud) if longitud.isdigit() else 8
    print('Contraseña generada:', generar_contraseña(longitud))
