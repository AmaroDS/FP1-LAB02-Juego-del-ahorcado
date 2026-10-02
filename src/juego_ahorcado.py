import random

def elige_palabra(fichero="palabras.txt"):
    """
    Devuelve una palabra aleatoria tomada de un fichero de texto.

    Parámetros:
        fichero: ruta al archivo que contiene las palabras (una por línea).

    Devuelve:
        Una palabra (str) elegida al azar del fichero.
    """
    with open(fichero, "r", encoding="utf-8") as f:
        lineas = f.readlines()
    # Quitar saltos de línea y espacios
    palabras = [linea.strip() for linea in lineas if linea.strip() != ""]
    return random.choice(palabras)


def normalizar(cadena: str) -> str:
    """
    Normaliza una cadena de texto realizando las siguientes operaciones:
        - convierte a minúsculas
        - quita espacios en blanco al principio y al final
        - elimina acentos y diéresis        
    
    Parámetros:
      cadena: cadena de texto que hay que sanear
    
    Devuelve:
      Cadena de texto con la palabra normalizada
    """
    cadena = cadena.lower().strip()
    cadena = cadena.replace("á","a").replace("é","e").replace("í", "i").replace("ó", "o").replace("ú", "u")
    return cadena.replace("ä","a").replace("ë","e").replace("ï", "i").replace("ö", "o").replace("ü", "u")

def enmascarar(palabra_secreta, letras_usadas: str="") -> str:
    '''Devuelve una cadena de texto con la palabra enmascarada. 
    Las letras que no están en letras_usadas se muestran como guiones bajos (_).

    Parámetros:
    - palabra_secreta: cadena de texto con la palabra que se debe enmascarar
    - letras_usadas: cadena de texto con las letras que se deben mostrar (por defecto cadena vacía)

    Devuelve:
      Cadena de texto con la palabra enmascarada
    '''
    palabra_enmascarada = ""
    for i in palabra_secreta:
        if i not in letras_usadas:
            palabra_enmascarada += "_"
        else:
            palabra_enmascarada += i
    return palabra_enmascarada


def ha_ganado(palabra_enmascarada: str) -> bool:
    '''Devuelve True si el jugador ha ganado (es decir, si no quedan letras por descubrir en la palabra enmascarada).

    Parámetros:
    - palabra_enmascarada: cadena de texto con la palabra enmascarada 

    Devuelve:
    - True si el jugador ha ganado, False en caso contrario
    '''
    return "_" not in palabra_enmascarada


def mostrar_estado(palabra_enmascarada, letras_usadas, intentos_restantes) -> None:

    '''Hace varios print del estado de como va la partida diciendote como va la palabra, las letras usadas y los intentos restantes

    Parámetros:
    - palabra_enmascarada: cadena de texto con la palabra enmascarada 
    - letras_usadas: cadena de texto con las letras usadas
    - intentos_restantes: entero con el nº de intentos restantes (<= 6)

    Devuelve:
    - None, no queremos que haga return, solo print
    '''
    
    print(f"Estado: {''.join(palabra_enmascarada)}")

    if letras_usadas == "":
        letras_usadas = "Ninguna"
    print(f"Letras usadas: {letras_usadas}")
    print(intentos_restantes)


def pedir_letra(letras_usadas):

    '''Te pide una letra, antes verfica que sea una letra y que no se haya usado antes

    Parámetros:
    - letras_usadas: cadena de texto con las letras usadas

    Devuelve:
    - letra: la letra que se ha usado
    '''

    letra = input("Dame una letra:")
    while not letra.isalpha():
        print("Debes introducir una letra")
        letra = input("Introduce una letra: ")
    while len(letra) != 1:
        print("Debes introducir una única letra")
        letra = input("Introduce una letra: ")
    while letra in letras_usadas:
        print("Esa letra ya la has introducido anteriormente")
        letra = input("Introduce una letra: ")
    return letra
    
def jugar(palabra_secreta, intentos_max=6):

    '''Sanea la palabra, la enmascara e inicia el bucle aqui se va pidiendo letras
    y se va desvelando la letra o perdiendo intentos si la palabra se desvela o se pierden todos los intentos termina el bucle

    Parámetros:
    - palabra_secreta: palabra que se coge del txt
    - intentos_max: intenos inciales y por tanto máximos

    Devuelve:
    - None, con esto ya se lleva a cabo el juego no necesitamos return
    '''

    palabra_saneada = normalizar(palabra_secreta)
    if palabra_saneada == "":
        return None
    palabra_enmascarada=enmascarar(palabra_saneada)
    intentos_restantes = intentos_max
    letras_usadas = ""

    while intentos_restantes > 0 and ha_ganado(palabra_enmascarada)==False:
        mostrar_estado(palabra_enmascarada, letras_usadas, intentos_restantes)
        letra = pedir_letra(letras_usadas=letras_usadas)
        letras_usadas += letra

        if letra not in palabra_saneada:
            print("❌ La letra no está en la palabra.")
            intentos_restantes -= 1
        else:
            print("✅ ¡Bien!")
            palabra_enmascarada= enmascarar(palabra_saneada, letras_usadas)

    if intentos_restantes>0:
        print(f"🎉 ¡Has ganado! La palabra era: {palabra_saneada}")
    else:
        print(f"¡Has perdido! La palabra era: {palabra_saneada}")

palabra=elige_palabra()
jugar(palabra)

