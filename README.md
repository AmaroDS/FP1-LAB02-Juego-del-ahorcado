# 🎯 Proyecto de Laboratorio: El Juego del Ahorcado  
## Fundamentos de Programación 1. Grado en Ingeniería Informática – Inteligencia Artificial (Universidad de Sevilla)

En este laboratorio vas a **implementar el juego del ahorcado** paso a paso.  
Este juego consiste en adivinar una palabra secreta, letra a letra. El jugador tiene un número limitado de intentos para descubrir la palabra antes de que el "ahorcado" se complete. Cada letra incorrecta reduce los intentos disponibles, mientras que las letras correctas revelan su posición en la palabra.  
El objetivo es adivinar la palabra completa antes de quedarse sin intentos.

---

## Preparación del entorno

👉 Para configurar Git y clonar el repositorio del laboratorio, consulta **[instrucciones_git.md](instrucciones_git.md)**.  

---

## ⏱ Duración estimada

2 horas

---

## ✅ ¿Qué se practica?

- Tipos de datos: `int`, `bool`, `str`
- Entrada y salida con `input()` / `print()`
- Expresiones y operadores
- Condicionales `if / elif / else`
- Bucles `while` y `for`
- Cadenas y métodos de `str`
- **Funciones**: definición, parámetros, valores por defecto, docstrings y valor de retorno
- **Pruebas** con `assert`

---

## 📁 Archivos del proyecto

Dispones de estos archivos en `src`:

| Archivo                  | Qué hace                                                                  |
|--------------------------|---------------------------------------------------------------------------|
| `juego_ahorcado.py`      | Todas las funciones y el bucle principal del juego están implementados aquí. |
| `juego_ahorcado_test.py` | Pruebas de algunas de las funciones de `juego_ahorcado.py`|


La función `elige_palabra` se proporciona ya implementada. Esta función devuelve una palabra secreta aleatoriamente.

---

## 📌 Ejercicio 1: Función `normalizar`

Implementa la función `normalizar` que recibe una cadena de texto y realiza algunas tareas de "saneamiento": 
- Convierte a minúsculas todas las letras
- Quita espacios en blanco que pudiera haber al principio y al final de la palabra
- Elimina acentos y diéresis si los hubiera

La función devuelve la cadena una vez saneada. 

Una vez implementada, prueba la función ejecutando el módulo `juego_ahorcado_test.py`. 


## 📌 Ejercicio 2: Función `enmascarar`

Implementa la función `enmascarar` que recibe una palabra y las letras que ya ha adivinado el jugador, y devuelve la palabra enmascarada. La palabra enmascarada es la misma palabra recibida sustituyendo por guiones bajos todas las letras que aún no han sido adivinadas.

Una vez implementada, prueba la función. Para ello, descomenta la llamada `test_enmascarar()` del módulo `juego_ahorcado_test.py` y ejecútalo.

## 📌 Ejercicio 3: Función `ha_ganado`

Implementa la función `ha_ganado` que recibe una palabra enmascarada y devuelve `True` si el jugador ya ha acertado todas las letras (no hay guiones).

Una vez implementada, prueba la función. Para ello, completa la implementación de la función `test_ha_ganado()` del módulo `juego_ahorcado_test.py`, descomenta la llamada a la función, y ejecútala. Usa estos tres casos de prueba, comprobando que se cumplen mediante `assert`:

* `ha_ganado("python")` debe devolver `True`
* `ha_ganado("p____n")` debe devolver `False`
* `ha_ganado("______")` debe devolver `False`


## 📌 Ejercicio 4: Función `mostrar_estado`

Implementa la función `mostrar_estado` que usaremos durante el juego para mostrar al jugador información sobre el transcurso del juego. Debe escribir la cabecera de la función y su cadena de documentación.

La función recibe por parámetros la palabra enmascarada, las letras ya usadas y los intentos restantes. Un ejemplo de la salida mostrada en el terminal al llamar a la función sería el siguiente:

```
Estado: c a _ c i _ _
Letras usadas: aeipsc
Intentos restantes: 3
```

Si las letras usadas recibidas son la cadena vacía (aún no se han usado letras), debe mostrarse `Letras usadas: ninguna`. 

Observe que las letras de la palabra enmascarada se muestran con un espacio en blanco entre cada dos letras, para mayor legibilidad. Use el método `join` del tipo `str` del siguiente modo para conseguirlo:

```python
   " ".join(palabra_enmascarada)
```

Una vez implementada, prueba la función desde el intérprete de Python:
- Abre el terminal pulsando `Ctrl + ñ`.
- Accede a la carpeta `src`, para ello ejecuta el comando `cd src`.
- Abre el intérprete interactivo de Python, ejecutando el comando `python`.
- Una vez dentro del intérprete interactivo de Python, importa la función que queremos probar, escribiendo la instrucción `from juego_ahorcado import mostrar_estado`.
- Llame a la función pasándole distintos parámetros y observe que la información mostrada en el terminal es la adecuada.


## 📌 Ejercicio 5: Función `pedir_letra`

Implementa la función `pedir_letra`, que solicita al jugador que introduzca una letra y se asegura de que la entrada proporcionada por el jugador sea válida. Debe escribir la cabecera de la función y su cadena de documentación.

Para que la entrada recibida del usuario sea válida debe cumplirse que:
- Sea una letra (y solo una)
- No sea una letra que ya se ha pedido anteriormente

La función recibe un parámetro con las letras ya solicitadas anteriormente. Si el jugador no introduce una entrada válida, la función le informa y se la vuelve a pedir, hasta que el jugador introduzca una letra válida. En ese momento, la función devuelve dicha letra, **siempre en minúculas**.

Una posible salida en el terminal de una llamada a la función sería esta (suponiendo que las letras usadas incluyen sólo a la letra `a`):
```
Introduce una letra: 5
   Debes introducir una letra
Introduce una letra: af
   Debes introducir una única letra
Introduce una letra: a
   Esa letra ya la has usado anteriormente
Introduce una letra: B
```

Y la función devolvería la cadena `"b"`.

Una vez implementada, prueba la función desde el intérprete de Python:
- Abre el terminal pulsando `Ctrl + ñ`.
- Accede a la carpeta `src`, para ello ejecuta el comando `cd src`.
- Abre el intérprete interactivo de Python, ejecutando el comando `python`.
- Una vez dentro del intérprete interactivo de Python, importa la función que queremos probar, escribiendo la instrucción `from juego_ahorcado import pedir_letra`.
- Llame a la función y compruebe que funciona como se ha especificado en este enunciado.


## 📌 Ejercicio 6: Función `jugar`

Esta es la función principal que implementa la lógica del juego. En este punto confluyen todas las funciones que hemos implementado hasta ahora.  

La función `jugar` recibe la palabra secreta que hay que adivinar y el número máximo de intentos (por defecto, será 6). Debe escribir la cabecera de la función y su cadena de documentación. 

A continuación, se describe el algoritmo a implementar:

1. **Inicialización**:  
   - Normalizamos la palabra mediante la función `normalizar`.  
   - Si la palabra está vacía, devolvemos `None` (y el juego termina).  
   - Enmascaramos la palabra mediante la función `enmascarar`.  
   - Inicializamos una variable con el número máximo de intentos.  
   - Inicializamos una variable con las letras usadas hasta el momento (cadena vacía).  

2. **Bucle principal**:  
   - Mientras el jugador tenga intentos restantes y no haya ganado:  
      - Muestra el estado del juego usando `mostrar_estado`.  
      - Pide una nueva letra usando `pedir_letra`.  
      - Añade a las letras usadas la que acabas de leer.  
      - Si la letra recibida no pertenece a la palabra secreta:              
         - Muestra un mensaje indicándolo.  
         - Resta 1 a los intentos.  
      - Si la letra recibida sí pertenece a la palabra secreta:  
         - Muestra un mensaje indicándolo.  
         - Actualiza la palabra enmascarada mediante la función `enmascarar`.  

3. **Fin del juego**: muestra un mensaje indicando si el jugador ha ganado o ha perdido, y cuál era la palabra original.

Una vez implementada, prueba la función desde el intérprete de Python:
- Abre el terminal pulsando `Ctrl + ñ`.
- Accede a la carpeta `src`, para ello ejecuta el comando `cd src`.
- Abre el intérprete interactivo de Python, ejecutando el comando `python`.
- Una vez dentro del intérprete interactivo de Python, importa la función que queremos probar, escribiendo la instrucción `from juego_ahorcado import jugar`.
- Llame a la función pasándole una palabra secreta, y compruebe que el juego se desarrolla de manera satisfactoria. 

A modo de ejemplo, se muestra a continuación una posible ejecución del juego (palabra secreta `canción`):

```
¡Bienvenido al juego del ahorcado!

Estado: _ _ _ _ _ _ _
Letras usadas: ninguna
Intentos restantes: 6
Introduce una letra: ae
   Debes introducir una única letra
Introduce una letra: 1
   Debes introducir una letra
Introduce una letra: a
✅ ¡Bien!

Estado: _ a _ _ _ _ _
Letras usadas: a
Intentos restantes: 6
Introduce una letra: e
❌ La letra no está en la palabra.

Estado: _ a _ _ _ _ _
Letras usadas: ae
Intentos restantes: 5
Introduce una letra: i
✅ ¡Bien!

Estado: _ a _ _ i _ _
Letras usadas: aei
Intentos restantes: 5
Introduce una letra: p
❌ La letra no está en la palabra.

Estado: _ a _ _ i _ _
Letras usadas: aeip
Intentos restantes: 4
Introduce una letra: s
❌ La letra no está en la palabra.

Estado: _ a _ _ i _ _
Letras usadas: aeips
Intentos restantes: 3
Introduce una letra: c
✅ ¡Bien!

Estado: c a _ c i _ _
Letras usadas: aeipsc
Intentos restantes: 3
Introduce una letra: n
✅ ¡Bien!

Estado: c a n c i _ n
Letras usadas: aeipscn
Intentos restantes: 3
Introduce una letra: o
✅ ¡Bien!

🎉 ¡Has ganado! La palabra era: canción
```

## 📌 Ejercicio 7: Programa principal

Escriba debajo de la definición de funciones el programa principal, es decir, las instrucciones que se ejecutarán cuando alguien lance nuestro programa mediante un comando `python juego_ahorcado.py`. 

El programa principal consiste en obtener una palabra aleatoria mediante la función `elige_palabra`, e invocar a la función `jugar` pasándole dicha palabra.

Prueba a ejecutar el módulo `juego_ahorcado.py`.
